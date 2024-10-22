# Results vs. 3.10.4

- fork: mdboom
- ref: pysequence_tuple
- machine: linux-x86_64
- commit hash: 3b5fdc8
- commit date: 2024-09-11
- overall geometric mean: 1.32x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240911-pythonperf2-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 287 ms: 1.22x faster                                                    |
| docutils       | 3.41 sec                                                     | 2.91 sec: 1.17x faster                                                  |
| html5lib       | 94.6 ms                                                      | 72.9 ms: 1.30x faster                                                   |
| tornado_http   | 157 ms                                                       | 118 ms: 1.33x faster                                                    |
| Geometric mean | (ref)                                                        | 1.25x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240911-pythonperf2-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|-------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 326 ms: 2.12x faster                                                    |
| async_tree_memoization  | 819 ms                                                       | 403 ms: 2.03x faster                                                    |
| async_tree_io           | 1.60 sec                                                     | 807 ms: 1.98x faster                                                    |
| async_tree_cpu_io_mixed | 936 ms                                                       | 580 ms: 1.61x faster                                                    |
| Geometric mean          | (ref)                                                        | 1.93x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240911-pythonperf2-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 85.3 ms: 1.57x faster                                                   |
| float          | 111 ms                                                       | 80.4 ms: 1.38x faster                                                   |
| pidigits       | 271 ms                                                       | 254 ms: 1.06x faster                                                    |
| Geometric mean | (ref)                                                        | 1.32x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240911-pythonperf2-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 140 ms: 1.36x faster                                                    |
| regex_dna      | 261 ms                                                       | 240 ms: 1.09x faster                                                    |
| regex_v8       | 27.2 ms                                                      | 25.8 ms: 1.05x faster                                                   |
| regex_effbot   | 3.09 ms                                                      | 3.46 ms: 1.12x slower                                                   |
| Geometric mean | (ref)                                                        | 1.08x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240911-pythonperf2-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                       | 315 us: 1.45x faster                                                    |
| unpickle_pure_python | 312 us                                                       | 226 us: 1.38x faster                                                    |
| json_dumps           | 14.5 ms                                                      | 11.1 ms: 1.31x faster                                                   |
| xml_etree_process    | 75.9 ms                                                      | 59.2 ms: 1.28x faster                                                   |
| json_loads           | 30.3 us                                                      | 24.9 us: 1.22x faster                                                   |
| tomli_loads          | 2.92 sec                                                     | 2.56 sec: 1.14x faster                                                  |
| xml_etree_parse      | 160 ms                                                       | 143 ms: 1.12x faster                                                    |
| xml_etree_iterparse  | 110 ms                                                       | 101 ms: 1.09x faster                                                    |
| xml_etree_generate   | 92.3 ms                                                      | 85.3 ms: 1.08x faster                                                   |
| pickle_dict          | 29.5 us                                                      | 29.8 us: 1.01x slower                                                   |
| pickle               | 9.89 us                                                      | 10.2 us: 1.03x slower                                                   |
| unpickle             | 13.5 us                                                      | 15.5 us: 1.15x slower                                                   |
| Geometric mean       | (ref)                                                        | 1.12x faster                                                            |

Benchmark hidden because not significant (2): pickle_list, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240911-pythonperf2-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                                   |
| python_startup_no_site | 7.33 ms                                                      | 8.95 ms: 1.22x slower                                                   |
| Geometric mean         | (ref)                                                        | 1.19x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240911-pythonperf2-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.4 ms: 1.42x faster                                                   |
| genshi_text     | 31.4 ms                                                      | 25.2 ms: 1.25x faster                                                   |
| django_template | 50.2 ms                                                      | 41.3 ms: 1.22x faster                                                   |
| genshi_xml      | 63.3 ms                                                      | 54.2 ms: 1.17x faster                                                   |
| Geometric mean  | (ref)                                                        | 1.26x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240911-pythonperf2-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|--------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 172 us: 3.12x faster                                                    |
| deltablue                | 7.50 ms                                                      | 3.51 ms: 2.13x faster                                                   |
| async_tree_none          | 692 ms                                                       | 326 ms: 2.12x faster                                                    |
| asyncio_tcp              | 779 ms                                                       | 367 ms: 2.12x faster                                                    |
| async_tree_memoization   | 819 ms                                                       | 403 ms: 2.03x faster                                                    |
| async_tree_io            | 1.60 sec                                                     | 807 ms: 1.98x faster                                                    |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.97x faster                                                  |
| generators               | 57.3 ms                                                      | 29.7 ms: 1.93x faster                                                   |
| go                       | 262 ms                                                       | 139 ms: 1.88x faster                                                    |
| raytrace                 | 489 ms                                                       | 278 ms: 1.76x faster                                                    |
| chaos                    | 109 ms                                                       | 63.2 ms: 1.72x faster                                                   |
| scimark_lu               | 167 ms                                                       | 98.1 ms: 1.70x faster                                                   |
| logging_silent           | 167 ns                                                       | 98.8 ns: 1.69x faster                                                   |
| deepcopy_memo            | 49.8 us                                                      | 29.7 us: 1.68x faster                                                   |
| crypto_pyaes             | 119 ms                                                       | 72.6 ms: 1.64x faster                                                   |
| deepcopy                 | 468 us                                                       | 287 us: 1.63x faster                                                    |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 580 ms: 1.61x faster                                                    |
| pylint                   | 566 ms                                                       | 352 ms: 1.61x faster                                                    |
| scimark_monte_carlo      | 107 ms                                                       | 68.3 ms: 1.57x faster                                                   |
| nbody                    | 134 ms                                                       | 85.3 ms: 1.57x faster                                                   |
| richards_super           | 90.6 ms                                                      | 57.9 ms: 1.56x faster                                                   |
| comprehensions           | 26.7 us                                                      | 17.4 us: 1.53x faster                                                   |
| sqlglot_parse            | 2.24 ms                                                      | 1.46 ms: 1.53x faster                                                   |
| scimark_sor              | 180 ms                                                       | 118 ms: 1.52x faster                                                    |
| pyflate                  | 733 ms                                                       | 484 ms: 1.52x faster                                                    |
| hexiom                   | 9.42 ms                                                      | 6.29 ms: 1.50x faster                                                   |
| sqlglot_transpile        | 2.68 ms                                                      | 1.84 ms: 1.46x faster                                                   |
| pickle_pure_python       | 455 us                                                       | 315 us: 1.45x faster                                                    |
| richards                 | 75.1 ms                                                      | 52.0 ms: 1.44x faster                                                   |
| spectral_norm            | 139 ms                                                       | 97.1 ms: 1.43x faster                                                   |
| mako                     | 14.7 ms                                                      | 10.4 ms: 1.42x faster                                                   |
| deepcopy_reduce          | 4.01 us                                                      | 2.87 us: 1.40x faster                                                   |
| unpickle_pure_python     | 312 us                                                       | 226 us: 1.38x faster                                                    |
| float                    | 111 ms                                                       | 80.4 ms: 1.38x faster                                                   |
| logging_simple           | 8.88 us                                                      | 6.47 us: 1.37x faster                                                   |
| pathlib                  | 21.4 ms                                                      | 15.6 ms: 1.37x faster                                                   |
| coroutines               | 30.3 ms                                                      | 22.3 ms: 1.36x faster                                                   |
| regex_compile            | 190 ms                                                       | 140 ms: 1.36x faster                                                    |
| logging_format           | 9.64 us                                                      | 7.12 us: 1.35x faster                                                   |
| thrift                   | 1.18 ms                                                      | 868 us: 1.35x faster                                                    |
| bench_mp_pool            | 6.37 ms                                                      | 4.75 ms: 1.34x faster                                                   |
| pycparser                | 1.67 sec                                                     | 1.26 sec: 1.33x faster                                                  |
| bench_thread_pool        | 1.14 ms                                                      | 859 us: 1.33x faster                                                    |
| tornado_http             | 157 ms                                                       | 118 ms: 1.33x faster                                                    |
| json_dumps               | 14.5 ms                                                      | 11.1 ms: 1.31x faster                                                   |
| html5lib                 | 94.6 ms                                                      | 72.9 ms: 1.30x faster                                                   |
| pprint_pformat           | 2.15 sec                                                     | 1.67 sec: 1.29x faster                                                  |
| pprint_safe_repr         | 1.05 sec                                                     | 816 ms: 1.29x faster                                                    |
| xml_etree_process        | 75.9 ms                                                      | 59.2 ms: 1.28x faster                                                   |
| nqueens                  | 115 ms                                                       | 90.5 ms: 1.27x faster                                                   |
| fannkuch                 | 483 ms                                                       | 380 ms: 1.27x faster                                                    |
| sympy_sum                | 193 ms                                                       | 153 ms: 1.26x faster                                                    |
| genshi_text              | 31.4 ms                                                      | 25.2 ms: 1.25x faster                                                   |
| sympy_str                | 360 ms                                                       | 293 ms: 1.23x faster                                                    |
| 2to3                     | 350 ms                                                       | 287 ms: 1.22x faster                                                    |
| sqlglot_normalize        | 144 ms                                                       | 118 ms: 1.22x faster                                                    |
| json_loads               | 30.3 us                                                      | 24.9 us: 1.22x faster                                                   |
| django_template          | 50.2 ms                                                      | 41.3 ms: 1.22x faster                                                   |
| sympy_integrate          | 28.2 ms                                                      | 23.2 ms: 1.21x faster                                                   |
| unpack_sequence          | 59.9 ns                                                      | 49.4 ns: 1.21x faster                                                   |
| dulwich_log              | 81.1 ms                                                      | 67.2 ms: 1.21x faster                                                   |
| mdp                      | 3.01 sec                                                     | 2.51 sec: 1.20x faster                                                  |
| sqlglot_optimize         | 70.1 ms                                                      | 58.5 ms: 1.20x faster                                                   |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.25 ms: 1.19x faster                                                   |
| sympy_expand             | 600 ms                                                       | 504 ms: 1.19x faster                                                    |
| scimark_fft              | 361 ms                                                       | 305 ms: 1.19x faster                                                    |
| docutils                 | 3.41 sec                                                     | 2.91 sec: 1.17x faster                                                  |
| genshi_xml               | 63.3 ms                                                      | 54.2 ms: 1.17x faster                                                   |
| async_generators         | 421 ms                                                       | 360 ms: 1.17x faster                                                    |
| tomli_loads              | 2.92 sec                                                     | 2.56 sec: 1.14x faster                                                  |
| xml_etree_parse          | 160 ms                                                       | 143 ms: 1.12x faster                                                    |
| json                     | 5.86 ms                                                      | 5.26 ms: 1.11x faster                                                   |
| meteor_contest           | 138 ms                                                       | 127 ms: 1.09x faster                                                    |
| xml_etree_iterparse      | 110 ms                                                       | 101 ms: 1.09x faster                                                    |
| regex_dna                | 261 ms                                                       | 240 ms: 1.09x faster                                                    |
| xml_etree_generate       | 92.3 ms                                                      | 85.3 ms: 1.08x faster                                                   |
| sqlite_synth             | 2.99 us                                                      | 2.76 us: 1.08x faster                                                   |
| pidigits                 | 271 ms                                                       | 254 ms: 1.06x faster                                                    |
| regex_v8                 | 27.2 ms                                                      | 25.8 ms: 1.05x faster                                                   |
| pickle_dict              | 29.5 us                                                      | 29.8 us: 1.01x slower                                                   |
| pickle                   | 9.89 us                                                      | 10.2 us: 1.03x slower                                                   |
| create_gc_cycles         | 1.76 ms                                                      | 1.95 ms: 1.10x slower                                                   |
| regex_effbot             | 3.09 ms                                                      | 3.46 ms: 1.12x slower                                                   |
| unpickle                 | 13.5 us                                                      | 15.5 us: 1.15x slower                                                   |
| telco                    | 7.23 ms                                                      | 8.35 ms: 1.16x slower                                                   |
| python_startup           | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                                   |
| python_startup_no_site   | 7.33 ms                                                      | 8.95 ms: 1.22x slower                                                   |
| coverage                 | 63.3 ms                                                      | 77.4 ms: 1.22x slower                                                   |
| gc_traversal             | 3.42 ms                                                      | 4.42 ms: 1.29x slower                                                   |
| Geometric mean           | (ref)                                                        | 1.32x faster                                                            |

Benchmark hidden because not significant (3): pickle_list, unpickle_list, asyncio_websockets
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240911-3.14.0a0-3b5fdc8/bm-20240911-pythonperf2-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.13x