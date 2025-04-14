# Results vs. 3.10.4

- fork: iritkatriel
- ref: stats
- machine: linux-x86_64
- commit hash: 4300c89
- commit date: 2025-04-06
- overall geometric mean: 1.466x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.33x faster
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250406-linux-x86_64-iritkatriel-stats-3.14.0a6+-4300c89 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 251 ms: 1.39x faster                                         |
| docutils       | 3.30 sec                                               | 2.59 sec: 1.27x faster                                       |
| html5lib       | 88.9 ms                                                | 60.5 ms: 1.47x faster                                        |
| Geometric mean | (ref)                                                  | 1.37x faster                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250406-linux-x86_64-iritkatriel-stats-3.14.0a6+-4300c89 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 615 ms: 2.88x faster                                         |
| async_tree_none         | 728 ms                                                 | 259 ms: 2.81x faster                                         |
| async_tree_memoization  | 870 ms                                                 | 312 ms: 2.79x faster                                         |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 483 ms: 2.10x faster                                         |
| Geometric mean          | (ref)                                                  | 2.63x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250406-linux-x86_64-iritkatriel-stats-3.14.0a6+-4300c89 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 117 ms                                                 | 68.2 ms: 1.72x faster                                        |
| nbody          | 154 ms                                                 | 92.2 ms: 1.66x faster                                        |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                         |
| Geometric mean | (ref)                                                  | 1.43x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250406-linux-x86_64-iritkatriel-stats-3.14.0a6+-4300c89 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 125 ms: 1.51x faster                                         |
| regex_v8       | 27.8 ms                                                | 23.0 ms: 1.21x faster                                        |
| regex_effbot   | 3.63 ms                                                | 3.32 ms: 1.09x faster                                        |
| regex_dna      | 227 ms                                                 | 220 ms: 1.03x faster                                         |
| Geometric mean | (ref)                                                  | 1.20x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250406-linux-x86_64-iritkatriel-stats-3.14.0a6+-4300c89 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.96 sec: 1.60x faster                                       |
| unpickle_pure_python | 331 us                                                 | 215 us: 1.54x faster                                         |
| pickle_pure_python   | 484 us                                                 | 315 us: 1.54x faster                                         |
| xml_etree_process    | 79.1 ms                                                | 58.3 ms: 1.36x faster                                        |
| json_dumps           | 14.2 ms                                                | 11.7 ms: 1.22x faster                                        |
| xml_etree_parse      | 168 ms                                                 | 141 ms: 1.19x faster                                         |
| xml_etree_generate   | 99.4 ms                                                | 83.5 ms: 1.19x faster                                        |
| xml_etree_iterparse  | 115 ms                                                 | 98.3 ms: 1.17x faster                                        |
| json_loads           | 31.2 us                                                | 29.7 us: 1.05x faster                                        |
| Geometric mean       | (ref)                                                  | 1.30x faster                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250406-linux-x86_64-iritkatriel-stats-3.14.0a6+-4300c89 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.2 ms: 1.11x faster                                        |
| python_startup_no_site | 5.93 ms                                                | 8.18 ms: 1.38x slower                                        |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250406-linux-x86_64-iritkatriel-stats-3.14.0a6+-4300c89 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 31.5 ms: 1.53x faster                                        |
| genshi_text     | 31.8 ms                                                | 20.9 ms: 1.52x faster                                        |
| mako            | 16.3 ms                                                | 11.3 ms: 1.45x faster                                        |
| genshi_xml      | 66.0 ms                                                | 49.3 ms: 1.34x faster                                        |
| Geometric mean  | (ref)                                                  | 1.46x faster                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250406-linux-x86_64-iritkatriel-stats-3.14.0a6+-4300c89 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 167 us: 3.25x faster                                         |
| async_tree_io            | 1.77 sec                                               | 615 ms: 2.88x faster                                         |
| async_tree_none          | 728 ms                                                 | 259 ms: 2.81x faster                                         |
| async_tree_memoization   | 870 ms                                                 | 312 ms: 2.79x faster                                         |
| generators               | 80.1 ms                                                | 29.6 ms: 2.71x faster                                        |
| deltablue                | 7.91 ms                                                | 3.37 ms: 2.35x faster                                        |
| mdp                      | 2.85 sec                                               | 1.23 sec: 2.32x faster                                       |
| go                       | 240 ms                                                 | 111 ms: 2.16x faster                                         |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 483 ms: 2.10x faster                                         |
| chaos                    | 115 ms                                                 | 56.4 ms: 2.05x faster                                        |
| deepcopy_memo            | 58.5 us                                                | 28.8 us: 2.03x faster                                        |
| pylint                   | 551 ms                                                 | 276 ms: 2.00x faster                                         |
| logging_silent           | 190 ns                                                 | 96.1 ns: 1.98x faster                                        |
| richards_super           | 94.7 ms                                                | 48.4 ms: 1.96x faster                                        |
| raytrace                 | 507 ms                                                 | 261 ms: 1.94x faster                                         |
| deepcopy                 | 479 us                                                 | 249 us: 1.92x faster                                         |
| richards                 | 79.3 ms                                                | 42.2 ms: 1.88x faster                                        |
| scimark_sor              | 220 ms                                                 | 119 ms: 1.84x faster                                         |
| scimark_monte_carlo      | 118 ms                                                 | 65.5 ms: 1.81x faster                                        |
| crypto_pyaes             | 128 ms                                                 | 73.3 ms: 1.74x faster                                        |
| float                    | 117 ms                                                 | 68.2 ms: 1.72x faster                                        |
| hexiom                   | 10.4 ms                                                | 6.14 ms: 1.69x faster                                        |
| comprehensions           | 28.8 us                                                | 17.0 us: 1.69x faster                                        |
| nbody                    | 154 ms                                                 | 92.2 ms: 1.66x faster                                        |
| spectral_norm            | 170 ms                                                 | 102 ms: 1.66x faster                                         |
| deepcopy_reduce          | 4.17 us                                                | 2.57 us: 1.62x faster                                        |
| tomli_loads              | 3.14 sec                                               | 1.96 sec: 1.60x faster                                       |
| pyflate                  | 716 ms                                                 | 462 ms: 1.55x faster                                         |
| unpickle_pure_python     | 331 us                                                 | 215 us: 1.54x faster                                         |
| pickle_pure_python       | 484 us                                                 | 315 us: 1.54x faster                                         |
| django_template          | 48.2 ms                                                | 31.5 ms: 1.53x faster                                        |
| genshi_text              | 31.8 ms                                                | 20.9 ms: 1.52x faster                                        |
| regex_compile            | 188 ms                                                 | 125 ms: 1.51x faster                                         |
| logging_simple           | 8.30 us                                                | 5.51 us: 1.51x faster                                        |
| coroutines               | 35.1 ms                                                | 23.3 ms: 1.50x faster                                        |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.50x faster                                         |
| logging_format           | 9.09 us                                                | 6.11 us: 1.49x faster                                        |
| html5lib                 | 88.9 ms                                                | 60.5 ms: 1.47x faster                                        |
| pprint_pformat           | 2.10 sec                                               | 1.44 sec: 1.46x faster                                       |
| pprint_safe_repr         | 1.02 sec                                               | 701 ms: 1.45x faster                                         |
| mako                     | 16.3 ms                                                | 11.3 ms: 1.45x faster                                        |
| dulwich_log              | 84.3 ms                                                | 59.4 ms: 1.42x faster                                        |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.7 ms: 1.40x faster                                        |
| 2to3                     | 348 ms                                                 | 251 ms: 1.39x faster                                         |
| scimark_fft              | 466 ms                                                 | 342 ms: 1.36x faster                                         |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.75 ms: 1.36x faster                                        |
| pycparser                | 1.58 sec                                               | 1.16 sec: 1.36x faster                                       |
| xml_etree_process        | 79.1 ms                                                | 58.3 ms: 1.36x faster                                        |
| sympy_integrate          | 25.8 ms                                                | 19.0 ms: 1.36x faster                                        |
| genshi_xml               | 66.0 ms                                                | 49.3 ms: 1.34x faster                                        |
| sympy_sum                | 196 ms                                                 | 149 ms: 1.32x faster                                         |
| nqueens                  | 106 ms                                                 | 80.6 ms: 1.31x faster                                        |
| sqlalchemy_declarative   | 172 ms                                                 | 131 ms: 1.31x faster                                         |
| sympy_str                | 346 ms                                                 | 269 ms: 1.29x faster                                         |
| fannkuch                 | 532 ms                                                 | 413 ms: 1.29x faster                                         |
| docutils                 | 3.30 sec                                               | 2.59 sec: 1.27x faster                                       |
| pathlib                  | 20.5 ms                                                | 16.5 ms: 1.24x faster                                        |
| sympy_expand             | 566 ms                                                 | 456 ms: 1.24x faster                                         |
| json_dumps               | 14.2 ms                                                | 11.7 ms: 1.22x faster                                        |
| regex_v8                 | 27.8 ms                                                | 23.0 ms: 1.21x faster                                        |
| xml_etree_parse          | 168 ms                                                 | 141 ms: 1.19x faster                                         |
| xml_etree_generate       | 99.4 ms                                                | 83.5 ms: 1.19x faster                                        |
| xml_etree_iterparse      | 115 ms                                                 | 98.3 ms: 1.17x faster                                        |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                         |
| bench_thread_pool        | 986 us                                                 | 883 us: 1.12x faster                                         |
| async_generators         | 444 ms                                                 | 397 ms: 1.12x faster                                         |
| python_startup           | 14.6 ms                                                | 13.2 ms: 1.11x faster                                        |
| regex_effbot             | 3.63 ms                                                | 3.32 ms: 1.09x faster                                        |
| sqlite_synth             | 3.02 us                                                | 2.78 us: 1.09x faster                                        |
| json                     | 5.69 ms                                                | 5.32 ms: 1.07x faster                                        |
| json_loads               | 31.2 us                                                | 29.7 us: 1.05x faster                                        |
| regex_dna                | 227 ms                                                 | 220 ms: 1.03x faster                                         |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                         |
| asyncio_websockets       | 559 ms                                                 | 553 ms: 1.01x faster                                         |
| telco                    | 7.27 ms                                                | 7.70 ms: 1.06x slower                                        |
| coverage                 | 79.4 ms                                                | 84.8 ms: 1.07x slower                                        |
| gc_traversal             | 3.62 ms                                                | 4.77 ms: 1.32x slower                                        |
| python_startup_no_site   | 5.93 ms                                                | 8.18 ms: 1.38x slower                                        |
| create_gc_cycles         | 1.62 ms                                                | 2.47 ms: 1.53x slower                                        |
| bench_mp_pool            | 24.0 ms                                                | 81.9 ms: 3.41x slower                                        |
| Geometric mean           | (ref)                                                  | 1.44x faster                                                 |
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250406-3.14.0a6+-4300c89/bm-20250406-linux-x86_64-iritkatriel-stats-3.14.0a6+-4300c89.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.466x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.37x
- 95% likely to have a speedup of 1.36x
- 99% likely to have a speedup of 1.33x

# Memory
- memory change: 1.27x