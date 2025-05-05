# Results vs. 3.10.4

- fork: kumaraditya303
- ref: experiment_gc_async
- machine: linux-x86_64
- commit hash: a8a0e1d
- commit date: 2025-05-03
- overall geometric mean: 1.309x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster
- Memory change: 1.53x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250503-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-a8a0e1d |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 291 ms: 1.20x faster                                                          |
| docutils       | 3.30 sec                                               | 2.80 sec: 1.18x faster                                                        |
| html5lib       | 88.9 ms                                                | 66.4 ms: 1.34x faster                                                         |
| Geometric mean | (ref)                                                  | 1.24x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250503-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-a8a0e1d |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 552 ms: 3.20x faster                                                          |
| async_tree_none         | 728 ms                                                 | 265 ms: 2.75x faster                                                          |
| async_tree_memoization  | 870 ms                                                 | 333 ms: 2.62x faster                                                          |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 503 ms: 2.02x faster                                                          |
| Geometric mean          | (ref)                                                  | 2.61x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250503-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-a8a0e1d |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 71.2 ms: 1.64x faster                                                         |
| nbody          | 154 ms                                                 | 128 ms: 1.20x faster                                                          |
| pidigits       | 191 ms                                                 | 182 ms: 1.05x faster                                                          |
| Geometric mean | (ref)                                                  | 1.28x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250503-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-a8a0e1d |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 144 ms: 1.31x faster                                                          |
| regex_v8       | 27.8 ms                                                | 22.9 ms: 1.21x faster                                                         |
| regex_dna      | 227 ms                                                 | 204 ms: 1.11x faster                                                          |
| regex_effbot   | 3.63 ms                                                | 3.32 ms: 1.09x faster                                                         |
| Geometric mean | (ref)                                                  | 1.18x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250503-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-a8a0e1d |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 343 us: 1.41x faster                                                          |
| tomli_loads          | 3.14 sec                                               | 2.23 sec: 1.41x faster                                                        |
| unpickle_pure_python | 331 us                                                 | 241 us: 1.37x faster                                                          |
| xml_etree_iterparse  | 115 ms                                                 | 95.8 ms: 1.20x faster                                                         |
| xml_etree_process    | 79.1 ms                                                | 68.0 ms: 1.16x faster                                                         |
| xml_etree_parse      | 168 ms                                                 | 151 ms: 1.11x faster                                                          |
| json_dumps           | 14.2 ms                                                | 13.1 ms: 1.08x faster                                                         |
| xml_etree_generate   | 99.4 ms                                                | 96.6 ms: 1.03x faster                                                         |
| json_loads           | 31.2 us                                                | 32.9 us: 1.06x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250503-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-a8a0e1d |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 15.5 ms: 1.06x slower                                                         |
| python_startup_no_site | 5.93 ms                                                | 9.11 ms: 1.54x slower                                                         |
| Geometric mean         | (ref)                                                  | 1.28x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250503-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-a8a0e1d |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 39.7 ms: 1.21x faster                                                         |
| genshi_text     | 31.8 ms                                                | 27.1 ms: 1.17x faster                                                         |
| genshi_xml      | 66.0 ms                                                | 58.1 ms: 1.14x faster                                                         |
| Geometric mean  | (ref)                                                  | 1.13x faster                                                                  |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250503-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-a8a0e1d |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_io            | 1.77 sec                                               | 552 ms: 3.20x faster                                                          |
| async_tree_none          | 728 ms                                                 | 265 ms: 2.75x faster                                                          |
| typing_runtime_protocols | 544 us                                                 | 201 us: 2.71x faster                                                          |
| async_tree_memoization   | 870 ms                                                 | 333 ms: 2.62x faster                                                          |
| generators               | 80.1 ms                                                | 31.7 ms: 2.53x faster                                                         |
| deltablue                | 7.91 ms                                                | 3.76 ms: 2.10x faster                                                         |
| mdp                      | 2.85 sec                                               | 1.40 sec: 2.03x faster                                                        |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 503 ms: 2.02x faster                                                          |
| go                       | 240 ms                                                 | 132 ms: 1.81x faster                                                          |
| pylint                   | 551 ms                                                 | 308 ms: 1.79x faster                                                          |
| logging_silent           | 190 ns                                                 | 108 ns: 1.76x faster                                                          |
| chaos                    | 115 ms                                                 | 67.7 ms: 1.70x faster                                                         |
| scimark_sor              | 220 ms                                                 | 133 ms: 1.65x faster                                                          |
| float                    | 117 ms                                                 | 71.2 ms: 1.64x faster                                                         |
| deepcopy                 | 479 us                                                 | 297 us: 1.61x faster                                                          |
| deepcopy_memo            | 58.5 us                                                | 36.4 us: 1.61x faster                                                         |
| gc_traversal             | 3.62 ms                                                | 2.28 ms: 1.59x faster                                                         |
| richards_super           | 94.7 ms                                                | 60.1 ms: 1.58x faster                                                         |
| raytrace                 | 507 ms                                                 | 323 ms: 1.57x faster                                                          |
| richards                 | 79.3 ms                                                | 51.6 ms: 1.54x faster                                                         |
| pyflate                  | 716 ms                                                 | 480 ms: 1.49x faster                                                          |
| comprehensions           | 28.8 us                                                | 19.7 us: 1.46x faster                                                         |
| scimark_monte_carlo      | 118 ms                                                 | 82.6 ms: 1.43x faster                                                         |
| spectral_norm            | 170 ms                                                 | 119 ms: 1.43x faster                                                          |
| hexiom                   | 10.4 ms                                                | 7.31 ms: 1.42x faster                                                         |
| crypto_pyaes             | 128 ms                                                 | 90.1 ms: 1.42x faster                                                         |
| pickle_pure_python       | 484 us                                                 | 343 us: 1.41x faster                                                          |
| tomli_loads              | 3.14 sec                                               | 2.23 sec: 1.41x faster                                                        |
| unpickle_pure_python     | 331 us                                                 | 241 us: 1.37x faster                                                          |
| coroutines               | 35.1 ms                                                | 25.8 ms: 1.36x faster                                                         |
| deepcopy_reduce          | 4.17 us                                                | 3.08 us: 1.35x faster                                                         |
| pycparser                | 1.58 sec                                               | 1.17 sec: 1.35x faster                                                        |
| dulwich_log              | 84.3 ms                                                | 62.7 ms: 1.35x faster                                                         |
| html5lib                 | 88.9 ms                                                | 66.4 ms: 1.34x faster                                                         |
| regex_compile            | 188 ms                                                 | 144 ms: 1.31x faster                                                          |
| scimark_lu               | 176 ms                                                 | 137 ms: 1.29x faster                                                          |
| logging_simple           | 8.30 us                                                | 6.64 us: 1.25x faster                                                         |
| pprint_safe_repr         | 1.02 sec                                               | 822 ms: 1.24x faster                                                          |
| pprint_pformat           | 2.10 sec                                               | 1.70 sec: 1.24x faster                                                        |
| regex_v8                 | 27.8 ms                                                | 22.9 ms: 1.21x faster                                                         |
| django_template          | 48.2 ms                                                | 39.7 ms: 1.21x faster                                                         |
| logging_format           | 9.09 us                                                | 7.51 us: 1.21x faster                                                         |
| xml_etree_iterparse      | 115 ms                                                 | 95.8 ms: 1.20x faster                                                         |
| nbody                    | 154 ms                                                 | 128 ms: 1.20x faster                                                          |
| 2to3                     | 348 ms                                                 | 291 ms: 1.20x faster                                                          |
| docutils                 | 3.30 sec                                               | 2.80 sec: 1.18x faster                                                        |
| genshi_text              | 31.8 ms                                                | 27.1 ms: 1.17x faster                                                         |
| sympy_integrate          | 25.8 ms                                                | 22.2 ms: 1.16x faster                                                         |
| xml_etree_process        | 79.1 ms                                                | 68.0 ms: 1.16x faster                                                         |
| nqueens                  | 106 ms                                                 | 91.7 ms: 1.15x faster                                                         |
| pathlib                  | 20.5 ms                                                | 17.8 ms: 1.15x faster                                                         |
| scimark_fft              | 466 ms                                                 | 406 ms: 1.15x faster                                                          |
| sympy_sum                | 196 ms                                                 | 172 ms: 1.14x faster                                                          |
| genshi_xml               | 66.0 ms                                                | 58.1 ms: 1.14x faster                                                         |
| sqlalchemy_imperative    | 23.3 ms                                                | 20.8 ms: 1.12x faster                                                         |
| sympy_str                | 346 ms                                                 | 308 ms: 1.12x faster                                                          |
| xml_etree_parse          | 168 ms                                                 | 151 ms: 1.11x faster                                                          |
| regex_dna                | 227 ms                                                 | 204 ms: 1.11x faster                                                          |
| regex_effbot             | 3.63 ms                                                | 3.32 ms: 1.09x faster                                                         |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.94 ms: 1.09x faster                                                         |
| sqlalchemy_declarative   | 172 ms                                                 | 158 ms: 1.09x faster                                                          |
| sympy_expand             | 566 ms                                                 | 525 ms: 1.08x faster                                                          |
| json_dumps               | 14.2 ms                                                | 13.1 ms: 1.08x faster                                                         |
| sqlite_synth             | 3.02 us                                                | 2.82 us: 1.07x faster                                                         |
| fannkuch                 | 532 ms                                                 | 498 ms: 1.07x faster                                                          |
| pidigits                 | 191 ms                                                 | 182 ms: 1.05x faster                                                          |
| xml_etree_generate       | 99.4 ms                                                | 96.6 ms: 1.03x faster                                                         |
| async_generators         | 444 ms                                                 | 434 ms: 1.02x faster                                                          |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                          |
| json                     | 5.69 ms                                                | 5.64 ms: 1.01x faster                                                         |
| create_gc_cycles         | 1.62 ms                                                | 1.67 ms: 1.03x slower                                                         |
| json_loads               | 31.2 us                                                | 32.9 us: 1.06x slower                                                         |
| python_startup           | 14.6 ms                                                | 15.5 ms: 1.06x slower                                                         |
| meteor_contest           | 120 ms                                                 | 130 ms: 1.09x slower                                                          |
| telco                    | 7.27 ms                                                | 9.35 ms: 1.29x slower                                                         |
| python_startup_no_site   | 5.93 ms                                                | 9.11 ms: 1.54x slower                                                         |
| coverage                 | 79.4 ms                                                | 125 ms: 1.57x slower                                                          |
| bench_thread_pool        | 986 us                                                 | 3.26 ms: 3.31x slower                                                         |
| bench_mp_pool            | 24.0 ms                                                | 90.7 ms: 3.78x slower                                                         |
| Geometric mean           | (ref)                                                  | 1.26x faster                                                                  |

Benchmark hidden because not significant (1): mako
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (23) of results/bm-20250503-3.14.0a7+-a8a0e1d-NOGIL/bm-20250503-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-a8a0e1d.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.309x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.17x

# Memory
- memory change: 1.53x