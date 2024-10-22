# Results vs. 3.10.4

- fork: python
- ref: b9e10d1a0fc4d8428d4b
- machine: linux-x86_64
- commit hash: b9e10d1
- commit date: 2024-08-19
- overall geometric mean: 1.36x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240819-pythonperf2-x86_64-python-b9e10d1a0fc4d8428d4b-3.14.0a0-b9e10d1 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 284 ms: 1.23x faster                                                        |
| docutils       | 3.41 sec                                                     | 2.97 sec: 1.15x faster                                                      |
| html5lib       | 94.6 ms                                                      | 72.5 ms: 1.31x faster                                                       |
| tornado_http   | 157 ms                                                       | 116 ms: 1.36x faster                                                        |
| Geometric mean | (ref)                                                        | 1.26x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240819-pythonperf2-x86_64-python-b9e10d1a0fc4d8428d4b-3.14.0a0-b9e10d1 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 334 ms: 2.07x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 402 ms: 2.04x faster                                                        |
| async_tree_io           | 1.60 sec                                                     | 803 ms: 1.99x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 576 ms: 1.63x faster                                                        |
| Geometric mean          | (ref)                                                        | 1.92x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240819-pythonperf2-x86_64-python-b9e10d1a0fc4d8428d4b-3.14.0a0-b9e10d1 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 85.1 ms: 1.58x faster                                                       |
| float          | 111 ms                                                       | 80.8 ms: 1.37x faster                                                       |
| pidigits       | 271 ms                                                       | 252 ms: 1.07x faster                                                        |
| Geometric mean | (ref)                                                        | 1.32x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240819-pythonperf2-x86_64-python-b9e10d1a0fc4d8428d4b-3.14.0a0-b9e10d1 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 139 ms: 1.36x faster                                                        |
| regex_dna      | 261 ms                                                       | 238 ms: 1.10x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 26.0 ms: 1.04x faster                                                       |
| regex_effbot   | 3.09 ms                                                      | 3.64 ms: 1.18x slower                                                       |
| Geometric mean | (ref)                                                        | 1.07x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240819-pythonperf2-x86_64-python-b9e10d1a0fc4d8428d4b-3.14.0a0-b9e10d1 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 214 us: 1.45x faster                                                        |
| pickle_pure_python   | 455 us                                                       | 315 us: 1.44x faster                                                        |
| json_dumps           | 14.5 ms                                                      | 10.7 ms: 1.36x faster                                                       |
| xml_etree_process    | 75.9 ms                                                      | 58.7 ms: 1.29x faster                                                       |
| tomli_loads          | 2.92 sec                                                     | 2.29 sec: 1.27x faster                                                      |
| json_loads           | 30.3 us                                                      | 25.0 us: 1.21x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 141 ms: 1.14x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 99.7 ms: 1.11x faster                                                       |
| xml_etree_generate   | 92.3 ms                                                      | 84.3 ms: 1.09x faster                                                       |
| Geometric mean       | (ref)                                                        | 1.26x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240819-pythonperf2-x86_64-python-b9e10d1a0fc4d8428d4b-3.14.0a0-b9e10d1 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.3 ms: 1.16x slower                                                       |
| python_startup_no_site | 7.33 ms                                                      | 9.05 ms: 1.23x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240819-pythonperf2-x86_64-python-b9e10d1a0fc4d8428d4b-3.14.0a0-b9e10d1 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.4 ms: 1.42x faster                                                       |
| django_template | 50.2 ms                                                      | 38.4 ms: 1.31x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 25.0 ms: 1.26x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 53.4 ms: 1.18x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.29x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240819-pythonperf2-x86_64-python-b9e10d1a0fc4d8428d4b-3.14.0a0-b9e10d1 |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 174 us: 3.08x faster                                                        |
| deltablue                | 7.50 ms                                                      | 3.35 ms: 2.24x faster                                                       |
| asyncio_tcp              | 779 ms                                                       | 374 ms: 2.08x faster                                                        |
| async_tree_none          | 692 ms                                                       | 334 ms: 2.07x faster                                                        |
| generators               | 57.3 ms                                                      | 28.1 ms: 2.04x faster                                                       |
| async_tree_memoization   | 819 ms                                                       | 402 ms: 2.04x faster                                                        |
| async_tree_io            | 1.60 sec                                                     | 803 ms: 1.99x faster                                                        |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.97x faster                                                      |
| raytrace                 | 489 ms                                                       | 265 ms: 1.85x faster                                                        |
| chaos                    | 109 ms                                                       | 61.3 ms: 1.77x faster                                                       |
| scimark_lu               | 167 ms                                                       | 95.8 ms: 1.74x faster                                                       |
| logging_silent           | 167 ns                                                       | 97.3 ns: 1.72x faster                                                       |
| deepcopy_memo            | 49.8 us                                                      | 29.4 us: 1.69x faster                                                       |
| go                       | 262 ms                                                       | 157 ms: 1.66x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 72.0 ms: 1.65x faster                                                       |
| pylint                   | 566 ms                                                       | 346 ms: 1.64x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 576 ms: 1.63x faster                                                        |
| deepcopy                 | 468 us                                                       | 288 us: 1.63x faster                                                        |
| richards_super           | 90.6 ms                                                      | 56.8 ms: 1.60x faster                                                       |
| sqlglot_parse            | 2.24 ms                                                      | 1.41 ms: 1.59x faster                                                       |
| scimark_monte_carlo      | 107 ms                                                       | 68.0 ms: 1.58x faster                                                       |
| pyflate                  | 733 ms                                                       | 464 ms: 1.58x faster                                                        |
| nbody                    | 134 ms                                                       | 85.1 ms: 1.58x faster                                                       |
| comprehensions           | 26.7 us                                                      | 17.0 us: 1.57x faster                                                       |
| scimark_sor              | 180 ms                                                       | 115 ms: 1.57x faster                                                        |
| sqlglot_transpile        | 2.68 ms                                                      | 1.78 ms: 1.51x faster                                                       |
| richards                 | 75.1 ms                                                      | 50.4 ms: 1.49x faster                                                       |
| hexiom                   | 9.42 ms                                                      | 6.33 ms: 1.49x faster                                                       |
| unpickle_pure_python     | 312 us                                                       | 214 us: 1.45x faster                                                        |
| pickle_pure_python       | 455 us                                                       | 315 us: 1.44x faster                                                        |
| spectral_norm            | 139 ms                                                       | 96.6 ms: 1.44x faster                                                       |
| logging_simple           | 8.88 us                                                      | 6.18 us: 1.44x faster                                                       |
| logging_format           | 9.64 us                                                      | 6.77 us: 1.42x faster                                                       |
| coroutines               | 30.3 ms                                                      | 21.3 ms: 1.42x faster                                                       |
| mako                     | 14.7 ms                                                      | 10.4 ms: 1.42x faster                                                       |
| bench_mp_pool            | 6.37 ms                                                      | 4.54 ms: 1.40x faster                                                       |
| deepcopy_reduce          | 4.01 us                                                      | 2.89 us: 1.39x faster                                                       |
| float                    | 111 ms                                                       | 80.8 ms: 1.37x faster                                                       |
| regex_compile            | 190 ms                                                       | 139 ms: 1.36x faster                                                        |
| json_dumps               | 14.5 ms                                                      | 10.7 ms: 1.36x faster                                                       |
| tornado_http             | 157 ms                                                       | 116 ms: 1.36x faster                                                        |
| thrift                   | 1.18 ms                                                      | 867 us: 1.36x faster                                                        |
| fannkuch                 | 483 ms                                                       | 358 ms: 1.35x faster                                                        |
| pycparser                | 1.67 sec                                                     | 1.25 sec: 1.34x faster                                                      |
| pathlib                  | 21.4 ms                                                      | 15.9 ms: 1.34x faster                                                       |
| bench_thread_pool        | 1.14 ms                                                      | 860 us: 1.33x faster                                                        |
| django_template          | 50.2 ms                                                      | 38.4 ms: 1.31x faster                                                       |
| html5lib                 | 94.6 ms                                                      | 72.5 ms: 1.31x faster                                                       |
| xml_etree_process        | 75.9 ms                                                      | 58.7 ms: 1.29x faster                                                       |
| pprint_pformat           | 2.15 sec                                                     | 1.68 sec: 1.28x faster                                                      |
| nqueens                  | 115 ms                                                       | 89.7 ms: 1.28x faster                                                       |
| pprint_safe_repr         | 1.05 sec                                                     | 820 ms: 1.28x faster                                                        |
| tomli_loads              | 2.92 sec                                                     | 2.29 sec: 1.27x faster                                                      |
| genshi_text              | 31.4 ms                                                      | 25.0 ms: 1.26x faster                                                       |
| sympy_sum                | 193 ms                                                       | 154 ms: 1.25x faster                                                        |
| 2to3                     | 350 ms                                                       | 284 ms: 1.23x faster                                                        |
| sympy_str                | 360 ms                                                       | 293 ms: 1.23x faster                                                        |
| sympy_integrate          | 28.2 ms                                                      | 23.2 ms: 1.21x faster                                                       |
| json_loads               | 30.3 us                                                      | 25.0 us: 1.21x faster                                                       |
| sqlglot_normalize        | 144 ms                                                       | 119 ms: 1.20x faster                                                        |
| mdp                      | 3.01 sec                                                     | 2.50 sec: 1.20x faster                                                      |
| sympy_expand             | 600 ms                                                       | 500 ms: 1.20x faster                                                        |
| sqlglot_optimize         | 70.1 ms                                                      | 59.1 ms: 1.19x faster                                                       |
| scimark_fft              | 361 ms                                                       | 305 ms: 1.18x faster                                                        |
| genshi_xml               | 63.3 ms                                                      | 53.4 ms: 1.18x faster                                                       |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.29 ms: 1.18x faster                                                       |
| async_generators         | 421 ms                                                       | 362 ms: 1.16x faster                                                        |
| docutils                 | 3.41 sec                                                     | 2.97 sec: 1.15x faster                                                      |
| xml_etree_parse          | 160 ms                                                       | 141 ms: 1.14x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 99.7 ms: 1.11x faster                                                       |
| json                     | 5.86 ms                                                      | 5.31 ms: 1.10x faster                                                       |
| regex_dna                | 261 ms                                                       | 238 ms: 1.10x faster                                                        |
| meteor_contest           | 138 ms                                                       | 126 ms: 1.10x faster                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 84.3 ms: 1.09x faster                                                       |
| pidigits                 | 271 ms                                                       | 252 ms: 1.07x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 26.0 ms: 1.04x faster                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 1.97 ms: 1.12x slower                                                       |
| telco                    | 7.23 ms                                                      | 8.19 ms: 1.13x slower                                                       |
| python_startup           | 11.5 ms                                                      | 13.3 ms: 1.16x slower                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.64 ms: 1.18x slower                                                       |
| coverage                 | 63.3 ms                                                      | 77.3 ms: 1.22x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 9.05 ms: 1.23x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 4.47 ms: 1.31x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.36x faster                                                                |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240819-3.14.0a0-b9e10d1/bm-20240819-pythonperf2-x86_64-python-b9e10d1a0fc4d8428d4b-3.14.0a0-b9e10d1.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: 1.13x