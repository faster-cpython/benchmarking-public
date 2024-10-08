# Results vs. 3.10.4

- fork: python
- ref: fe85a8291d9aa11c9ce9
- machine: linux-x86_64
- commit hash: fe85a82
- commit date: 2024-08-26
- overall geometric mean: 1.35x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240826-pythonperf2-x86_64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 281 ms: 1.25x faster                                                        |
| docutils       | 3.41 sec                                                     | 2.95 sec: 1.16x faster                                                      |
| html5lib       | 94.6 ms                                                      | 72.7 ms: 1.30x faster                                                       |
| tornado_http   | 157 ms                                                       | 116 ms: 1.36x faster                                                        |
| Geometric mean | (ref)                                                        | 1.26x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240826-pythonperf2-x86_64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 319 ms: 2.17x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 401 ms: 2.04x faster                                                        |
| async_tree_io           | 1.60 sec                                                     | 802 ms: 1.99x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 571 ms: 1.64x faster                                                        |
| Geometric mean          | (ref)                                                        | 1.95x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240826-pythonperf2-x86_64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 85.9 ms: 1.56x faster                                                       |
| float          | 111 ms                                                       | 79.5 ms: 1.40x faster                                                       |
| pidigits       | 271 ms                                                       | 252 ms: 1.07x faster                                                        |
| Geometric mean | (ref)                                                        | 1.33x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240826-pythonperf2-x86_64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 141 ms: 1.35x faster                                                        |
| regex_dna      | 261 ms                                                       | 254 ms: 1.03x faster                                                        |
| regex_effbot   | 3.09 ms                                                      | 3.57 ms: 1.15x slower                                                       |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240826-pythonperf2-x86_64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 213 us: 1.47x faster                                                        |
| pickle_pure_python   | 455 us                                                       | 316 us: 1.44x faster                                                        |
| json_dumps           | 14.5 ms                                                      | 10.6 ms: 1.37x faster                                                       |
| xml_etree_process    | 75.9 ms                                                      | 59.5 ms: 1.28x faster                                                       |
| json_loads           | 30.3 us                                                      | 25.1 us: 1.21x faster                                                       |
| tomli_loads          | 2.92 sec                                                     | 2.58 sec: 1.13x faster                                                      |
| xml_etree_parse      | 160 ms                                                       | 143 ms: 1.12x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 100 ms: 1.10x faster                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 84.7 ms: 1.09x faster                                                       |
| Geometric mean       | (ref)                                                        | 1.24x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240826-pythonperf2-x86_64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.3 ms: 1.16x slower                                                       |
| python_startup_no_site | 7.33 ms                                                      | 9.02 ms: 1.23x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.19x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240826-pythonperf2-x86_64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.4 ms: 1.42x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 24.6 ms: 1.28x faster                                                       |
| django_template | 50.2 ms                                                      | 40.4 ms: 1.24x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 56.2 ms: 1.13x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.26x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240826-pythonperf2-x86_64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 170 us: 3.16x faster                                                        |
| deltablue                | 7.50 ms                                                      | 3.35 ms: 2.24x faster                                                       |
| async_tree_none          | 692 ms                                                       | 319 ms: 2.17x faster                                                        |
| asyncio_tcp              | 779 ms                                                       | 369 ms: 2.11x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 401 ms: 2.04x faster                                                        |
| generators               | 57.3 ms                                                      | 28.5 ms: 2.01x faster                                                       |
| async_tree_io            | 1.60 sec                                                     | 802 ms: 1.99x faster                                                        |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.57 sec: 1.97x faster                                                      |
| raytrace                 | 489 ms                                                       | 272 ms: 1.80x faster                                                        |
| chaos                    | 109 ms                                                       | 61.2 ms: 1.78x faster                                                       |
| scimark_lu               | 167 ms                                                       | 94.7 ms: 1.76x faster                                                       |
| logging_silent           | 167 ns                                                       | 97.9 ns: 1.71x faster                                                       |
| deepcopy_memo            | 49.8 us                                                      | 29.8 us: 1.67x faster                                                       |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 571 ms: 1.64x faster                                                        |
| scimark_sor              | 180 ms                                                       | 110 ms: 1.64x faster                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 65.7 ms: 1.64x faster                                                       |
| crypto_pyaes             | 119 ms                                                       | 73.0 ms: 1.63x faster                                                       |
| richards_super           | 90.6 ms                                                      | 55.7 ms: 1.63x faster                                                       |
| pylint                   | 566 ms                                                       | 348 ms: 1.63x faster                                                        |
| deepcopy                 | 468 us                                                       | 291 us: 1.61x faster                                                        |
| sqlglot_parse            | 2.24 ms                                                      | 1.43 ms: 1.57x faster                                                       |
| nbody                    | 134 ms                                                       | 85.9 ms: 1.56x faster                                                       |
| pyflate                  | 733 ms                                                       | 471 ms: 1.56x faster                                                        |
| comprehensions           | 26.7 us                                                      | 17.5 us: 1.53x faster                                                       |
| richards                 | 75.1 ms                                                      | 49.6 ms: 1.51x faster                                                       |
| hexiom                   | 9.42 ms                                                      | 6.29 ms: 1.50x faster                                                       |
| sqlglot_transpile        | 2.68 ms                                                      | 1.80 ms: 1.49x faster                                                       |
| unpickle_pure_python     | 312 us                                                       | 213 us: 1.47x faster                                                        |
| go                       | 262 ms                                                       | 179 ms: 1.46x faster                                                        |
| pickle_pure_python       | 455 us                                                       | 316 us: 1.44x faster                                                        |
| spectral_norm            | 139 ms                                                       | 96.7 ms: 1.44x faster                                                       |
| bench_mp_pool            | 6.37 ms                                                      | 4.48 ms: 1.42x faster                                                       |
| coroutines               | 30.3 ms                                                      | 21.3 ms: 1.42x faster                                                       |
| mako                     | 14.7 ms                                                      | 10.4 ms: 1.42x faster                                                       |
| float                    | 111 ms                                                       | 79.5 ms: 1.40x faster                                                       |
| thrift                   | 1.18 ms                                                      | 846 us: 1.39x faster                                                        |
| logging_simple           | 8.88 us                                                      | 6.44 us: 1.38x faster                                                       |
| pycparser                | 1.67 sec                                                     | 1.23 sec: 1.37x faster                                                      |
| json_dumps               | 14.5 ms                                                      | 10.6 ms: 1.37x faster                                                       |
| logging_format           | 9.64 us                                                      | 7.09 us: 1.36x faster                                                       |
| deepcopy_reduce          | 4.01 us                                                      | 2.95 us: 1.36x faster                                                       |
| fannkuch                 | 483 ms                                                       | 356 ms: 1.36x faster                                                        |
| tornado_http             | 157 ms                                                       | 116 ms: 1.36x faster                                                        |
| pathlib                  | 21.4 ms                                                      | 15.8 ms: 1.35x faster                                                       |
| regex_compile            | 190 ms                                                       | 141 ms: 1.35x faster                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 856 us: 1.33x faster                                                        |
| pprint_pformat           | 2.15 sec                                                     | 1.64 sec: 1.31x faster                                                      |
| nqueens                  | 115 ms                                                       | 87.7 ms: 1.31x faster                                                       |
| pprint_safe_repr         | 1.05 sec                                                     | 804 ms: 1.30x faster                                                        |
| html5lib                 | 94.6 ms                                                      | 72.7 ms: 1.30x faster                                                       |
| sympy_sum                | 193 ms                                                       | 150 ms: 1.28x faster                                                        |
| genshi_text              | 31.4 ms                                                      | 24.6 ms: 1.28x faster                                                       |
| xml_etree_process        | 75.9 ms                                                      | 59.5 ms: 1.28x faster                                                       |
| 2to3                     | 350 ms                                                       | 281 ms: 1.25x faster                                                        |
| django_template          | 50.2 ms                                                      | 40.4 ms: 1.24x faster                                                       |
| sympy_str                | 360 ms                                                       | 290 ms: 1.24x faster                                                        |
| sympy_integrate          | 28.2 ms                                                      | 22.9 ms: 1.23x faster                                                       |
| json_loads               | 30.3 us                                                      | 25.1 us: 1.21x faster                                                       |
| sympy_expand             | 600 ms                                                       | 502 ms: 1.19x faster                                                        |
| sqlglot_normalize        | 144 ms                                                       | 120 ms: 1.19x faster                                                        |
| mdp                      | 3.01 sec                                                     | 2.52 sec: 1.19x faster                                                      |
| scimark_fft              | 361 ms                                                       | 304 ms: 1.19x faster                                                        |
| sqlglot_optimize         | 70.1 ms                                                      | 59.2 ms: 1.19x faster                                                       |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.33 ms: 1.17x faster                                                       |
| async_generators         | 421 ms                                                       | 363 ms: 1.16x faster                                                        |
| docutils                 | 3.41 sec                                                     | 2.95 sec: 1.16x faster                                                      |
| tomli_loads              | 2.92 sec                                                     | 2.58 sec: 1.13x faster                                                      |
| genshi_xml               | 63.3 ms                                                      | 56.2 ms: 1.13x faster                                                       |
| xml_etree_parse          | 160 ms                                                       | 143 ms: 1.12x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 100 ms: 1.10x faster                                                        |
| json                     | 5.86 ms                                                      | 5.34 ms: 1.10x faster                                                       |
| xml_etree_generate       | 92.3 ms                                                      | 84.7 ms: 1.09x faster                                                       |
| meteor_contest           | 138 ms                                                       | 128 ms: 1.08x faster                                                        |
| pidigits                 | 271 ms                                                       | 252 ms: 1.07x faster                                                        |
| regex_dna                | 261 ms                                                       | 254 ms: 1.03x faster                                                        |
| asyncio_websockets       | 390 ms                                                       | 395 ms: 1.01x slower                                                        |
| create_gc_cycles         | 1.76 ms                                                      | 1.89 ms: 1.07x slower                                                       |
| telco                    | 7.23 ms                                                      | 8.26 ms: 1.14x slower                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.57 ms: 1.15x slower                                                       |
| python_startup           | 11.5 ms                                                      | 13.3 ms: 1.16x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 9.02 ms: 1.23x slower                                                       |
| coverage                 | 63.3 ms                                                      | 81.8 ms: 1.29x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 4.43 ms: 1.30x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.35x faster                                                                |

Benchmark hidden because not significant (1): regex_v8
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240826-3.14.0a0-fe85a82/bm-20240826-pythonperf2-x86_64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.24x

# Memory
- memory change: 1.13x