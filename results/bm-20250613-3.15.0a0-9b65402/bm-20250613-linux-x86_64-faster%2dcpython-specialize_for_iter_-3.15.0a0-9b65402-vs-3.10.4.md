# Results vs. 3.10.4

- fork: faster-cpython
- ref: specialize_for_iter_
- machine: linux-x86_64
- commit hash: 9b65402
- commit date: 2025-06-13
- overall geometric mean: 1.322x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x faster
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250613-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 254 ms: 1.37x faster                                                            |
| docutils       | 3.30 sec                                               | 2.56 sec: 1.29x faster                                                          |
| html5lib       | 88.9 ms                                                | 62.3 ms: 1.43x faster                                                           |
| Geometric mean | (ref)                                                  | 1.36x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250613-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 598 ms: 2.96x faster                                                            |
| async_tree_none         | 728 ms                                                 | 259 ms: 2.81x faster                                                            |
| async_tree_memoization  | 870 ms                                                 | 313 ms: 2.78x faster                                                            |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 496 ms: 2.05x faster                                                            |
| Geometric mean          | (ref)                                                  | 2.62x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250613-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 73.9 ms: 1.58x faster                                                           |
| nbody          | 154 ms                                                 | 100 ms: 1.53x faster                                                            |
| pidigits       | 191 ms                                                 | 188 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                  | 1.35x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250613-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 127 ms: 1.48x faster                                                            |
| regex_v8       | 27.8 ms                                                | 22.1 ms: 1.26x faster                                                           |
| regex_dna      | 227 ms                                                 | 184 ms: 1.23x faster                                                            |
| regex_effbot   | 3.63 ms                                                | 3.11 ms: 1.17x faster                                                           |
| Geometric mean | (ref)                                                  | 1.28x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250613-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.99 sec: 1.58x faster                                                          |
| pickle_pure_python   | 484 us                                                 | 317 us: 1.53x faster                                                            |
| unpickle_pure_python | 331 us                                                 | 220 us: 1.50x faster                                                            |
| xml_etree_process    | 79.1 ms                                                | 60.2 ms: 1.32x faster                                                           |
| json_dumps           | 14.2 ms                                                | 10.9 ms: 1.29x faster                                                           |
| xml_etree_parse      | 168 ms                                                 | 141 ms: 1.19x faster                                                            |
| xml_etree_generate   | 99.4 ms                                                | 85.4 ms: 1.16x faster                                                           |
| xml_etree_iterparse  | 115 ms                                                 | 99.3 ms: 1.16x faster                                                           |
| json_loads           | 31.2 us                                                | 27.7 us: 1.13x faster                                                           |
| Geometric mean       | (ref)                                                  | 1.31x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250613-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.2 ms: 1.20x faster                                                           |
| python_startup_no_site | 5.93 ms                                                | 6.91 ms: 1.17x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250613-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 32.2 ms: 1.50x faster                                                           |
| genshi_text     | 31.8 ms                                                | 21.5 ms: 1.48x faster                                                           |
| mako            | 16.3 ms                                                | 11.3 ms: 1.44x faster                                                           |
| genshi_xml      | 66.0 ms                                                | 50.2 ms: 1.31x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250613-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 170 us: 3.20x faster                                                            |
| async_tree_io            | 1.77 sec                                               | 598 ms: 2.96x faster                                                            |
| async_tree_none          | 728 ms                                                 | 259 ms: 2.81x faster                                                            |
| async_tree_memoization   | 870 ms                                                 | 313 ms: 2.78x faster                                                            |
| generators               | 80.1 ms                                                | 30.0 ms: 2.67x faster                                                           |
| mdp                      | 2.85 sec                                               | 1.23 sec: 2.31x faster                                                          |
| deltablue                | 7.91 ms                                                | 3.54 ms: 2.23x faster                                                           |
| go                       | 240 ms                                                 | 112 ms: 2.14x faster                                                            |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 496 ms: 2.05x faster                                                            |
| deepcopy_memo            | 58.5 us                                                | 29.2 us: 2.00x faster                                                           |
| pylint                   | 551 ms                                                 | 278 ms: 1.98x faster                                                            |
| chaos                    | 115 ms                                                 | 59.5 ms: 1.94x faster                                                           |
| richards_super           | 94.7 ms                                                | 49.5 ms: 1.91x faster                                                           |
| raytrace                 | 507 ms                                                 | 270 ms: 1.87x faster                                                            |
| deepcopy                 | 479 us                                                 | 261 us: 1.84x faster                                                            |
| scimark_sor              | 220 ms                                                 | 120 ms: 1.83x faster                                                            |
| richards                 | 79.3 ms                                                | 43.4 ms: 1.83x faster                                                           |
| comprehensions           | 28.8 us                                                | 16.0 us: 1.79x faster                                                           |
| scimark_monte_carlo      | 118 ms                                                 | 68.4 ms: 1.73x faster                                                           |
| hexiom                   | 10.4 ms                                                | 6.03 ms: 1.72x faster                                                           |
| crypto_pyaes             | 128 ms                                                 | 75.1 ms: 1.70x faster                                                           |
| pyflate                  | 716 ms                                                 | 430 ms: 1.67x faster                                                            |
| float                    | 117 ms                                                 | 73.9 ms: 1.58x faster                                                           |
| tomli_loads              | 3.14 sec                                               | 1.99 sec: 1.58x faster                                                          |
| spectral_norm            | 170 ms                                                 | 109 ms: 1.56x faster                                                            |
| nbody                    | 154 ms                                                 | 100 ms: 1.53x faster                                                            |
| deepcopy_reduce          | 4.17 us                                                | 2.72 us: 1.53x faster                                                           |
| pickle_pure_python       | 484 us                                                 | 317 us: 1.53x faster                                                            |
| unpickle_pure_python     | 331 us                                                 | 220 us: 1.50x faster                                                            |
| django_template          | 48.2 ms                                                | 32.2 ms: 1.50x faster                                                           |
| scimark_lu               | 176 ms                                                 | 118 ms: 1.49x faster                                                            |
| regex_compile            | 188 ms                                                 | 127 ms: 1.48x faster                                                            |
| genshi_text              | 31.8 ms                                                | 21.5 ms: 1.48x faster                                                           |
| mako                     | 16.3 ms                                                | 11.3 ms: 1.44x faster                                                           |
| html5lib                 | 88.9 ms                                                | 62.3 ms: 1.43x faster                                                           |
| dulwich_log              | 84.3 ms                                                | 59.5 ms: 1.42x faster                                                           |
| pycparser                | 1.58 sec                                               | 1.11 sec: 1.42x faster                                                          |
| coroutines               | 35.1 ms                                                | 25.0 ms: 1.40x faster                                                           |
| 2to3                     | 348 ms                                                 | 254 ms: 1.37x faster                                                            |
| sympy_integrate          | 25.8 ms                                                | 19.0 ms: 1.36x faster                                                           |
| logging_simple           | 8.30 us                                                | 6.17 us: 1.35x faster                                                           |
| sympy_sum                | 196 ms                                                 | 149 ms: 1.32x faster                                                            |
| logging_format           | 9.09 us                                                | 6.89 us: 1.32x faster                                                           |
| xml_etree_process        | 79.1 ms                                                | 60.2 ms: 1.32x faster                                                           |
| genshi_xml               | 66.0 ms                                                | 50.2 ms: 1.31x faster                                                           |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.97 ms: 1.30x faster                                                           |
| nqueens                  | 106 ms                                                 | 81.3 ms: 1.30x faster                                                           |
| json_dumps               | 14.2 ms                                                | 10.9 ms: 1.29x faster                                                           |
| sympy_str                | 346 ms                                                 | 268 ms: 1.29x faster                                                            |
| docutils                 | 3.30 sec                                               | 2.56 sec: 1.29x faster                                                          |
| fannkuch                 | 532 ms                                                 | 414 ms: 1.28x faster                                                            |
| pprint_pformat           | 2.10 sec                                               | 1.67 sec: 1.26x faster                                                          |
| regex_v8                 | 27.8 ms                                                | 22.1 ms: 1.26x faster                                                           |
| pprint_safe_repr         | 1.02 sec                                               | 818 ms: 1.24x faster                                                            |
| sympy_expand             | 566 ms                                                 | 455 ms: 1.24x faster                                                            |
| regex_dna                | 227 ms                                                 | 184 ms: 1.23x faster                                                            |
| scimark_fft              | 466 ms                                                 | 384 ms: 1.21x faster                                                            |
| pathlib                  | 20.5 ms                                                | 17.0 ms: 1.20x faster                                                           |
| python_startup           | 14.6 ms                                                | 12.2 ms: 1.20x faster                                                           |
| xml_etree_parse          | 168 ms                                                 | 141 ms: 1.19x faster                                                            |
| regex_effbot             | 3.63 ms                                                | 3.11 ms: 1.17x faster                                                           |
| xml_etree_generate       | 99.4 ms                                                | 85.4 ms: 1.16x faster                                                           |
| xml_etree_iterparse      | 115 ms                                                 | 99.3 ms: 1.16x faster                                                           |
| meteor_contest           | 120 ms                                                 | 105 ms: 1.14x faster                                                            |
| json_loads               | 31.2 us                                                | 27.7 us: 1.13x faster                                                           |
| json                     | 5.69 ms                                                | 5.22 ms: 1.09x faster                                                           |
| async_generators         | 444 ms                                                 | 407 ms: 1.09x faster                                                            |
| sqlite_synth             | 3.02 us                                                | 2.86 us: 1.06x faster                                                           |
| pidigits                 | 191 ms                                                 | 188 ms: 1.01x faster                                                            |
| asyncio_websockets       | 559 ms                                                 | 553 ms: 1.01x faster                                                            |
| telco                    | 7.27 ms                                                | 8.02 ms: 1.10x slower                                                           |
| python_startup_no_site   | 5.93 ms                                                | 6.91 ms: 1.17x slower                                                           |
| gc_traversal             | 3.62 ms                                                | 5.17 ms: 1.43x slower                                                           |
| create_gc_cycles         | 1.62 ms                                                | 2.58 ms: 1.60x slower                                                           |
| logging_silent           | 190 ns                                                 | 473 ns: 2.49x slower                                                            |
| coverage                 | 79.4 ms                                                | 419 ms: 5.27x slower                                                            |
| thrift                   | 1.07 ms                                                | 147 ms: 137.51x slower                                                          |
| Geometric mean           | (ref)                                                  | 1.30x faster                                                                    |
Ignored benchmarks (24) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250613-3.15.0a0-9b65402/bm-20250613-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.322x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.28x

# Memory
- memory change: 1.31x