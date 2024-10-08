# Results vs. 3.10.4

- fork: mdboom
- ref: simplify_richcompare
- machine: linux-x86_64
- commit hash: 2fa7b0e
- commit date: 2024-09-04
- overall geometric mean: 1.36x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240904-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 284 ms: 1.23x faster                                                        |
| docutils       | 3.41 sec                                                     | 2.92 sec: 1.17x faster                                                      |
| html5lib       | 94.6 ms                                                      | 70.9 ms: 1.33x faster                                                       |
| tornado_http   | 157 ms                                                       | 116 ms: 1.36x faster                                                        |
| Geometric mean | (ref)                                                        | 1.27x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240904-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 319 ms: 2.17x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 397 ms: 2.06x faster                                                        |
| async_tree_io           | 1.60 sec                                                     | 816 ms: 1.96x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 570 ms: 1.64x faster                                                        |
| Geometric mean          | (ref)                                                        | 1.95x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240904-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 85.8 ms: 1.56x faster                                                       |
| float          | 111 ms                                                       | 79.2 ms: 1.40x faster                                                       |
| pidigits       | 271 ms                                                       | 252 ms: 1.07x faster                                                        |
| Geometric mean | (ref)                                                        | 1.33x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240904-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 141 ms: 1.35x faster                                                        |
| regex_dna      | 261 ms                                                       | 255 ms: 1.02x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 26.8 ms: 1.01x faster                                                       |
| regex_effbot   | 3.09 ms                                                      | 3.47 ms: 1.12x slower                                                       |
| Geometric mean | (ref)                                                        | 1.06x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240904-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                       | 310 us: 1.47x faster                                                        |
| unpickle_pure_python | 312 us                                                       | 216 us: 1.45x faster                                                        |
| json_dumps           | 14.5 ms                                                      | 10.9 ms: 1.33x faster                                                       |
| xml_etree_process    | 75.9 ms                                                      | 59.3 ms: 1.28x faster                                                       |
| json_loads           | 30.3 us                                                      | 25.1 us: 1.21x faster                                                       |
| tomli_loads          | 2.92 sec                                                     | 2.56 sec: 1.14x faster                                                      |
| xml_etree_parse      | 160 ms                                                       | 145 ms: 1.10x faster                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 84.1 ms: 1.10x faster                                                       |
| xml_etree_iterparse  | 110 ms                                                       | 103 ms: 1.08x faster                                                        |
| Geometric mean       | (ref)                                                        | 1.23x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240904-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.4 ms: 1.17x slower                                                       |
| python_startup_no_site | 7.33 ms                                                      | 9.08 ms: 1.24x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240904-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.4 ms: 1.41x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 25.2 ms: 1.25x faster                                                       |
| django_template | 50.2 ms                                                      | 40.3 ms: 1.24x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 54.8 ms: 1.15x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.26x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240904-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 175 us: 3.07x faster                                                        |
| deltablue                | 7.50 ms                                                      | 3.42 ms: 2.19x faster                                                       |
| async_tree_none          | 692 ms                                                       | 319 ms: 2.17x faster                                                        |
| asyncio_tcp              | 779 ms                                                       | 366 ms: 2.13x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 397 ms: 2.06x faster                                                        |
| generators               | 57.3 ms                                                      | 28.4 ms: 2.02x faster                                                       |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.97x faster                                                      |
| async_tree_io            | 1.60 sec                                                     | 816 ms: 1.96x faster                                                        |
| go                       | 262 ms                                                       | 134 ms: 1.96x faster                                                        |
| raytrace                 | 489 ms                                                       | 275 ms: 1.78x faster                                                        |
| scimark_lu               | 167 ms                                                       | 95.7 ms: 1.74x faster                                                       |
| chaos                    | 109 ms                                                       | 62.8 ms: 1.73x faster                                                       |
| deepcopy_memo            | 49.8 us                                                      | 29.4 us: 1.69x faster                                                       |
| logging_silent           | 167 ns                                                       | 99.3 ns: 1.69x faster                                                       |
| scimark_sor              | 180 ms                                                       | 109 ms: 1.66x faster                                                        |
| deepcopy                 | 468 us                                                       | 285 us: 1.64x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 570 ms: 1.64x faster                                                        |
| richards_super           | 90.6 ms                                                      | 56.0 ms: 1.62x faster                                                       |
| crypto_pyaes             | 119 ms                                                       | 74.1 ms: 1.61x faster                                                       |
| pylint                   | 566 ms                                                       | 353 ms: 1.61x faster                                                        |
| sqlglot_parse            | 2.24 ms                                                      | 1.42 ms: 1.57x faster                                                       |
| scimark_monte_carlo      | 107 ms                                                       | 68.4 ms: 1.57x faster                                                       |
| nbody                    | 134 ms                                                       | 85.8 ms: 1.56x faster                                                       |
| comprehensions           | 26.7 us                                                      | 17.4 us: 1.53x faster                                                       |
| pyflate                  | 733 ms                                                       | 481 ms: 1.52x faster                                                        |
| richards                 | 75.1 ms                                                      | 50.1 ms: 1.50x faster                                                       |
| hexiom                   | 9.42 ms                                                      | 6.32 ms: 1.49x faster                                                       |
| sqlglot_transpile        | 2.68 ms                                                      | 1.80 ms: 1.49x faster                                                       |
| pickle_pure_python       | 455 us                                                       | 310 us: 1.47x faster                                                        |
| spectral_norm            | 139 ms                                                       | 96.0 ms: 1.45x faster                                                       |
| unpickle_pure_python     | 312 us                                                       | 216 us: 1.45x faster                                                        |
| mako                     | 14.7 ms                                                      | 10.4 ms: 1.41x faster                                                       |
| bench_mp_pool            | 6.37 ms                                                      | 4.53 ms: 1.41x faster                                                       |
| float                    | 111 ms                                                       | 79.2 ms: 1.40x faster                                                       |
| logging_format           | 9.64 us                                                      | 6.88 us: 1.40x faster                                                       |
| logging_simple           | 8.88 us                                                      | 6.34 us: 1.40x faster                                                       |
| deepcopy_reduce          | 4.01 us                                                      | 2.89 us: 1.39x faster                                                       |
| thrift                   | 1.18 ms                                                      | 857 us: 1.37x faster                                                        |
| pycparser                | 1.67 sec                                                     | 1.23 sec: 1.37x faster                                                      |
| pathlib                  | 21.4 ms                                                      | 15.7 ms: 1.36x faster                                                       |
| tornado_http             | 157 ms                                                       | 116 ms: 1.36x faster                                                        |
| coroutines               | 30.3 ms                                                      | 22.4 ms: 1.35x faster                                                       |
| regex_compile            | 190 ms                                                       | 141 ms: 1.35x faster                                                        |
| fannkuch                 | 483 ms                                                       | 360 ms: 1.34x faster                                                        |
| json_dumps               | 14.5 ms                                                      | 10.9 ms: 1.33x faster                                                       |
| html5lib                 | 94.6 ms                                                      | 70.9 ms: 1.33x faster                                                       |
| bench_thread_pool        | 1.14 ms                                                      | 863 us: 1.32x faster                                                        |
| pprint_pformat           | 2.15 sec                                                     | 1.64 sec: 1.31x faster                                                      |
| pprint_safe_repr         | 1.05 sec                                                     | 802 ms: 1.31x faster                                                        |
| nqueens                  | 115 ms                                                       | 89.7 ms: 1.28x faster                                                       |
| xml_etree_process        | 75.9 ms                                                      | 59.3 ms: 1.28x faster                                                       |
| sympy_sum                | 193 ms                                                       | 152 ms: 1.26x faster                                                        |
| genshi_text              | 31.4 ms                                                      | 25.2 ms: 1.25x faster                                                       |
| django_template          | 50.2 ms                                                      | 40.3 ms: 1.24x faster                                                       |
| 2to3                     | 350 ms                                                       | 284 ms: 1.23x faster                                                        |
| sympy_str                | 360 ms                                                       | 294 ms: 1.23x faster                                                        |
| sympy_integrate          | 28.2 ms                                                      | 23.0 ms: 1.23x faster                                                       |
| scimark_fft              | 361 ms                                                       | 296 ms: 1.22x faster                                                        |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.18 ms: 1.22x faster                                                       |
| json_loads               | 30.3 us                                                      | 25.1 us: 1.21x faster                                                       |
| mdp                      | 3.01 sec                                                     | 2.51 sec: 1.20x faster                                                      |
| sympy_expand             | 600 ms                                                       | 503 ms: 1.19x faster                                                        |
| sqlglot_normalize        | 144 ms                                                       | 121 ms: 1.19x faster                                                        |
| sqlglot_optimize         | 70.1 ms                                                      | 59.3 ms: 1.18x faster                                                       |
| docutils                 | 3.41 sec                                                     | 2.92 sec: 1.17x faster                                                      |
| genshi_xml               | 63.3 ms                                                      | 54.8 ms: 1.15x faster                                                       |
| tomli_loads              | 2.92 sec                                                     | 2.56 sec: 1.14x faster                                                      |
| async_generators         | 421 ms                                                       | 371 ms: 1.14x faster                                                        |
| json                     | 5.86 ms                                                      | 5.28 ms: 1.11x faster                                                       |
| xml_etree_parse          | 160 ms                                                       | 145 ms: 1.10x faster                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 84.1 ms: 1.10x faster                                                       |
| xml_etree_iterparse      | 110 ms                                                       | 103 ms: 1.08x faster                                                        |
| meteor_contest           | 138 ms                                                       | 128 ms: 1.08x faster                                                        |
| pidigits                 | 271 ms                                                       | 252 ms: 1.07x faster                                                        |
| regex_dna                | 261 ms                                                       | 255 ms: 1.02x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 26.8 ms: 1.01x faster                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.47 ms: 1.12x slower                                                       |
| telco                    | 7.23 ms                                                      | 8.17 ms: 1.13x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 2.00 ms: 1.13x slower                                                       |
| python_startup           | 11.5 ms                                                      | 13.4 ms: 1.17x slower                                                       |
| coverage                 | 63.3 ms                                                      | 74.9 ms: 1.18x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 9.08 ms: 1.24x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 4.63 ms: 1.36x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.36x faster                                                                |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240904-3.14.0a0-2fa7b0e/bm-20240904-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: 1.13x