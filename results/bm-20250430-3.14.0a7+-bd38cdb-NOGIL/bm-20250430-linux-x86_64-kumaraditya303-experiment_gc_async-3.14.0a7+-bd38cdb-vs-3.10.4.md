# Results vs. 3.10.4

- fork: kumaraditya303
- ref: experiment_gc_async
- machine: linux-x86_64
- commit hash: bd38cdb
- commit date: 2025-04-30
- overall geometric mean: 1.323x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: 1.53x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-bd38cdb |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 291 ms: 1.20x faster                                                          |
| docutils       | 3.30 sec                                               | 2.78 sec: 1.19x faster                                                        |
| html5lib       | 88.9 ms                                                | 67.2 ms: 1.32x faster                                                         |
| Geometric mean | (ref)                                                  | 1.23x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-bd38cdb |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 548 ms: 3.23x faster                                                          |
| async_tree_none         | 728 ms                                                 | 262 ms: 2.78x faster                                                          |
| async_tree_memoization  | 870 ms                                                 | 330 ms: 2.63x faster                                                          |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 498 ms: 2.04x faster                                                          |
| Geometric mean          | (ref)                                                  | 2.63x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-bd38cdb |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 70.3 ms: 1.67x faster                                                         |
| nbody          | 154 ms                                                 | 129 ms: 1.19x faster                                                          |
| pidigits       | 191 ms                                                 | 181 ms: 1.06x faster                                                          |
| Geometric mean | (ref)                                                  | 1.28x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-bd38cdb |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 144 ms: 1.31x faster                                                          |
| regex_v8       | 27.8 ms                                                | 22.0 ms: 1.26x faster                                                         |
| regex_effbot   | 3.63 ms                                                | 3.15 ms: 1.15x faster                                                         |
| regex_dna      | 227 ms                                                 | 206 ms: 1.10x faster                                                          |
| Geometric mean | (ref)                                                  | 1.20x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-bd38cdb |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 345 us: 1.40x faster                                                          |
| tomli_loads          | 3.14 sec                                               | 2.24 sec: 1.40x faster                                                        |
| unpickle_pure_python | 331 us                                                 | 238 us: 1.39x faster                                                          |
| xml_etree_iterparse  | 115 ms                                                 | 96.4 ms: 1.20x faster                                                         |
| xml_etree_process    | 79.1 ms                                                | 68.1 ms: 1.16x faster                                                         |
| xml_etree_parse      | 168 ms                                                 | 148 ms: 1.13x faster                                                          |
| json_dumps           | 14.2 ms                                                | 12.9 ms: 1.10x faster                                                         |
| xml_etree_generate   | 99.4 ms                                                | 96.1 ms: 1.03x faster                                                         |
| json_loads           | 31.2 us                                                | 32.7 us: 1.05x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.19x faster                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-bd38cdb |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 15.4 ms: 1.06x slower                                                         |
| python_startup_no_site | 5.93 ms                                                | 9.06 ms: 1.53x slower                                                         |
| Geometric mean         | (ref)                                                  | 1.27x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-bd38cdb |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 38.9 ms: 1.24x faster                                                         |
| genshi_text     | 31.8 ms                                                | 26.7 ms: 1.19x faster                                                         |
| genshi_xml      | 66.0 ms                                                | 57.8 ms: 1.14x faster                                                         |
| mako            | 16.3 ms                                                | 16.2 ms: 1.01x faster                                                         |
| Geometric mean  | (ref)                                                  | 1.14x faster                                                                  |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-bd38cdb |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_io            | 1.77 sec                                               | 548 ms: 3.23x faster                                                          |
| async_tree_none          | 728 ms                                                 | 262 ms: 2.78x faster                                                          |
| typing_runtime_protocols | 544 us                                                 | 202 us: 2.69x faster                                                          |
| async_tree_memoization   | 870 ms                                                 | 330 ms: 2.63x faster                                                          |
| generators               | 80.1 ms                                                | 30.6 ms: 2.62x faster                                                         |
| deltablue                | 7.91 ms                                                | 3.65 ms: 2.17x faster                                                         |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 498 ms: 2.04x faster                                                          |
| mdp                      | 2.85 sec                                               | 1.40 sec: 2.04x faster                                                        |
| pylint                   | 551 ms                                                 | 293 ms: 1.88x faster                                                          |
| go                       | 240 ms                                                 | 129 ms: 1.86x faster                                                          |
| logging_silent           | 190 ns                                                 | 103 ns: 1.85x faster                                                          |
| chaos                    | 115 ms                                                 | 67.3 ms: 1.72x faster                                                         |
| gc_traversal             | 3.62 ms                                                | 2.14 ms: 1.70x faster                                                         |
| scimark_sor              | 220 ms                                                 | 131 ms: 1.67x faster                                                          |
| float                    | 117 ms                                                 | 70.3 ms: 1.67x faster                                                         |
| deepcopy                 | 479 us                                                 | 294 us: 1.63x faster                                                          |
| deepcopy_memo            | 58.5 us                                                | 36.0 us: 1.62x faster                                                         |
| raytrace                 | 507 ms                                                 | 316 ms: 1.60x faster                                                          |
| richards_super           | 94.7 ms                                                | 59.3 ms: 1.60x faster                                                         |
| richards                 | 79.3 ms                                                | 50.2 ms: 1.58x faster                                                         |
| pyflate                  | 716 ms                                                 | 489 ms: 1.47x faster                                                          |
| hexiom                   | 10.4 ms                                                | 7.21 ms: 1.44x faster                                                         |
| scimark_monte_carlo      | 118 ms                                                 | 82.0 ms: 1.44x faster                                                         |
| spectral_norm            | 170 ms                                                 | 118 ms: 1.44x faster                                                          |
| comprehensions           | 28.8 us                                                | 20.0 us: 1.44x faster                                                         |
| crypto_pyaes             | 128 ms                                                 | 89.3 ms: 1.43x faster                                                         |
| pycparser                | 1.58 sec                                               | 1.10 sec: 1.43x faster                                                        |
| coroutines               | 35.1 ms                                                | 25.0 ms: 1.40x faster                                                         |
| pickle_pure_python       | 484 us                                                 | 345 us: 1.40x faster                                                          |
| tomli_loads              | 3.14 sec                                               | 2.24 sec: 1.40x faster                                                        |
| unpickle_pure_python     | 331 us                                                 | 238 us: 1.39x faster                                                          |
| deepcopy_reduce          | 4.17 us                                                | 3.09 us: 1.35x faster                                                         |
| dulwich_log              | 84.3 ms                                                | 62.8 ms: 1.34x faster                                                         |
| html5lib                 | 88.9 ms                                                | 67.2 ms: 1.32x faster                                                         |
| scimark_lu               | 176 ms                                                 | 134 ms: 1.31x faster                                                          |
| regex_compile            | 188 ms                                                 | 144 ms: 1.31x faster                                                          |
| pprint_pformat           | 2.10 sec                                               | 1.66 sec: 1.27x faster                                                        |
| pprint_safe_repr         | 1.02 sec                                               | 803 ms: 1.27x faster                                                          |
| regex_v8                 | 27.8 ms                                                | 22.0 ms: 1.26x faster                                                         |
| logging_simple           | 8.30 us                                                | 6.66 us: 1.25x faster                                                         |
| django_template          | 48.2 ms                                                | 38.9 ms: 1.24x faster                                                         |
| logging_format           | 9.09 us                                                | 7.51 us: 1.21x faster                                                         |
| 2to3                     | 348 ms                                                 | 291 ms: 1.20x faster                                                          |
| xml_etree_iterparse      | 115 ms                                                 | 96.4 ms: 1.20x faster                                                         |
| genshi_text              | 31.8 ms                                                | 26.7 ms: 1.19x faster                                                         |
| nbody                    | 154 ms                                                 | 129 ms: 1.19x faster                                                          |
| docutils                 | 3.30 sec                                               | 2.78 sec: 1.19x faster                                                        |
| scimark_fft              | 466 ms                                                 | 395 ms: 1.18x faster                                                          |
| sympy_integrate          | 25.8 ms                                                | 22.1 ms: 1.17x faster                                                         |
| xml_etree_process        | 79.1 ms                                                | 68.1 ms: 1.16x faster                                                         |
| regex_effbot             | 3.63 ms                                                | 3.15 ms: 1.15x faster                                                         |
| nqueens                  | 106 ms                                                 | 91.9 ms: 1.15x faster                                                         |
| pathlib                  | 20.5 ms                                                | 17.8 ms: 1.15x faster                                                         |
| sympy_sum                | 196 ms                                                 | 171 ms: 1.15x faster                                                          |
| genshi_xml               | 66.0 ms                                                | 57.8 ms: 1.14x faster                                                         |
| sympy_str                | 346 ms                                                 | 304 ms: 1.14x faster                                                          |
| sqlalchemy_imperative    | 23.3 ms                                                | 20.5 ms: 1.14x faster                                                         |
| xml_etree_parse          | 168 ms                                                 | 148 ms: 1.13x faster                                                          |
| regex_dna                | 227 ms                                                 | 206 ms: 1.10x faster                                                          |
| sympy_expand             | 566 ms                                                 | 515 ms: 1.10x faster                                                          |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.89 ms: 1.10x faster                                                         |
| json_dumps               | 14.2 ms                                                | 12.9 ms: 1.10x faster                                                         |
| sqlalchemy_declarative   | 172 ms                                                 | 158 ms: 1.09x faster                                                          |
| sqlite_synth             | 3.02 us                                                | 2.79 us: 1.08x faster                                                         |
| fannkuch                 | 532 ms                                                 | 502 ms: 1.06x faster                                                          |
| pidigits                 | 191 ms                                                 | 181 ms: 1.06x faster                                                          |
| xml_etree_generate       | 99.4 ms                                                | 96.1 ms: 1.03x faster                                                         |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                                          |
| json                     | 5.69 ms                                                | 5.64 ms: 1.01x faster                                                         |
| mako                     | 16.3 ms                                                | 16.2 ms: 1.01x faster                                                         |
| async_generators         | 444 ms                                                 | 442 ms: 1.00x faster                                                          |
| create_gc_cycles         | 1.62 ms                                                | 1.65 ms: 1.02x slower                                                         |
| json_loads               | 31.2 us                                                | 32.7 us: 1.05x slower                                                         |
| python_startup           | 14.6 ms                                                | 15.4 ms: 1.06x slower                                                         |
| meteor_contest           | 120 ms                                                 | 129 ms: 1.08x slower                                                          |
| telco                    | 7.27 ms                                                | 9.00 ms: 1.24x slower                                                         |
| python_startup_no_site   | 5.93 ms                                                | 9.06 ms: 1.53x slower                                                         |
| coverage                 | 79.4 ms                                                | 124 ms: 1.56x slower                                                          |
| bench_thread_pool        | 986 us                                                 | 3.24 ms: 3.29x slower                                                         |
| bench_mp_pool            | 24.0 ms                                                | 90.6 ms: 3.77x slower                                                         |
| Geometric mean           | (ref)                                                  | 1.28x faster                                                                  |
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (23) of results/bm-20250430-3.14.0a7+-bd38cdb-NOGIL/bm-20250430-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-bd38cdb.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.323x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: 1.53x