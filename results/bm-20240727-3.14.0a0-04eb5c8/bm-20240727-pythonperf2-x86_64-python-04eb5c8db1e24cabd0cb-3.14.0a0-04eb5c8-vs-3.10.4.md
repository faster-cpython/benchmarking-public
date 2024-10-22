# Results vs. 3.10.4

- fork: python
- ref: 04eb5c8db1e24cabd0cb
- machine: linux-x86_64
- commit hash: 04eb5c8
- commit date: 2024-07-27
- overall geometric mean: 1.35x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 285 ms: 1.23x faster                                                        |
| docutils       | 3.41 sec                                                     | 2.98 sec: 1.15x faster                                                      |
| html5lib       | 94.6 ms                                                      | 72.9 ms: 1.30x faster                                                       |
| tornado_http   | 157 ms                                                       | 117 ms: 1.34x faster                                                        |
| Geometric mean | (ref)                                                        | 1.25x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 333 ms: 2.08x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 402 ms: 2.04x faster                                                        |
| async_tree_io           | 1.60 sec                                                     | 813 ms: 1.97x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 573 ms: 1.63x faster                                                        |
| Geometric mean          | (ref)                                                        | 1.92x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 86.7 ms: 1.55x faster                                                       |
| float          | 111 ms                                                       | 81.0 ms: 1.37x faster                                                       |
| pidigits       | 271 ms                                                       | 253 ms: 1.07x faster                                                        |
| Geometric mean | (ref)                                                        | 1.31x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 140 ms: 1.36x faster                                                        |
| regex_dna      | 261 ms                                                       | 242 ms: 1.08x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 26.8 ms: 1.01x faster                                                       |
| regex_effbot   | 3.09 ms                                                      | 3.50 ms: 1.13x slower                                                       |
| Geometric mean | (ref)                                                        | 1.07x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 218 us: 1.43x faster                                                        |
| pickle_pure_python   | 455 us                                                       | 320 us: 1.42x faster                                                        |
| json_dumps           | 14.5 ms                                                      | 10.9 ms: 1.34x faster                                                       |
| tomli_loads          | 2.92 sec                                                     | 2.20 sec: 1.32x faster                                                      |
| xml_etree_process    | 75.9 ms                                                      | 59.3 ms: 1.28x faster                                                       |
| json_loads           | 30.3 us                                                      | 25.7 us: 1.18x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 145 ms: 1.11x faster                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 85.0 ms: 1.09x faster                                                       |
| xml_etree_iterparse  | 110 ms                                                       | 105 ms: 1.06x faster                                                        |
| Geometric mean       | (ref)                                                        | 1.24x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.3 ms: 1.16x slower                                                       |
| python_startup_no_site | 7.33 ms                                                      | 9.05 ms: 1.23x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.4 ms: 1.41x faster                                                       |
| django_template | 50.2 ms                                                      | 38.7 ms: 1.30x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 25.1 ms: 1.25x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 56.6 ms: 1.12x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.26x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 175 us: 3.06x faster                                                        |
| deltablue                | 7.50 ms                                                      | 3.40 ms: 2.21x faster                                                       |
| asyncio_tcp              | 779 ms                                                       | 374 ms: 2.08x faster                                                        |
| async_tree_none          | 692 ms                                                       | 333 ms: 2.08x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 402 ms: 2.04x faster                                                        |
| generators               | 57.3 ms                                                      | 28.8 ms: 1.99x faster                                                       |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.57 sec: 1.97x faster                                                      |
| async_tree_io            | 1.60 sec                                                     | 813 ms: 1.97x faster                                                        |
| raytrace                 | 489 ms                                                       | 274 ms: 1.79x faster                                                        |
| logging_silent           | 167 ns                                                       | 96.6 ns: 1.73x faster                                                       |
| chaos                    | 109 ms                                                       | 62.8 ms: 1.73x faster                                                       |
| scimark_lu               | 167 ms                                                       | 98.6 ms: 1.69x faster                                                       |
| go                       | 262 ms                                                       | 158 ms: 1.66x faster                                                        |
| pylint                   | 566 ms                                                       | 346 ms: 1.64x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 573 ms: 1.63x faster                                                        |
| deepcopy_memo            | 49.8 us                                                      | 30.5 us: 1.63x faster                                                       |
| crypto_pyaes             | 119 ms                                                       | 73.7 ms: 1.62x faster                                                       |
| sqlglot_parse            | 2.24 ms                                                      | 1.39 ms: 1.61x faster                                                       |
| deepcopy                 | 468 us                                                       | 292 us: 1.61x faster                                                        |
| richards_super           | 90.6 ms                                                      | 57.2 ms: 1.58x faster                                                       |
| scimark_monte_carlo      | 107 ms                                                       | 68.9 ms: 1.56x faster                                                       |
| nbody                    | 134 ms                                                       | 86.7 ms: 1.55x faster                                                       |
| pyflate                  | 733 ms                                                       | 479 ms: 1.53x faster                                                        |
| comprehensions           | 26.7 us                                                      | 17.4 us: 1.53x faster                                                       |
| sqlglot_transpile        | 2.68 ms                                                      | 1.76 ms: 1.53x faster                                                       |
| scimark_sor              | 180 ms                                                       | 120 ms: 1.50x faster                                                        |
| hexiom                   | 9.42 ms                                                      | 6.34 ms: 1.49x faster                                                       |
| richards                 | 75.1 ms                                                      | 51.4 ms: 1.46x faster                                                       |
| spectral_norm            | 139 ms                                                       | 96.2 ms: 1.45x faster                                                       |
| unpickle_pure_python     | 312 us                                                       | 218 us: 1.43x faster                                                        |
| logging_simple           | 8.88 us                                                      | 6.22 us: 1.43x faster                                                       |
| coroutines               | 30.3 ms                                                      | 21.3 ms: 1.43x faster                                                       |
| pickle_pure_python       | 455 us                                                       | 320 us: 1.42x faster                                                        |
| mako                     | 14.7 ms                                                      | 10.4 ms: 1.41x faster                                                       |
| logging_format           | 9.64 us                                                      | 6.87 us: 1.40x faster                                                       |
| bench_mp_pool            | 6.37 ms                                                      | 4.61 ms: 1.38x faster                                                       |
| deepcopy_reduce          | 4.01 us                                                      | 2.91 us: 1.38x faster                                                       |
| pycparser                | 1.67 sec                                                     | 1.22 sec: 1.38x faster                                                      |
| float                    | 111 ms                                                       | 81.0 ms: 1.37x faster                                                       |
| regex_compile            | 190 ms                                                       | 140 ms: 1.36x faster                                                        |
| thrift                   | 1.18 ms                                                      | 866 us: 1.36x faster                                                        |
| fannkuch                 | 483 ms                                                       | 359 ms: 1.34x faster                                                        |
| tornado_http             | 157 ms                                                       | 117 ms: 1.34x faster                                                        |
| pathlib                  | 21.4 ms                                                      | 16.0 ms: 1.34x faster                                                       |
| json_dumps               | 14.5 ms                                                      | 10.9 ms: 1.34x faster                                                       |
| bench_thread_pool        | 1.14 ms                                                      | 861 us: 1.33x faster                                                        |
| tomli_loads              | 2.92 sec                                                     | 2.20 sec: 1.32x faster                                                      |
| nqueens                  | 115 ms                                                       | 88.1 ms: 1.31x faster                                                       |
| html5lib                 | 94.6 ms                                                      | 72.9 ms: 1.30x faster                                                       |
| django_template          | 50.2 ms                                                      | 38.7 ms: 1.30x faster                                                       |
| xml_etree_process        | 75.9 ms                                                      | 59.3 ms: 1.28x faster                                                       |
| pprint_pformat           | 2.15 sec                                                     | 1.71 sec: 1.26x faster                                                      |
| sympy_sum                | 193 ms                                                       | 153 ms: 1.26x faster                                                        |
| genshi_text              | 31.4 ms                                                      | 25.1 ms: 1.25x faster                                                       |
| pprint_safe_repr         | 1.05 sec                                                     | 838 ms: 1.25x faster                                                        |
| dask                     | 472 ms                                                       | 380 ms: 1.24x faster                                                        |
| sympy_str                | 360 ms                                                       | 292 ms: 1.23x faster                                                        |
| 2to3                     | 350 ms                                                       | 285 ms: 1.23x faster                                                        |
| sympy_integrate          | 28.2 ms                                                      | 23.1 ms: 1.22x faster                                                       |
| sqlglot_normalize        | 144 ms                                                       | 118 ms: 1.22x faster                                                        |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.19 ms: 1.21x faster                                                       |
| mdp                      | 3.01 sec                                                     | 2.49 sec: 1.21x faster                                                      |
| sqlglot_optimize         | 70.1 ms                                                      | 58.4 ms: 1.20x faster                                                       |
| sympy_expand             | 600 ms                                                       | 502 ms: 1.19x faster                                                        |
| scimark_fft              | 361 ms                                                       | 304 ms: 1.19x faster                                                        |
| json_loads               | 30.3 us                                                      | 25.7 us: 1.18x faster                                                       |
| async_generators         | 421 ms                                                       | 367 ms: 1.15x faster                                                        |
| docutils                 | 3.41 sec                                                     | 2.98 sec: 1.15x faster                                                      |
| genshi_xml               | 63.3 ms                                                      | 56.6 ms: 1.12x faster                                                       |
| xml_etree_parse          | 160 ms                                                       | 145 ms: 1.11x faster                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 85.0 ms: 1.09x faster                                                       |
| json                     | 5.86 ms                                                      | 5.41 ms: 1.08x faster                                                       |
| regex_dna                | 261 ms                                                       | 242 ms: 1.08x faster                                                        |
| meteor_contest           | 138 ms                                                       | 129 ms: 1.07x faster                                                        |
| pidigits                 | 271 ms                                                       | 253 ms: 1.07x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 105 ms: 1.06x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 26.8 ms: 1.01x faster                                                       |
| telco                    | 7.23 ms                                                      | 8.11 ms: 1.12x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 1.98 ms: 1.12x slower                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.50 ms: 1.13x slower                                                       |
| python_startup           | 11.5 ms                                                      | 13.3 ms: 1.16x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 9.05 ms: 1.23x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 4.35 ms: 1.27x slower                                                       |
| coverage                 | 63.3 ms                                                      | 84.2 ms: 1.33x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.35x faster                                                                |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240727-3.14.0a0-04eb5c8/bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: 1.13x