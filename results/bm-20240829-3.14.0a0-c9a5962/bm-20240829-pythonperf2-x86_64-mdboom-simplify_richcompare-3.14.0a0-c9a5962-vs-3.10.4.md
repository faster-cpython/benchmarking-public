# Results vs. 3.10.4

- fork: mdboom
- ref: simplify_richcompare
- machine: linux-x86_64
- commit hash: c9a5962
- commit date: 2024-08-29
- overall geometric mean: 1.36x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 281 ms: 1.24x faster                                                        |
| docutils       | 3.41 sec                                                     | 2.91 sec: 1.17x faster                                                      |
| html5lib       | 94.6 ms                                                      | 69.2 ms: 1.37x faster                                                       |
| tornado_http   | 157 ms                                                       | 115 ms: 1.37x faster                                                        |
| Geometric mean | (ref)                                                        | 1.29x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 318 ms: 2.17x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 395 ms: 2.07x faster                                                        |
| async_tree_io           | 1.60 sec                                                     | 817 ms: 1.96x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 570 ms: 1.64x faster                                                        |
| Geometric mean          | (ref)                                                        | 1.95x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 84.1 ms: 1.59x faster                                                       |
| float          | 111 ms                                                       | 78.9 ms: 1.41x faster                                                       |
| pidigits       | 271 ms                                                       | 253 ms: 1.07x faster                                                        |
| Geometric mean | (ref)                                                        | 1.34x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 139 ms: 1.36x faster                                                        |
| regex_dna      | 261 ms                                                       | 254 ms: 1.03x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 27.3 ms: 1.01x slower                                                       |
| regex_effbot   | 3.09 ms                                                      | 3.42 ms: 1.11x slower                                                       |
| Geometric mean | (ref)                                                        | 1.06x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 212 us: 1.47x faster                                                        |
| pickle_pure_python   | 455 us                                                       | 313 us: 1.45x faster                                                        |
| json_dumps           | 14.5 ms                                                      | 10.8 ms: 1.35x faster                                                       |
| xml_etree_process    | 75.9 ms                                                      | 58.8 ms: 1.29x faster                                                       |
| json_loads           | 30.3 us                                                      | 25.1 us: 1.21x faster                                                       |
| tomli_loads          | 2.92 sec                                                     | 2.60 sec: 1.12x faster                                                      |
| xml_etree_parse      | 160 ms                                                       | 143 ms: 1.12x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 100 ms: 1.10x faster                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 84.1 ms: 1.10x faster                                                       |
| Geometric mean       | (ref)                                                        | 1.24x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                                       |
| python_startup_no_site | 7.33 ms                                                      | 9.08 ms: 1.24x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.3 ms: 1.42x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 24.6 ms: 1.28x faster                                                       |
| django_template | 50.2 ms                                                      | 40.2 ms: 1.25x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 54.5 ms: 1.16x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.27x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 172 us: 3.13x faster                                                        |
| deltablue                | 7.50 ms                                                      | 3.37 ms: 2.23x faster                                                       |
| async_tree_none          | 692 ms                                                       | 318 ms: 2.17x faster                                                        |
| asyncio_tcp              | 779 ms                                                       | 367 ms: 2.12x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 395 ms: 2.07x faster                                                        |
| generators               | 57.3 ms                                                      | 28.5 ms: 2.01x faster                                                       |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.57 sec: 1.97x faster                                                      |
| async_tree_io            | 1.60 sec                                                     | 817 ms: 1.96x faster                                                        |
| go                       | 262 ms                                                       | 135 ms: 1.95x faster                                                        |
| raytrace                 | 489 ms                                                       | 268 ms: 1.82x faster                                                        |
| chaos                    | 109 ms                                                       | 60.5 ms: 1.80x faster                                                       |
| scimark_lu               | 167 ms                                                       | 96.0 ms: 1.74x faster                                                       |
| deepcopy_memo            | 49.8 us                                                      | 28.9 us: 1.72x faster                                                       |
| logging_silent           | 167 ns                                                       | 97.5 ns: 1.72x faster                                                       |
| scimark_monte_carlo      | 107 ms                                                       | 64.7 ms: 1.66x faster                                                       |
| scimark_sor              | 180 ms                                                       | 109 ms: 1.66x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 570 ms: 1.64x faster                                                        |
| deepcopy                 | 468 us                                                       | 286 us: 1.64x faster                                                        |
| richards_super           | 90.6 ms                                                      | 55.7 ms: 1.63x faster                                                       |
| pylint                   | 566 ms                                                       | 349 ms: 1.62x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 73.5 ms: 1.62x faster                                                       |
| nbody                    | 134 ms                                                       | 84.1 ms: 1.59x faster                                                       |
| sqlglot_parse            | 2.24 ms                                                      | 1.41 ms: 1.59x faster                                                       |
| comprehensions           | 26.7 us                                                      | 17.4 us: 1.53x faster                                                       |
| pyflate                  | 733 ms                                                       | 484 ms: 1.51x faster                                                        |
| richards                 | 75.1 ms                                                      | 49.6 ms: 1.51x faster                                                       |
| sqlglot_transpile        | 2.68 ms                                                      | 1.78 ms: 1.50x faster                                                       |
| hexiom                   | 9.42 ms                                                      | 6.31 ms: 1.49x faster                                                       |
| unpickle_pure_python     | 312 us                                                       | 212 us: 1.47x faster                                                        |
| pickle_pure_python       | 455 us                                                       | 313 us: 1.45x faster                                                        |
| spectral_norm            | 139 ms                                                       | 96.0 ms: 1.45x faster                                                       |
| logging_simple           | 8.88 us                                                      | 6.22 us: 1.43x faster                                                       |
| mako                     | 14.7 ms                                                      | 10.3 ms: 1.42x faster                                                       |
| logging_format           | 9.64 us                                                      | 6.81 us: 1.42x faster                                                       |
| float                    | 111 ms                                                       | 78.9 ms: 1.41x faster                                                       |
| coroutines               | 30.3 ms                                                      | 21.6 ms: 1.41x faster                                                       |
| thrift                   | 1.18 ms                                                      | 841 us: 1.40x faster                                                        |
| deepcopy_reduce          | 4.01 us                                                      | 2.89 us: 1.39x faster                                                       |
| bench_mp_pool            | 6.37 ms                                                      | 4.65 ms: 1.37x faster                                                       |
| pycparser                | 1.67 sec                                                     | 1.22 sec: 1.37x faster                                                      |
| html5lib                 | 94.6 ms                                                      | 69.2 ms: 1.37x faster                                                       |
| tornado_http             | 157 ms                                                       | 115 ms: 1.37x faster                                                        |
| regex_compile            | 190 ms                                                       | 139 ms: 1.36x faster                                                        |
| fannkuch                 | 483 ms                                                       | 354 ms: 1.36x faster                                                        |
| pathlib                  | 21.4 ms                                                      | 15.8 ms: 1.35x faster                                                       |
| json_dumps               | 14.5 ms                                                      | 10.8 ms: 1.35x faster                                                       |
| bench_thread_pool        | 1.14 ms                                                      | 852 us: 1.34x faster                                                        |
| pprint_safe_repr         | 1.05 sec                                                     | 796 ms: 1.32x faster                                                        |
| pprint_pformat           | 2.15 sec                                                     | 1.64 sec: 1.32x faster                                                      |
| xml_etree_process        | 75.9 ms                                                      | 58.8 ms: 1.29x faster                                                       |
| nqueens                  | 115 ms                                                       | 89.4 ms: 1.29x faster                                                       |
| genshi_text              | 31.4 ms                                                      | 24.6 ms: 1.28x faster                                                       |
| sympy_sum                | 193 ms                                                       | 151 ms: 1.27x faster                                                        |
| django_template          | 50.2 ms                                                      | 40.2 ms: 1.25x faster                                                       |
| 2to3                     | 350 ms                                                       | 281 ms: 1.24x faster                                                        |
| sympy_str                | 360 ms                                                       | 290 ms: 1.24x faster                                                        |
| sympy_integrate          | 28.2 ms                                                      | 22.9 ms: 1.23x faster                                                       |
| json_loads               | 30.3 us                                                      | 25.1 us: 1.21x faster                                                       |
| sympy_expand             | 600 ms                                                       | 496 ms: 1.21x faster                                                        |
| scimark_fft              | 361 ms                                                       | 299 ms: 1.21x faster                                                        |
| sqlglot_normalize        | 144 ms                                                       | 120 ms: 1.20x faster                                                        |
| mdp                      | 3.01 sec                                                     | 2.52 sec: 1.19x faster                                                      |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.26 ms: 1.19x faster                                                       |
| sqlglot_optimize         | 70.1 ms                                                      | 59.2 ms: 1.19x faster                                                       |
| docutils                 | 3.41 sec                                                     | 2.91 sec: 1.17x faster                                                      |
| async_generators         | 421 ms                                                       | 361 ms: 1.17x faster                                                        |
| genshi_xml               | 63.3 ms                                                      | 54.5 ms: 1.16x faster                                                       |
| json                     | 5.86 ms                                                      | 5.23 ms: 1.12x faster                                                       |
| tomli_loads              | 2.92 sec                                                     | 2.60 sec: 1.12x faster                                                      |
| xml_etree_parse          | 160 ms                                                       | 143 ms: 1.12x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 100 ms: 1.10x faster                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 84.1 ms: 1.10x faster                                                       |
| meteor_contest           | 138 ms                                                       | 126 ms: 1.10x faster                                                        |
| pidigits                 | 271 ms                                                       | 253 ms: 1.07x faster                                                        |
| regex_dna                | 261 ms                                                       | 254 ms: 1.03x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 27.3 ms: 1.01x slower                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.42 ms: 1.11x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 2.00 ms: 1.14x slower                                                       |
| telco                    | 7.23 ms                                                      | 8.24 ms: 1.14x slower                                                       |
| python_startup           | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 9.08 ms: 1.24x slower                                                       |
| coverage                 | 63.3 ms                                                      | 82.1 ms: 1.30x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 4.48 ms: 1.31x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.36x faster                                                                |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240829-3.14.0a0-c9a5962/bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.24x

# Memory
- memory change: 1.13x