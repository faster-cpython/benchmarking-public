# Results vs. 3.10.4

- fork: bdraco
- ref: speed_up_async_sched
- machine: linux-x86_64
- commit hash: f78838c
- commit date: 2024-08-24
- overall geometric mean: 1.35x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240824-pythonperf2-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 281 ms: 1.24x faster                                                        |
| docutils       | 3.41 sec                                                     | 2.97 sec: 1.15x faster                                                      |
| html5lib       | 94.6 ms                                                      | 73.1 ms: 1.30x faster                                                       |
| tornado_http   | 157 ms                                                       | 117 ms: 1.35x faster                                                        |
| Geometric mean | (ref)                                                        | 1.26x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240824-pythonperf2-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 318 ms: 2.18x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 404 ms: 2.03x faster                                                        |
| async_tree_io           | 1.60 sec                                                     | 827 ms: 1.93x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 558 ms: 1.68x faster                                                        |
| Geometric mean          | (ref)                                                        | 1.94x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240824-pythonperf2-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 88.1 ms: 1.52x faster                                                       |
| float          | 111 ms                                                       | 78.9 ms: 1.41x faster                                                       |
| pidigits       | 271 ms                                                       | 252 ms: 1.08x faster                                                        |
| Geometric mean | (ref)                                                        | 1.32x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240824-pythonperf2-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 140 ms: 1.36x faster                                                        |
| regex_dna      | 261 ms                                                       | 234 ms: 1.11x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 25.3 ms: 1.07x faster                                                       |
| regex_effbot   | 3.09 ms                                                      | 3.51 ms: 1.14x slower                                                       |
| Geometric mean | (ref)                                                        | 1.09x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240824-pythonperf2-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 216 us: 1.44x faster                                                        |
| pickle_pure_python   | 455 us                                                       | 317 us: 1.44x faster                                                        |
| json_dumps           | 14.5 ms                                                      | 10.8 ms: 1.34x faster                                                       |
| xml_etree_process    | 75.9 ms                                                      | 60.8 ms: 1.25x faster                                                       |
| json_loads           | 30.3 us                                                      | 25.1 us: 1.21x faster                                                       |
| tomli_loads          | 2.92 sec                                                     | 2.56 sec: 1.14x faster                                                      |
| xml_etree_parse      | 160 ms                                                       | 144 ms: 1.11x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 102 ms: 1.09x faster                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 87.4 ms: 1.06x faster                                                       |
| Geometric mean       | (ref)                                                        | 1.22x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240824-pythonperf2-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                                       |
| python_startup_no_site | 7.33 ms                                                      | 9.05 ms: 1.24x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240824-pythonperf2-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.4 ms: 1.41x faster                                                       |
| django_template | 50.2 ms                                                      | 39.0 ms: 1.29x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 24.9 ms: 1.26x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 54.3 ms: 1.17x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.28x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240824-pythonperf2-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 172 us: 3.13x faster                                                        |
| deltablue                | 7.50 ms                                                      | 3.44 ms: 2.18x faster                                                       |
| async_tree_none          | 692 ms                                                       | 318 ms: 2.18x faster                                                        |
| asyncio_tcp              | 779 ms                                                       | 366 ms: 2.13x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 404 ms: 2.03x faster                                                        |
| generators               | 57.3 ms                                                      | 28.8 ms: 1.99x faster                                                       |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.59 sec: 1.96x faster                                                      |
| async_tree_io            | 1.60 sec                                                     | 827 ms: 1.93x faster                                                        |
| raytrace                 | 489 ms                                                       | 267 ms: 1.83x faster                                                        |
| chaos                    | 109 ms                                                       | 61.1 ms: 1.78x faster                                                       |
| scimark_lu               | 167 ms                                                       | 96.8 ms: 1.72x faster                                                       |
| deepcopy_memo            | 49.8 us                                                      | 29.0 us: 1.71x faster                                                       |
| logging_silent           | 167 ns                                                       | 99.3 ns: 1.68x faster                                                       |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 558 ms: 1.68x faster                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 65.1 ms: 1.65x faster                                                       |
| deepcopy                 | 468 us                                                       | 285 us: 1.64x faster                                                        |
| richards_super           | 90.6 ms                                                      | 56.0 ms: 1.62x faster                                                       |
| pylint                   | 566 ms                                                       | 350 ms: 1.62x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 74.6 ms: 1.60x faster                                                       |
| sqlglot_parse            | 2.24 ms                                                      | 1.43 ms: 1.57x faster                                                       |
| pyflate                  | 733 ms                                                       | 474 ms: 1.55x faster                                                        |
| comprehensions           | 26.7 us                                                      | 17.3 us: 1.54x faster                                                       |
| scimark_sor              | 180 ms                                                       | 118 ms: 1.53x faster                                                        |
| nbody                    | 134 ms                                                       | 88.1 ms: 1.52x faster                                                       |
| hexiom                   | 9.42 ms                                                      | 6.23 ms: 1.51x faster                                                       |
| richards                 | 75.1 ms                                                      | 50.3 ms: 1.49x faster                                                       |
| sqlglot_transpile        | 2.68 ms                                                      | 1.80 ms: 1.49x faster                                                       |
| go                       | 262 ms                                                       | 181 ms: 1.45x faster                                                        |
| unpickle_pure_python     | 312 us                                                       | 216 us: 1.44x faster                                                        |
| spectral_norm            | 139 ms                                                       | 96.8 ms: 1.44x faster                                                       |
| pickle_pure_python       | 455 us                                                       | 317 us: 1.44x faster                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 4.48 ms: 1.42x faster                                                       |
| coroutines               | 30.3 ms                                                      | 21.3 ms: 1.42x faster                                                       |
| float                    | 111 ms                                                       | 78.9 ms: 1.41x faster                                                       |
| mako                     | 14.7 ms                                                      | 10.4 ms: 1.41x faster                                                       |
| thrift                   | 1.18 ms                                                      | 846 us: 1.39x faster                                                        |
| fannkuch                 | 483 ms                                                       | 352 ms: 1.37x faster                                                        |
| deepcopy_reduce          | 4.01 us                                                      | 2.93 us: 1.37x faster                                                       |
| logging_simple           | 8.88 us                                                      | 6.52 us: 1.36x faster                                                       |
| regex_compile            | 190 ms                                                       | 140 ms: 1.36x faster                                                        |
| pathlib                  | 21.4 ms                                                      | 15.9 ms: 1.35x faster                                                       |
| tornado_http             | 157 ms                                                       | 117 ms: 1.35x faster                                                        |
| json_dumps               | 14.5 ms                                                      | 10.8 ms: 1.34x faster                                                       |
| logging_format           | 9.64 us                                                      | 7.19 us: 1.34x faster                                                       |
| bench_thread_pool        | 1.14 ms                                                      | 859 us: 1.33x faster                                                        |
| pycparser                | 1.67 sec                                                     | 1.27 sec: 1.32x faster                                                      |
| pprint_pformat           | 2.15 sec                                                     | 1.64 sec: 1.32x faster                                                      |
| pprint_safe_repr         | 1.05 sec                                                     | 807 ms: 1.30x faster                                                        |
| html5lib                 | 94.6 ms                                                      | 73.1 ms: 1.30x faster                                                       |
| django_template          | 50.2 ms                                                      | 39.0 ms: 1.29x faster                                                       |
| nqueens                  | 115 ms                                                       | 90.0 ms: 1.28x faster                                                       |
| sympy_sum                | 193 ms                                                       | 152 ms: 1.27x faster                                                        |
| genshi_text              | 31.4 ms                                                      | 24.9 ms: 1.26x faster                                                       |
| xml_etree_process        | 75.9 ms                                                      | 60.8 ms: 1.25x faster                                                       |
| 2to3                     | 350 ms                                                       | 281 ms: 1.24x faster                                                        |
| sympy_str                | 360 ms                                                       | 290 ms: 1.24x faster                                                        |
| sympy_integrate          | 28.2 ms                                                      | 23.0 ms: 1.22x faster                                                       |
| mdp                      | 3.01 sec                                                     | 2.48 sec: 1.21x faster                                                      |
| json_loads               | 30.3 us                                                      | 25.1 us: 1.21x faster                                                       |
| sqlglot_normalize        | 144 ms                                                       | 119 ms: 1.21x faster                                                        |
| scimark_fft              | 361 ms                                                       | 300 ms: 1.20x faster                                                        |
| sympy_expand             | 600 ms                                                       | 499 ms: 1.20x faster                                                        |
| sqlglot_optimize         | 70.1 ms                                                      | 59.0 ms: 1.19x faster                                                       |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.34 ms: 1.17x faster                                                       |
| genshi_xml               | 63.3 ms                                                      | 54.3 ms: 1.17x faster                                                       |
| docutils                 | 3.41 sec                                                     | 2.97 sec: 1.15x faster                                                      |
| async_generators         | 421 ms                                                       | 368 ms: 1.14x faster                                                        |
| tomli_loads              | 2.92 sec                                                     | 2.56 sec: 1.14x faster                                                      |
| regex_dna                | 261 ms                                                       | 234 ms: 1.11x faster                                                        |
| xml_etree_parse          | 160 ms                                                       | 144 ms: 1.11x faster                                                        |
| meteor_contest           | 138 ms                                                       | 126 ms: 1.10x faster                                                        |
| json                     | 5.86 ms                                                      | 5.40 ms: 1.09x faster                                                       |
| xml_etree_iterparse      | 110 ms                                                       | 102 ms: 1.09x faster                                                        |
| pidigits                 | 271 ms                                                       | 252 ms: 1.08x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 25.3 ms: 1.07x faster                                                       |
| xml_etree_generate       | 92.3 ms                                                      | 87.4 ms: 1.06x faster                                                       |
| telco                    | 7.23 ms                                                      | 8.18 ms: 1.13x slower                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.51 ms: 1.14x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 2.02 ms: 1.15x slower                                                       |
| python_startup           | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 9.05 ms: 1.24x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 4.48 ms: 1.31x slower                                                       |
| coverage                 | 63.3 ms                                                      | 83.1 ms: 1.31x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.35x faster                                                                |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240824-3.14.0a0-f78838c/bm-20240824-pythonperf2-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: 1.13x