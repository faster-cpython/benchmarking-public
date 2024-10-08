# Results vs. 3.10.4

- fork: mdboom
- ref: unicodekeys_compare_
- machine: linux-x86_64
- commit hash: 23c2a0c
- commit date: 2024-08-29
- overall geometric mean: 1.36x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf2-x86_64-mdboom-unicodekeys_compare_-3.14.0a0-23c2a0c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 283 ms: 1.24x faster                                                        |
| docutils       | 3.41 sec                                                     | 2.91 sec: 1.17x faster                                                      |
| html5lib       | 94.6 ms                                                      | 70.7 ms: 1.34x faster                                                       |
| tornado_http   | 157 ms                                                       | 116 ms: 1.35x faster                                                        |
| Geometric mean | (ref)                                                        | 1.27x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf2-x86_64-mdboom-unicodekeys_compare_-3.14.0a0-23c2a0c |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 320 ms: 2.16x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 399 ms: 2.05x faster                                                        |
| async_tree_io           | 1.60 sec                                                     | 804 ms: 1.99x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 572 ms: 1.64x faster                                                        |
| Geometric mean          | (ref)                                                        | 1.95x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf2-x86_64-mdboom-unicodekeys_compare_-3.14.0a0-23c2a0c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 85.2 ms: 1.57x faster                                                       |
| float          | 111 ms                                                       | 81.0 ms: 1.37x faster                                                       |
| pidigits       | 271 ms                                                       | 253 ms: 1.07x faster                                                        |
| Geometric mean | (ref)                                                        | 1.32x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf2-x86_64-mdboom-unicodekeys_compare_-3.14.0a0-23c2a0c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 140 ms: 1.36x faster                                                        |
| regex_dna      | 261 ms                                                       | 233 ms: 1.12x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 26.2 ms: 1.04x faster                                                       |
| regex_effbot   | 3.09 ms                                                      | 3.45 ms: 1.12x slower                                                       |
| Geometric mean | (ref)                                                        | 1.09x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf2-x86_64-mdboom-unicodekeys_compare_-3.14.0a0-23c2a0c |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                       | 313 us: 1.46x faster                                                        |
| unpickle_pure_python | 312 us                                                       | 221 us: 1.41x faster                                                        |
| json_dumps           | 14.5 ms                                                      | 10.9 ms: 1.33x faster                                                       |
| xml_etree_process    | 75.9 ms                                                      | 59.8 ms: 1.27x faster                                                       |
| json_loads           | 30.3 us                                                      | 25.2 us: 1.20x faster                                                       |
| tomli_loads          | 2.92 sec                                                     | 2.57 sec: 1.13x faster                                                      |
| xml_etree_parse      | 160 ms                                                       | 145 ms: 1.10x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 101 ms: 1.10x faster                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 84.9 ms: 1.09x faster                                                       |
| Geometric mean       | (ref)                                                        | 1.23x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf2-x86_64-mdboom-unicodekeys_compare_-3.14.0a0-23c2a0c |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                                       |
| python_startup_no_site | 7.33 ms                                                      | 9.07 ms: 1.24x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf2-x86_64-mdboom-unicodekeys_compare_-3.14.0a0-23c2a0c |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.3 ms: 1.42x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 24.7 ms: 1.27x faster                                                       |
| django_template | 50.2 ms                                                      | 40.7 ms: 1.23x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 55.2 ms: 1.15x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.27x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf2-x86_64-mdboom-unicodekeys_compare_-3.14.0a0-23c2a0c |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 170 us: 3.16x faster                                                        |
| deltablue                | 7.50 ms                                                      | 3.44 ms: 2.18x faster                                                       |
| async_tree_none          | 692 ms                                                       | 320 ms: 2.16x faster                                                        |
| asyncio_tcp              | 779 ms                                                       | 371 ms: 2.10x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 399 ms: 2.05x faster                                                        |
| generators               | 57.3 ms                                                      | 28.7 ms: 2.00x faster                                                       |
| async_tree_io            | 1.60 sec                                                     | 804 ms: 1.99x faster                                                        |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.97x faster                                                      |
| go                       | 262 ms                                                       | 134 ms: 1.95x faster                                                        |
| raytrace                 | 489 ms                                                       | 276 ms: 1.77x faster                                                        |
| chaos                    | 109 ms                                                       | 61.9 ms: 1.75x faster                                                       |
| scimark_lu               | 167 ms                                                       | 95.2 ms: 1.75x faster                                                       |
| logging_silent           | 167 ns                                                       | 98.0 ns: 1.71x faster                                                       |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 572 ms: 1.64x faster                                                        |
| deepcopy_memo            | 49.8 us                                                      | 30.5 us: 1.63x faster                                                       |
| pylint                   | 566 ms                                                       | 348 ms: 1.63x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 73.3 ms: 1.63x faster                                                       |
| deepcopy                 | 468 us                                                       | 288 us: 1.62x faster                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 66.5 ms: 1.61x faster                                                       |
| richards_super           | 90.6 ms                                                      | 56.2 ms: 1.61x faster                                                       |
| sqlglot_parse            | 2.24 ms                                                      | 1.42 ms: 1.58x faster                                                       |
| nbody                    | 134 ms                                                       | 85.2 ms: 1.57x faster                                                       |
| comprehensions           | 26.7 us                                                      | 17.2 us: 1.55x faster                                                       |
| pyflate                  | 733 ms                                                       | 479 ms: 1.53x faster                                                        |
| scimark_sor              | 180 ms                                                       | 119 ms: 1.52x faster                                                        |
| hexiom                   | 9.42 ms                                                      | 6.30 ms: 1.49x faster                                                       |
| sqlglot_transpile        | 2.68 ms                                                      | 1.80 ms: 1.49x faster                                                       |
| richards                 | 75.1 ms                                                      | 50.4 ms: 1.49x faster                                                       |
| pickle_pure_python       | 455 us                                                       | 313 us: 1.46x faster                                                        |
| spectral_norm            | 139 ms                                                       | 96.6 ms: 1.44x faster                                                       |
| mako                     | 14.7 ms                                                      | 10.3 ms: 1.42x faster                                                       |
| logging_simple           | 8.88 us                                                      | 6.26 us: 1.42x faster                                                       |
| unpickle_pure_python     | 312 us                                                       | 221 us: 1.41x faster                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 4.52 ms: 1.41x faster                                                       |
| logging_format           | 9.64 us                                                      | 6.84 us: 1.41x faster                                                       |
| coroutines               | 30.3 ms                                                      | 21.5 ms: 1.41x faster                                                       |
| float                    | 111 ms                                                       | 81.0 ms: 1.37x faster                                                       |
| deepcopy_reduce          | 4.01 us                                                      | 2.95 us: 1.36x faster                                                       |
| regex_compile            | 190 ms                                                       | 140 ms: 1.36x faster                                                        |
| tornado_http             | 157 ms                                                       | 116 ms: 1.35x faster                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 849 us: 1.34x faster                                                        |
| pathlib                  | 21.4 ms                                                      | 15.9 ms: 1.34x faster                                                       |
| fannkuch                 | 483 ms                                                       | 359 ms: 1.34x faster                                                        |
| thrift                   | 1.18 ms                                                      | 876 us: 1.34x faster                                                        |
| pycparser                | 1.67 sec                                                     | 1.25 sec: 1.34x faster                                                      |
| html5lib                 | 94.6 ms                                                      | 70.7 ms: 1.34x faster                                                       |
| json_dumps               | 14.5 ms                                                      | 10.9 ms: 1.33x faster                                                       |
| pprint_pformat           | 2.15 sec                                                     | 1.65 sec: 1.31x faster                                                      |
| pprint_safe_repr         | 1.05 sec                                                     | 809 ms: 1.30x faster                                                        |
| nqueens                  | 115 ms                                                       | 89.4 ms: 1.29x faster                                                       |
| sympy_sum                | 193 ms                                                       | 150 ms: 1.28x faster                                                        |
| genshi_text              | 31.4 ms                                                      | 24.7 ms: 1.27x faster                                                       |
| xml_etree_process        | 75.9 ms                                                      | 59.8 ms: 1.27x faster                                                       |
| sympy_str                | 360 ms                                                       | 289 ms: 1.25x faster                                                        |
| 2to3                     | 350 ms                                                       | 283 ms: 1.24x faster                                                        |
| django_template          | 50.2 ms                                                      | 40.7 ms: 1.23x faster                                                       |
| sympy_integrate          | 28.2 ms                                                      | 22.9 ms: 1.23x faster                                                       |
| sympy_expand             | 600 ms                                                       | 495 ms: 1.21x faster                                                        |
| mdp                      | 3.01 sec                                                     | 2.49 sec: 1.21x faster                                                      |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.22 ms: 1.20x faster                                                       |
| json_loads               | 30.3 us                                                      | 25.2 us: 1.20x faster                                                       |
| scimark_fft              | 361 ms                                                       | 301 ms: 1.20x faster                                                        |
| sqlglot_normalize        | 144 ms                                                       | 120 ms: 1.20x faster                                                        |
| sqlglot_optimize         | 70.1 ms                                                      | 59.1 ms: 1.19x faster                                                       |
| docutils                 | 3.41 sec                                                     | 2.91 sec: 1.17x faster                                                      |
| genshi_xml               | 63.3 ms                                                      | 55.2 ms: 1.15x faster                                                       |
| async_generators         | 421 ms                                                       | 369 ms: 1.14x faster                                                        |
| tomli_loads              | 2.92 sec                                                     | 2.57 sec: 1.13x faster                                                      |
| regex_dna                | 261 ms                                                       | 233 ms: 1.12x faster                                                        |
| json                     | 5.86 ms                                                      | 5.27 ms: 1.11x faster                                                       |
| xml_etree_parse          | 160 ms                                                       | 145 ms: 1.10x faster                                                        |
| meteor_contest           | 138 ms                                                       | 126 ms: 1.10x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 101 ms: 1.10x faster                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 84.9 ms: 1.09x faster                                                       |
| pidigits                 | 271 ms                                                       | 253 ms: 1.07x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 26.2 ms: 1.04x faster                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.45 ms: 1.12x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 1.98 ms: 1.12x slower                                                       |
| telco                    | 7.23 ms                                                      | 8.30 ms: 1.15x slower                                                       |
| python_startup           | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 9.07 ms: 1.24x slower                                                       |
| coverage                 | 63.3 ms                                                      | 79.6 ms: 1.26x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 4.47 ms: 1.31x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.36x faster                                                                |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240829-3.14.0a0-23c2a0c/bm-20240829-pythonperf2-x86_64-mdboom-unicodekeys_compare_-3.14.0a0-23c2a0c.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: 1.13x