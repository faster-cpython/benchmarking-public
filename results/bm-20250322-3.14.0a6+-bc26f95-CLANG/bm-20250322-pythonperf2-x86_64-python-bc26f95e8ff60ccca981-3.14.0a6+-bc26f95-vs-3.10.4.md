# Results vs. 3.10.4

- fork: python
- ref: bc26f95e8ff60ccca981
- machine: linux-x86_64
- commit hash: bc26f95
- commit date: 2025-03-22
- overall geometric mean: 1.380x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 277 ms: 1.26x faster                                                         |
| docutils       | 3.41 sec                                                     | 2.86 sec: 1.19x faster                                                       |
| html5lib       | 94.6 ms                                                      | 67.5 ms: 1.40x faster                                                        |
| Geometric mean | (ref)                                                        | 1.28x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 616 ms: 2.59x faster                                                         |
| async_tree_memoization  | 819 ms                                                       | 320 ms: 2.56x faster                                                         |
| async_tree_none         | 692 ms                                                       | 278 ms: 2.49x faster                                                         |
| async_tree_cpu_io_mixed | 936 ms                                                       | 523 ms: 1.79x faster                                                         |
| Geometric mean          | (ref)                                                        | 2.33x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 68.1 ms: 1.63x faster                                                        |
| nbody          | 134 ms                                                       | 86.6 ms: 1.55x faster                                                        |
| pidigits       | 271 ms                                                       | 291 ms: 1.08x slower                                                         |
| Geometric mean | (ref)                                                        | 1.33x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 135 ms: 1.41x faster                                                         |
| regex_dna      | 261 ms                                                       | 225 ms: 1.16x faster                                                         |
| regex_v8       | 27.2 ms                                                      | 23.7 ms: 1.15x faster                                                        |
| regex_effbot   | 3.09 ms                                                      | 3.05 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                        | 1.17x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 209 us: 1.49x faster                                                         |
| pickle_pure_python   | 455 us                                                       | 316 us: 1.44x faster                                                         |
| tomli_loads          | 2.92 sec                                                     | 2.07 sec: 1.41x faster                                                       |
| xml_etree_process    | 75.9 ms                                                      | 55.8 ms: 1.36x faster                                                        |
| json_dumps           | 14.5 ms                                                      | 11.6 ms: 1.25x faster                                                        |
| json_loads           | 30.3 us                                                      | 25.4 us: 1.20x faster                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 79.3 ms: 1.16x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 103 ms: 1.08x faster                                                         |
| unpickle_list        | 4.65 us                                                      | 4.48 us: 1.04x faster                                                        |
| unpickle             | 13.5 us                                                      | 13.7 us: 1.02x slower                                                        |
| pickle_list          | 4.12 us                                                      | 4.30 us: 1.05x slower                                                        |
| pickle               | 9.89 us                                                      | 12.0 us: 1.21x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.14x faster                                                                 |

Benchmark hidden because not significant (2): pickle_dict, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 16.2 ms: 1.41x slower                                                        |
| python_startup_no_site | 7.33 ms                                                      | 10.5 ms: 1.43x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.42x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 33.6 ms: 1.49x faster                                                        |
| genshi_text     | 31.4 ms                                                      | 22.3 ms: 1.41x faster                                                        |
| mako            | 14.7 ms                                                      | 11.0 ms: 1.34x faster                                                        |
| genshi_xml      | 63.3 ms                                                      | 51.7 ms: 1.22x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.36x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 164 us: 3.28x faster                                                         |
| async_tree_io            | 1.60 sec                                                     | 616 ms: 2.59x faster                                                         |
| async_tree_memoization   | 819 ms                                                       | 320 ms: 2.56x faster                                                         |
| async_tree_none          | 692 ms                                                       | 278 ms: 2.49x faster                                                         |
| deltablue                | 7.50 ms                                                      | 3.17 ms: 2.36x faster                                                        |
| go                       | 262 ms                                                       | 124 ms: 2.11x faster                                                         |
| asyncio_tcp              | 779 ms                                                       | 375 ms: 2.08x faster                                                         |
| logging_silent           | 167 ns                                                       | 81.1 ns: 2.06x faster                                                        |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.96x faster                                                       |
| scimark_sor              | 180 ms                                                       | 92.9 ms: 1.94x faster                                                        |
| generators               | 57.3 ms                                                      | 29.9 ms: 1.92x faster                                                        |
| scimark_lu               | 167 ms                                                       | 88.2 ms: 1.89x faster                                                        |
| raytrace                 | 489 ms                                                       | 262 ms: 1.86x faster                                                         |
| chaos                    | 109 ms                                                       | 58.5 ms: 1.86x faster                                                        |
| deepcopy_memo            | 49.8 us                                                      | 27.3 us: 1.82x faster                                                        |
| richards_super           | 90.6 ms                                                      | 49.9 ms: 1.82x faster                                                        |
| pylint                   | 566 ms                                                       | 313 ms: 1.81x faster                                                         |
| pyflate                  | 733 ms                                                       | 409 ms: 1.79x faster                                                         |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 523 ms: 1.79x faster                                                         |
| scimark_monte_carlo      | 107 ms                                                       | 60.3 ms: 1.78x faster                                                        |
| spectral_norm            | 139 ms                                                       | 78.9 ms: 1.76x faster                                                        |
| deepcopy                 | 468 us                                                       | 268 us: 1.75x faster                                                         |
| richards                 | 75.1 ms                                                      | 43.8 ms: 1.71x faster                                                        |
| comprehensions           | 26.7 us                                                      | 16.3 us: 1.64x faster                                                        |
| float                    | 111 ms                                                       | 68.1 ms: 1.63x faster                                                        |
| hexiom                   | 9.42 ms                                                      | 5.85 ms: 1.61x faster                                                        |
| nbody                    | 134 ms                                                       | 86.6 ms: 1.55x faster                                                        |
| coroutines               | 30.3 ms                                                      | 19.8 ms: 1.53x faster                                                        |
| django_template          | 50.2 ms                                                      | 33.6 ms: 1.49x faster                                                        |
| unpickle_pure_python     | 312 us                                                       | 209 us: 1.49x faster                                                         |
| crypto_pyaes             | 119 ms                                                       | 81.3 ms: 1.47x faster                                                        |
| deepcopy_reduce          | 4.01 us                                                      | 2.74 us: 1.47x faster                                                        |
| logging_simple           | 8.88 us                                                      | 6.12 us: 1.45x faster                                                        |
| pickle_pure_python       | 455 us                                                       | 316 us: 1.44x faster                                                         |
| logging_format           | 9.64 us                                                      | 6.76 us: 1.43x faster                                                        |
| thrift                   | 1.18 ms                                                      | 826 us: 1.42x faster                                                         |
| tomli_loads              | 2.92 sec                                                     | 2.07 sec: 1.41x faster                                                       |
| regex_compile            | 190 ms                                                       | 135 ms: 1.41x faster                                                         |
| genshi_text              | 31.4 ms                                                      | 22.3 ms: 1.41x faster                                                        |
| html5lib                 | 94.6 ms                                                      | 67.5 ms: 1.40x faster                                                        |
| pycparser                | 1.67 sec                                                     | 1.23 sec: 1.36x faster                                                       |
| xml_etree_process        | 75.9 ms                                                      | 55.8 ms: 1.36x faster                                                        |
| pprint_pformat           | 2.15 sec                                                     | 1.58 sec: 1.36x faster                                                       |
| dulwich_log              | 81.1 ms                                                      | 60.0 ms: 1.35x faster                                                        |
| pprint_safe_repr         | 1.05 sec                                                     | 782 ms: 1.34x faster                                                         |
| mako                     | 14.7 ms                                                      | 11.0 ms: 1.34x faster                                                        |
| sqlalchemy_declarative   | 190 ms                                                       | 142 ms: 1.34x faster                                                         |
| nqueens                  | 115 ms                                                       | 88.0 ms: 1.31x faster                                                        |
| sqlalchemy_imperative    | 22.7 ms                                                      | 17.5 ms: 1.30x faster                                                        |
| sympy_integrate          | 28.2 ms                                                      | 21.8 ms: 1.29x faster                                                        |
| pathlib                  | 21.4 ms                                                      | 16.5 ms: 1.29x faster                                                        |
| sympy_sum                | 193 ms                                                       | 150 ms: 1.29x faster                                                         |
| scimark_fft              | 361 ms                                                       | 282 ms: 1.28x faster                                                         |
| fannkuch                 | 483 ms                                                       | 381 ms: 1.27x faster                                                         |
| sympy_str                | 360 ms                                                       | 284 ms: 1.27x faster                                                         |
| 2to3                     | 350 ms                                                       | 277 ms: 1.26x faster                                                         |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.04 ms: 1.26x faster                                                        |
| json_dumps               | 14.5 ms                                                      | 11.6 ms: 1.25x faster                                                        |
| sympy_expand             | 600 ms                                                       | 487 ms: 1.23x faster                                                         |
| genshi_xml               | 63.3 ms                                                      | 51.7 ms: 1.22x faster                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 935 us: 1.22x faster                                                         |
| json_loads               | 30.3 us                                                      | 25.4 us: 1.20x faster                                                        |
| docutils                 | 3.41 sec                                                     | 2.86 sec: 1.19x faster                                                       |
| xml_etree_generate       | 92.3 ms                                                      | 79.3 ms: 1.16x faster                                                        |
| regex_dna                | 261 ms                                                       | 225 ms: 1.16x faster                                                         |
| regex_v8                 | 27.2 ms                                                      | 23.7 ms: 1.15x faster                                                        |
| json                     | 5.86 ms                                                      | 5.12 ms: 1.14x faster                                                        |
| mdp                      | 3.01 sec                                                     | 2.65 sec: 1.13x faster                                                       |
| xml_etree_iterparse      | 110 ms                                                       | 103 ms: 1.08x faster                                                         |
| sqlite_synth             | 2.99 us                                                      | 2.81 us: 1.07x faster                                                        |
| meteor_contest           | 138 ms                                                       | 133 ms: 1.04x faster                                                         |
| unpickle_list            | 4.65 us                                                      | 4.48 us: 1.04x faster                                                        |
| asyncio_websockets       | 390 ms                                                       | 383 ms: 1.02x faster                                                         |
| regex_effbot             | 3.09 ms                                                      | 3.05 ms: 1.01x faster                                                        |
| async_generators         | 421 ms                                                       | 425 ms: 1.01x slower                                                         |
| unpickle                 | 13.5 us                                                      | 13.7 us: 1.02x slower                                                        |
| telco                    | 7.23 ms                                                      | 7.39 ms: 1.02x slower                                                        |
| unpack_sequence          | 59.9 ns                                                      | 61.4 ns: 1.02x slower                                                        |
| pickle_list              | 4.12 us                                                      | 4.30 us: 1.05x slower                                                        |
| pidigits                 | 271 ms                                                       | 291 ms: 1.08x slower                                                         |
| coverage                 | 63.3 ms                                                      | 71.8 ms: 1.14x slower                                                        |
| pickle                   | 9.89 us                                                      | 12.0 us: 1.21x slower                                                        |
| python_startup           | 11.5 ms                                                      | 16.2 ms: 1.41x slower                                                        |
| python_startup_no_site   | 7.33 ms                                                      | 10.5 ms: 1.43x slower                                                        |
| create_gc_cycles         | 1.76 ms                                                      | 2.88 ms: 1.64x slower                                                        |
| gc_traversal             | 3.42 ms                                                      | 5.85 ms: 1.71x slower                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 1.10 sec: 172.07x slower                                                     |
| Geometric mean           | (ref)                                                        | 1.28x faster                                                                 |

Benchmark hidden because not significant (2): pickle_dict, xml_etree_parse
Ignored benchmarks (11) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (15) of results/bm-20250322-3.14.0a6+-bc26f95-CLANG/bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.380x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.27x

# Memory
- memory change: 1.33x