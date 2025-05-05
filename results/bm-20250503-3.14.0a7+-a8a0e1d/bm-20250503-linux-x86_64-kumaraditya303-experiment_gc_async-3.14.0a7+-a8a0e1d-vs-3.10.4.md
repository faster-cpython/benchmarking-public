# Results vs. 3.10.4

- fork: kumaraditya303
- ref: experiment_gc_async
- machine: linux-x86_64
- commit hash: a8a0e1d
- commit date: 2025-05-03
- overall geometric mean: 1.426x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.31x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250503-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-a8a0e1d |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 253 ms: 1.38x faster                                                          |
| docutils       | 3.30 sec                                               | 2.62 sec: 1.26x faster                                                        |
| html5lib       | 88.9 ms                                                | 61.4 ms: 1.45x faster                                                         |
| Geometric mean | (ref)                                                  | 1.36x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250503-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-a8a0e1d |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_memoization  | 870 ms                                                 | 383 ms: 2.27x faster                                                          |
| async_tree_none         | 728 ms                                                 | 321 ms: 2.27x faster                                                          |
| async_tree_io           | 1.77 sec                                               | 804 ms: 2.20x faster                                                          |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 561 ms: 1.81x faster                                                          |
| Geometric mean          | (ref)                                                  | 2.13x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250503-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-a8a0e1d |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 71.1 ms: 1.65x faster                                                         |
| nbody          | 154 ms                                                 | 96.3 ms: 1.59x faster                                                         |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                          |
| Geometric mean | (ref)                                                  | 1.39x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250503-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-a8a0e1d |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 127 ms: 1.48x faster                                                          |
| regex_v8       | 27.8 ms                                                | 22.8 ms: 1.22x faster                                                         |
| regex_dna      | 227 ms                                                 | 207 ms: 1.10x faster                                                          |
| regex_effbot   | 3.63 ms                                                | 3.33 ms: 1.09x faster                                                         |
| Geometric mean | (ref)                                                  | 1.21x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250503-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-a8a0e1d |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 2.02 sec: 1.55x faster                                                        |
| unpickle_pure_python | 331 us                                                 | 218 us: 1.52x faster                                                          |
| pickle_pure_python   | 484 us                                                 | 320 us: 1.52x faster                                                          |
| xml_etree_process    | 79.1 ms                                                | 59.8 ms: 1.32x faster                                                         |
| json_dumps           | 14.2 ms                                                | 11.8 ms: 1.20x faster                                                         |
| xml_etree_iterparse  | 115 ms                                                 | 99.8 ms: 1.16x faster                                                         |
| xml_etree_parse      | 168 ms                                                 | 145 ms: 1.16x faster                                                          |
| xml_etree_generate   | 99.4 ms                                                | 86.1 ms: 1.16x faster                                                         |
| json_loads           | 31.2 us                                                | 30.0 us: 1.04x faster                                                         |
| Geometric mean       | (ref)                                                  | 1.28x faster                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250503-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-a8a0e1d |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.2 ms: 1.10x faster                                                         |
| python_startup_no_site | 5.93 ms                                                | 6.95 ms: 1.17x slower                                                         |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250503-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-a8a0e1d |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 31.8 ms: 1.51x faster                                                         |
| genshi_text     | 31.8 ms                                                | 21.2 ms: 1.50x faster                                                         |
| mako            | 16.3 ms                                                | 11.8 ms: 1.39x faster                                                         |
| genshi_xml      | 66.0 ms                                                | 49.2 ms: 1.34x faster                                                         |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                                  |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250503-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-a8a0e1d |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 166 us: 3.27x faster                                                          |
| generators               | 80.1 ms                                                | 29.2 ms: 2.74x faster                                                         |
| deltablue                | 7.91 ms                                                | 3.38 ms: 2.34x faster                                                         |
| mdp                      | 2.85 sec                                               | 1.23 sec: 2.32x faster                                                        |
| async_tree_memoization   | 870 ms                                                 | 383 ms: 2.27x faster                                                          |
| async_tree_none          | 728 ms                                                 | 321 ms: 2.27x faster                                                          |
| async_tree_io            | 1.77 sec                                               | 804 ms: 2.20x faster                                                          |
| go                       | 240 ms                                                 | 113 ms: 2.12x faster                                                          |
| deepcopy_memo            | 58.5 us                                                | 29.6 us: 1.97x faster                                                         |
| pylint                   | 551 ms                                                 | 281 ms: 1.96x faster                                                          |
| chaos                    | 115 ms                                                 | 59.5 ms: 1.94x faster                                                         |
| logging_silent           | 190 ns                                                 | 99.4 ns: 1.91x faster                                                         |
| richards_super           | 94.7 ms                                                | 50.5 ms: 1.88x faster                                                         |
| raytrace                 | 507 ms                                                 | 272 ms: 1.86x faster                                                          |
| deepcopy                 | 479 us                                                 | 262 us: 1.83x faster                                                          |
| scimark_sor              | 220 ms                                                 | 121 ms: 1.82x faster                                                          |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 561 ms: 1.81x faster                                                          |
| richards                 | 79.3 ms                                                | 44.4 ms: 1.78x faster                                                         |
| scimark_monte_carlo      | 118 ms                                                 | 67.7 ms: 1.74x faster                                                         |
| crypto_pyaes             | 128 ms                                                 | 75.2 ms: 1.70x faster                                                         |
| pyflate                  | 716 ms                                                 | 426 ms: 1.68x faster                                                          |
| comprehensions           | 28.8 us                                                | 17.2 us: 1.67x faster                                                         |
| float                    | 117 ms                                                 | 71.1 ms: 1.65x faster                                                         |
| hexiom                   | 10.4 ms                                                | 6.32 ms: 1.64x faster                                                         |
| nbody                    | 154 ms                                                 | 96.3 ms: 1.59x faster                                                         |
| spectral_norm            | 170 ms                                                 | 108 ms: 1.57x faster                                                          |
| tomli_loads              | 3.14 sec                                               | 2.02 sec: 1.55x faster                                                        |
| unpickle_pure_python     | 331 us                                                 | 218 us: 1.52x faster                                                          |
| pickle_pure_python       | 484 us                                                 | 320 us: 1.52x faster                                                          |
| django_template          | 48.2 ms                                                | 31.8 ms: 1.51x faster                                                         |
| deepcopy_reduce          | 4.17 us                                                | 2.76 us: 1.51x faster                                                         |
| genshi_text              | 31.8 ms                                                | 21.2 ms: 1.50x faster                                                         |
| logging_simple           | 8.30 us                                                | 5.59 us: 1.49x faster                                                         |
| scimark_lu               | 176 ms                                                 | 119 ms: 1.48x faster                                                          |
| regex_compile            | 188 ms                                                 | 127 ms: 1.48x faster                                                          |
| logging_format           | 9.09 us                                                | 6.26 us: 1.45x faster                                                         |
| html5lib                 | 88.9 ms                                                | 61.4 ms: 1.45x faster                                                         |
| pprint_pformat           | 2.10 sec                                               | 1.48 sec: 1.42x faster                                                        |
| dulwich_log              | 84.3 ms                                                | 59.9 ms: 1.41x faster                                                         |
| pprint_safe_repr         | 1.02 sec                                               | 730 ms: 1.39x faster                                                          |
| mako                     | 16.3 ms                                                | 11.8 ms: 1.39x faster                                                         |
| pycparser                | 1.58 sec                                               | 1.14 sec: 1.38x faster                                                        |
| 2to3                     | 348 ms                                                 | 253 ms: 1.38x faster                                                          |
| coroutines               | 35.1 ms                                                | 25.8 ms: 1.36x faster                                                         |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.2 ms: 1.36x faster                                                         |
| sympy_integrate          | 25.8 ms                                                | 19.1 ms: 1.35x faster                                                         |
| genshi_xml               | 66.0 ms                                                | 49.2 ms: 1.34x faster                                                         |
| xml_etree_process        | 79.1 ms                                                | 59.8 ms: 1.32x faster                                                         |
| sympy_sum                | 196 ms                                                 | 149 ms: 1.32x faster                                                          |
| nqueens                  | 106 ms                                                 | 81.0 ms: 1.31x faster                                                         |
| sqlalchemy_declarative   | 172 ms                                                 | 133 ms: 1.30x faster                                                          |
| sympy_str                | 346 ms                                                 | 267 ms: 1.30x faster                                                          |
| fannkuch                 | 532 ms                                                 | 410 ms: 1.30x faster                                                          |
| scimark_fft              | 466 ms                                                 | 369 ms: 1.26x faster                                                          |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.14 ms: 1.26x faster                                                         |
| docutils                 | 3.30 sec                                               | 2.62 sec: 1.26x faster                                                        |
| sympy_expand             | 566 ms                                                 | 454 ms: 1.25x faster                                                          |
| regex_v8                 | 27.8 ms                                                | 22.8 ms: 1.22x faster                                                         |
| pathlib                  | 20.5 ms                                                | 16.9 ms: 1.21x faster                                                         |
| json_dumps               | 14.2 ms                                                | 11.8 ms: 1.20x faster                                                         |
| xml_etree_iterparse      | 115 ms                                                 | 99.8 ms: 1.16x faster                                                         |
| xml_etree_parse          | 168 ms                                                 | 145 ms: 1.16x faster                                                          |
| xml_etree_generate       | 99.4 ms                                                | 86.1 ms: 1.16x faster                                                         |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                          |
| bench_thread_pool        | 986 us                                                 | 888 us: 1.11x faster                                                          |
| python_startup           | 14.6 ms                                                | 13.2 ms: 1.10x faster                                                         |
| regex_dna                | 227 ms                                                 | 207 ms: 1.10x faster                                                          |
| regex_effbot             | 3.63 ms                                                | 3.33 ms: 1.09x faster                                                         |
| async_generators         | 444 ms                                                 | 413 ms: 1.07x faster                                                          |
| json                     | 5.69 ms                                                | 5.31 ms: 1.07x faster                                                         |
| sqlite_synth             | 3.02 us                                                | 2.87 us: 1.05x faster                                                         |
| json_loads               | 31.2 us                                                | 30.0 us: 1.04x faster                                                         |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                          |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                                          |
| telco                    | 7.27 ms                                                | 8.02 ms: 1.10x slower                                                         |
| python_startup_no_site   | 5.93 ms                                                | 6.95 ms: 1.17x slower                                                         |
| coverage                 | 79.4 ms                                                | 94.5 ms: 1.19x slower                                                         |
| gc_traversal             | 3.62 ms                                                | 5.01 ms: 1.38x slower                                                         |
| create_gc_cycles         | 1.62 ms                                                | 2.51 ms: 1.55x slower                                                         |
| bench_mp_pool            | 24.0 ms                                                | 83.5 ms: 3.48x slower                                                         |
| Geometric mean           | (ref)                                                  | 1.40x faster                                                                  |
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (23) of results/bm-20250503-3.14.0a7+-a8a0e1d/bm-20250503-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-a8a0e1d.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.426x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.35x
- 95% likely to have a speedup of 1.34x
- 99% likely to have a speedup of 1.31x

# Memory
- memory change: 1.28x