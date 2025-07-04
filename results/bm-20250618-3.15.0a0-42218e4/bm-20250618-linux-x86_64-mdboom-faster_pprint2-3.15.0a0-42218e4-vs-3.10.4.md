# Results vs. 3.10.4

- fork: mdboom
- ref: faster_pprint2
- machine: linux-x86_64
- commit hash: 42218e4
- commit date: 2025-06-18
- overall geometric mean: 1.455x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.32x faster
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250618-linux-x86_64-mdboom-faster_pprint2-3.15.0a0-42218e4 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 255 ms: 1.36x faster                                            |
| docutils       | 3.30 sec                                               | 2.58 sec: 1.28x faster                                          |
| html5lib       | 88.9 ms                                                | 61.9 ms: 1.43x faster                                           |
| Geometric mean | (ref)                                                  | 1.36x faster                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250618-linux-x86_64-mdboom-faster_pprint2-3.15.0a0-42218e4 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 598 ms: 2.96x faster                                            |
| async_tree_none         | 728 ms                                                 | 262 ms: 2.78x faster                                            |
| async_tree_memoization  | 870 ms                                                 | 313 ms: 2.78x faster                                            |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 497 ms: 2.04x faster                                            |
| Geometric mean          | (ref)                                                  | 2.61x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250618-linux-x86_64-mdboom-faster_pprint2-3.15.0a0-42218e4 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 117 ms                                                 | 72.9 ms: 1.61x faster                                           |
| nbody          | 154 ms                                                 | 97.8 ms: 1.57x faster                                           |
| pidigits       | 191 ms                                                 | 192 ms: 1.00x slower                                            |
| Geometric mean | (ref)                                                  | 1.36x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250618-linux-x86_64-mdboom-faster_pprint2-3.15.0a0-42218e4 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 127 ms: 1.49x faster                                            |
| regex_v8       | 27.8 ms                                                | 23.0 ms: 1.21x faster                                           |
| regex_effbot   | 3.63 ms                                                | 3.31 ms: 1.10x faster                                           |
| regex_dna      | 227 ms                                                 | 215 ms: 1.06x faster                                            |
| Geometric mean | (ref)                                                  | 1.20x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250618-linux-x86_64-mdboom-faster_pprint2-3.15.0a0-42218e4 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 2.03 sec: 1.55x faster                                          |
| unpickle_pure_python | 331 us                                                 | 218 us: 1.51x faster                                            |
| pickle_pure_python   | 484 us                                                 | 323 us: 1.50x faster                                            |
| xml_etree_process    | 79.1 ms                                                | 59.9 ms: 1.32x faster                                           |
| json_dumps           | 14.2 ms                                                | 11.3 ms: 1.26x faster                                           |
| xml_etree_parse      | 168 ms                                                 | 141 ms: 1.19x faster                                            |
| xml_etree_iterparse  | 115 ms                                                 | 98.2 ms: 1.18x faster                                           |
| xml_etree_generate   | 99.4 ms                                                | 85.2 ms: 1.17x faster                                           |
| json_loads           | 31.2 us                                                | 28.2 us: 1.11x faster                                           |
| Geometric mean       | (ref)                                                  | 1.30x faster                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250618-linux-x86_64-mdboom-faster_pprint2-3.15.0a0-42218e4 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.2 ms: 1.20x faster                                           |
| python_startup_no_site | 5.93 ms                                                | 6.92 ms: 1.17x slower                                           |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250618-linux-x86_64-mdboom-faster_pprint2-3.15.0a0-42218e4 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 32.3 ms: 1.49x faster                                           |
| genshi_text     | 31.8 ms                                                | 21.4 ms: 1.49x faster                                           |
| mako            | 16.3 ms                                                | 11.7 ms: 1.39x faster                                           |
| genshi_xml      | 66.0 ms                                                | 48.8 ms: 1.35x faster                                           |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250618-linux-x86_64-mdboom-faster_pprint2-3.15.0a0-42218e4 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 169 us: 3.23x faster                                            |
| async_tree_io            | 1.77 sec                                               | 598 ms: 2.96x faster                                            |
| async_tree_none          | 728 ms                                                 | 262 ms: 2.78x faster                                            |
| async_tree_memoization   | 870 ms                                                 | 313 ms: 2.78x faster                                            |
| generators               | 80.1 ms                                                | 29.8 ms: 2.69x faster                                           |
| mdp                      | 2.85 sec                                               | 1.22 sec: 2.33x faster                                          |
| deltablue                | 7.91 ms                                                | 3.47 ms: 2.28x faster                                           |
| go                       | 240 ms                                                 | 111 ms: 2.16x faster                                            |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 497 ms: 2.04x faster                                            |
| deepcopy_memo            | 58.5 us                                                | 29.1 us: 2.01x faster                                           |
| pylint                   | 551 ms                                                 | 279 ms: 1.98x faster                                            |
| richards_super           | 94.7 ms                                                | 49.3 ms: 1.92x faster                                           |
| chaos                    | 115 ms                                                 | 61.1 ms: 1.89x faster                                           |
| deepcopy                 | 479 us                                                 | 255 us: 1.88x faster                                            |
| raytrace                 | 507 ms                                                 | 271 ms: 1.87x faster                                            |
| scimark_sor              | 220 ms                                                 | 119 ms: 1.85x faster                                            |
| richards                 | 79.3 ms                                                | 42.9 ms: 1.85x faster                                           |
| comprehensions           | 28.8 us                                                | 16.0 us: 1.80x faster                                           |
| scimark_monte_carlo      | 118 ms                                                 | 65.9 ms: 1.79x faster                                           |
| hexiom                   | 10.4 ms                                                | 5.97 ms: 1.74x faster                                           |
| djangocms                | 38.4 us                                                | 22.1 us: 1.74x faster                                           |
| pyflate                  | 716 ms                                                 | 423 ms: 1.69x faster                                            |
| crypto_pyaes             | 128 ms                                                 | 75.6 ms: 1.69x faster                                           |
| float                    | 117 ms                                                 | 72.9 ms: 1.61x faster                                           |
| spectral_norm            | 170 ms                                                 | 107 ms: 1.59x faster                                            |
| nbody                    | 154 ms                                                 | 97.8 ms: 1.57x faster                                           |
| tomli_loads              | 3.14 sec                                               | 2.03 sec: 1.55x faster                                          |
| unpickle_pure_python     | 331 us                                                 | 218 us: 1.51x faster                                            |
| deepcopy_reduce          | 4.17 us                                                | 2.76 us: 1.51x faster                                           |
| pickle_pure_python       | 484 us                                                 | 323 us: 1.50x faster                                            |
| scimark_lu               | 176 ms                                                 | 118 ms: 1.50x faster                                            |
| django_template          | 48.2 ms                                                | 32.3 ms: 1.49x faster                                           |
| regex_compile            | 188 ms                                                 | 127 ms: 1.49x faster                                            |
| genshi_text              | 31.8 ms                                                | 21.4 ms: 1.49x faster                                           |
| html5lib                 | 88.9 ms                                                | 61.9 ms: 1.43x faster                                           |
| dulwich_log              | 84.3 ms                                                | 59.1 ms: 1.43x faster                                           |
| pprint_pformat           | 2.10 sec                                               | 1.49 sec: 1.41x faster                                          |
| coroutines               | 35.1 ms                                                | 25.0 ms: 1.40x faster                                           |
| thrift                   | 1.07 ms                                                | 766 us: 1.40x faster                                            |
| pprint_safe_repr         | 1.02 sec                                               | 729 ms: 1.40x faster                                            |
| mako                     | 16.3 ms                                                | 11.7 ms: 1.39x faster                                           |
| sympy_integrate          | 25.8 ms                                                | 18.9 ms: 1.37x faster                                           |
| 2to3                     | 348 ms                                                 | 255 ms: 1.36x faster                                            |
| pycparser                | 1.58 sec                                               | 1.16 sec: 1.36x faster                                          |
| genshi_xml               | 66.0 ms                                                | 48.8 ms: 1.35x faster                                           |
| sympy_sum                | 196 ms                                                 | 147 ms: 1.33x faster                                            |
| logging_simple           | 8.30 us                                                | 6.24 us: 1.33x faster                                           |
| logging_format           | 9.09 us                                                | 6.87 us: 1.32x faster                                           |
| xml_etree_process        | 79.1 ms                                                | 59.9 ms: 1.32x faster                                           |
| nqueens                  | 106 ms                                                 | 80.8 ms: 1.31x faster                                           |
| sympy_str                | 346 ms                                                 | 264 ms: 1.31x faster                                            |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.00 ms: 1.29x faster                                           |
| scimark_fft              | 466 ms                                                 | 364 ms: 1.28x faster                                            |
| fannkuch                 | 532 ms                                                 | 416 ms: 1.28x faster                                            |
| docutils                 | 3.30 sec                                               | 2.58 sec: 1.28x faster                                          |
| json_dumps               | 14.2 ms                                                | 11.3 ms: 1.26x faster                                           |
| sympy_expand             | 566 ms                                                 | 449 ms: 1.26x faster                                            |
| regex_v8                 | 27.8 ms                                                | 23.0 ms: 1.21x faster                                           |
| pathlib                  | 20.5 ms                                                | 17.0 ms: 1.21x faster                                           |
| python_startup           | 14.6 ms                                                | 12.2 ms: 1.20x faster                                           |
| xml_etree_parse          | 168 ms                                                 | 141 ms: 1.19x faster                                            |
| xml_etree_iterparse      | 115 ms                                                 | 98.2 ms: 1.18x faster                                           |
| xml_etree_generate       | 99.4 ms                                                | 85.2 ms: 1.17x faster                                           |
| meteor_contest           | 120 ms                                                 | 104 ms: 1.15x faster                                            |
| json_loads               | 31.2 us                                                | 28.2 us: 1.11x faster                                           |
| json                     | 5.69 ms                                                | 5.17 ms: 1.10x faster                                           |
| regex_effbot             | 3.63 ms                                                | 3.31 ms: 1.10x faster                                           |
| async_generators         | 444 ms                                                 | 409 ms: 1.09x faster                                            |
| regex_dna                | 227 ms                                                 | 215 ms: 1.06x faster                                            |
| sqlite_synth             | 3.02 us                                                | 2.90 us: 1.04x faster                                           |
| asyncio_websockets       | 559 ms                                                 | 553 ms: 1.01x faster                                            |
| pidigits                 | 191 ms                                                 | 192 ms: 1.00x slower                                            |
| telco                    | 7.27 ms                                                | 7.96 ms: 1.10x slower                                           |
| coverage                 | 79.4 ms                                                | 87.1 ms: 1.10x slower                                           |
| python_startup_no_site   | 5.93 ms                                                | 6.92 ms: 1.17x slower                                           |
| gc_traversal             | 3.62 ms                                                | 5.06 ms: 1.40x slower                                           |
| create_gc_cycles         | 1.62 ms                                                | 2.59 ms: 1.60x slower                                           |
| logging_silent           | 190 ns                                                 | 469 ns: 2.47x slower                                            |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                    |
Ignored benchmarks (23) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250618-3.15.0a0-42218e4/bm-20250618-linux-x86_64-mdboom-faster_pprint2-3.15.0a0-42218e4.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.455x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.36x
- 95% likely to have a speedup of 1.34x
- 99% likely to have a speedup of 1.32x

# Memory
- memory change: 1.31x