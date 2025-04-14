# Results vs. 3.10.4

- fork: python
- ref: v3.13.0rc1
- machine: linux-x86_64
- commit hash: e4a3e78
- commit date: 2024-07-31
- overall geometric mean: 1.305x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-pythonperf2-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 289 ms: 1.21x faster                                               |
| chameleon      | 9.44 ms                                                      | 7.33 ms: 1.29x faster                                              |
| docutils       | 3.41 sec                                                     | 2.97 sec: 1.15x faster                                             |
| html5lib       | 94.6 ms                                                      | 72.8 ms: 1.30x faster                                              |
| tornado_http   | 157 ms                                                       | 118 ms: 1.33x faster                                               |
| Geometric mean | (ref)                                                        | 1.25x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-pythonperf2-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|-------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 368 ms: 1.88x faster                                               |
| async_tree_io           | 1.60 sec                                                     | 895 ms: 1.79x faster                                               |
| async_tree_memoization  | 819 ms                                                       | 466 ms: 1.76x faster                                               |
| async_tree_cpu_io_mixed | 936 ms                                                       | 612 ms: 1.53x faster                                               |
| Geometric mean          | (ref)                                                        | 1.73x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-pythonperf2-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 92.0 ms: 1.46x faster                                              |
| float          | 111 ms                                                       | 80.3 ms: 1.38x faster                                              |
| pidigits       | 271 ms                                                       | 254 ms: 1.07x faster                                               |
| Geometric mean | (ref)                                                        | 1.29x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-pythonperf2-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 143 ms: 1.33x faster                                               |
| regex_dna      | 261 ms                                                       | 245 ms: 1.06x faster                                               |
| regex_v8       | 27.2 ms                                                      | 26.4 ms: 1.03x faster                                              |
| regex_effbot   | 3.09 ms                                                      | 3.39 ms: 1.10x slower                                              |
| Geometric mean | (ref)                                                        | 1.07x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-pythonperf2-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 213 us: 1.47x faster                                               |
| pickle_pure_python   | 455 us                                                       | 317 us: 1.44x faster                                               |
| tomli_loads          | 2.92 sec                                                     | 2.19 sec: 1.33x faster                                             |
| json_dumps           | 14.5 ms                                                      | 11.2 ms: 1.30x faster                                              |
| json_loads           | 30.3 us                                                      | 24.1 us: 1.26x faster                                              |
| xml_etree_process    | 75.9 ms                                                      | 61.0 ms: 1.24x faster                                              |
| xml_etree_parse      | 160 ms                                                       | 141 ms: 1.13x faster                                               |
| xml_etree_iterparse  | 110 ms                                                       | 103 ms: 1.07x faster                                               |
| xml_etree_generate   | 92.3 ms                                                      | 86.2 ms: 1.07x faster                                              |
| Geometric mean       | (ref)                                                        | 1.25x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-pythonperf2-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.3 ms: 1.16x slower                                              |
| python_startup_no_site | 7.33 ms                                                      | 8.98 ms: 1.23x slower                                              |
| Geometric mean         | (ref)                                                        | 1.19x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-pythonperf2-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.5 ms: 1.40x faster                                              |
| django_template | 50.2 ms                                                      | 39.3 ms: 1.28x faster                                              |
| genshi_text     | 31.4 ms                                                      | 25.5 ms: 1.23x faster                                              |
| genshi_xml      | 63.3 ms                                                      | 53.4 ms: 1.19x faster                                              |
| Geometric mean  | (ref)                                                        | 1.27x faster                                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-pythonperf2-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|--------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 174 us: 3.09x faster                                               |
| deltablue                | 7.50 ms                                                      | 3.34 ms: 2.25x faster                                              |
| asyncio_tcp              | 779 ms                                                       | 376 ms: 2.07x faster                                               |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.57 sec: 1.97x faster                                             |
| async_tree_none          | 692 ms                                                       | 368 ms: 1.88x faster                                               |
| raytrace                 | 489 ms                                                       | 265 ms: 1.84x faster                                               |
| chaos                    | 109 ms                                                       | 60.1 ms: 1.81x faster                                              |
| async_tree_io            | 1.60 sec                                                     | 895 ms: 1.79x faster                                               |
| async_tree_memoization   | 819 ms                                                       | 466 ms: 1.76x faster                                               |
| logging_silent           | 167 ns                                                       | 97.9 ns: 1.71x faster                                              |
| generators               | 57.3 ms                                                      | 33.9 ms: 1.69x faster                                              |
| scimark_lu               | 167 ms                                                       | 99.0 ms: 1.69x faster                                              |
| go                       | 262 ms                                                       | 158 ms: 1.66x faster                                               |
| crypto_pyaes             | 119 ms                                                       | 73.1 ms: 1.63x faster                                              |
| pylint                   | 566 ms                                                       | 352 ms: 1.61x faster                                               |
| scimark_monte_carlo      | 107 ms                                                       | 67.0 ms: 1.60x faster                                              |
| sqlglot_parse            | 2.24 ms                                                      | 1.41 ms: 1.59x faster                                              |
| richards_super           | 90.6 ms                                                      | 57.4 ms: 1.58x faster                                              |
| pyflate                  | 733 ms                                                       | 469 ms: 1.56x faster                                               |
| comprehensions           | 26.7 us                                                      | 17.2 us: 1.55x faster                                              |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 612 ms: 1.53x faster                                               |
| sqlglot_transpile        | 2.68 ms                                                      | 1.79 ms: 1.50x faster                                              |
| richards                 | 75.1 ms                                                      | 50.9 ms: 1.48x faster                                              |
| hexiom                   | 9.42 ms                                                      | 6.40 ms: 1.47x faster                                              |
| unpickle_pure_python     | 312 us                                                       | 213 us: 1.47x faster                                               |
| nbody                    | 134 ms                                                       | 92.0 ms: 1.46x faster                                              |
| pickle_pure_python       | 455 us                                                       | 317 us: 1.44x faster                                               |
| spectral_norm            | 139 ms                                                       | 97.6 ms: 1.42x faster                                              |
| coroutines               | 30.3 ms                                                      | 21.3 ms: 1.42x faster                                              |
| scimark_sor              | 180 ms                                                       | 127 ms: 1.42x faster                                               |
| mako                     | 14.7 ms                                                      | 10.5 ms: 1.40x faster                                              |
| float                    | 111 ms                                                       | 80.3 ms: 1.38x faster                                              |
| logging_format           | 9.64 us                                                      | 6.99 us: 1.38x faster                                              |
| logging_simple           | 8.88 us                                                      | 6.46 us: 1.37x faster                                              |
| fannkuch                 | 483 ms                                                       | 356 ms: 1.35x faster                                               |
| bench_mp_pool            | 6.37 ms                                                      | 4.71 ms: 1.35x faster                                              |
| tornado_http             | 157 ms                                                       | 118 ms: 1.33x faster                                               |
| tomli_loads              | 2.92 sec                                                     | 2.19 sec: 1.33x faster                                             |
| pycparser                | 1.67 sec                                                     | 1.26 sec: 1.33x faster                                             |
| regex_compile            | 190 ms                                                       | 143 ms: 1.33x faster                                               |
| thrift                   | 1.18 ms                                                      | 888 us: 1.32x faster                                               |
| html5lib                 | 94.6 ms                                                      | 72.8 ms: 1.30x faster                                              |
| deepcopy_memo            | 49.8 us                                                      | 38.3 us: 1.30x faster                                              |
| json_dumps               | 14.5 ms                                                      | 11.2 ms: 1.30x faster                                              |
| chameleon                | 9.44 ms                                                      | 7.33 ms: 1.29x faster                                              |
| pprint_pformat           | 2.15 sec                                                     | 1.69 sec: 1.28x faster                                             |
| django_template          | 50.2 ms                                                      | 39.3 ms: 1.28x faster                                              |
| nqueens                  | 115 ms                                                       | 90.4 ms: 1.27x faster                                              |
| dulwich_log              | 81.1 ms                                                      | 64.2 ms: 1.26x faster                                              |
| pprint_safe_repr         | 1.05 sec                                                     | 831 ms: 1.26x faster                                               |
| json_loads               | 30.3 us                                                      | 24.1 us: 1.26x faster                                              |
| bench_thread_pool        | 1.14 ms                                                      | 907 us: 1.26x faster                                               |
| xml_etree_process        | 75.9 ms                                                      | 61.0 ms: 1.24x faster                                              |
| pathlib                  | 21.4 ms                                                      | 17.2 ms: 1.24x faster                                              |
| sympy_sum                | 193 ms                                                       | 156 ms: 1.24x faster                                               |
| genshi_text              | 31.4 ms                                                      | 25.5 ms: 1.23x faster                                              |
| deepcopy                 | 468 us                                                       | 385 us: 1.21x faster                                               |
| mypy2                    | 933 ms                                                       | 769 ms: 1.21x faster                                               |
| 2to3                     | 350 ms                                                       | 289 ms: 1.21x faster                                               |
| sympy_str                | 360 ms                                                       | 298 ms: 1.21x faster                                               |
| mdp                      | 3.01 sec                                                     | 2.49 sec: 1.21x faster                                             |
| sympy_integrate          | 28.2 ms                                                      | 23.5 ms: 1.20x faster                                              |
| dask                     | 472 ms                                                       | 398 ms: 1.19x faster                                               |
| genshi_xml               | 63.3 ms                                                      | 53.4 ms: 1.19x faster                                              |
| sqlglot_normalize        | 144 ms                                                       | 121 ms: 1.18x faster                                               |
| sympy_expand             | 600 ms                                                       | 508 ms: 1.18x faster                                               |
| sqlglot_optimize         | 70.1 ms                                                      | 59.7 ms: 1.17x faster                                              |
| scimark_fft              | 361 ms                                                       | 308 ms: 1.17x faster                                               |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.38 ms: 1.16x faster                                              |
| docutils                 | 3.41 sec                                                     | 2.97 sec: 1.15x faster                                             |
| deepcopy_reduce          | 4.01 us                                                      | 3.50 us: 1.15x faster                                              |
| async_generators         | 421 ms                                                       | 370 ms: 1.14x faster                                               |
| xml_etree_parse          | 160 ms                                                       | 141 ms: 1.13x faster                                               |
| json                     | 5.86 ms                                                      | 5.20 ms: 1.13x faster                                              |
| xml_etree_iterparse      | 110 ms                                                       | 103 ms: 1.07x faster                                               |
| meteor_contest           | 138 ms                                                       | 129 ms: 1.07x faster                                               |
| xml_etree_generate       | 92.3 ms                                                      | 86.2 ms: 1.07x faster                                              |
| pidigits                 | 271 ms                                                       | 254 ms: 1.07x faster                                               |
| regex_dna                | 261 ms                                                       | 245 ms: 1.06x faster                                               |
| regex_v8                 | 27.2 ms                                                      | 26.4 ms: 1.03x faster                                              |
| regex_effbot             | 3.09 ms                                                      | 3.39 ms: 1.10x slower                                              |
| create_gc_cycles         | 1.76 ms                                                      | 2.01 ms: 1.14x slower                                              |
| python_startup           | 11.5 ms                                                      | 13.3 ms: 1.16x slower                                              |
| telco                    | 7.23 ms                                                      | 8.43 ms: 1.17x slower                                              |
| python_startup_no_site   | 7.33 ms                                                      | 8.98 ms: 1.23x slower                                              |
| coverage                 | 63.3 ms                                                      | 79.8 ms: 1.26x slower                                              |
| gc_traversal             | 3.42 ms                                                      | 4.45 ms: 1.30x slower                                              |
| Geometric mean           | (ref)                                                        | 1.32x faster                                                       |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240731-3.13.0rc1-e4a3e78/bm-20240731-pythonperf2-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

- Geometric mean (including insignificant results): 1.305x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.13x