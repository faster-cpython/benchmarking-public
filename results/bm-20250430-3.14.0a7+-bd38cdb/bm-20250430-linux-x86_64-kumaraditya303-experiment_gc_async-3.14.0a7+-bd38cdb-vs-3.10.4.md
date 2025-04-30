# Results vs. 3.10.4

- fork: kumaraditya303
- ref: experiment_gc_async
- machine: linux-x86_64
- commit hash: bd38cdb
- commit date: 2025-04-30
- overall geometric mean: 1.423x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-bd38cdb |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 254 ms: 1.37x faster                                                          |
| docutils       | 3.30 sec                                               | 2.63 sec: 1.25x faster                                                        |
| html5lib       | 88.9 ms                                                | 60.2 ms: 1.48x faster                                                         |
| Geometric mean | (ref)                                                  | 1.36x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-bd38cdb |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 320 ms: 2.27x faster                                                          |
| async_tree_memoization  | 870 ms                                                 | 384 ms: 2.26x faster                                                          |
| async_tree_io           | 1.77 sec                                               | 804 ms: 2.20x faster                                                          |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 574 ms: 1.77x faster                                                          |
| Geometric mean          | (ref)                                                  | 2.12x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-bd38cdb |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 71.2 ms: 1.64x faster                                                         |
| nbody          | 154 ms                                                 | 99.2 ms: 1.55x faster                                                         |
| pidigits       | 191 ms                                                 | 191 ms: 1.00x slower                                                          |
| Geometric mean | (ref)                                                  | 1.36x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-bd38cdb |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 127 ms: 1.48x faster                                                          |
| regex_v8       | 27.8 ms                                                | 22.5 ms: 1.23x faster                                                         |
| regex_effbot   | 3.63 ms                                                | 3.11 ms: 1.17x faster                                                         |
| regex_dna      | 227 ms                                                 | 207 ms: 1.10x faster                                                          |
| Geometric mean | (ref)                                                  | 1.24x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-bd38cdb |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 2.05 sec: 1.53x faster                                                        |
| pickle_pure_python   | 484 us                                                 | 318 us: 1.52x faster                                                          |
| unpickle_pure_python | 331 us                                                 | 219 us: 1.51x faster                                                          |
| xml_etree_process    | 79.1 ms                                                | 59.2 ms: 1.34x faster                                                         |
| xml_etree_parse      | 168 ms                                                 | 142 ms: 1.19x faster                                                          |
| xml_etree_generate   | 99.4 ms                                                | 84.9 ms: 1.17x faster                                                         |
| xml_etree_iterparse  | 115 ms                                                 | 99.2 ms: 1.16x faster                                                         |
| json_dumps           | 14.2 ms                                                | 12.2 ms: 1.16x faster                                                         |
| json_loads           | 31.2 us                                                | 30.5 us: 1.02x faster                                                         |
| Geometric mean       | (ref)                                                  | 1.28x faster                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-bd38cdb |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.1 ms: 1.11x faster                                                         |
| python_startup_no_site | 5.93 ms                                                | 6.93 ms: 1.17x slower                                                         |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-bd38cdb |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 21.1 ms: 1.50x faster                                                         |
| django_template | 48.2 ms                                                | 33.1 ms: 1.45x faster                                                         |
| mako            | 16.3 ms                                                | 11.6 ms: 1.40x faster                                                         |
| genshi_xml      | 66.0 ms                                                | 50.4 ms: 1.31x faster                                                         |
| Geometric mean  | (ref)                                                  | 1.42x faster                                                                  |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-bd38cdb |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 169 us: 3.22x faster                                                          |
| generators               | 80.1 ms                                                | 29.4 ms: 2.73x faster                                                         |
| deltablue                | 7.91 ms                                                | 3.33 ms: 2.38x faster                                                         |
| mdp                      | 2.85 sec                                               | 1.22 sec: 2.33x faster                                                        |
| async_tree_none          | 728 ms                                                 | 320 ms: 2.27x faster                                                          |
| async_tree_memoization   | 870 ms                                                 | 384 ms: 2.26x faster                                                          |
| async_tree_io            | 1.77 sec                                               | 804 ms: 2.20x faster                                                          |
| go                       | 240 ms                                                 | 113 ms: 2.13x faster                                                          |
| deepcopy_memo            | 58.5 us                                                | 29.0 us: 2.01x faster                                                         |
| pylint                   | 551 ms                                                 | 281 ms: 1.96x faster                                                          |
| chaos                    | 115 ms                                                 | 59.6 ms: 1.94x faster                                                         |
| richards_super           | 94.7 ms                                                | 49.9 ms: 1.90x faster                                                         |
| logging_silent           | 190 ns                                                 | 100 ns: 1.90x faster                                                          |
| raytrace                 | 507 ms                                                 | 269 ms: 1.88x faster                                                          |
| deepcopy                 | 479 us                                                 | 260 us: 1.84x faster                                                          |
| richards                 | 79.3 ms                                                | 43.4 ms: 1.83x faster                                                         |
| scimark_sor              | 220 ms                                                 | 121 ms: 1.81x faster                                                          |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 574 ms: 1.77x faster                                                          |
| scimark_monte_carlo      | 118 ms                                                 | 68.1 ms: 1.73x faster                                                         |
| comprehensions           | 28.8 us                                                | 17.0 us: 1.69x faster                                                         |
| crypto_pyaes             | 128 ms                                                 | 76.3 ms: 1.67x faster                                                         |
| hexiom                   | 10.4 ms                                                | 6.25 ms: 1.66x faster                                                         |
| float                    | 117 ms                                                 | 71.2 ms: 1.64x faster                                                         |
| spectral_norm            | 170 ms                                                 | 108 ms: 1.58x faster                                                          |
| pyflate                  | 716 ms                                                 | 456 ms: 1.57x faster                                                          |
| nbody                    | 154 ms                                                 | 99.2 ms: 1.55x faster                                                         |
| tomli_loads              | 3.14 sec                                               | 2.05 sec: 1.53x faster                                                        |
| deepcopy_reduce          | 4.17 us                                                | 2.73 us: 1.53x faster                                                         |
| pickle_pure_python       | 484 us                                                 | 318 us: 1.52x faster                                                          |
| scimark_lu               | 176 ms                                                 | 116 ms: 1.52x faster                                                          |
| unpickle_pure_python     | 331 us                                                 | 219 us: 1.51x faster                                                          |
| genshi_text              | 31.8 ms                                                | 21.1 ms: 1.50x faster                                                         |
| regex_compile            | 188 ms                                                 | 127 ms: 1.48x faster                                                          |
| html5lib                 | 88.9 ms                                                | 60.2 ms: 1.48x faster                                                         |
| logging_simple           | 8.30 us                                                | 5.63 us: 1.47x faster                                                         |
| logging_format           | 9.09 us                                                | 6.25 us: 1.45x faster                                                         |
| django_template          | 48.2 ms                                                | 33.1 ms: 1.45x faster                                                         |
| pprint_pformat           | 2.10 sec                                               | 1.50 sec: 1.40x faster                                                        |
| mako                     | 16.3 ms                                                | 11.6 ms: 1.40x faster                                                         |
| dulwich_log              | 84.3 ms                                                | 60.4 ms: 1.40x faster                                                         |
| pprint_safe_repr         | 1.02 sec                                               | 741 ms: 1.37x faster                                                          |
| 2to3                     | 348 ms                                                 | 254 ms: 1.37x faster                                                          |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.3 ms: 1.35x faster                                                         |
| sympy_integrate          | 25.8 ms                                                | 19.2 ms: 1.34x faster                                                         |
| pycparser                | 1.58 sec                                               | 1.18 sec: 1.34x faster                                                        |
| xml_etree_process        | 79.1 ms                                                | 59.2 ms: 1.34x faster                                                         |
| coroutines               | 35.1 ms                                                | 26.3 ms: 1.33x faster                                                         |
| sympy_sum                | 196 ms                                                 | 149 ms: 1.32x faster                                                          |
| genshi_xml               | 66.0 ms                                                | 50.4 ms: 1.31x faster                                                         |
| sqlalchemy_declarative   | 172 ms                                                 | 133 ms: 1.29x faster                                                          |
| sympy_str                | 346 ms                                                 | 270 ms: 1.28x faster                                                          |
| nqueens                  | 106 ms                                                 | 83.1 ms: 1.27x faster                                                         |
| fannkuch                 | 532 ms                                                 | 421 ms: 1.26x faster                                                          |
| scimark_fft              | 466 ms                                                 | 369 ms: 1.26x faster                                                          |
| docutils                 | 3.30 sec                                               | 2.63 sec: 1.25x faster                                                        |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.19 ms: 1.25x faster                                                         |
| regex_v8                 | 27.8 ms                                                | 22.5 ms: 1.23x faster                                                         |
| sympy_expand             | 566 ms                                                 | 463 ms: 1.22x faster                                                          |
| xml_etree_parse          | 168 ms                                                 | 142 ms: 1.19x faster                                                          |
| pathlib                  | 20.5 ms                                                | 17.4 ms: 1.18x faster                                                         |
| xml_etree_generate       | 99.4 ms                                                | 84.9 ms: 1.17x faster                                                         |
| regex_effbot             | 3.63 ms                                                | 3.11 ms: 1.17x faster                                                         |
| xml_etree_iterparse      | 115 ms                                                 | 99.2 ms: 1.16x faster                                                         |
| json_dumps               | 14.2 ms                                                | 12.2 ms: 1.16x faster                                                         |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                          |
| python_startup           | 14.6 ms                                                | 13.1 ms: 1.11x faster                                                         |
| bench_thread_pool        | 986 us                                                 | 893 us: 1.10x faster                                                          |
| regex_dna                | 227 ms                                                 | 207 ms: 1.10x faster                                                          |
| async_generators         | 444 ms                                                 | 411 ms: 1.08x faster                                                          |
| sqlite_synth             | 3.02 us                                                | 2.84 us: 1.06x faster                                                         |
| json                     | 5.69 ms                                                | 5.49 ms: 1.04x faster                                                         |
| json_loads               | 31.2 us                                                | 30.5 us: 1.02x faster                                                         |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                          |
| pidigits                 | 191 ms                                                 | 191 ms: 1.00x slower                                                          |
| telco                    | 7.27 ms                                                | 7.95 ms: 1.09x slower                                                         |
| coverage                 | 79.4 ms                                                | 91.5 ms: 1.15x slower                                                         |
| python_startup_no_site   | 5.93 ms                                                | 6.93 ms: 1.17x slower                                                         |
| gc_traversal             | 3.62 ms                                                | 4.78 ms: 1.32x slower                                                         |
| create_gc_cycles         | 1.62 ms                                                | 2.47 ms: 1.52x slower                                                         |
| bench_mp_pool            | 24.0 ms                                                | 82.9 ms: 3.45x slower                                                         |
| Geometric mean           | (ref)                                                  | 1.40x faster                                                                  |
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (23) of results/bm-20250430-3.14.0a7+-bd38cdb/bm-20250430-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-bd38cdb.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.423x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.28x