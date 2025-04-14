# Results vs. 3.10.4

- fork: faster-cpython
- ref: immortal_stickiness
- machine: linux-x86_64
- commit hash: 2a08194
- commit date: 2025-03-12
- overall geometric mean: 1.439x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250312-linux-x86_64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 256 ms: 1.36x faster                                                            |
| docutils       | 3.30 sec                                               | 2.62 sec: 1.26x faster                                                          |
| html5lib       | 88.9 ms                                                | 61.2 ms: 1.45x faster                                                           |
| Geometric mean | (ref)                                                  | 1.35x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250312-linux-x86_64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 607 ms: 2.92x faster                                                            |
| async_tree_none         | 728 ms                                                 | 256 ms: 2.85x faster                                                            |
| async_tree_memoization  | 870 ms                                                 | 315 ms: 2.77x faster                                                            |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 485 ms: 2.09x faster                                                            |
| Geometric mean          | (ref)                                                  | 2.63x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250312-linux-x86_64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 70.0 ms: 1.67x faster                                                           |
| nbody          | 154 ms                                                 | 95.7 ms: 1.60x faster                                                           |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                            |
| Geometric mean | (ref)                                                  | 1.40x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250312-linux-x86_64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 125 ms: 1.51x faster                                                            |
| regex_v8       | 27.8 ms                                                | 23.5 ms: 1.18x faster                                                           |
| regex_effbot   | 3.63 ms                                                | 3.53 ms: 1.03x faster                                                           |
| regex_dna      | 227 ms                                                 | 225 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                  | 1.17x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250312-linux-x86_64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.97 sec: 1.59x faster                                                          |
| pickle_pure_python   | 484 us                                                 | 314 us: 1.54x faster                                                            |
| unpickle_pure_python | 331 us                                                 | 217 us: 1.53x faster                                                            |
| xml_etree_process    | 79.1 ms                                                | 58.0 ms: 1.36x faster                                                           |
| json_dumps           | 14.2 ms                                                | 11.4 ms: 1.24x faster                                                           |
| xml_etree_parse      | 168 ms                                                 | 140 ms: 1.20x faster                                                            |
| xml_etree_generate   | 99.4 ms                                                | 83.3 ms: 1.19x faster                                                           |
| xml_etree_iterparse  | 115 ms                                                 | 98.2 ms: 1.18x faster                                                           |
| json_loads           | 31.2 us                                                | 30.2 us: 1.03x faster                                                           |
| Geometric mean       | (ref)                                                  | 1.30x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250312-linux-x86_64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.1 ms: 1.12x faster                                                           |
| python_startup_no_site | 5.93 ms                                                | 8.19 ms: 1.38x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250312-linux-x86_64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 31.4 ms: 1.53x faster                                                           |
| mako            | 16.3 ms                                                | 11.1 ms: 1.47x faster                                                           |
| genshi_text     | 31.8 ms                                                | 21.8 ms: 1.46x faster                                                           |
| genshi_xml      | 66.0 ms                                                | 49.9 ms: 1.32x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250312-linux-x86_64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 160 us: 3.40x faster                                                            |
| async_tree_io            | 1.77 sec                                               | 607 ms: 2.92x faster                                                            |
| async_tree_none          | 728 ms                                                 | 256 ms: 2.85x faster                                                            |
| generators               | 80.1 ms                                                | 28.6 ms: 2.80x faster                                                           |
| async_tree_memoization   | 870 ms                                                 | 315 ms: 2.77x faster                                                            |
| deltablue                | 7.91 ms                                                | 3.08 ms: 2.57x faster                                                           |
| go                       | 240 ms                                                 | 114 ms: 2.11x faster                                                            |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 485 ms: 2.09x faster                                                            |
| logging_silent           | 190 ns                                                 | 93.6 ns: 2.03x faster                                                           |
| deepcopy_memo            | 58.5 us                                                | 29.1 us: 2.01x faster                                                           |
| pylint                   | 551 ms                                                 | 276 ms: 2.00x faster                                                            |
| richards_super           | 94.7 ms                                                | 49.0 ms: 1.93x faster                                                           |
| chaos                    | 115 ms                                                 | 59.7 ms: 1.93x faster                                                           |
| raytrace                 | 507 ms                                                 | 266 ms: 1.90x faster                                                            |
| scimark_sor              | 220 ms                                                 | 117 ms: 1.88x faster                                                            |
| richards                 | 79.3 ms                                                | 42.6 ms: 1.86x faster                                                           |
| deepcopy                 | 479 us                                                 | 261 us: 1.84x faster                                                            |
| spectral_norm            | 170 ms                                                 | 98.4 ms: 1.73x faster                                                           |
| scimark_monte_carlo      | 118 ms                                                 | 68.5 ms: 1.73x faster                                                           |
| comprehensions           | 28.8 us                                                | 16.7 us: 1.72x faster                                                           |
| hexiom                   | 10.4 ms                                                | 6.13 ms: 1.70x faster                                                           |
| crypto_pyaes             | 128 ms                                                 | 76.4 ms: 1.67x faster                                                           |
| float                    | 117 ms                                                 | 70.0 ms: 1.67x faster                                                           |
| nbody                    | 154 ms                                                 | 95.7 ms: 1.60x faster                                                           |
| tomli_loads              | 3.14 sec                                               | 1.97 sec: 1.59x faster                                                          |
| pyflate                  | 716 ms                                                 | 463 ms: 1.55x faster                                                            |
| pickle_pure_python       | 484 us                                                 | 314 us: 1.54x faster                                                            |
| scimark_lu               | 176 ms                                                 | 114 ms: 1.54x faster                                                            |
| deepcopy_reduce          | 4.17 us                                                | 2.71 us: 1.54x faster                                                           |
| django_template          | 48.2 ms                                                | 31.4 ms: 1.53x faster                                                           |
| unpickle_pure_python     | 331 us                                                 | 217 us: 1.53x faster                                                            |
| regex_compile            | 188 ms                                                 | 125 ms: 1.51x faster                                                            |
| coroutines               | 35.1 ms                                                | 23.4 ms: 1.50x faster                                                           |
| logging_simple           | 8.30 us                                                | 5.55 us: 1.50x faster                                                           |
| mako                     | 16.3 ms                                                | 11.1 ms: 1.47x faster                                                           |
| logging_format           | 9.09 us                                                | 6.23 us: 1.46x faster                                                           |
| genshi_text              | 31.8 ms                                                | 21.8 ms: 1.46x faster                                                           |
| html5lib                 | 88.9 ms                                                | 61.2 ms: 1.45x faster                                                           |
| dulwich_log              | 84.3 ms                                                | 58.2 ms: 1.45x faster                                                           |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.5 ms: 1.42x faster                                                           |
| pprint_pformat           | 2.10 sec                                               | 1.49 sec: 1.41x faster                                                          |
| pprint_safe_repr         | 1.02 sec                                               | 730 ms: 1.39x faster                                                            |
| thrift                   | 1.07 ms                                                | 774 us: 1.38x faster                                                            |
| xml_etree_process        | 79.1 ms                                                | 58.0 ms: 1.36x faster                                                           |
| 2to3                     | 348 ms                                                 | 256 ms: 1.36x faster                                                            |
| pycparser                | 1.58 sec                                               | 1.17 sec: 1.34x faster                                                          |
| sympy_sum                | 196 ms                                                 | 147 ms: 1.33x faster                                                            |
| genshi_xml               | 66.0 ms                                                | 49.9 ms: 1.32x faster                                                           |
| sqlalchemy_declarative   | 172 ms                                                 | 130 ms: 1.32x faster                                                            |
| scimark_fft              | 466 ms                                                 | 353 ms: 1.32x faster                                                            |
| sympy_integrate          | 25.8 ms                                                | 19.8 ms: 1.31x faster                                                           |
| sympy_str                | 346 ms                                                 | 267 ms: 1.29x faster                                                            |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.01 ms: 1.29x faster                                                           |
| nqueens                  | 106 ms                                                 | 83.5 ms: 1.27x faster                                                           |
| docutils                 | 3.30 sec                                               | 2.62 sec: 1.26x faster                                                          |
| sympy_expand             | 566 ms                                                 | 450 ms: 1.26x faster                                                            |
| json_dumps               | 14.2 ms                                                | 11.4 ms: 1.24x faster                                                           |
| fannkuch                 | 532 ms                                                 | 430 ms: 1.24x faster                                                            |
| pathlib                  | 20.5 ms                                                | 16.8 ms: 1.22x faster                                                           |
| xml_etree_parse          | 168 ms                                                 | 140 ms: 1.20x faster                                                            |
| xml_etree_generate       | 99.4 ms                                                | 83.3 ms: 1.19x faster                                                           |
| regex_v8                 | 27.8 ms                                                | 23.5 ms: 1.18x faster                                                           |
| xml_etree_iterparse      | 115 ms                                                 | 98.2 ms: 1.18x faster                                                           |
| mdp                      | 2.85 sec                                               | 2.49 sec: 1.14x faster                                                          |
| async_generators         | 444 ms                                                 | 391 ms: 1.13x faster                                                            |
| bench_thread_pool        | 986 us                                                 | 872 us: 1.13x faster                                                            |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                            |
| python_startup           | 14.6 ms                                                | 13.1 ms: 1.12x faster                                                           |
| sqlite_synth             | 3.02 us                                                | 2.80 us: 1.08x faster                                                           |
| json                     | 5.69 ms                                                | 5.32 ms: 1.07x faster                                                           |
| json_loads               | 31.2 us                                                | 30.2 us: 1.03x faster                                                           |
| regex_effbot             | 3.63 ms                                                | 3.53 ms: 1.03x faster                                                           |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                            |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                                            |
| regex_dna                | 227 ms                                                 | 225 ms: 1.01x faster                                                            |
| telco                    | 7.27 ms                                                | 7.92 ms: 1.09x slower                                                           |
| coverage                 | 79.4 ms                                                | 93.2 ms: 1.17x slower                                                           |
| gc_traversal             | 3.62 ms                                                | 4.92 ms: 1.36x slower                                                           |
| python_startup_no_site   | 5.93 ms                                                | 8.19 ms: 1.38x slower                                                           |
| create_gc_cycles         | 1.62 ms                                                | 2.50 ms: 1.54x slower                                                           |
| bench_mp_pool            | 24.0 ms                                                | 82.8 ms: 3.45x slower                                                           |
| Geometric mean           | (ref)                                                  | 1.41x faster                                                                    |
Ignored benchmarks (20) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250312-3.14.0a5+-2a08194/bm-20250312-linux-x86_64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.439x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.28x