# Results vs. 3.10.4

- fork: python
- ref: v3.14.0a1
- machine: linux-x86_64
- commit hash: 8cdaca8
- commit date: 2024-10-15
- overall geometric mean: 1.325x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.26x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 282 ms: 1.24x faster                                             |
| docutils       | 3.41 sec                                                     | 2.90 sec: 1.18x faster                                           |
| html5lib       | 94.6 ms                                                      | 71.1 ms: 1.33x faster                                            |
| tornado_http   | 157 ms                                                       | 117 ms: 1.34x faster                                             |
| Geometric mean | (ref)                                                        | 1.27x faster                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 332 ms: 2.08x faster                                             |
| async_tree_memoization  | 819 ms                                                       | 415 ms: 1.97x faster                                             |
| async_tree_io           | 1.60 sec                                                     | 827 ms: 1.93x faster                                             |
| async_tree_cpu_io_mixed | 936 ms                                                       | 558 ms: 1.68x faster                                             |
| Geometric mean          | (ref)                                                        | 1.91x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 90.1 ms: 1.49x faster                                            |
| float          | 111 ms                                                       | 82.2 ms: 1.35x faster                                            |
| pidigits       | 271 ms                                                       | 252 ms: 1.08x faster                                             |
| Geometric mean | (ref)                                                        | 1.29x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 139 ms: 1.37x faster                                             |
| regex_v8       | 27.2 ms                                                      | 24.7 ms: 1.10x faster                                            |
| regex_dna      | 261 ms                                                       | 243 ms: 1.08x faster                                             |
| regex_effbot   | 3.09 ms                                                      | 3.43 ms: 1.11x slower                                            |
| Geometric mean | (ref)                                                        | 1.10x faster                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 214 us: 1.46x faster                                             |
| pickle_pure_python   | 455 us                                                       | 320 us: 1.42x faster                                             |
| json_dumps           | 14.5 ms                                                      | 11.4 ms: 1.27x faster                                            |
| xml_etree_process    | 75.9 ms                                                      | 60.0 ms: 1.27x faster                                            |
| json_loads           | 30.3 us                                                      | 25.3 us: 1.20x faster                                            |
| tomli_loads          | 2.92 sec                                                     | 2.50 sec: 1.17x faster                                           |
| xml_etree_parse      | 160 ms                                                       | 144 ms: 1.11x faster                                             |
| xml_etree_iterparse  | 110 ms                                                       | 102 ms: 1.09x faster                                             |
| xml_etree_generate   | 92.3 ms                                                      | 85.2 ms: 1.08x faster                                            |
| unpickle_list        | 4.65 us                                                      | 4.58 us: 1.01x faster                                            |
| pickle_list          | 4.12 us                                                      | 4.31 us: 1.05x slower                                            |
| pickle_dict          | 29.5 us                                                      | 31.0 us: 1.05x slower                                            |
| pickle               | 9.89 us                                                      | 10.5 us: 1.06x slower                                            |
| unpickle             | 13.5 us                                                      | 15.2 us: 1.13x slower                                            |
| Geometric mean       | (ref)                                                        | 1.12x faster                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 8.96 ms: 1.22x slower                                            |
| python_startup         | 11.5 ms                                                      | 15.0 ms: 1.30x slower                                            |
| Geometric mean         | (ref)                                                        | 1.26x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.7 ms: 1.37x faster                                            |
| genshi_text     | 31.4 ms                                                      | 25.0 ms: 1.26x faster                                            |
| django_template | 50.2 ms                                                      | 41.0 ms: 1.22x faster                                            |
| genshi_xml      | 63.3 ms                                                      | 54.4 ms: 1.16x faster                                            |
| Geometric mean  | (ref)                                                        | 1.25x faster                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 173 us: 3.11x faster                                             |
| deltablue                | 7.50 ms                                                      | 3.44 ms: 2.18x faster                                            |
| asyncio_tcp              | 779 ms                                                       | 371 ms: 2.10x faster                                             |
| async_tree_none          | 692 ms                                                       | 332 ms: 2.08x faster                                             |
| async_tree_memoization   | 819 ms                                                       | 415 ms: 1.97x faster                                             |
| go                       | 262 ms                                                       | 133 ms: 1.97x faster                                             |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.97x faster                                           |
| generators               | 57.3 ms                                                      | 29.3 ms: 1.95x faster                                            |
| async_tree_io            | 1.60 sec                                                     | 827 ms: 1.93x faster                                             |
| raytrace                 | 489 ms                                                       | 270 ms: 1.81x faster                                             |
| chaos                    | 109 ms                                                       | 60.7 ms: 1.79x faster                                            |
| scimark_lu               | 167 ms                                                       | 94.2 ms: 1.77x faster                                            |
| logging_silent           | 167 ns                                                       | 98.0 ns: 1.71x faster                                            |
| deepcopy_memo            | 49.8 us                                                      | 29.4 us: 1.69x faster                                            |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 558 ms: 1.68x faster                                             |
| scimark_monte_carlo      | 107 ms                                                       | 65.4 ms: 1.64x faster                                            |
| pylint                   | 566 ms                                                       | 345 ms: 1.64x faster                                             |
| richards_super           | 90.6 ms                                                      | 55.6 ms: 1.63x faster                                            |
| scimark_sor              | 180 ms                                                       | 111 ms: 1.62x faster                                             |
| crypto_pyaes             | 119 ms                                                       | 73.4 ms: 1.62x faster                                            |
| deepcopy                 | 468 us                                                       | 289 us: 1.62x faster                                             |
| sqlglot_parse            | 2.24 ms                                                      | 1.39 ms: 1.60x faster                                            |
| pyflate                  | 733 ms                                                       | 469 ms: 1.56x faster                                             |
| comprehensions           | 26.7 us                                                      | 17.4 us: 1.53x faster                                            |
| richards                 | 75.1 ms                                                      | 49.5 ms: 1.52x faster                                            |
| sqlglot_transpile        | 2.68 ms                                                      | 1.77 ms: 1.51x faster                                            |
| hexiom                   | 9.42 ms                                                      | 6.24 ms: 1.51x faster                                            |
| nbody                    | 134 ms                                                       | 90.1 ms: 1.49x faster                                            |
| unpickle_pure_python     | 312 us                                                       | 214 us: 1.46x faster                                             |
| spectral_norm            | 139 ms                                                       | 96.0 ms: 1.45x faster                                            |
| coroutines               | 30.3 ms                                                      | 21.1 ms: 1.44x faster                                            |
| pickle_pure_python       | 455 us                                                       | 320 us: 1.42x faster                                             |
| mako                     | 14.7 ms                                                      | 10.7 ms: 1.37x faster                                            |
| regex_compile            | 190 ms                                                       | 139 ms: 1.37x faster                                             |
| fannkuch                 | 483 ms                                                       | 354 ms: 1.36x faster                                             |
| deepcopy_reduce          | 4.01 us                                                      | 2.96 us: 1.35x faster                                            |
| float                    | 111 ms                                                       | 82.2 ms: 1.35x faster                                            |
| logging_simple           | 8.88 us                                                      | 6.57 us: 1.35x faster                                            |
| logging_format           | 9.64 us                                                      | 7.14 us: 1.35x faster                                            |
| thrift                   | 1.18 ms                                                      | 873 us: 1.35x faster                                             |
| pathlib                  | 21.4 ms                                                      | 15.9 ms: 1.35x faster                                            |
| tornado_http             | 157 ms                                                       | 117 ms: 1.34x faster                                             |
| pycparser                | 1.67 sec                                                     | 1.25 sec: 1.34x faster                                           |
| html5lib                 | 94.6 ms                                                      | 71.1 ms: 1.33x faster                                            |
| pprint_pformat           | 2.15 sec                                                     | 1.63 sec: 1.32x faster                                           |
| pprint_safe_repr         | 1.05 sec                                                     | 803 ms: 1.31x faster                                             |
| nqueens                  | 115 ms                                                       | 88.0 ms: 1.31x faster                                            |
| json_dumps               | 14.5 ms                                                      | 11.4 ms: 1.27x faster                                            |
| xml_etree_process        | 75.9 ms                                                      | 60.0 ms: 1.27x faster                                            |
| scimark_fft              | 361 ms                                                       | 286 ms: 1.26x faster                                             |
| sympy_sum                | 193 ms                                                       | 153 ms: 1.26x faster                                             |
| bench_thread_pool        | 1.14 ms                                                      | 908 us: 1.26x faster                                             |
| genshi_text              | 31.4 ms                                                      | 25.0 ms: 1.26x faster                                            |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.06 ms: 1.25x faster                                            |
| 2to3                     | 350 ms                                                       | 282 ms: 1.24x faster                                             |
| sympy_str                | 360 ms                                                       | 293 ms: 1.23x faster                                             |
| django_template          | 50.2 ms                                                      | 41.0 ms: 1.22x faster                                            |
| sqlglot_normalize        | 144 ms                                                       | 118 ms: 1.21x faster                                             |
| sympy_expand             | 600 ms                                                       | 498 ms: 1.20x faster                                             |
| sympy_integrate          | 28.2 ms                                                      | 23.4 ms: 1.20x faster                                            |
| dulwich_log              | 81.1 ms                                                      | 67.5 ms: 1.20x faster                                            |
| mdp                      | 3.01 sec                                                     | 2.51 sec: 1.20x faster                                           |
| json_loads               | 30.3 us                                                      | 25.3 us: 1.20x faster                                            |
| sqlglot_optimize         | 70.1 ms                                                      | 59.1 ms: 1.19x faster                                            |
| docutils                 | 3.41 sec                                                     | 2.90 sec: 1.18x faster                                           |
| tomli_loads              | 2.92 sec                                                     | 2.50 sec: 1.17x faster                                           |
| genshi_xml               | 63.3 ms                                                      | 54.4 ms: 1.16x faster                                            |
| async_generators         | 421 ms                                                       | 364 ms: 1.16x faster                                             |
| json                     | 5.86 ms                                                      | 5.16 ms: 1.14x faster                                            |
| xml_etree_parse          | 160 ms                                                       | 144 ms: 1.11x faster                                             |
| meteor_contest           | 138 ms                                                       | 125 ms: 1.11x faster                                             |
| regex_v8                 | 27.2 ms                                                      | 24.7 ms: 1.10x faster                                            |
| sqlite_synth             | 2.99 us                                                      | 2.74 us: 1.09x faster                                            |
| xml_etree_iterparse      | 110 ms                                                       | 102 ms: 1.09x faster                                             |
| xml_etree_generate       | 92.3 ms                                                      | 85.2 ms: 1.08x faster                                            |
| regex_dna                | 261 ms                                                       | 243 ms: 1.08x faster                                             |
| pidigits                 | 271 ms                                                       | 252 ms: 1.08x faster                                             |
| unpack_sequence          | 59.9 ns                                                      | 58.9 ns: 1.02x faster                                            |
| unpickle_list            | 4.65 us                                                      | 4.58 us: 1.01x faster                                            |
| asyncio_websockets       | 390 ms                                                       | 385 ms: 1.01x faster                                             |
| pickle_list              | 4.12 us                                                      | 4.31 us: 1.05x slower                                            |
| pickle_dict              | 29.5 us                                                      | 31.0 us: 1.05x slower                                            |
| pickle                   | 9.89 us                                                      | 10.5 us: 1.06x slower                                            |
| regex_effbot             | 3.09 ms                                                      | 3.43 ms: 1.11x slower                                            |
| unpickle                 | 13.5 us                                                      | 15.2 us: 1.13x slower                                            |
| telco                    | 7.23 ms                                                      | 8.23 ms: 1.14x slower                                            |
| python_startup_no_site   | 7.33 ms                                                      | 8.96 ms: 1.22x slower                                            |
| python_startup           | 11.5 ms                                                      | 15.0 ms: 1.30x slower                                            |
| coverage                 | 63.3 ms                                                      | 82.6 ms: 1.31x slower                                            |
| gc_traversal             | 3.42 ms                                                      | 5.32 ms: 1.56x slower                                            |
| create_gc_cycles         | 1.76 ms                                                      | 2.97 ms: 1.68x slower                                            |
| bench_mp_pool            | 6.37 ms                                                      | 1.94 sec: 304.00x slower                                         |
| Geometric mean           | (ref)                                                        | 1.23x faster                                                     |
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20241015-3.14.0a1-8cdaca8/bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx

- Geometric mean (including insignificant results): 1.325x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: 1.26x