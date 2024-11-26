# Results vs. 3.10.4

- fork: python
- ref: e913d2c87f1ae4e7a4ae
- machine: linux-x86_64
- commit hash: e913d2c
- commit date: 2024-08-15
- overall geometric mean: 1.337x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240815-pythonperf2-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 285 ms: 1.23x faster                                                        |
| docutils       | 3.41 sec                                                     | 2.97 sec: 1.15x faster                                                      |
| html5lib       | 94.6 ms                                                      | 72.7 ms: 1.30x faster                                                       |
| tornado_http   | 157 ms                                                       | 118 ms: 1.33x faster                                                        |
| Geometric mean | (ref)                                                        | 1.25x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240815-pythonperf2-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 331 ms: 2.09x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 400 ms: 2.05x faster                                                        |
| async_tree_io           | 1.60 sec                                                     | 808 ms: 1.98x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 575 ms: 1.63x faster                                                        |
| Geometric mean          | (ref)                                                        | 1.93x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240815-pythonperf2-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 89.8 ms: 1.49x faster                                                       |
| float          | 111 ms                                                       | 82.3 ms: 1.35x faster                                                       |
| pidigits       | 271 ms                                                       | 253 ms: 1.07x faster                                                        |
| Geometric mean | (ref)                                                        | 1.29x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240815-pythonperf2-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 139 ms: 1.37x faster                                                        |
| regex_dna      | 261 ms                                                       | 234 ms: 1.12x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 25.6 ms: 1.06x faster                                                       |
| regex_effbot   | 3.09 ms                                                      | 3.56 ms: 1.15x slower                                                       |
| Geometric mean | (ref)                                                        | 1.09x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240815-pythonperf2-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 213 us: 1.46x faster                                                        |
| pickle_pure_python   | 455 us                                                       | 313 us: 1.45x faster                                                        |
| json_dumps           | 14.5 ms                                                      | 10.7 ms: 1.36x faster                                                       |
| tomli_loads          | 2.92 sec                                                     | 2.26 sec: 1.29x faster                                                      |
| xml_etree_process    | 75.9 ms                                                      | 58.9 ms: 1.29x faster                                                       |
| json_loads           | 30.3 us                                                      | 25.2 us: 1.20x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 144 ms: 1.11x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 100 ms: 1.10x faster                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 83.8 ms: 1.10x faster                                                       |
| Geometric mean       | (ref)                                                        | 1.26x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240815-pythonperf2-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.3 ms: 1.16x slower                                                       |
| python_startup_no_site | 7.33 ms                                                      | 9.04 ms: 1.23x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240815-pythonperf2-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.3 ms: 1.42x faster                                                       |
| django_template | 50.2 ms                                                      | 39.5 ms: 1.27x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 25.1 ms: 1.25x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 55.3 ms: 1.14x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.27x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240815-pythonperf2-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 175 us: 3.06x faster                                                        |
| deltablue                | 7.50 ms                                                      | 3.41 ms: 2.20x faster                                                       |
| async_tree_none          | 692 ms                                                       | 331 ms: 2.09x faster                                                        |
| asyncio_tcp              | 779 ms                                                       | 374 ms: 2.08x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 400 ms: 2.05x faster                                                        |
| generators               | 57.3 ms                                                      | 28.7 ms: 1.99x faster                                                       |
| async_tree_io            | 1.60 sec                                                     | 808 ms: 1.98x faster                                                        |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.96x faster                                                      |
| raytrace                 | 489 ms                                                       | 265 ms: 1.84x faster                                                        |
| scimark_lu               | 167 ms                                                       | 94.1 ms: 1.77x faster                                                       |
| chaos                    | 109 ms                                                       | 61.4 ms: 1.77x faster                                                       |
| logging_silent           | 167 ns                                                       | 98.1 ns: 1.71x faster                                                       |
| scimark_sor              | 180 ms                                                       | 108 ms: 1.67x faster                                                        |
| deepcopy_memo            | 49.8 us                                                      | 30.3 us: 1.64x faster                                                       |
| crypto_pyaes             | 119 ms                                                       | 72.8 ms: 1.64x faster                                                       |
| pylint                   | 566 ms                                                       | 346 ms: 1.63x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 575 ms: 1.63x faster                                                        |
| go                       | 262 ms                                                       | 163 ms: 1.61x faster                                                        |
| sqlglot_parse            | 2.24 ms                                                      | 1.40 ms: 1.60x faster                                                       |
| deepcopy                 | 468 us                                                       | 292 us: 1.60x faster                                                        |
| richards_super           | 90.6 ms                                                      | 56.7 ms: 1.60x faster                                                       |
| scimark_monte_carlo      | 107 ms                                                       | 67.4 ms: 1.59x faster                                                       |
| comprehensions           | 26.7 us                                                      | 17.3 us: 1.54x faster                                                       |
| sqlglot_transpile        | 2.68 ms                                                      | 1.77 ms: 1.51x faster                                                       |
| richards                 | 75.1 ms                                                      | 50.1 ms: 1.50x faster                                                       |
| nbody                    | 134 ms                                                       | 89.8 ms: 1.49x faster                                                       |
| pyflate                  | 733 ms                                                       | 491 ms: 1.49x faster                                                        |
| hexiom                   | 9.42 ms                                                      | 6.32 ms: 1.49x faster                                                       |
| unpickle_pure_python     | 312 us                                                       | 213 us: 1.46x faster                                                        |
| pickle_pure_python       | 455 us                                                       | 313 us: 1.45x faster                                                        |
| spectral_norm            | 139 ms                                                       | 96.1 ms: 1.45x faster                                                       |
| logging_simple           | 8.88 us                                                      | 6.18 us: 1.44x faster                                                       |
| mako                     | 14.7 ms                                                      | 10.3 ms: 1.42x faster                                                       |
| logging_format           | 9.64 us                                                      | 6.80 us: 1.42x faster                                                       |
| bench_mp_pool            | 6.37 ms                                                      | 4.51 ms: 1.41x faster                                                       |
| coroutines               | 30.3 ms                                                      | 22.1 ms: 1.37x faster                                                       |
| regex_compile            | 190 ms                                                       | 139 ms: 1.37x faster                                                        |
| thrift                   | 1.18 ms                                                      | 863 us: 1.36x faster                                                        |
| json_dumps               | 14.5 ms                                                      | 10.7 ms: 1.36x faster                                                       |
| pycparser                | 1.67 sec                                                     | 1.24 sec: 1.35x faster                                                      |
| float                    | 111 ms                                                       | 82.3 ms: 1.35x faster                                                       |
| deepcopy_reduce          | 4.01 us                                                      | 2.97 us: 1.35x faster                                                       |
| pathlib                  | 21.4 ms                                                      | 16.0 ms: 1.34x faster                                                       |
| tornado_http             | 157 ms                                                       | 118 ms: 1.33x faster                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 870 us: 1.31x faster                                                        |
| html5lib                 | 94.6 ms                                                      | 72.7 ms: 1.30x faster                                                       |
| tomli_loads              | 2.92 sec                                                     | 2.26 sec: 1.29x faster                                                      |
| fannkuch                 | 483 ms                                                       | 374 ms: 1.29x faster                                                        |
| xml_etree_process        | 75.9 ms                                                      | 58.9 ms: 1.29x faster                                                       |
| nqueens                  | 115 ms                                                       | 90.4 ms: 1.27x faster                                                       |
| django_template          | 50.2 ms                                                      | 39.5 ms: 1.27x faster                                                       |
| pprint_pformat           | 2.15 sec                                                     | 1.70 sec: 1.27x faster                                                      |
| sympy_sum                | 193 ms                                                       | 153 ms: 1.26x faster                                                        |
| genshi_text              | 31.4 ms                                                      | 25.1 ms: 1.25x faster                                                       |
| pprint_safe_repr         | 1.05 sec                                                     | 839 ms: 1.25x faster                                                        |
| sympy_str                | 360 ms                                                       | 293 ms: 1.23x faster                                                        |
| 2to3                     | 350 ms                                                       | 285 ms: 1.23x faster                                                        |
| sympy_integrate          | 28.2 ms                                                      | 23.2 ms: 1.21x faster                                                       |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.19 ms: 1.21x faster                                                       |
| scimark_fft              | 361 ms                                                       | 299 ms: 1.21x faster                                                        |
| sympy_expand             | 600 ms                                                       | 499 ms: 1.20x faster                                                        |
| json_loads               | 30.3 us                                                      | 25.2 us: 1.20x faster                                                       |
| async_generators         | 421 ms                                                       | 352 ms: 1.19x faster                                                        |
| sqlglot_normalize        | 144 ms                                                       | 121 ms: 1.19x faster                                                        |
| sqlglot_optimize         | 70.1 ms                                                      | 59.0 ms: 1.19x faster                                                       |
| mdp                      | 3.01 sec                                                     | 2.54 sec: 1.18x faster                                                      |
| docutils                 | 3.41 sec                                                     | 2.97 sec: 1.15x faster                                                      |
| genshi_xml               | 63.3 ms                                                      | 55.3 ms: 1.14x faster                                                       |
| regex_dna                | 261 ms                                                       | 234 ms: 1.12x faster                                                        |
| xml_etree_parse          | 160 ms                                                       | 144 ms: 1.11x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 100 ms: 1.10x faster                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 83.8 ms: 1.10x faster                                                       |
| meteor_contest           | 138 ms                                                       | 126 ms: 1.10x faster                                                        |
| json                     | 5.86 ms                                                      | 5.41 ms: 1.08x faster                                                       |
| pidigits                 | 271 ms                                                       | 253 ms: 1.07x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 25.6 ms: 1.06x faster                                                       |
| telco                    | 7.23 ms                                                      | 7.90 ms: 1.09x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 1.98 ms: 1.12x slower                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.56 ms: 1.15x slower                                                       |
| python_startup           | 11.5 ms                                                      | 13.3 ms: 1.16x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 9.04 ms: 1.23x slower                                                       |
| coverage                 | 63.3 ms                                                      | 79.6 ms: 1.26x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 4.40 ms: 1.29x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.35x faster                                                                |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240815-3.14.0a0-e913d2c/bm-20240815-pythonperf2-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

- Geometric mean (including insignificant results): 1.337x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: 1.13x