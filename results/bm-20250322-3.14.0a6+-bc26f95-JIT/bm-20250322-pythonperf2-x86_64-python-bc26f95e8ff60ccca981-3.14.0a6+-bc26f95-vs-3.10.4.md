# Results vs. 3.10.4

- fork: python
- ref: bc26f95e8ff60ccca981
- machine: linux-x86_64
- commit hash: bc26f95
- commit date: 2025-03-22
- overall geometric mean: 1.310x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 293 ms: 1.19x faster                                                         |
| docutils       | 3.41 sec                                                     | 3.00 sec: 1.14x faster                                                       |
| html5lib       | 94.6 ms                                                      | 71.0 ms: 1.33x faster                                                        |
| Geometric mean | (ref)                                                        | 1.22x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 654 ms: 2.45x faster                                                         |
| async_tree_memoization  | 819 ms                                                       | 341 ms: 2.40x faster                                                         |
| async_tree_none         | 692 ms                                                       | 299 ms: 2.31x faster                                                         |
| async_tree_cpu_io_mixed | 936 ms                                                       | 520 ms: 1.80x faster                                                         |
| Geometric mean          | (ref)                                                        | 2.22x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 66.0 ms: 1.68x faster                                                        |
| nbody          | 134 ms                                                       | 94.5 ms: 1.42x faster                                                        |
| pidigits       | 271 ms                                                       | 253 ms: 1.07x faster                                                         |
| Geometric mean | (ref)                                                        | 1.37x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 141 ms: 1.35x faster                                                         |
| regex_v8       | 27.2 ms                                                      | 23.1 ms: 1.18x faster                                                        |
| regex_dna      | 261 ms                                                       | 230 ms: 1.13x faster                                                         |
| regex_effbot   | 3.09 ms                                                      | 2.98 ms: 1.04x faster                                                        |
| Geometric mean | (ref)                                                        | 1.17x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 222 us: 1.40x faster                                                         |
| tomli_loads          | 2.92 sec                                                     | 2.12 sec: 1.37x faster                                                       |
| xml_etree_process    | 75.9 ms                                                      | 58.0 ms: 1.31x faster                                                        |
| pickle_pure_python   | 455 us                                                       | 352 us: 1.29x faster                                                         |
| json_dumps           | 14.5 ms                                                      | 11.5 ms: 1.26x faster                                                        |
| xml_etree_parse      | 160 ms                                                       | 135 ms: 1.18x faster                                                         |
| xml_etree_iterparse  | 110 ms                                                       | 96.8 ms: 1.14x faster                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 81.5 ms: 1.13x faster                                                        |
| json_loads           | 30.3 us                                                      | 26.8 us: 1.13x faster                                                        |
| unpickle             | 13.5 us                                                      | 14.3 us: 1.06x slower                                                        |
| unpickle_list        | 4.65 us                                                      | 5.24 us: 1.13x slower                                                        |
| pickle               | 9.89 us                                                      | 12.1 us: 1.22x slower                                                        |
| pickle_dict          | 29.5 us                                                      | 36.4 us: 1.23x slower                                                        |
| pickle_list          | 4.12 us                                                      | 5.16 us: 1.25x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.09x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 16.5 ms: 1.43x slower                                                        |
| python_startup_no_site | 7.33 ms                                                      | 10.5 ms: 1.44x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.43x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.5 ms: 1.40x faster                                                        |
| django_template | 50.2 ms                                                      | 37.2 ms: 1.35x faster                                                        |
| genshi_text     | 31.4 ms                                                      | 23.9 ms: 1.32x faster                                                        |
| genshi_xml      | 63.3 ms                                                      | 56.9 ms: 1.11x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.29x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 181 us: 2.96x faster                                                         |
| async_tree_io            | 1.60 sec                                                     | 654 ms: 2.45x faster                                                         |
| deltablue                | 7.50 ms                                                      | 3.12 ms: 2.40x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 341 ms: 2.40x faster                                                         |
| async_tree_none          | 692 ms                                                       | 299 ms: 2.31x faster                                                         |
| asyncio_tcp              | 779 ms                                                       | 374 ms: 2.09x faster                                                         |
| generators               | 57.3 ms                                                      | 28.8 ms: 1.99x faster                                                        |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.59 sec: 1.96x faster                                                       |
| richards_super           | 90.6 ms                                                      | 46.8 ms: 1.94x faster                                                        |
| richards                 | 75.1 ms                                                      | 40.7 ms: 1.85x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 520 ms: 1.80x faster                                                         |
| logging_silent           | 167 ns                                                       | 93.6 ns: 1.79x faster                                                        |
| go                       | 262 ms                                                       | 150 ms: 1.75x faster                                                         |
| pylint                   | 566 ms                                                       | 325 ms: 1.74x faster                                                         |
| deepcopy_memo            | 49.8 us                                                      | 29.5 us: 1.68x faster                                                        |
| float                    | 111 ms                                                       | 66.0 ms: 1.68x faster                                                        |
| raytrace                 | 489 ms                                                       | 293 ms: 1.67x faster                                                         |
| pyflate                  | 733 ms                                                       | 447 ms: 1.64x faster                                                         |
| scimark_sor              | 180 ms                                                       | 111 ms: 1.63x faster                                                         |
| chaos                    | 109 ms                                                       | 67.0 ms: 1.62x faster                                                        |
| scimark_lu               | 167 ms                                                       | 103 ms: 1.62x faster                                                         |
| spectral_norm            | 139 ms                                                       | 86.0 ms: 1.62x faster                                                        |
| deepcopy                 | 468 us                                                       | 303 us: 1.55x faster                                                         |
| scimark_monte_carlo      | 107 ms                                                       | 71.1 ms: 1.51x faster                                                        |
| nbody                    | 134 ms                                                       | 94.5 ms: 1.42x faster                                                        |
| coroutines               | 30.3 ms                                                      | 21.5 ms: 1.41x faster                                                        |
| mako                     | 14.7 ms                                                      | 10.5 ms: 1.40x faster                                                        |
| unpickle_pure_python     | 312 us                                                       | 222 us: 1.40x faster                                                         |
| tomli_loads              | 2.92 sec                                                     | 2.12 sec: 1.37x faster                                                       |
| crypto_pyaes             | 119 ms                                                       | 87.2 ms: 1.37x faster                                                        |
| hexiom                   | 9.42 ms                                                      | 6.97 ms: 1.35x faster                                                        |
| regex_compile            | 190 ms                                                       | 141 ms: 1.35x faster                                                         |
| django_template          | 50.2 ms                                                      | 37.2 ms: 1.35x faster                                                        |
| logging_simple           | 8.88 us                                                      | 6.60 us: 1.35x faster                                                        |
| thrift                   | 1.18 ms                                                      | 877 us: 1.34x faster                                                         |
| logging_format           | 9.64 us                                                      | 7.20 us: 1.34x faster                                                        |
| html5lib                 | 94.6 ms                                                      | 71.0 ms: 1.33x faster                                                        |
| deepcopy_reduce          | 4.01 us                                                      | 3.04 us: 1.32x faster                                                        |
| genshi_text              | 31.4 ms                                                      | 23.9 ms: 1.32x faster                                                        |
| xml_etree_process        | 75.9 ms                                                      | 58.0 ms: 1.31x faster                                                        |
| pickle_pure_python       | 455 us                                                       | 352 us: 1.29x faster                                                         |
| pprint_pformat           | 2.15 sec                                                     | 1.67 sec: 1.29x faster                                                       |
| dulwich_log              | 81.1 ms                                                      | 63.2 ms: 1.28x faster                                                        |
| pycparser                | 1.67 sec                                                     | 1.31 sec: 1.27x faster                                                       |
| comprehensions           | 26.7 us                                                      | 21.1 us: 1.27x faster                                                        |
| sqlalchemy_declarative   | 190 ms                                                       | 150 ms: 1.27x faster                                                         |
| json_dumps               | 14.5 ms                                                      | 11.5 ms: 1.26x faster                                                        |
| pprint_safe_repr         | 1.05 sec                                                     | 832 ms: 1.26x faster                                                         |
| sqlalchemy_imperative    | 22.7 ms                                                      | 18.3 ms: 1.24x faster                                                        |
| sympy_sum                | 193 ms                                                       | 156 ms: 1.23x faster                                                         |
| pathlib                  | 21.4 ms                                                      | 17.5 ms: 1.22x faster                                                        |
| nqueens                  | 115 ms                                                       | 95.0 ms: 1.21x faster                                                        |
| sympy_integrate          | 28.2 ms                                                      | 23.4 ms: 1.20x faster                                                        |
| sympy_str                | 360 ms                                                       | 299 ms: 1.20x faster                                                         |
| 2to3                     | 350 ms                                                       | 293 ms: 1.19x faster                                                         |
| xml_etree_parse          | 160 ms                                                       | 135 ms: 1.18x faster                                                         |
| regex_v8                 | 27.2 ms                                                      | 23.1 ms: 1.18x faster                                                        |
| mdp                      | 3.01 sec                                                     | 2.56 sec: 1.17x faster                                                       |
| fannkuch                 | 483 ms                                                       | 413 ms: 1.17x faster                                                         |
| bench_thread_pool        | 1.14 ms                                                      | 983 us: 1.16x faster                                                         |
| sympy_expand             | 600 ms                                                       | 517 ms: 1.16x faster                                                         |
| scimark_fft              | 361 ms                                                       | 316 ms: 1.14x faster                                                         |
| xml_etree_iterparse      | 110 ms                                                       | 96.8 ms: 1.14x faster                                                        |
| docutils                 | 3.41 sec                                                     | 3.00 sec: 1.14x faster                                                       |
| regex_dna                | 261 ms                                                       | 230 ms: 1.13x faster                                                         |
| xml_etree_generate       | 92.3 ms                                                      | 81.5 ms: 1.13x faster                                                        |
| json_loads               | 30.3 us                                                      | 26.8 us: 1.13x faster                                                        |
| genshi_xml               | 63.3 ms                                                      | 56.9 ms: 1.11x faster                                                        |
| json                     | 5.86 ms                                                      | 5.41 ms: 1.08x faster                                                        |
| sqlite_synth             | 2.99 us                                                      | 2.79 us: 1.07x faster                                                        |
| pidigits                 | 271 ms                                                       | 253 ms: 1.07x faster                                                         |
| regex_effbot             | 3.09 ms                                                      | 2.98 ms: 1.04x faster                                                        |
| meteor_contest           | 138 ms                                                       | 134 ms: 1.03x faster                                                         |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 5.00 ms: 1.02x faster                                                        |
| asyncio_websockets       | 390 ms                                                       | 385 ms: 1.01x faster                                                         |
| async_generators         | 421 ms                                                       | 446 ms: 1.06x slower                                                         |
| unpickle                 | 13.5 us                                                      | 14.3 us: 1.06x slower                                                        |
| telco                    | 7.23 ms                                                      | 8.09 ms: 1.12x slower                                                        |
| unpickle_list            | 4.65 us                                                      | 5.24 us: 1.13x slower                                                        |
| pickle                   | 9.89 us                                                      | 12.1 us: 1.22x slower                                                        |
| pickle_dict              | 29.5 us                                                      | 36.4 us: 1.23x slower                                                        |
| coverage                 | 63.3 ms                                                      | 78.2 ms: 1.24x slower                                                        |
| pickle_list              | 4.12 us                                                      | 5.16 us: 1.25x slower                                                        |
| python_startup           | 11.5 ms                                                      | 16.5 ms: 1.43x slower                                                        |
| python_startup_no_site   | 7.33 ms                                                      | 10.5 ms: 1.44x slower                                                        |
| create_gc_cycles         | 1.76 ms                                                      | 2.73 ms: 1.55x slower                                                        |
| gc_traversal             | 3.42 ms                                                      | 6.37 ms: 1.87x slower                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 1.11 sec: 173.56x slower                                                     |
| Geometric mean           | (ref)                                                        | 1.21x faster                                                                 |

Benchmark hidden because not significant (1): unpack_sequence
Ignored benchmarks (11) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (15) of results/bm-20250322-3.14.0a6+-bc26f95-JIT/bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.310x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: 1.31x