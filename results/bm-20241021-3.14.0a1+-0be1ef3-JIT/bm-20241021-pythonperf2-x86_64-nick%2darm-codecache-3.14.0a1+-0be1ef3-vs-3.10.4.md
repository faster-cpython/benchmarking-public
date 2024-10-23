# Results vs. 3.10.4

- fork: nick-arm
- ref: codecache
- machine: linux-x86_64
- commit hash: 0be1ef3
- commit date: 2024-10-21
- overall geometric mean: 1.19x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster
- Memory change: 1.36x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 314 ms: 1.11x faster                                                  |
| docutils       | 3.41 sec                                                     | 3.18 sec: 1.07x faster                                                |
| html5lib       | 94.6 ms                                                      | 70.4 ms: 1.34x faster                                                 |
| tornado_http   | 157 ms                                                       | 123 ms: 1.28x faster                                                  |
| Geometric mean | (ref)                                                        | 1.20x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 341 ms: 2.03x faster                                                  |
| async_tree_memoization  | 819 ms                                                       | 412 ms: 1.99x faster                                                  |
| async_tree_io           | 1.60 sec                                                     | 835 ms: 1.91x faster                                                  |
| async_tree_cpu_io_mixed | 936 ms                                                       | 577 ms: 1.62x faster                                                  |
| Geometric mean          | (ref)                                                        | 1.88x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 87.0 ms: 1.54x faster                                                 |
| float          | 111 ms                                                       | 79.6 ms: 1.40x faster                                                 |
| pidigits       | 271 ms                                                       | 251 ms: 1.08x faster                                                  |
| Geometric mean | (ref)                                                        | 1.32x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 147 ms: 1.29x faster                                                  |
| regex_v8       | 27.2 ms                                                      | 25.9 ms: 1.05x faster                                                 |
| regex_dna      | 261 ms                                                       | 257 ms: 1.02x faster                                                  |
| regex_effbot   | 3.09 ms                                                      | 3.73 ms: 1.21x slower                                                 |
| Geometric mean | (ref)                                                        | 1.03x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 220 us: 1.42x faster                                                  |
| tomli_loads          | 2.92 sec                                                     | 2.11 sec: 1.38x faster                                                |
| pickle_pure_python   | 455 us                                                       | 332 us: 1.37x faster                                                  |
| json_dumps           | 14.5 ms                                                      | 11.1 ms: 1.31x faster                                                 |
| xml_etree_process    | 75.9 ms                                                      | 58.1 ms: 1.31x faster                                                 |
| json_loads           | 30.3 us                                                      | 25.0 us: 1.21x faster                                                 |
| xml_etree_generate   | 92.3 ms                                                      | 81.1 ms: 1.14x faster                                                 |
| xml_etree_iterparse  | 110 ms                                                       | 100 ms: 1.10x faster                                                  |
| xml_etree_parse      | 160 ms                                                       | 146 ms: 1.10x faster                                                  |
| Geometric mean       | (ref)                                                        | 1.25x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 9.03 ms: 1.23x slower                                                 |
| python_startup         | 11.5 ms                                                      | 14.9 ms: 1.30x slower                                                 |
| Geometric mean         | (ref)                                                        | 1.26x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.62 ms: 1.53x faster                                                 |
| django_template | 50.2 ms                                                      | 43.1 ms: 1.17x faster                                                 |
| genshi_text     | 31.4 ms                                                      | 27.7 ms: 1.13x faster                                                 |
| genshi_xml      | 63.3 ms                                                      | 61.9 ms: 1.02x faster                                                 |
| Geometric mean  | (ref)                                                        | 1.20x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 183 us: 2.93x faster                                                  |
| deltablue                | 7.50 ms                                                      | 3.34 ms: 2.25x faster                                                 |
| async_tree_none          | 692 ms                                                       | 341 ms: 2.03x faster                                                  |
| async_tree_memoization   | 819 ms                                                       | 412 ms: 1.99x faster                                                  |
| async_tree_io            | 1.60 sec                                                     | 835 ms: 1.91x faster                                                  |
| logging_silent           | 167 ns                                                       | 92.3 ns: 1.81x faster                                                 |
| scimark_lu               | 167 ms                                                       | 95.4 ms: 1.75x faster                                                 |
| scimark_sor              | 180 ms                                                       | 105 ms: 1.72x faster                                                  |
| go                       | 262 ms                                                       | 155 ms: 1.69x faster                                                  |
| richards                 | 75.1 ms                                                      | 45.1 ms: 1.67x faster                                                 |
| richards_super           | 90.6 ms                                                      | 54.7 ms: 1.66x faster                                                 |
| deepcopy_memo            | 49.8 us                                                      | 30.3 us: 1.65x faster                                                 |
| crypto_pyaes             | 119 ms                                                       | 73.0 ms: 1.63x faster                                                 |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 577 ms: 1.62x faster                                                  |
| chaos                    | 109 ms                                                       | 68.7 ms: 1.58x faster                                                 |
| pyflate                  | 733 ms                                                       | 466 ms: 1.57x faster                                                  |
| scimark_monte_carlo      | 107 ms                                                       | 68.8 ms: 1.56x faster                                                 |
| raytrace                 | 489 ms                                                       | 316 ms: 1.55x faster                                                  |
| nbody                    | 134 ms                                                       | 87.0 ms: 1.54x faster                                                 |
| mako                     | 14.7 ms                                                      | 9.62 ms: 1.53x faster                                                 |
| sqlglot_parse            | 2.24 ms                                                      | 1.50 ms: 1.50x faster                                                 |
| deepcopy                 | 468 us                                                       | 314 us: 1.49x faster                                                  |
| generators               | 57.3 ms                                                      | 38.7 ms: 1.48x faster                                                 |
| spectral_norm            | 139 ms                                                       | 94.8 ms: 1.47x faster                                                 |
| unpickle_pure_python     | 312 us                                                       | 220 us: 1.42x faster                                                  |
| comprehensions           | 26.7 us                                                      | 18.8 us: 1.42x faster                                                 |
| float                    | 111 ms                                                       | 79.6 ms: 1.40x faster                                                 |
| tomli_loads              | 2.92 sec                                                     | 2.11 sec: 1.38x faster                                                |
| pickle_pure_python       | 455 us                                                       | 332 us: 1.37x faster                                                  |
| sqlglot_transpile        | 2.68 ms                                                      | 1.96 ms: 1.37x faster                                                 |
| pylint                   | 566 ms                                                       | 415 ms: 1.37x faster                                                  |
| coroutines               | 30.3 ms                                                      | 22.3 ms: 1.36x faster                                                 |
| pathlib                  | 21.4 ms                                                      | 15.8 ms: 1.35x faster                                                 |
| html5lib                 | 94.6 ms                                                      | 70.4 ms: 1.34x faster                                                 |
| logging_format           | 9.64 us                                                      | 7.23 us: 1.33x faster                                                 |
| pprint_safe_repr         | 1.05 sec                                                     | 788 ms: 1.33x faster                                                  |
| deepcopy_reduce          | 4.01 us                                                      | 3.04 us: 1.32x faster                                                 |
| logging_simple           | 8.88 us                                                      | 6.75 us: 1.32x faster                                                 |
| fannkuch                 | 483 ms                                                       | 367 ms: 1.31x faster                                                  |
| pycparser                | 1.67 sec                                                     | 1.27 sec: 1.31x faster                                                |
| thrift                   | 1.18 ms                                                      | 897 us: 1.31x faster                                                  |
| json_dumps               | 14.5 ms                                                      | 11.1 ms: 1.31x faster                                                 |
| pprint_pformat           | 2.15 sec                                                     | 1.65 sec: 1.31x faster                                                |
| xml_etree_process        | 75.9 ms                                                      | 58.1 ms: 1.31x faster                                                 |
| hexiom                   | 9.42 ms                                                      | 7.21 ms: 1.31x faster                                                 |
| regex_compile            | 190 ms                                                       | 147 ms: 1.29x faster                                                  |
| dulwich_log              | 81.1 ms                                                      | 63.5 ms: 1.28x faster                                                 |
| tornado_http             | 157 ms                                                       | 123 ms: 1.28x faster                                                  |
| scimark_fft              | 361 ms                                                       | 285 ms: 1.27x faster                                                  |
| json_loads               | 30.3 us                                                      | 25.0 us: 1.21x faster                                                 |
| bench_thread_pool        | 1.14 ms                                                      | 940 us: 1.21x faster                                                  |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.21 ms: 1.21x faster                                                 |
| mdp                      | 3.01 sec                                                     | 2.57 sec: 1.17x faster                                                |
| django_template          | 50.2 ms                                                      | 43.1 ms: 1.17x faster                                                 |
| sympy_expand             | 600 ms                                                       | 527 ms: 1.14x faster                                                  |
| xml_etree_generate       | 92.3 ms                                                      | 81.1 ms: 1.14x faster                                                 |
| sympy_str                | 360 ms                                                       | 317 ms: 1.14x faster                                                  |
| genshi_text              | 31.4 ms                                                      | 27.7 ms: 1.13x faster                                                 |
| nqueens                  | 115 ms                                                       | 102 ms: 1.13x faster                                                  |
| json                     | 5.86 ms                                                      | 5.22 ms: 1.12x faster                                                 |
| 2to3                     | 350 ms                                                       | 314 ms: 1.11x faster                                                  |
| sympy_sum                | 193 ms                                                       | 173 ms: 1.11x faster                                                  |
| xml_etree_iterparse      | 110 ms                                                       | 100 ms: 1.10x faster                                                  |
| xml_etree_parse          | 160 ms                                                       | 146 ms: 1.10x faster                                                  |
| async_generators         | 421 ms                                                       | 387 ms: 1.09x faster                                                  |
| sqlglot_normalize        | 144 ms                                                       | 133 ms: 1.08x faster                                                  |
| pidigits                 | 271 ms                                                       | 251 ms: 1.08x faster                                                  |
| docutils                 | 3.41 sec                                                     | 3.18 sec: 1.07x faster                                                |
| regex_v8                 | 27.2 ms                                                      | 25.9 ms: 1.05x faster                                                 |
| meteor_contest           | 138 ms                                                       | 132 ms: 1.05x faster                                                  |
| sympy_integrate          | 28.2 ms                                                      | 27.2 ms: 1.04x faster                                                 |
| genshi_xml               | 63.3 ms                                                      | 61.9 ms: 1.02x faster                                                 |
| sqlglot_optimize         | 70.1 ms                                                      | 68.8 ms: 1.02x faster                                                 |
| asyncio_websockets       | 390 ms                                                       | 382 ms: 1.02x faster                                                  |
| regex_dna                | 261 ms                                                       | 257 ms: 1.02x faster                                                  |
| telco                    | 7.23 ms                                                      | 7.78 ms: 1.08x slower                                                 |
| regex_effbot             | 3.09 ms                                                      | 3.73 ms: 1.21x slower                                                 |
| coverage                 | 63.3 ms                                                      | 77.8 ms: 1.23x slower                                                 |
| python_startup_no_site   | 7.33 ms                                                      | 9.03 ms: 1.23x slower                                                 |
| python_startup           | 11.5 ms                                                      | 14.9 ms: 1.30x slower                                                 |
| create_gc_cycles         | 1.76 ms                                                      | 2.90 ms: 1.65x slower                                                 |
| gc_traversal             | 3.42 ms                                                      | 5.81 ms: 1.70x slower                                                 |
| bench_mp_pool            | 6.37 ms                                                      | 3.17 sec: 497.35x slower                                              |
| Geometric mean           | (ref)                                                        | 1.19x faster                                                          |
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20241021-3.14.0a1+-0be1ef3-JIT/bm-20241021-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.17x

# Memory
- memory change: 1.36x