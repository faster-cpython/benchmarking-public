# Results vs. 3.10.4

- fork: python
- ref: 04eb5c8db1e24cabd0cb
- machine: linux-x86_64
- commit hash: 04eb5c8
- commit date: 2024-07-27
- overall geometric mean: 1.33x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 308 ms: 1.14x faster                                                        |
| docutils       | 3.41 sec                                                     | 3.15 sec: 1.09x faster                                                      |
| html5lib       | 94.6 ms                                                      | 70.6 ms: 1.34x faster                                                       |
| tornado_http   | 157 ms                                                       | 120 ms: 1.31x faster                                                        |
| Geometric mean | (ref)                                                        | 1.21x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 323 ms: 2.14x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 413 ms: 1.98x faster                                                        |
| async_tree_io           | 1.60 sec                                                     | 826 ms: 1.94x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 568 ms: 1.65x faster                                                        |
| Geometric mean          | (ref)                                                        | 1.92x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 84.0 ms: 1.60x faster                                                       |
| float          | 111 ms                                                       | 74.5 ms: 1.49x faster                                                       |
| pidigits       | 271 ms                                                       | 250 ms: 1.08x faster                                                        |
| Geometric mean | (ref)                                                        | 1.37x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 134 ms: 1.41x faster                                                        |
| regex_dna      | 261 ms                                                       | 259 ms: 1.01x faster                                                        |
| regex_effbot   | 3.09 ms                                                      | 3.60 ms: 1.16x slower                                                       |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 211 us: 1.48x faster                                                        |
| pickle_pure_python   | 455 us                                                       | 320 us: 1.42x faster                                                        |
| tomli_loads          | 2.92 sec                                                     | 2.10 sec: 1.39x faster                                                      |
| json_dumps           | 14.5 ms                                                      | 10.8 ms: 1.35x faster                                                       |
| xml_etree_process    | 75.9 ms                                                      | 57.6 ms: 1.32x faster                                                       |
| json_loads           | 30.3 us                                                      | 25.5 us: 1.19x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 141 ms: 1.14x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 97.8 ms: 1.13x faster                                                       |
| xml_etree_generate   | 92.3 ms                                                      | 82.3 ms: 1.12x faster                                                       |
| Geometric mean       | (ref)                                                        | 1.27x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                                       |
| python_startup_no_site | 7.33 ms                                                      | 9.06 ms: 1.24x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.07 ms: 1.62x faster                                                       |
| django_template | 50.2 ms                                                      | 41.4 ms: 1.21x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 29.1 ms: 1.08x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 64.5 ms: 1.02x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.20x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 188 us: 2.85x faster                                                        |
| async_tree_none          | 692 ms                                                       | 323 ms: 2.14x faster                                                        |
| deltablue                | 7.50 ms                                                      | 3.61 ms: 2.07x faster                                                       |
| asyncio_tcp              | 779 ms                                                       | 376 ms: 2.07x faster                                                        |
| generators               | 57.3 ms                                                      | 28.9 ms: 1.99x faster                                                       |
| async_tree_memoization   | 819 ms                                                       | 413 ms: 1.98x faster                                                        |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.96x faster                                                      |
| async_tree_io            | 1.60 sec                                                     | 826 ms: 1.94x faster                                                        |
| richards_super           | 90.6 ms                                                      | 52.3 ms: 1.73x faster                                                       |
| deepcopy_memo            | 49.8 us                                                      | 28.8 us: 1.73x faster                                                       |
| spectral_norm            | 139 ms                                                       | 81.4 ms: 1.71x faster                                                       |
| crypto_pyaes             | 119 ms                                                       | 69.9 ms: 1.70x faster                                                       |
| pyflate                  | 733 ms                                                       | 433 ms: 1.69x faster                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 64.3 ms: 1.67x faster                                                       |
| logging_silent           | 167 ns                                                       | 100 ns: 1.67x faster                                                        |
| richards                 | 75.1 ms                                                      | 45.5 ms: 1.65x faster                                                       |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 568 ms: 1.65x faster                                                        |
| chaos                    | 109 ms                                                       | 66.0 ms: 1.65x faster                                                       |
| raytrace                 | 489 ms                                                       | 300 ms: 1.63x faster                                                        |
| mako                     | 14.7 ms                                                      | 9.07 ms: 1.62x faster                                                       |
| nbody                    | 134 ms                                                       | 84.0 ms: 1.60x faster                                                       |
| go                       | 262 ms                                                       | 166 ms: 1.58x faster                                                        |
| sqlglot_parse            | 2.24 ms                                                      | 1.42 ms: 1.57x faster                                                       |
| deepcopy                 | 468 us                                                       | 308 us: 1.52x faster                                                        |
| float                    | 111 ms                                                       | 74.5 ms: 1.49x faster                                                       |
| unpickle_pure_python     | 312 us                                                       | 211 us: 1.48x faster                                                        |
| pylint                   | 566 ms                                                       | 383 ms: 1.48x faster                                                        |
| scimark_lu               | 167 ms                                                       | 113 ms: 1.48x faster                                                        |
| comprehensions           | 26.7 us                                                      | 18.2 us: 1.47x faster                                                       |
| sqlglot_transpile        | 2.68 ms                                                      | 1.84 ms: 1.46x faster                                                       |
| hexiom                   | 9.42 ms                                                      | 6.60 ms: 1.43x faster                                                       |
| pickle_pure_python       | 455 us                                                       | 320 us: 1.42x faster                                                        |
| regex_compile            | 190 ms                                                       | 134 ms: 1.41x faster                                                        |
| logging_simple           | 8.88 us                                                      | 6.35 us: 1.40x faster                                                       |
| coroutines               | 30.3 ms                                                      | 21.7 ms: 1.39x faster                                                       |
| tomli_loads              | 2.92 sec                                                     | 2.10 sec: 1.39x faster                                                      |
| fannkuch                 | 483 ms                                                       | 351 ms: 1.38x faster                                                        |
| logging_format           | 9.64 us                                                      | 7.03 us: 1.37x faster                                                       |
| pycparser                | 1.67 sec                                                     | 1.24 sec: 1.35x faster                                                      |
| json_dumps               | 14.5 ms                                                      | 10.8 ms: 1.35x faster                                                       |
| html5lib                 | 94.6 ms                                                      | 70.6 ms: 1.34x faster                                                       |
| deepcopy_reduce          | 4.01 us                                                      | 3.02 us: 1.33x faster                                                       |
| pprint_safe_repr         | 1.05 sec                                                     | 796 ms: 1.32x faster                                                        |
| xml_etree_process        | 75.9 ms                                                      | 57.6 ms: 1.32x faster                                                       |
| pathlib                  | 21.4 ms                                                      | 16.2 ms: 1.32x faster                                                       |
| pprint_pformat           | 2.15 sec                                                     | 1.64 sec: 1.31x faster                                                      |
| bench_mp_pool            | 6.37 ms                                                      | 4.87 ms: 1.31x faster                                                       |
| tornado_http             | 157 ms                                                       | 120 ms: 1.31x faster                                                        |
| thrift                   | 1.18 ms                                                      | 903 us: 1.30x faster                                                        |
| scimark_sor              | 180 ms                                                       | 142 ms: 1.27x faster                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 902 us: 1.26x faster                                                        |
| scimark_fft              | 361 ms                                                       | 292 ms: 1.24x faster                                                        |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.16 ms: 1.22x faster                                                       |
| django_template          | 50.2 ms                                                      | 41.4 ms: 1.21x faster                                                       |
| dask                     | 472 ms                                                       | 392 ms: 1.21x faster                                                        |
| nqueens                  | 115 ms                                                       | 96.1 ms: 1.20x faster                                                       |
| json_loads               | 30.3 us                                                      | 25.5 us: 1.19x faster                                                       |
| mdp                      | 3.01 sec                                                     | 2.57 sec: 1.17x faster                                                      |
| sympy_sum                | 193 ms                                                       | 166 ms: 1.16x faster                                                        |
| sympy_str                | 360 ms                                                       | 310 ms: 1.16x faster                                                        |
| sympy_expand             | 600 ms                                                       | 524 ms: 1.15x faster                                                        |
| xml_etree_parse          | 160 ms                                                       | 141 ms: 1.14x faster                                                        |
| 2to3                     | 350 ms                                                       | 308 ms: 1.14x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 97.8 ms: 1.13x faster                                                       |
| xml_etree_generate       | 92.3 ms                                                      | 82.3 ms: 1.12x faster                                                       |
| sqlglot_optimize         | 70.1 ms                                                      | 63.8 ms: 1.10x faster                                                       |
| sympy_integrate          | 28.2 ms                                                      | 25.6 ms: 1.10x faster                                                       |
| sqlglot_normalize        | 144 ms                                                       | 131 ms: 1.09x faster                                                        |
| meteor_contest           | 138 ms                                                       | 127 ms: 1.09x faster                                                        |
| async_generators         | 421 ms                                                       | 387 ms: 1.09x faster                                                        |
| docutils                 | 3.41 sec                                                     | 3.15 sec: 1.09x faster                                                      |
| pidigits                 | 271 ms                                                       | 250 ms: 1.08x faster                                                        |
| genshi_text              | 31.4 ms                                                      | 29.1 ms: 1.08x faster                                                       |
| json                     | 5.86 ms                                                      | 5.56 ms: 1.06x faster                                                       |
| regex_dna                | 261 ms                                                       | 259 ms: 1.01x faster                                                        |
| genshi_xml               | 63.3 ms                                                      | 64.5 ms: 1.02x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 1.94 ms: 1.10x slower                                                       |
| telco                    | 7.23 ms                                                      | 8.02 ms: 1.11x slower                                                       |
| python_startup           | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.60 ms: 1.16x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 9.06 ms: 1.24x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 4.35 ms: 1.27x slower                                                       |
| coverage                 | 63.3 ms                                                      | 81.9 ms: 1.29x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.33x faster                                                                |

Benchmark hidden because not significant (2): regex_v8, asyncio_websockets
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240727-3.14.0a0-04eb5c8-JIT/bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: 1.20x