# Results vs. 3.10.4

- fork: python
- ref: 33903c53dbdb768e1ef7
- machine: linux-x86_64
- commit hash: 33903c5
- commit date: 2024-07-01
- overall geometric mean: 1.32x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240701-pythonperf2-x86_64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 305 ms: 1.15x faster                                                        |
| docutils       | 3.41 sec                                                     | 3.12 sec: 1.09x faster                                                      |
| html5lib       | 94.6 ms                                                      | 74.0 ms: 1.28x faster                                                       |
| tornado_http   | 157 ms                                                       | 120 ms: 1.30x faster                                                        |
| Geometric mean | (ref)                                                        | 1.20x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240701-pythonperf2-x86_64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 338 ms: 2.05x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 409 ms: 2.00x faster                                                        |
| async_tree_io           | 1.60 sec                                                     | 813 ms: 1.97x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 582 ms: 1.61x faster                                                        |
| Geometric mean          | (ref)                                                        | 1.90x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240701-pythonperf2-x86_64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 85.2 ms: 1.57x faster                                                       |
| float          | 111 ms                                                       | 75.0 ms: 1.48x faster                                                       |
| pidigits       | 271 ms                                                       | 250 ms: 1.08x faster                                                        |
| Geometric mean | (ref)                                                        | 1.36x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240701-pythonperf2-x86_64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 137 ms: 1.39x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 27.0 ms: 1.00x faster                                                       |
| regex_dna      | 261 ms                                                       | 264 ms: 1.01x slower                                                        |
| regex_effbot   | 3.09 ms                                                      | 3.74 ms: 1.21x slower                                                       |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240701-pythonperf2-x86_64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 216 us: 1.44x faster                                                        |
| pickle_pure_python   | 455 us                                                       | 317 us: 1.44x faster                                                        |
| tomli_loads          | 2.92 sec                                                     | 2.09 sec: 1.40x faster                                                      |
| json_dumps           | 14.5 ms                                                      | 10.9 ms: 1.33x faster                                                       |
| xml_etree_process    | 75.9 ms                                                      | 58.5 ms: 1.30x faster                                                       |
| json_loads           | 30.3 us                                                      | 25.0 us: 1.21x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 141 ms: 1.13x faster                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 82.1 ms: 1.12x faster                                                       |
| xml_etree_iterparse  | 110 ms                                                       | 99.4 ms: 1.11x faster                                                       |
| Geometric mean       | (ref)                                                        | 1.27x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240701-pythonperf2-x86_64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                                       |
| python_startup_no_site | 7.33 ms                                                      | 9.08 ms: 1.24x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240701-pythonperf2-x86_64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.26 ms: 1.59x faster                                                       |
| django_template | 50.2 ms                                                      | 41.3 ms: 1.22x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 28.4 ms: 1.11x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 65.5 ms: 1.03x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.20x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240701-pythonperf2-x86_64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 185 us: 2.90x faster                                                        |
| deltablue                | 7.50 ms                                                      | 3.63 ms: 2.07x faster                                                       |
| asyncio_tcp              | 779 ms                                                       | 378 ms: 2.06x faster                                                        |
| async_tree_none          | 692 ms                                                       | 338 ms: 2.05x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 409 ms: 2.00x faster                                                        |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.97x faster                                                      |
| async_tree_io            | 1.60 sec                                                     | 813 ms: 1.97x faster                                                        |
| raytrace                 | 489 ms                                                       | 288 ms: 1.70x faster                                                        |
| richards_super           | 90.6 ms                                                      | 53.7 ms: 1.69x faster                                                       |
| deepcopy_memo            | 49.8 us                                                      | 29.5 us: 1.68x faster                                                       |
| crypto_pyaes             | 119 ms                                                       | 70.7 ms: 1.68x faster                                                       |
| generators               | 57.3 ms                                                      | 34.6 ms: 1.66x faster                                                       |
| richards                 | 75.1 ms                                                      | 45.8 ms: 1.64x faster                                                       |
| chaos                    | 109 ms                                                       | 66.4 ms: 1.64x faster                                                       |
| scimark_monte_carlo      | 107 ms                                                       | 66.0 ms: 1.63x faster                                                       |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 582 ms: 1.61x faster                                                        |
| go                       | 262 ms                                                       | 163 ms: 1.61x faster                                                        |
| logging_silent           | 167 ns                                                       | 105 ns: 1.60x faster                                                        |
| spectral_norm            | 139 ms                                                       | 87.4 ms: 1.59x faster                                                       |
| mako                     | 14.7 ms                                                      | 9.26 ms: 1.59x faster                                                       |
| nbody                    | 134 ms                                                       | 85.2 ms: 1.57x faster                                                       |
| pyflate                  | 733 ms                                                       | 466 ms: 1.57x faster                                                        |
| sqlglot_parse            | 2.24 ms                                                      | 1.42 ms: 1.57x faster                                                       |
| deepcopy                 | 468 us                                                       | 306 us: 1.53x faster                                                        |
| pylint                   | 566 ms                                                       | 378 ms: 1.50x faster                                                        |
| float                    | 111 ms                                                       | 75.0 ms: 1.48x faster                                                       |
| sqlglot_transpile        | 2.68 ms                                                      | 1.83 ms: 1.47x faster                                                       |
| scimark_lu               | 167 ms                                                       | 114 ms: 1.46x faster                                                        |
| logging_simple           | 8.88 us                                                      | 6.13 us: 1.45x faster                                                       |
| comprehensions           | 26.7 us                                                      | 18.5 us: 1.45x faster                                                       |
| unpickle_pure_python     | 312 us                                                       | 216 us: 1.44x faster                                                        |
| pickle_pure_python       | 455 us                                                       | 317 us: 1.44x faster                                                        |
| coroutines               | 30.3 ms                                                      | 21.5 ms: 1.41x faster                                                       |
| logging_format           | 9.64 us                                                      | 6.84 us: 1.41x faster                                                       |
| fannkuch                 | 483 ms                                                       | 343 ms: 1.41x faster                                                        |
| tomli_loads              | 2.92 sec                                                     | 2.09 sec: 1.40x faster                                                      |
| scimark_sor              | 180 ms                                                       | 129 ms: 1.40x faster                                                        |
| hexiom                   | 9.42 ms                                                      | 6.75 ms: 1.40x faster                                                       |
| regex_compile            | 190 ms                                                       | 137 ms: 1.39x faster                                                        |
| pycparser                | 1.67 sec                                                     | 1.21 sec: 1.38x faster                                                      |
| bench_mp_pool            | 6.37 ms                                                      | 4.75 ms: 1.34x faster                                                       |
| json_dumps               | 14.5 ms                                                      | 10.9 ms: 1.33x faster                                                       |
| pathlib                  | 21.4 ms                                                      | 16.2 ms: 1.32x faster                                                       |
| tornado_http             | 157 ms                                                       | 120 ms: 1.30x faster                                                        |
| pprint_pformat           | 2.15 sec                                                     | 1.65 sec: 1.30x faster                                                      |
| pprint_safe_repr         | 1.05 sec                                                     | 806 ms: 1.30x faster                                                        |
| xml_etree_process        | 75.9 ms                                                      | 58.5 ms: 1.30x faster                                                       |
| deepcopy_reduce          | 4.01 us                                                      | 3.12 us: 1.29x faster                                                       |
| html5lib                 | 94.6 ms                                                      | 74.0 ms: 1.28x faster                                                       |
| thrift                   | 1.18 ms                                                      | 922 us: 1.27x faster                                                        |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.01 ms: 1.27x faster                                                       |
| scimark_fft              | 361 ms                                                       | 294 ms: 1.23x faster                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 929 us: 1.23x faster                                                        |
| dulwich_log              | 81.1 ms                                                      | 66.4 ms: 1.22x faster                                                       |
| django_template          | 50.2 ms                                                      | 41.3 ms: 1.22x faster                                                       |
| json_loads               | 30.3 us                                                      | 25.0 us: 1.21x faster                                                       |
| nqueens                  | 115 ms                                                       | 96.1 ms: 1.20x faster                                                       |
| dask                     | 472 ms                                                       | 397 ms: 1.19x faster                                                        |
| sympy_sum                | 193 ms                                                       | 165 ms: 1.17x faster                                                        |
| sympy_str                | 360 ms                                                       | 309 ms: 1.16x faster                                                        |
| mdp                      | 3.01 sec                                                     | 2.59 sec: 1.16x faster                                                      |
| sympy_expand             | 600 ms                                                       | 522 ms: 1.15x faster                                                        |
| 2to3                     | 350 ms                                                       | 305 ms: 1.15x faster                                                        |
| xml_etree_parse          | 160 ms                                                       | 141 ms: 1.13x faster                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 82.1 ms: 1.12x faster                                                       |
| sqlglot_optimize         | 70.1 ms                                                      | 62.7 ms: 1.12x faster                                                       |
| xml_etree_iterparse      | 110 ms                                                       | 99.4 ms: 1.11x faster                                                       |
| genshi_text              | 31.4 ms                                                      | 28.4 ms: 1.11x faster                                                       |
| sympy_integrate          | 28.2 ms                                                      | 25.5 ms: 1.10x faster                                                       |
| sqlglot_normalize        | 144 ms                                                       | 130 ms: 1.10x faster                                                        |
| docutils                 | 3.41 sec                                                     | 3.12 sec: 1.09x faster                                                      |
| pidigits                 | 271 ms                                                       | 250 ms: 1.08x faster                                                        |
| json                     | 5.86 ms                                                      | 5.43 ms: 1.08x faster                                                       |
| async_generators         | 421 ms                                                       | 398 ms: 1.06x faster                                                        |
| meteor_contest           | 138 ms                                                       | 131 ms: 1.06x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 27.0 ms: 1.00x faster                                                       |
| regex_dna                | 261 ms                                                       | 264 ms: 1.01x slower                                                        |
| genshi_xml               | 63.3 ms                                                      | 65.5 ms: 1.03x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 1.93 ms: 1.10x slower                                                       |
| telco                    | 7.23 ms                                                      | 8.21 ms: 1.14x slower                                                       |
| python_startup           | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.74 ms: 1.21x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 9.08 ms: 1.24x slower                                                       |
| coverage                 | 63.3 ms                                                      | 83.5 ms: 1.32x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 4.66 ms: 1.36x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.32x faster                                                                |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240701-3.14.0a0-33903c5-JIT/bm-20240701-pythonperf2-x86_64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: 1.19x