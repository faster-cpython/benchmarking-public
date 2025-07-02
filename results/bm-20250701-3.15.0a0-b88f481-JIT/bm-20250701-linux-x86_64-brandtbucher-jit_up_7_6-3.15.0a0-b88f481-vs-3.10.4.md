# Results vs. 3.10.4

- fork: brandtbucher
- ref: jit_up_7_6
- machine: linux-x86_64
- commit hash: b88f481
- commit date: 2025-07-01
- overall geometric mean: 1.486x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.34x faster
- Memory change: 1.36x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250701-linux-x86_64-brandtbucher-jit_up_7_6-3.15.0a0-b88f481 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 265 ms: 1.31x faster                                              |
| docutils       | 3.30 sec                                               | 2.67 sec: 1.23x faster                                            |
| html5lib       | 88.9 ms                                                | 62.0 ms: 1.43x faster                                             |
| Geometric mean | (ref)                                                  | 1.32x faster                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250701-linux-x86_64-brandtbucher-jit_up_7_6-3.15.0a0-b88f481 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 603 ms: 2.93x faster                                              |
| async_tree_none         | 728 ms                                                 | 261 ms: 2.79x faster                                              |
| async_tree_memoization  | 870 ms                                                 | 313 ms: 2.78x faster                                              |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 492 ms: 2.07x faster                                              |
| Geometric mean          | (ref)                                                  | 2.62x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250701-linux-x86_64-brandtbucher-jit_up_7_6-3.15.0a0-b88f481 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 117 ms                                                 | 65.7 ms: 1.78x faster                                             |
| nbody          | 154 ms                                                 | 93.0 ms: 1.65x faster                                             |
| pidigits       | 191 ms                                                 | 196 ms: 1.03x slower                                              |
| Geometric mean | (ref)                                                  | 1.42x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250701-linux-x86_64-brandtbucher-jit_up_7_6-3.15.0a0-b88f481 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 129 ms: 1.46x faster                                              |
| regex_v8       | 27.8 ms                                                | 22.5 ms: 1.24x faster                                             |
| regex_dna      | 227 ms                                                 | 202 ms: 1.12x faster                                              |
| regex_effbot   | 3.63 ms                                                | 3.32 ms: 1.09x faster                                             |
| Geometric mean | (ref)                                                  | 1.22x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250701-linux-x86_64-brandtbucher-jit_up_7_6-3.15.0a0-b88f481 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.84 sec: 1.70x faster                                            |
| unpickle_pure_python | 331 us                                                 | 196 us: 1.69x faster                                              |
| pickle_pure_python   | 484 us                                                 | 321 us: 1.51x faster                                              |
| xml_etree_process    | 79.1 ms                                                | 55.8 ms: 1.42x faster                                             |
| json_dumps           | 14.2 ms                                                | 11.0 ms: 1.29x faster                                             |
| xml_etree_generate   | 99.4 ms                                                | 80.4 ms: 1.24x faster                                             |
| xml_etree_parse      | 168 ms                                                 | 139 ms: 1.20x faster                                              |
| xml_etree_iterparse  | 115 ms                                                 | 98.2 ms: 1.18x faster                                             |
| json_loads           | 31.2 us                                                | 28.3 us: 1.10x faster                                             |
| Geometric mean       | (ref)                                                  | 1.35x faster                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250701-linux-x86_64-brandtbucher-jit_up_7_6-3.15.0a0-b88f481 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.2 ms: 1.20x faster                                             |
| python_startup_no_site | 5.93 ms                                                | 6.94 ms: 1.17x slower                                             |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250701-linux-x86_64-brandtbucher-jit_up_7_6-3.15.0a0-b88f481 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.5 ms: 1.55x faster                                             |
| genshi_text     | 31.8 ms                                                | 21.5 ms: 1.48x faster                                             |
| django_template | 48.2 ms                                                | 32.7 ms: 1.47x faster                                             |
| genshi_xml      | 66.0 ms                                                | 50.5 ms: 1.31x faster                                             |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250701-linux-x86_64-brandtbucher-jit_up_7_6-3.15.0a0-b88f481 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 167 us: 3.25x faster                                              |
| async_tree_io            | 1.77 sec                                               | 603 ms: 2.93x faster                                              |
| async_tree_none          | 728 ms                                                 | 261 ms: 2.79x faster                                              |
| async_tree_memoization   | 870 ms                                                 | 313 ms: 2.78x faster                                              |
| generators               | 80.1 ms                                                | 30.4 ms: 2.63x faster                                             |
| richards_super           | 94.7 ms                                                | 36.2 ms: 2.62x faster                                             |
| deltablue                | 7.91 ms                                                | 3.05 ms: 2.60x faster                                             |
| richards                 | 79.3 ms                                                | 31.3 ms: 2.53x faster                                             |
| mdp                      | 2.85 sec                                               | 1.23 sec: 2.31x faster                                            |
| go                       | 240 ms                                                 | 114 ms: 2.11x faster                                              |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 492 ms: 2.07x faster                                              |
| deepcopy_memo            | 58.5 us                                                | 29.7 us: 1.97x faster                                             |
| pylint                   | 551 ms                                                 | 288 ms: 1.91x faster                                              |
| chaos                    | 115 ms                                                 | 60.4 ms: 1.91x faster                                             |
| raytrace                 | 507 ms                                                 | 271 ms: 1.87x faster                                              |
| scimark_sor              | 220 ms                                                 | 118 ms: 1.87x faster                                              |
| deepcopy                 | 479 us                                                 | 259 us: 1.85x faster                                              |
| spectral_norm            | 170 ms                                                 | 92.2 ms: 1.84x faster                                             |
| logging_silent           | 190 ns                                                 | 103 ns: 1.84x faster                                              |
| scimark_monte_carlo      | 118 ms                                                 | 66.2 ms: 1.78x faster                                             |
| float                    | 117 ms                                                 | 65.7 ms: 1.78x faster                                             |
| pyflate                  | 716 ms                                                 | 406 ms: 1.76x faster                                              |
| comprehensions           | 28.8 us                                                | 16.4 us: 1.75x faster                                             |
| crypto_pyaes             | 128 ms                                                 | 73.8 ms: 1.73x faster                                             |
| tomli_loads              | 3.14 sec                                               | 1.84 sec: 1.70x faster                                            |
| unpickle_pure_python     | 331 us                                                 | 196 us: 1.69x faster                                              |
| hexiom                   | 10.4 ms                                                | 6.22 ms: 1.67x faster                                             |
| djangocms                | 38.4 us                                                | 23.0 us: 1.67x faster                                             |
| nbody                    | 154 ms                                                 | 93.0 ms: 1.65x faster                                             |
| mako                     | 16.3 ms                                                | 10.5 ms: 1.55x faster                                             |
| deepcopy_reduce          | 4.17 us                                                | 2.75 us: 1.52x faster                                             |
| pickle_pure_python       | 484 us                                                 | 321 us: 1.51x faster                                              |
| scimark_lu               | 176 ms                                                 | 118 ms: 1.50x faster                                              |
| genshi_text              | 31.8 ms                                                | 21.5 ms: 1.48x faster                                             |
| logging_simple           | 8.30 us                                                | 5.61 us: 1.48x faster                                             |
| scimark_fft              | 466 ms                                                 | 315 ms: 1.48x faster                                              |
| django_template          | 48.2 ms                                                | 32.7 ms: 1.47x faster                                             |
| regex_compile            | 188 ms                                                 | 129 ms: 1.46x faster                                              |
| logging_format           | 9.09 us                                                | 6.26 us: 1.45x faster                                             |
| pprint_pformat           | 2.10 sec                                               | 1.45 sec: 1.45x faster                                            |
| html5lib                 | 88.9 ms                                                | 62.0 ms: 1.43x faster                                             |
| xml_etree_process        | 79.1 ms                                                | 55.8 ms: 1.42x faster                                             |
| pprint_safe_repr         | 1.02 sec                                               | 719 ms: 1.41x faster                                              |
| dulwich_log              | 84.3 ms                                                | 59.7 ms: 1.41x faster                                             |
| coroutines               | 35.1 ms                                                | 25.0 ms: 1.40x faster                                             |
| pycparser                | 1.58 sec                                               | 1.13 sec: 1.40x faster                                            |
| thrift                   | 1.07 ms                                                | 777 us: 1.38x faster                                              |
| fannkuch                 | 532 ms                                                 | 391 ms: 1.36x faster                                              |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.82 ms: 1.34x faster                                             |
| 2to3                     | 348 ms                                                 | 265 ms: 1.31x faster                                              |
| genshi_xml               | 66.0 ms                                                | 50.5 ms: 1.31x faster                                             |
| sympy_integrate          | 25.8 ms                                                | 19.8 ms: 1.31x faster                                             |
| nqueens                  | 106 ms                                                 | 81.5 ms: 1.30x faster                                             |
| json_dumps               | 14.2 ms                                                | 11.0 ms: 1.29x faster                                             |
| sympy_sum                | 196 ms                                                 | 154 ms: 1.28x faster                                              |
| sympy_str                | 346 ms                                                 | 274 ms: 1.26x faster                                              |
| regex_v8                 | 27.8 ms                                                | 22.5 ms: 1.24x faster                                             |
| xml_etree_generate       | 99.4 ms                                                | 80.4 ms: 1.24x faster                                             |
| docutils                 | 3.30 sec                                               | 2.67 sec: 1.23x faster                                            |
| sympy_expand             | 566 ms                                                 | 467 ms: 1.21x faster                                              |
| xml_etree_parse          | 168 ms                                                 | 139 ms: 1.20x faster                                              |
| python_startup           | 14.6 ms                                                | 12.2 ms: 1.20x faster                                             |
| pathlib                  | 20.5 ms                                                | 17.2 ms: 1.19x faster                                             |
| xml_etree_iterparse      | 115 ms                                                 | 98.2 ms: 1.18x faster                                             |
| regex_dna                | 227 ms                                                 | 202 ms: 1.12x faster                                              |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                              |
| json_loads               | 31.2 us                                                | 28.3 us: 1.10x faster                                             |
| regex_effbot             | 3.63 ms                                                | 3.32 ms: 1.09x faster                                             |
| json                     | 5.69 ms                                                | 5.24 ms: 1.09x faster                                             |
| sqlite_synth             | 3.02 us                                                | 2.82 us: 1.07x faster                                             |
| async_generators         | 444 ms                                                 | 434 ms: 1.02x faster                                              |
| asyncio_websockets       | 559 ms                                                 | 553 ms: 1.01x faster                                              |
| pidigits                 | 191 ms                                                 | 196 ms: 1.03x slower                                              |
| telco                    | 7.27 ms                                                | 7.63 ms: 1.05x slower                                             |
| coverage                 | 79.4 ms                                                | 88.5 ms: 1.11x slower                                             |
| python_startup_no_site   | 5.93 ms                                                | 6.94 ms: 1.17x slower                                             |
| gc_traversal             | 3.62 ms                                                | 4.91 ms: 1.36x slower                                             |
| create_gc_cycles         | 1.62 ms                                                | 2.60 ms: 1.61x slower                                             |
| Geometric mean           | (ref)                                                  | 1.49x faster                                                      |
Ignored benchmarks (23) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250701-3.15.0a0-b88f481-JIT/bm-20250701-linux-x86_64-brandtbucher-jit_up_7_6-3.15.0a0-b88f481.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.486x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.39x
- 95% likely to have a speedup of 1.37x
- 99% likely to have a speedup of 1.34x

# Memory
- memory change: 1.36x