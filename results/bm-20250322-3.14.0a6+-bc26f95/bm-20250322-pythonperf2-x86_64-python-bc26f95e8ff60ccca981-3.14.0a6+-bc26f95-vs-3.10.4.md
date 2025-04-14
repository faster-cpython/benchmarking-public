# Results vs. 3.10.4

- fork: python
- ref: bc26f95e8ff60ccca981
- machine: linux-x86_64
- commit hash: bc26f95
- commit date: 2025-03-22
- overall geometric mean: 1.313x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.29x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 287 ms: 1.22x faster                                                         |
| docutils       | 3.41 sec                                                     | 2.92 sec: 1.17x faster                                                       |
| html5lib       | 94.6 ms                                                      | 69.0 ms: 1.37x faster                                                        |
| Geometric mean | (ref)                                                        | 1.25x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 653 ms: 2.45x faster                                                         |
| async_tree_memoization  | 819 ms                                                       | 343 ms: 2.39x faster                                                         |
| async_tree_none         | 692 ms                                                       | 295 ms: 2.35x faster                                                         |
| async_tree_cpu_io_mixed | 936 ms                                                       | 520 ms: 1.80x faster                                                         |
| Geometric mean          | (ref)                                                        | 2.23x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 71.7 ms: 1.55x faster                                                        |
| nbody          | 134 ms                                                       | 109 ms: 1.23x faster                                                         |
| pidigits       | 271 ms                                                       | 254 ms: 1.06x faster                                                         |
| Geometric mean | (ref)                                                        | 1.27x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 136 ms: 1.39x faster                                                         |
| regex_v8       | 27.2 ms                                                      | 24.3 ms: 1.12x faster                                                        |
| regex_dna      | 261 ms                                                       | 235 ms: 1.11x faster                                                         |
| regex_effbot   | 3.09 ms                                                      | 3.02 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                        | 1.15x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 220 us: 1.42x faster                                                         |
| pickle_pure_python   | 455 us                                                       | 337 us: 1.35x faster                                                         |
| tomli_loads          | 2.92 sec                                                     | 2.22 sec: 1.31x faster                                                       |
| json_dumps           | 14.5 ms                                                      | 11.5 ms: 1.27x faster                                                        |
| xml_etree_process    | 75.9 ms                                                      | 60.3 ms: 1.26x faster                                                        |
| xml_etree_parse      | 160 ms                                                       | 138 ms: 1.16x faster                                                         |
| json_loads           | 30.3 us                                                      | 26.4 us: 1.15x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 98.0 ms: 1.13x faster                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 85.2 ms: 1.08x faster                                                        |
| unpickle             | 13.5 us                                                      | 14.0 us: 1.04x slower                                                        |
| unpickle_list        | 4.65 us                                                      | 5.05 us: 1.09x slower                                                        |
| pickle_dict          | 29.5 us                                                      | 35.2 us: 1.19x slower                                                        |
| pickle_list          | 4.12 us                                                      | 5.12 us: 1.24x slower                                                        |
| pickle               | 9.89 us                                                      | 12.5 us: 1.26x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.08x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 16.4 ms: 1.42x slower                                                        |
| python_startup_no_site | 7.33 ms                                                      | 10.5 ms: 1.43x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.43x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.9 ms: 1.35x faster                                                        |
| django_template | 50.2 ms                                                      | 37.4 ms: 1.34x faster                                                        |
| genshi_text     | 31.4 ms                                                      | 24.6 ms: 1.28x faster                                                        |
| genshi_xml      | 63.3 ms                                                      | 56.3 ms: 1.12x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.27x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 178 us: 3.01x faster                                                         |
| async_tree_io            | 1.60 sec                                                     | 653 ms: 2.45x faster                                                         |
| async_tree_memoization   | 819 ms                                                       | 343 ms: 2.39x faster                                                         |
| async_tree_none          | 692 ms                                                       | 295 ms: 2.35x faster                                                         |
| deltablue                | 7.50 ms                                                      | 3.36 ms: 2.23x faster                                                        |
| asyncio_tcp              | 779 ms                                                       | 375 ms: 2.08x faster                                                         |
| generators               | 57.3 ms                                                      | 29.2 ms: 1.97x faster                                                        |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.96x faster                                                       |
| go                       | 262 ms                                                       | 134 ms: 1.95x faster                                                         |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 520 ms: 1.80x faster                                                         |
| logging_silent           | 167 ns                                                       | 93.2 ns: 1.79x faster                                                        |
| pylint                   | 566 ms                                                       | 318 ms: 1.78x faster                                                         |
| raytrace                 | 489 ms                                                       | 284 ms: 1.72x faster                                                         |
| deepcopy_memo            | 49.8 us                                                      | 29.1 us: 1.71x faster                                                        |
| chaos                    | 109 ms                                                       | 63.7 ms: 1.70x faster                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 64.7 ms: 1.66x faster                                                        |
| scimark_sor              | 180 ms                                                       | 109 ms: 1.66x faster                                                         |
| scimark_lu               | 167 ms                                                       | 101 ms: 1.66x faster                                                         |
| richards_super           | 90.6 ms                                                      | 55.2 ms: 1.64x faster                                                        |
| deepcopy                 | 468 us                                                       | 294 us: 1.59x faster                                                         |
| pyflate                  | 733 ms                                                       | 468 ms: 1.56x faster                                                         |
| float                    | 111 ms                                                       | 71.7 ms: 1.55x faster                                                        |
| spectral_norm            | 139 ms                                                       | 89.8 ms: 1.55x faster                                                        |
| richards                 | 75.1 ms                                                      | 48.7 ms: 1.54x faster                                                        |
| comprehensions           | 26.7 us                                                      | 17.7 us: 1.50x faster                                                        |
| hexiom                   | 9.42 ms                                                      | 6.49 ms: 1.45x faster                                                        |
| coroutines               | 30.3 ms                                                      | 21.2 ms: 1.43x faster                                                        |
| unpickle_pure_python     | 312 us                                                       | 220 us: 1.42x faster                                                         |
| crypto_pyaes             | 119 ms                                                       | 84.6 ms: 1.41x faster                                                        |
| regex_compile            | 190 ms                                                       | 136 ms: 1.39x faster                                                         |
| html5lib                 | 94.6 ms                                                      | 69.0 ms: 1.37x faster                                                        |
| thrift                   | 1.18 ms                                                      | 865 us: 1.36x faster                                                         |
| pickle_pure_python       | 455 us                                                       | 337 us: 1.35x faster                                                         |
| deepcopy_reduce          | 4.01 us                                                      | 2.98 us: 1.35x faster                                                        |
| mako                     | 14.7 ms                                                      | 10.9 ms: 1.35x faster                                                        |
| django_template          | 50.2 ms                                                      | 37.4 ms: 1.34x faster                                                        |
| logging_simple           | 8.88 us                                                      | 6.65 us: 1.33x faster                                                        |
| logging_format           | 9.64 us                                                      | 7.27 us: 1.33x faster                                                        |
| tomli_loads              | 2.92 sec                                                     | 2.22 sec: 1.31x faster                                                       |
| pycparser                | 1.67 sec                                                     | 1.28 sec: 1.31x faster                                                       |
| pprint_pformat           | 2.15 sec                                                     | 1.65 sec: 1.30x faster                                                       |
| dulwich_log              | 81.1 ms                                                      | 62.3 ms: 1.30x faster                                                        |
| sqlalchemy_declarative   | 190 ms                                                       | 146 ms: 1.30x faster                                                         |
| pprint_safe_repr         | 1.05 sec                                                     | 817 ms: 1.29x faster                                                         |
| genshi_text              | 31.4 ms                                                      | 24.6 ms: 1.28x faster                                                        |
| json_dumps               | 14.5 ms                                                      | 11.5 ms: 1.27x faster                                                        |
| xml_etree_process        | 75.9 ms                                                      | 60.3 ms: 1.26x faster                                                        |
| sqlalchemy_imperative    | 22.7 ms                                                      | 18.1 ms: 1.26x faster                                                        |
| fannkuch                 | 483 ms                                                       | 384 ms: 1.26x faster                                                         |
| sympy_sum                | 193 ms                                                       | 154 ms: 1.25x faster                                                         |
| pathlib                  | 21.4 ms                                                      | 17.1 ms: 1.25x faster                                                        |
| sympy_integrate          | 28.2 ms                                                      | 22.8 ms: 1.24x faster                                                        |
| nbody                    | 134 ms                                                       | 109 ms: 1.23x faster                                                         |
| sympy_str                | 360 ms                                                       | 293 ms: 1.23x faster                                                         |
| 2to3                     | 350 ms                                                       | 287 ms: 1.22x faster                                                         |
| bench_thread_pool        | 1.14 ms                                                      | 945 us: 1.21x faster                                                         |
| nqueens                  | 115 ms                                                       | 95.3 ms: 1.21x faster                                                        |
| mdp                      | 3.01 sec                                                     | 2.49 sec: 1.21x faster                                                       |
| sympy_expand             | 600 ms                                                       | 499 ms: 1.20x faster                                                         |
| docutils                 | 3.41 sec                                                     | 2.92 sec: 1.17x faster                                                       |
| xml_etree_parse          | 160 ms                                                       | 138 ms: 1.16x faster                                                         |
| scimark_fft              | 361 ms                                                       | 314 ms: 1.15x faster                                                         |
| json_loads               | 30.3 us                                                      | 26.4 us: 1.15x faster                                                        |
| unpack_sequence          | 59.9 ns                                                      | 52.2 ns: 1.15x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 98.0 ms: 1.13x faster                                                        |
| genshi_xml               | 63.3 ms                                                      | 56.3 ms: 1.12x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 24.3 ms: 1.12x faster                                                        |
| regex_dna                | 261 ms                                                       | 235 ms: 1.11x faster                                                         |
| json                     | 5.86 ms                                                      | 5.40 ms: 1.09x faster                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 85.2 ms: 1.08x faster                                                        |
| meteor_contest           | 138 ms                                                       | 128 ms: 1.08x faster                                                         |
| pidigits                 | 271 ms                                                       | 254 ms: 1.06x faster                                                         |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.78 ms: 1.06x faster                                                        |
| sqlite_synth             | 2.99 us                                                      | 2.83 us: 1.06x faster                                                        |
| regex_effbot             | 3.09 ms                                                      | 3.02 ms: 1.02x faster                                                        |
| async_generators         | 421 ms                                                       | 423 ms: 1.00x slower                                                         |
| unpickle                 | 13.5 us                                                      | 14.0 us: 1.04x slower                                                        |
| unpickle_list            | 4.65 us                                                      | 5.05 us: 1.09x slower                                                        |
| telco                    | 7.23 ms                                                      | 8.10 ms: 1.12x slower                                                        |
| pickle_dict              | 29.5 us                                                      | 35.2 us: 1.19x slower                                                        |
| pickle_list              | 4.12 us                                                      | 5.12 us: 1.24x slower                                                        |
| pickle                   | 9.89 us                                                      | 12.5 us: 1.26x slower                                                        |
| coverage                 | 63.3 ms                                                      | 80.2 ms: 1.27x slower                                                        |
| python_startup           | 11.5 ms                                                      | 16.4 ms: 1.42x slower                                                        |
| python_startup_no_site   | 7.33 ms                                                      | 10.5 ms: 1.43x slower                                                        |
| create_gc_cycles         | 1.76 ms                                                      | 2.82 ms: 1.60x slower                                                        |
| gc_traversal             | 3.42 ms                                                      | 6.62 ms: 1.94x slower                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 957 ms: 150.13x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.22x faster                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (11) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (15) of results/bm-20250322-3.14.0a6+-bc26f95/bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.313x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: 1.29x