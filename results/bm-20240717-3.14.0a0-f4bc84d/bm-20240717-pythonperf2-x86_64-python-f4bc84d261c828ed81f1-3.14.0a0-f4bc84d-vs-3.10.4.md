# Results vs. 3.10.4

- fork: python
- ref: f4bc84d261c828ed81f1
- machine: linux-x86_64
- commit hash: f4bc84d
- commit date: 2024-07-17
- overall geometric mean: 1.35x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240717-pythonperf2-x86_64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 289 ms: 1.21x faster                                                        |
| docutils       | 3.41 sec                                                     | 2.97 sec: 1.15x faster                                                      |
| html5lib       | 94.6 ms                                                      | 73.4 ms: 1.29x faster                                                       |
| tornado_http   | 157 ms                                                       | 119 ms: 1.32x faster                                                        |
| Geometric mean | (ref)                                                        | 1.24x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240717-pythonperf2-x86_64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 336 ms: 2.06x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 403 ms: 2.03x faster                                                        |
| async_tree_io           | 1.60 sec                                                     | 796 ms: 2.01x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 578 ms: 1.62x faster                                                        |
| Geometric mean          | (ref)                                                        | 1.92x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240717-pythonperf2-x86_64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 90.9 ms: 1.47x faster                                                       |
| float          | 111 ms                                                       | 79.9 ms: 1.39x faster                                                       |
| pidigits       | 271 ms                                                       | 253 ms: 1.07x faster                                                        |
| Geometric mean | (ref)                                                        | 1.30x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240717-pythonperf2-x86_64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 140 ms: 1.35x faster                                                        |
| regex_dna      | 261 ms                                                       | 241 ms: 1.09x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 26.3 ms: 1.03x faster                                                       |
| regex_effbot   | 3.09 ms                                                      | 3.56 ms: 1.15x slower                                                       |
| Geometric mean | (ref)                                                        | 1.07x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240717-pythonperf2-x86_64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                       | 313 us: 1.45x faster                                                        |
| unpickle_pure_python | 312 us                                                       | 224 us: 1.40x faster                                                        |
| json_dumps           | 14.5 ms                                                      | 11.0 ms: 1.32x faster                                                       |
| xml_etree_process    | 75.9 ms                                                      | 59.8 ms: 1.27x faster                                                       |
| tomli_loads          | 2.92 sec                                                     | 2.43 sec: 1.20x faster                                                      |
| json_loads           | 30.3 us                                                      | 25.4 us: 1.19x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 143 ms: 1.12x faster                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 84.5 ms: 1.09x faster                                                       |
| xml_etree_iterparse  | 110 ms                                                       | 105 ms: 1.05x faster                                                        |
| Geometric mean       | (ref)                                                        | 1.23x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240717-pythonperf2-x86_64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.5 ms: 1.17x slower                                                       |
| python_startup_no_site | 7.33 ms                                                      | 9.11 ms: 1.24x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.21x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240717-pythonperf2-x86_64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.5 ms: 1.40x faster                                                       |
| django_template | 50.2 ms                                                      | 38.9 ms: 1.29x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 25.2 ms: 1.25x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 56.0 ms: 1.13x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.26x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240717-pythonperf2-x86_64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 169 us: 3.17x faster                                                        |
| deltablue                | 7.50 ms                                                      | 3.41 ms: 2.20x faster                                                       |
| asyncio_tcp              | 779 ms                                                       | 373 ms: 2.09x faster                                                        |
| async_tree_none          | 692 ms                                                       | 336 ms: 2.06x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 403 ms: 2.03x faster                                                        |
| async_tree_io            | 1.60 sec                                                     | 796 ms: 2.01x faster                                                        |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.96x faster                                                      |
| raytrace                 | 489 ms                                                       | 272 ms: 1.80x faster                                                        |
| chaos                    | 109 ms                                                       | 61.4 ms: 1.77x faster                                                       |
| scimark_lu               | 167 ms                                                       | 96.1 ms: 1.74x faster                                                       |
| logging_silent           | 167 ns                                                       | 97.8 ns: 1.71x faster                                                       |
| deepcopy_memo            | 49.8 us                                                      | 29.3 us: 1.70x faster                                                       |
| generators               | 57.3 ms                                                      | 33.9 ms: 1.69x faster                                                       |
| pylint                   | 566 ms                                                       | 337 ms: 1.68x faster                                                        |
| go                       | 262 ms                                                       | 156 ms: 1.68x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 71.6 ms: 1.67x faster                                                       |
| deepcopy                 | 468 us                                                       | 283 us: 1.65x faster                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 65.0 ms: 1.65x faster                                                       |
| scimark_sor              | 180 ms                                                       | 110 ms: 1.64x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 578 ms: 1.62x faster                                                        |
| comprehensions           | 26.7 us                                                      | 17.0 us: 1.57x faster                                                       |
| pyflate                  | 733 ms                                                       | 468 ms: 1.57x faster                                                        |
| sqlglot_parse            | 2.24 ms                                                      | 1.43 ms: 1.56x faster                                                       |
| richards_super           | 90.6 ms                                                      | 57.9 ms: 1.56x faster                                                       |
| hexiom                   | 9.42 ms                                                      | 6.21 ms: 1.52x faster                                                       |
| sqlglot_transpile        | 2.68 ms                                                      | 1.81 ms: 1.49x faster                                                       |
| nbody                    | 134 ms                                                       | 90.9 ms: 1.47x faster                                                       |
| richards                 | 75.1 ms                                                      | 51.5 ms: 1.46x faster                                                       |
| pickle_pure_python       | 455 us                                                       | 313 us: 1.45x faster                                                        |
| spectral_norm            | 139 ms                                                       | 96.4 ms: 1.44x faster                                                       |
| coroutines               | 30.3 ms                                                      | 21.1 ms: 1.44x faster                                                       |
| logging_simple           | 8.88 us                                                      | 6.31 us: 1.41x faster                                                       |
| mako                     | 14.7 ms                                                      | 10.5 ms: 1.40x faster                                                       |
| unpickle_pure_python     | 312 us                                                       | 224 us: 1.40x faster                                                        |
| float                    | 111 ms                                                       | 79.9 ms: 1.39x faster                                                       |
| deepcopy_reduce          | 4.01 us                                                      | 2.89 us: 1.39x faster                                                       |
| logging_format           | 9.64 us                                                      | 6.96 us: 1.39x faster                                                       |
| bench_mp_pool            | 6.37 ms                                                      | 4.67 ms: 1.37x faster                                                       |
| regex_compile            | 190 ms                                                       | 140 ms: 1.35x faster                                                        |
| pathlib                  | 21.4 ms                                                      | 15.9 ms: 1.34x faster                                                       |
| pycparser                | 1.67 sec                                                     | 1.25 sec: 1.34x faster                                                      |
| json_dumps               | 14.5 ms                                                      | 11.0 ms: 1.32x faster                                                       |
| fannkuch                 | 483 ms                                                       | 365 ms: 1.32x faster                                                        |
| tornado_http             | 157 ms                                                       | 119 ms: 1.32x faster                                                        |
| thrift                   | 1.18 ms                                                      | 900 us: 1.31x faster                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 875 us: 1.30x faster                                                        |
| nqueens                  | 115 ms                                                       | 88.2 ms: 1.30x faster                                                       |
| pprint_pformat           | 2.15 sec                                                     | 1.67 sec: 1.29x faster                                                      |
| django_template          | 50.2 ms                                                      | 38.9 ms: 1.29x faster                                                       |
| html5lib                 | 94.6 ms                                                      | 73.4 ms: 1.29x faster                                                       |
| pprint_safe_repr         | 1.05 sec                                                     | 817 ms: 1.28x faster                                                        |
| xml_etree_process        | 75.9 ms                                                      | 59.8 ms: 1.27x faster                                                       |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.04 ms: 1.26x faster                                                       |
| genshi_text              | 31.4 ms                                                      | 25.2 ms: 1.25x faster                                                       |
| sympy_sum                | 193 ms                                                       | 156 ms: 1.24x faster                                                        |
| sympy_str                | 360 ms                                                       | 294 ms: 1.23x faster                                                        |
| 2to3                     | 350 ms                                                       | 289 ms: 1.21x faster                                                        |
| sympy_integrate          | 28.2 ms                                                      | 23.2 ms: 1.21x faster                                                       |
| sqlglot_normalize        | 144 ms                                                       | 119 ms: 1.21x faster                                                        |
| mdp                      | 3.01 sec                                                     | 2.50 sec: 1.20x faster                                                      |
| tomli_loads              | 2.92 sec                                                     | 2.43 sec: 1.20x faster                                                      |
| sqlglot_optimize         | 70.1 ms                                                      | 58.8 ms: 1.19x faster                                                       |
| scimark_fft              | 361 ms                                                       | 303 ms: 1.19x faster                                                        |
| json_loads               | 30.3 us                                                      | 25.4 us: 1.19x faster                                                       |
| dulwich_log              | 81.1 ms                                                      | 68.2 ms: 1.19x faster                                                       |
| sympy_expand             | 600 ms                                                       | 505 ms: 1.19x faster                                                        |
| async_generators         | 421 ms                                                       | 362 ms: 1.16x faster                                                        |
| docutils                 | 3.41 sec                                                     | 2.97 sec: 1.15x faster                                                      |
| genshi_xml               | 63.3 ms                                                      | 56.0 ms: 1.13x faster                                                       |
| xml_etree_parse          | 160 ms                                                       | 143 ms: 1.12x faster                                                        |
| meteor_contest           | 138 ms                                                       | 124 ms: 1.12x faster                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 84.5 ms: 1.09x faster                                                       |
| json                     | 5.86 ms                                                      | 5.38 ms: 1.09x faster                                                       |
| regex_dna                | 261 ms                                                       | 241 ms: 1.09x faster                                                        |
| pidigits                 | 271 ms                                                       | 253 ms: 1.07x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 105 ms: 1.05x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 26.3 ms: 1.03x faster                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 2.00 ms: 1.13x slower                                                       |
| telco                    | 7.23 ms                                                      | 8.27 ms: 1.14x slower                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.56 ms: 1.15x slower                                                       |
| python_startup           | 11.5 ms                                                      | 13.5 ms: 1.17x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 9.11 ms: 1.24x slower                                                       |
| coverage                 | 63.3 ms                                                      | 80.6 ms: 1.27x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 4.48 ms: 1.31x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.35x faster                                                                |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240717-3.14.0a0-f4bc84d/bm-20240717-pythonperf2-x86_64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.13x