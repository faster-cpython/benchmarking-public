# Results vs. 3.10.4

- fork: brandtbucher
- ref: warmer_side_exits
- machine: linux-x86_64
- commit hash: 8423e72
- commit date: 2024-07-01
- overall geometric mean: 1.32x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: 1.22x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240701-pythonperf2-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 309 ms: 1.13x faster                                                           |
| docutils       | 3.41 sec                                                     | 3.14 sec: 1.09x faster                                                         |
| html5lib       | 94.6 ms                                                      | 73.0 ms: 1.30x faster                                                          |
| tornado_http   | 157 ms                                                       | 121 ms: 1.30x faster                                                           |
| Geometric mean | (ref)                                                        | 1.20x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240701-pythonperf2-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|-------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 343 ms: 2.01x faster                                                           |
| async_tree_memoization  | 819 ms                                                       | 410 ms: 2.00x faster                                                           |
| async_tree_io           | 1.60 sec                                                     | 808 ms: 1.98x faster                                                           |
| async_tree_cpu_io_mixed | 936 ms                                                       | 584 ms: 1.60x faster                                                           |
| Geometric mean          | (ref)                                                        | 1.89x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240701-pythonperf2-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 83.1 ms: 1.61x faster                                                          |
| float          | 111 ms                                                       | 75.2 ms: 1.48x faster                                                          |
| pidigits       | 271 ms                                                       | 250 ms: 1.08x faster                                                           |
| Geometric mean | (ref)                                                        | 1.37x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240701-pythonperf2-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 138 ms: 1.38x faster                                                           |
| regex_dna      | 261 ms                                                       | 240 ms: 1.09x faster                                                           |
| regex_v8       | 27.2 ms                                                      | 25.5 ms: 1.07x faster                                                          |
| regex_effbot   | 3.09 ms                                                      | 3.66 ms: 1.18x slower                                                          |
| Geometric mean | (ref)                                                        | 1.08x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240701-pythonperf2-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 202 us: 1.54x faster                                                           |
| pickle_pure_python   | 455 us                                                       | 317 us: 1.44x faster                                                           |
| tomli_loads          | 2.92 sec                                                     | 2.10 sec: 1.39x faster                                                         |
| json_dumps           | 14.5 ms                                                      | 10.8 ms: 1.35x faster                                                          |
| xml_etree_process    | 75.9 ms                                                      | 58.3 ms: 1.30x faster                                                          |
| json_loads           | 30.3 us                                                      | 25.2 us: 1.20x faster                                                          |
| xml_etree_parse      | 160 ms                                                       | 143 ms: 1.12x faster                                                           |
| xml_etree_generate   | 92.3 ms                                                      | 82.5 ms: 1.12x faster                                                          |
| xml_etree_iterparse  | 110 ms                                                       | 98.9 ms: 1.12x faster                                                          |
| Geometric mean       | (ref)                                                        | 1.28x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240701-pythonperf2-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.4 ms: 1.17x slower                                                          |
| python_startup_no_site | 7.33 ms                                                      | 9.11 ms: 1.24x slower                                                          |
| Geometric mean         | (ref)                                                        | 1.21x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240701-pythonperf2-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 8.97 ms: 1.64x faster                                                          |
| django_template | 50.2 ms                                                      | 42.2 ms: 1.19x faster                                                          |
| genshi_text     | 31.4 ms                                                      | 27.2 ms: 1.15x faster                                                          |
| genshi_xml      | 63.3 ms                                                      | 62.0 ms: 1.02x faster                                                          |
| Geometric mean  | (ref)                                                        | 1.23x faster                                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240701-pythonperf2-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|--------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 184 us: 2.91x faster                                                           |
| asyncio_tcp              | 779 ms                                                       | 380 ms: 2.05x faster                                                           |
| async_tree_none          | 692 ms                                                       | 343 ms: 2.01x faster                                                           |
| async_tree_memoization   | 819 ms                                                       | 410 ms: 2.00x faster                                                           |
| async_tree_io            | 1.60 sec                                                     | 808 ms: 1.98x faster                                                           |
| deltablue                | 7.50 ms                                                      | 3.80 ms: 1.97x faster                                                          |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.96x faster                                                         |
| deepcopy_memo            | 49.8 us                                                      | 29.1 us: 1.71x faster                                                          |
| richards_super           | 90.6 ms                                                      | 53.1 ms: 1.71x faster                                                          |
| crypto_pyaes             | 119 ms                                                       | 71.2 ms: 1.67x faster                                                          |
| spectral_norm            | 139 ms                                                       | 83.2 ms: 1.67x faster                                                          |
| pyflate                  | 733 ms                                                       | 443 ms: 1.66x faster                                                           |
| logging_silent           | 167 ns                                                       | 101 ns: 1.65x faster                                                           |
| mako                     | 14.7 ms                                                      | 8.97 ms: 1.64x faster                                                          |
| richards                 | 75.1 ms                                                      | 45.8 ms: 1.64x faster                                                          |
| raytrace                 | 489 ms                                                       | 300 ms: 1.63x faster                                                           |
| scimark_monte_carlo      | 107 ms                                                       | 65.9 ms: 1.63x faster                                                          |
| generators               | 57.3 ms                                                      | 35.2 ms: 1.63x faster                                                          |
| chaos                    | 109 ms                                                       | 67.0 ms: 1.62x faster                                                          |
| nbody                    | 134 ms                                                       | 83.1 ms: 1.61x faster                                                          |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 584 ms: 1.60x faster                                                           |
| go                       | 262 ms                                                       | 165 ms: 1.58x faster                                                           |
| sqlglot_parse            | 2.24 ms                                                      | 1.42 ms: 1.57x faster                                                          |
| unpickle_pure_python     | 312 us                                                       | 202 us: 1.54x faster                                                           |
| deepcopy                 | 468 us                                                       | 307 us: 1.52x faster                                                           |
| float                    | 111 ms                                                       | 75.2 ms: 1.48x faster                                                          |
| pylint                   | 566 ms                                                       | 385 ms: 1.47x faster                                                           |
| sqlglot_transpile        | 2.68 ms                                                      | 1.82 ms: 1.47x faster                                                          |
| scimark_lu               | 167 ms                                                       | 115 ms: 1.45x faster                                                           |
| comprehensions           | 26.7 us                                                      | 18.5 us: 1.45x faster                                                          |
| pickle_pure_python       | 455 us                                                       | 317 us: 1.44x faster                                                           |
| coroutines               | 30.3 ms                                                      | 21.2 ms: 1.43x faster                                                          |
| hexiom                   | 9.42 ms                                                      | 6.70 ms: 1.41x faster                                                          |
| tomli_loads              | 2.92 sec                                                     | 2.10 sec: 1.39x faster                                                         |
| logging_simple           | 8.88 us                                                      | 6.40 us: 1.39x faster                                                          |
| regex_compile            | 190 ms                                                       | 138 ms: 1.38x faster                                                           |
| fannkuch                 | 483 ms                                                       | 352 ms: 1.37x faster                                                           |
| scimark_sor              | 180 ms                                                       | 132 ms: 1.36x faster                                                           |
| logging_format           | 9.64 us                                                      | 7.11 us: 1.36x faster                                                          |
| json_dumps               | 14.5 ms                                                      | 10.8 ms: 1.35x faster                                                          |
| pathlib                  | 21.4 ms                                                      | 16.1 ms: 1.33x faster                                                          |
| thrift                   | 1.18 ms                                                      | 889 us: 1.32x faster                                                           |
| pprint_safe_repr         | 1.05 sec                                                     | 797 ms: 1.32x faster                                                           |
| pprint_pformat           | 2.15 sec                                                     | 1.64 sec: 1.31x faster                                                         |
| deepcopy_reduce          | 4.01 us                                                      | 3.06 us: 1.31x faster                                                          |
| bench_mp_pool            | 6.37 ms                                                      | 4.86 ms: 1.31x faster                                                          |
| xml_etree_process        | 75.9 ms                                                      | 58.3 ms: 1.30x faster                                                          |
| pycparser                | 1.67 sec                                                     | 1.29 sec: 1.30x faster                                                         |
| tornado_http             | 157 ms                                                       | 121 ms: 1.30x faster                                                           |
| html5lib                 | 94.6 ms                                                      | 73.0 ms: 1.30x faster                                                          |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.05 ms: 1.26x faster                                                          |
| bench_thread_pool        | 1.14 ms                                                      | 926 us: 1.23x faster                                                           |
| scimark_fft              | 361 ms                                                       | 293 ms: 1.23x faster                                                           |
| dulwich_log              | 81.1 ms                                                      | 66.4 ms: 1.22x faster                                                          |
| json_loads               | 30.3 us                                                      | 25.2 us: 1.20x faster                                                          |
| nqueens                  | 115 ms                                                       | 95.5 ms: 1.20x faster                                                          |
| django_template          | 50.2 ms                                                      | 42.2 ms: 1.19x faster                                                          |
| mdp                      | 3.01 sec                                                     | 2.54 sec: 1.18x faster                                                         |
| dask                     | 472 ms                                                       | 399 ms: 1.18x faster                                                           |
| sympy_str                | 360 ms                                                       | 311 ms: 1.16x faster                                                           |
| genshi_text              | 31.4 ms                                                      | 27.2 ms: 1.15x faster                                                          |
| sympy_sum                | 193 ms                                                       | 167 ms: 1.15x faster                                                           |
| sympy_expand             | 600 ms                                                       | 528 ms: 1.14x faster                                                           |
| 2to3                     | 350 ms                                                       | 309 ms: 1.13x faster                                                           |
| sqlglot_normalize        | 144 ms                                                       | 128 ms: 1.13x faster                                                           |
| xml_etree_parse          | 160 ms                                                       | 143 ms: 1.12x faster                                                           |
| xml_etree_generate       | 92.3 ms                                                      | 82.5 ms: 1.12x faster                                                          |
| xml_etree_iterparse      | 110 ms                                                       | 98.9 ms: 1.12x faster                                                          |
| sqlglot_optimize         | 70.1 ms                                                      | 63.1 ms: 1.11x faster                                                          |
| async_generators         | 421 ms                                                       | 385 ms: 1.09x faster                                                           |
| regex_dna                | 261 ms                                                       | 240 ms: 1.09x faster                                                           |
| docutils                 | 3.41 sec                                                     | 3.14 sec: 1.09x faster                                                         |
| sympy_integrate          | 28.2 ms                                                      | 26.0 ms: 1.08x faster                                                          |
| pidigits                 | 271 ms                                                       | 250 ms: 1.08x faster                                                           |
| json                     | 5.86 ms                                                      | 5.47 ms: 1.07x faster                                                          |
| regex_v8                 | 27.2 ms                                                      | 25.5 ms: 1.07x faster                                                          |
| meteor_contest           | 138 ms                                                       | 131 ms: 1.06x faster                                                           |
| genshi_xml               | 63.3 ms                                                      | 62.0 ms: 1.02x faster                                                          |
| asyncio_websockets       | 390 ms                                                       | 401 ms: 1.03x slower                                                           |
| create_gc_cycles         | 1.76 ms                                                      | 1.95 ms: 1.11x slower                                                          |
| telco                    | 7.23 ms                                                      | 8.10 ms: 1.12x slower                                                          |
| python_startup           | 11.5 ms                                                      | 13.4 ms: 1.17x slower                                                          |
| regex_effbot             | 3.09 ms                                                      | 3.66 ms: 1.18x slower                                                          |
| python_startup_no_site   | 7.33 ms                                                      | 9.11 ms: 1.24x slower                                                          |
| coverage                 | 63.3 ms                                                      | 82.0 ms: 1.30x slower                                                          |
| gc_traversal             | 3.42 ms                                                      | 4.49 ms: 1.31x slower                                                          |
| Geometric mean           | (ref)                                                        | 1.32x faster                                                                   |
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240701-3.14.0a0-8423e72-JIT/bm-20240701-pythonperf2-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: 1.22x