# Results vs. 3.10.4

- fork: faster-cpython
- ref: specialize_for_iter_
- machine: linux-x86_64
- commit hash: c41d531
- commit date: 2025-06-16
- overall geometric mean: 1.322x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x faster
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250616-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 254 ms: 1.37x faster                                                            |
| docutils       | 3.30 sec                                               | 2.57 sec: 1.28x faster                                                          |
| html5lib       | 88.9 ms                                                | 61.6 ms: 1.44x faster                                                           |
| Geometric mean | (ref)                                                  | 1.37x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250616-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 600 ms: 2.95x faster                                                            |
| async_tree_none         | 728 ms                                                 | 260 ms: 2.80x faster                                                            |
| async_tree_memoization  | 870 ms                                                 | 312 ms: 2.79x faster                                                            |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 499 ms: 2.04x faster                                                            |
| Geometric mean          | (ref)                                                  | 2.62x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250616-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 72.8 ms: 1.61x faster                                                           |
| nbody          | 154 ms                                                 | 97.8 ms: 1.57x faster                                                           |
| pidigits       | 191 ms                                                 | 188 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                  | 1.37x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250616-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 127 ms: 1.48x faster                                                            |
| regex_v8       | 27.8 ms                                                | 22.2 ms: 1.25x faster                                                           |
| regex_dna      | 227 ms                                                 | 191 ms: 1.18x faster                                                            |
| regex_effbot   | 3.63 ms                                                | 3.15 ms: 1.15x faster                                                           |
| Geometric mean | (ref)                                                  | 1.26x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250616-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 2.03 sec: 1.55x faster                                                          |
| pickle_pure_python   | 484 us                                                 | 319 us: 1.52x faster                                                            |
| unpickle_pure_python | 331 us                                                 | 219 us: 1.51x faster                                                            |
| xml_etree_process    | 79.1 ms                                                | 60.6 ms: 1.31x faster                                                           |
| json_dumps           | 14.2 ms                                                | 11.1 ms: 1.28x faster                                                           |
| xml_etree_parse      | 168 ms                                                 | 143 ms: 1.17x faster                                                            |
| xml_etree_iterparse  | 115 ms                                                 | 99.3 ms: 1.16x faster                                                           |
| xml_etree_generate   | 99.4 ms                                                | 85.9 ms: 1.16x faster                                                           |
| json_loads           | 31.2 us                                                | 28.5 us: 1.09x faster                                                           |
| Geometric mean       | (ref)                                                  | 1.29x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250616-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.2 ms: 1.20x faster                                                           |
| python_startup_no_site | 5.93 ms                                                | 6.93 ms: 1.17x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250616-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 32.5 ms: 1.48x faster                                                           |
| genshi_text     | 31.8 ms                                                | 21.7 ms: 1.47x faster                                                           |
| mako            | 16.3 ms                                                | 11.3 ms: 1.44x faster                                                           |
| genshi_xml      | 66.0 ms                                                | 50.0 ms: 1.32x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250616-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 166 us: 3.27x faster                                                            |
| async_tree_io            | 1.77 sec                                               | 600 ms: 2.95x faster                                                            |
| async_tree_none          | 728 ms                                                 | 260 ms: 2.80x faster                                                            |
| async_tree_memoization   | 870 ms                                                 | 312 ms: 2.79x faster                                                            |
| generators               | 80.1 ms                                                | 29.6 ms: 2.70x faster                                                           |
| mdp                      | 2.85 sec                                               | 1.22 sec: 2.33x faster                                                          |
| deltablue                | 7.91 ms                                                | 3.49 ms: 2.27x faster                                                           |
| go                       | 240 ms                                                 | 111 ms: 2.17x faster                                                            |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 499 ms: 2.04x faster                                                            |
| deepcopy_memo            | 58.5 us                                                | 29.2 us: 2.01x faster                                                           |
| pylint                   | 551 ms                                                 | 277 ms: 1.99x faster                                                            |
| chaos                    | 115 ms                                                 | 59.2 ms: 1.95x faster                                                           |
| richards_super           | 94.7 ms                                                | 49.4 ms: 1.92x faster                                                           |
| raytrace                 | 507 ms                                                 | 269 ms: 1.88x faster                                                            |
| scimark_sor              | 220 ms                                                 | 120 ms: 1.84x faster                                                            |
| deepcopy                 | 479 us                                                 | 261 us: 1.84x faster                                                            |
| richards                 | 79.3 ms                                                | 43.5 ms: 1.82x faster                                                           |
| comprehensions           | 28.8 us                                                | 16.0 us: 1.80x faster                                                           |
| scimark_monte_carlo      | 118 ms                                                 | 67.2 ms: 1.76x faster                                                           |
| crypto_pyaes             | 128 ms                                                 | 74.2 ms: 1.72x faster                                                           |
| hexiom                   | 10.4 ms                                                | 6.05 ms: 1.72x faster                                                           |
| pyflate                  | 716 ms                                                 | 435 ms: 1.65x faster                                                            |
| float                    | 117 ms                                                 | 72.8 ms: 1.61x faster                                                           |
| nbody                    | 154 ms                                                 | 97.8 ms: 1.57x faster                                                           |
| tomli_loads              | 3.14 sec                                               | 2.03 sec: 1.55x faster                                                          |
| spectral_norm            | 170 ms                                                 | 111 ms: 1.53x faster                                                            |
| pickle_pure_python       | 484 us                                                 | 319 us: 1.52x faster                                                            |
| scimark_lu               | 176 ms                                                 | 116 ms: 1.52x faster                                                            |
| unpickle_pure_python     | 331 us                                                 | 219 us: 1.51x faster                                                            |
| deepcopy_reduce          | 4.17 us                                                | 2.79 us: 1.50x faster                                                           |
| regex_compile            | 188 ms                                                 | 127 ms: 1.48x faster                                                            |
| django_template          | 48.2 ms                                                | 32.5 ms: 1.48x faster                                                           |
| genshi_text              | 31.8 ms                                                | 21.7 ms: 1.47x faster                                                           |
| html5lib                 | 88.9 ms                                                | 61.6 ms: 1.44x faster                                                           |
| mako                     | 16.3 ms                                                | 11.3 ms: 1.44x faster                                                           |
| dulwich_log              | 84.3 ms                                                | 59.2 ms: 1.43x faster                                                           |
| coroutines               | 35.1 ms                                                | 25.1 ms: 1.40x faster                                                           |
| pycparser                | 1.58 sec                                               | 1.13 sec: 1.40x faster                                                          |
| 2to3                     | 348 ms                                                 | 254 ms: 1.37x faster                                                            |
| logging_simple           | 8.30 us                                                | 6.07 us: 1.37x faster                                                           |
| sympy_integrate          | 25.8 ms                                                | 18.9 ms: 1.36x faster                                                           |
| logging_format           | 9.09 us                                                | 6.77 us: 1.34x faster                                                           |
| sympy_sum                | 196 ms                                                 | 148 ms: 1.33x faster                                                            |
| genshi_xml               | 66.0 ms                                                | 50.0 ms: 1.32x faster                                                           |
| nqueens                  | 106 ms                                                 | 80.8 ms: 1.31x faster                                                           |
| xml_etree_process        | 79.1 ms                                                | 60.6 ms: 1.31x faster                                                           |
| sympy_str                | 346 ms                                                 | 266 ms: 1.30x faster                                                            |
| docutils                 | 3.30 sec                                               | 2.57 sec: 1.28x faster                                                          |
| pprint_pformat           | 2.10 sec                                               | 1.65 sec: 1.28x faster                                                          |
| json_dumps               | 14.2 ms                                                | 11.1 ms: 1.28x faster                                                           |
| fannkuch                 | 532 ms                                                 | 418 ms: 1.27x faster                                                            |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.11 ms: 1.26x faster                                                           |
| pprint_safe_repr         | 1.02 sec                                               | 810 ms: 1.26x faster                                                            |
| sympy_expand             | 566 ms                                                 | 452 ms: 1.25x faster                                                            |
| regex_v8                 | 27.8 ms                                                | 22.2 ms: 1.25x faster                                                           |
| scimark_fft              | 466 ms                                                 | 383 ms: 1.22x faster                                                            |
| pathlib                  | 20.5 ms                                                | 17.0 ms: 1.20x faster                                                           |
| python_startup           | 14.6 ms                                                | 12.2 ms: 1.20x faster                                                           |
| regex_dna                | 227 ms                                                 | 191 ms: 1.18x faster                                                            |
| xml_etree_parse          | 168 ms                                                 | 143 ms: 1.17x faster                                                            |
| xml_etree_iterparse      | 115 ms                                                 | 99.3 ms: 1.16x faster                                                           |
| xml_etree_generate       | 99.4 ms                                                | 85.9 ms: 1.16x faster                                                           |
| regex_effbot             | 3.63 ms                                                | 3.15 ms: 1.15x faster                                                           |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                            |
| json_loads               | 31.2 us                                                | 28.5 us: 1.09x faster                                                           |
| json                     | 5.69 ms                                                | 5.29 ms: 1.08x faster                                                           |
| async_generators         | 444 ms                                                 | 414 ms: 1.07x faster                                                            |
| sqlite_synth             | 3.02 us                                                | 2.86 us: 1.06x faster                                                           |
| pidigits                 | 191 ms                                                 | 188 ms: 1.02x faster                                                            |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                                            |
| telco                    | 7.27 ms                                                | 7.98 ms: 1.10x slower                                                           |
| python_startup_no_site   | 5.93 ms                                                | 6.93 ms: 1.17x slower                                                           |
| gc_traversal             | 3.62 ms                                                | 5.07 ms: 1.40x slower                                                           |
| create_gc_cycles         | 1.62 ms                                                | 2.59 ms: 1.60x slower                                                           |
| logging_silent           | 190 ns                                                 | 475 ns: 2.50x slower                                                            |
| coverage                 | 79.4 ms                                                | 418 ms: 5.26x slower                                                            |
| thrift                   | 1.07 ms                                                | 149 ms: 138.73x slower                                                          |
| Geometric mean           | (ref)                                                  | 1.30x faster                                                                    |
Ignored benchmarks (24) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250616-3.15.0a0-c41d531/bm-20250616-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.322x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.28x

# Memory
- memory change: 1.31x