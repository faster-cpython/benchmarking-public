# Results vs. 3.10.4

- fork: faster-cpython
- ref: explicit_check_perio
- machine: linux-x86_64
- commit hash: 892a89d
- commit date: 2025-06-26
- overall geometric mean: 1.450x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250626-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 256 ms: 1.36x faster                                                            |
| docutils       | 3.30 sec                                               | 2.58 sec: 1.28x faster                                                          |
| html5lib       | 88.9 ms                                                | 61.7 ms: 1.44x faster                                                           |
| Geometric mean | (ref)                                                  | 1.36x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250626-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 599 ms: 2.95x faster                                                            |
| async_tree_none         | 728 ms                                                 | 261 ms: 2.79x faster                                                            |
| async_tree_memoization  | 870 ms                                                 | 315 ms: 2.76x faster                                                            |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 489 ms: 2.08x faster                                                            |
| Geometric mean          | (ref)                                                  | 2.62x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250626-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 72.9 ms: 1.61x faster                                                           |
| nbody          | 154 ms                                                 | 97.0 ms: 1.58x faster                                                           |
| pidigits       | 191 ms                                                 | 196 ms: 1.03x slower                                                            |
| Geometric mean | (ref)                                                  | 1.35x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250626-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 127 ms: 1.49x faster                                                            |
| regex_v8       | 27.8 ms                                                | 23.2 ms: 1.20x faster                                                           |
| regex_effbot   | 3.63 ms                                                | 3.31 ms: 1.10x faster                                                           |
| regex_dna      | 227 ms                                                 | 212 ms: 1.07x faster                                                            |
| Geometric mean | (ref)                                                  | 1.20x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250626-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.98 sec: 1.59x faster                                                          |
| unpickle_pure_python | 331 us                                                 | 219 us: 1.51x faster                                                            |
| pickle_pure_python   | 484 us                                                 | 321 us: 1.51x faster                                                            |
| xml_etree_process    | 79.1 ms                                                | 60.1 ms: 1.32x faster                                                           |
| json_dumps           | 14.2 ms                                                | 11.0 ms: 1.29x faster                                                           |
| xml_etree_generate   | 99.4 ms                                                | 85.4 ms: 1.16x faster                                                           |
| xml_etree_iterparse  | 115 ms                                                 | 99.5 ms: 1.16x faster                                                           |
| xml_etree_parse      | 168 ms                                                 | 145 ms: 1.16x faster                                                            |
| json_loads           | 31.2 us                                                | 28.2 us: 1.11x faster                                                           |
| Geometric mean       | (ref)                                                  | 1.30x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250626-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.2 ms: 1.20x faster                                                           |
| python_startup_no_site | 5.93 ms                                                | 6.93 ms: 1.17x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250626-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 21.5 ms: 1.48x faster                                                           |
| django_template | 48.2 ms                                                | 33.1 ms: 1.45x faster                                                           |
| mako            | 16.3 ms                                                | 11.3 ms: 1.45x faster                                                           |
| genshi_xml      | 66.0 ms                                                | 50.1 ms: 1.32x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.42x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250626-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 167 us: 3.26x faster                                                            |
| async_tree_io            | 1.77 sec                                               | 599 ms: 2.95x faster                                                            |
| async_tree_none          | 728 ms                                                 | 261 ms: 2.79x faster                                                            |
| async_tree_memoization   | 870 ms                                                 | 315 ms: 2.76x faster                                                            |
| generators               | 80.1 ms                                                | 30.4 ms: 2.64x faster                                                           |
| mdp                      | 2.85 sec                                               | 1.22 sec: 2.33x faster                                                          |
| deltablue                | 7.91 ms                                                | 3.47 ms: 2.28x faster                                                           |
| go                       | 240 ms                                                 | 110 ms: 2.19x faster                                                            |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 489 ms: 2.08x faster                                                            |
| pylint                   | 551 ms                                                 | 279 ms: 1.98x faster                                                            |
| deepcopy_memo            | 58.5 us                                                | 29.8 us: 1.97x faster                                                           |
| chaos                    | 115 ms                                                 | 60.0 ms: 1.92x faster                                                           |
| richards_super           | 94.7 ms                                                | 49.5 ms: 1.91x faster                                                           |
| raytrace                 | 507 ms                                                 | 268 ms: 1.89x faster                                                            |
| scimark_sor              | 220 ms                                                 | 117 ms: 1.88x faster                                                            |
| deepcopy                 | 479 us                                                 | 258 us: 1.86x faster                                                            |
| richards                 | 79.3 ms                                                | 43.6 ms: 1.82x faster                                                           |
| comprehensions           | 28.8 us                                                | 16.1 us: 1.78x faster                                                           |
| scimark_monte_carlo      | 118 ms                                                 | 67.2 ms: 1.76x faster                                                           |
| djangocms                | 38.4 us                                                | 22.3 us: 1.72x faster                                                           |
| hexiom                   | 10.4 ms                                                | 6.11 ms: 1.70x faster                                                           |
| crypto_pyaes             | 128 ms                                                 | 75.4 ms: 1.69x faster                                                           |
| spectral_norm            | 170 ms                                                 | 100 ms: 1.69x faster                                                            |
| pyflate                  | 716 ms                                                 | 428 ms: 1.67x faster                                                            |
| float                    | 117 ms                                                 | 72.9 ms: 1.61x faster                                                           |
| tomli_loads              | 3.14 sec                                               | 1.98 sec: 1.59x faster                                                          |
| nbody                    | 154 ms                                                 | 97.0 ms: 1.58x faster                                                           |
| scimark_lu               | 176 ms                                                 | 114 ms: 1.54x faster                                                            |
| deepcopy_reduce          | 4.17 us                                                | 2.72 us: 1.53x faster                                                           |
| unpickle_pure_python     | 331 us                                                 | 219 us: 1.51x faster                                                            |
| pickle_pure_python       | 484 us                                                 | 321 us: 1.51x faster                                                            |
| regex_compile            | 188 ms                                                 | 127 ms: 1.49x faster                                                            |
| genshi_text              | 31.8 ms                                                | 21.5 ms: 1.48x faster                                                           |
| django_template          | 48.2 ms                                                | 33.1 ms: 1.45x faster                                                           |
| mako                     | 16.3 ms                                                | 11.3 ms: 1.45x faster                                                           |
| html5lib                 | 88.9 ms                                                | 61.7 ms: 1.44x faster                                                           |
| coroutines               | 35.1 ms                                                | 24.5 ms: 1.43x faster                                                           |
| dulwich_log              | 84.3 ms                                                | 58.9 ms: 1.43x faster                                                           |
| thrift                   | 1.07 ms                                                | 785 us: 1.36x faster                                                            |
| 2to3                     | 348 ms                                                 | 256 ms: 1.36x faster                                                            |
| sympy_integrate          | 25.8 ms                                                | 19.0 ms: 1.36x faster                                                           |
| pycparser                | 1.58 sec                                               | 1.17 sec: 1.34x faster                                                          |
| sympy_sum                | 196 ms                                                 | 148 ms: 1.33x faster                                                            |
| logging_simple           | 8.30 us                                                | 6.27 us: 1.32x faster                                                           |
| genshi_xml               | 66.0 ms                                                | 50.1 ms: 1.32x faster                                                           |
| xml_etree_process        | 79.1 ms                                                | 60.1 ms: 1.32x faster                                                           |
| fannkuch                 | 532 ms                                                 | 404 ms: 1.31x faster                                                            |
| scimark_fft              | 466 ms                                                 | 359 ms: 1.30x faster                                                            |
| sympy_str                | 346 ms                                                 | 267 ms: 1.29x faster                                                            |
| nqueens                  | 106 ms                                                 | 81.8 ms: 1.29x faster                                                           |
| json_dumps               | 14.2 ms                                                | 11.0 ms: 1.29x faster                                                           |
| logging_format           | 9.09 us                                                | 7.06 us: 1.29x faster                                                           |
| pprint_pformat           | 2.10 sec                                               | 1.64 sec: 1.28x faster                                                          |
| docutils                 | 3.30 sec                                               | 2.58 sec: 1.28x faster                                                          |
| pprint_safe_repr         | 1.02 sec                                               | 798 ms: 1.27x faster                                                            |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.08 ms: 1.27x faster                                                           |
| sympy_expand             | 566 ms                                                 | 453 ms: 1.25x faster                                                            |
| pathlib                  | 20.5 ms                                                | 17.0 ms: 1.20x faster                                                           |
| python_startup           | 14.6 ms                                                | 12.2 ms: 1.20x faster                                                           |
| regex_v8                 | 27.8 ms                                                | 23.2 ms: 1.20x faster                                                           |
| xml_etree_generate       | 99.4 ms                                                | 85.4 ms: 1.16x faster                                                           |
| xml_etree_iterparse      | 115 ms                                                 | 99.5 ms: 1.16x faster                                                           |
| xml_etree_parse          | 168 ms                                                 | 145 ms: 1.16x faster                                                            |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                            |
| json_loads               | 31.2 us                                                | 28.2 us: 1.11x faster                                                           |
| regex_effbot             | 3.63 ms                                                | 3.31 ms: 1.10x faster                                                           |
| async_generators         | 444 ms                                                 | 408 ms: 1.09x faster                                                            |
| json                     | 5.69 ms                                                | 5.27 ms: 1.08x faster                                                           |
| regex_dna                | 227 ms                                                 | 212 ms: 1.07x faster                                                            |
| sqlite_synth             | 3.02 us                                                | 2.85 us: 1.06x faster                                                           |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                            |
| pidigits                 | 191 ms                                                 | 196 ms: 1.03x slower                                                            |
| coverage                 | 79.4 ms                                                | 87.6 ms: 1.10x slower                                                           |
| telco                    | 7.27 ms                                                | 8.04 ms: 1.11x slower                                                           |
| python_startup_no_site   | 5.93 ms                                                | 6.93 ms: 1.17x slower                                                           |
| gc_traversal             | 3.62 ms                                                | 5.13 ms: 1.42x slower                                                           |
| create_gc_cycles         | 1.62 ms                                                | 2.59 ms: 1.60x slower                                                           |
| logging_silent           | 190 ns                                                 | 481 ns: 2.54x slower                                                            |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                                    |
Ignored benchmarks (23) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250626-3.15.0a0-892a89d/bm-20250626-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.450x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.31x