# Results vs. 3.10.4

- fork: faster-cpython
- ref: fast_side_exits
- machine: linux-x86_64
- commit hash: 73832b2
- commit date: 2025-07-08
- overall geometric mean: 1.329x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: 1.40x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250708-pythonperf2-x86_64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 286 ms: 1.22x faster                                                             |
| docutils       | 3.41 sec                                                     | 2.91 sec: 1.17x faster                                                           |
| html5lib       | 94.6 ms                                                      | 66.8 ms: 1.42x faster                                                            |
| Geometric mean | (ref)                                                        | 1.27x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250708-pythonperf2-x86_64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2 |
|-------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 624 ms: 2.56x faster                                                             |
| async_tree_none         | 692 ms                                                       | 275 ms: 2.52x faster                                                             |
| async_tree_memoization  | 819 ms                                                       | 331 ms: 2.47x faster                                                             |
| async_tree_cpu_io_mixed | 936 ms                                                       | 503 ms: 1.86x faster                                                             |
| Geometric mean          | (ref)                                                        | 2.33x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250708-pythonperf2-x86_64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 63.6 ms: 1.75x faster                                                            |
| nbody          | 134 ms                                                       | 99.7 ms: 1.35x faster                                                            |
| pidigits       | 271 ms                                                       | 255 ms: 1.06x faster                                                             |
| Geometric mean | (ref)                                                        | 1.36x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250708-pythonperf2-x86_64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 133 ms: 1.42x faster                                                             |
| regex_dna      | 261 ms                                                       | 225 ms: 1.16x faster                                                             |
| regex_v8       | 27.2 ms                                                      | 23.6 ms: 1.15x faster                                                            |
| regex_effbot   | 3.09 ms                                                      | 3.67 ms: 1.19x slower                                                            |
| Geometric mean | (ref)                                                        | 1.12x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250708-pythonperf2-x86_64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 198 us: 1.58x faster                                                             |
| tomli_loads          | 2.92 sec                                                     | 1.94 sec: 1.50x faster                                                           |
| xml_etree_process    | 75.9 ms                                                      | 55.4 ms: 1.37x faster                                                            |
| pickle_pure_python   | 455 us                                                       | 338 us: 1.35x faster                                                             |
| json_dumps           | 14.5 ms                                                      | 11.1 ms: 1.31x faster                                                            |
| json_loads           | 30.3 us                                                      | 25.2 us: 1.21x faster                                                            |
| xml_etree_parse      | 160 ms                                                       | 134 ms: 1.19x faster                                                             |
| xml_etree_generate   | 92.3 ms                                                      | 78.9 ms: 1.17x faster                                                            |
| xml_etree_iterparse  | 110 ms                                                       | 96.9 ms: 1.14x faster                                                            |
| Geometric mean       | (ref)                                                        | 1.31x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250708-pythonperf2-x86_64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 8.86 ms: 1.21x slower                                                            |
| python_startup         | 11.5 ms                                                      | 15.4 ms: 1.34x slower                                                            |
| Geometric mean         | (ref)                                                        | 1.27x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250708-pythonperf2-x86_64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2 |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.1 ms: 1.46x faster                                                            |
| django_template | 50.2 ms                                                      | 35.4 ms: 1.42x faster                                                            |
| genshi_text     | 31.4 ms                                                      | 23.2 ms: 1.35x faster                                                            |
| genshi_xml      | 63.3 ms                                                      | 54.2 ms: 1.17x faster                                                            |
| Geometric mean  | (ref)                                                        | 1.35x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250708-pythonperf2-x86_64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2 |
|--------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 174 us: 3.08x faster                                                             |
| deltablue                | 7.50 ms                                                      | 2.89 ms: 2.60x faster                                                            |
| async_tree_io            | 1.60 sec                                                     | 624 ms: 2.56x faster                                                             |
| async_tree_none          | 692 ms                                                       | 275 ms: 2.52x faster                                                             |
| async_tree_memoization   | 819 ms                                                       | 331 ms: 2.47x faster                                                             |
| mdp                      | 3.01 sec                                                     | 1.29 sec: 2.33x faster                                                           |
| richards_super           | 90.6 ms                                                      | 40.3 ms: 2.25x faster                                                            |
| richards                 | 75.1 ms                                                      | 34.5 ms: 2.17x faster                                                            |
| go                       | 262 ms                                                       | 127 ms: 2.06x faster                                                             |
| generators               | 57.3 ms                                                      | 28.2 ms: 2.03x faster                                                            |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 503 ms: 1.86x faster                                                             |
| pyflate                  | 733 ms                                                       | 405 ms: 1.81x faster                                                             |
| chaos                    | 109 ms                                                       | 60.4 ms: 1.80x faster                                                            |
| logging_silent           | 167 ns                                                       | 93.3 ns: 1.79x faster                                                            |
| deepcopy_memo            | 49.8 us                                                      | 28.1 us: 1.77x faster                                                            |
| float                    | 111 ms                                                       | 63.6 ms: 1.75x faster                                                            |
| pylint                   | 566 ms                                                       | 325 ms: 1.74x faster                                                             |
| scimark_sor              | 180 ms                                                       | 105 ms: 1.71x faster                                                             |
| spectral_norm            | 139 ms                                                       | 81.3 ms: 1.71x faster                                                            |
| scimark_monte_carlo      | 107 ms                                                       | 63.3 ms: 1.70x faster                                                            |
| deepcopy                 | 468 us                                                       | 281 us: 1.66x faster                                                             |
| raytrace                 | 489 ms                                                       | 294 ms: 1.66x faster                                                             |
| scimark_lu               | 167 ms                                                       | 101 ms: 1.66x faster                                                             |
| unpickle_pure_python     | 312 us                                                       | 198 us: 1.58x faster                                                             |
| crypto_pyaes             | 119 ms                                                       | 77.6 ms: 1.54x faster                                                            |
| hexiom                   | 9.42 ms                                                      | 6.13 ms: 1.54x faster                                                            |
| comprehensions           | 26.7 us                                                      | 17.5 us: 1.53x faster                                                            |
| tomli_loads              | 2.92 sec                                                     | 1.94 sec: 1.50x faster                                                           |
| mako                     | 14.7 ms                                                      | 10.1 ms: 1.46x faster                                                            |
| logging_simple           | 8.88 us                                                      | 6.15 us: 1.44x faster                                                            |
| regex_compile            | 190 ms                                                       | 133 ms: 1.42x faster                                                             |
| logging_format           | 9.64 us                                                      | 6.79 us: 1.42x faster                                                            |
| django_template          | 50.2 ms                                                      | 35.4 ms: 1.42x faster                                                            |
| html5lib                 | 94.6 ms                                                      | 66.8 ms: 1.42x faster                                                            |
| thrift                   | 1.18 ms                                                      | 835 us: 1.41x faster                                                             |
| pprint_pformat           | 2.15 sec                                                     | 1.54 sec: 1.40x faster                                                           |
| xml_etree_process        | 75.9 ms                                                      | 55.4 ms: 1.37x faster                                                            |
| pprint_safe_repr         | 1.05 sec                                                     | 766 ms: 1.37x faster                                                             |
| coroutines               | 30.3 ms                                                      | 22.3 ms: 1.36x faster                                                            |
| dulwich_log              | 81.1 ms                                                      | 59.8 ms: 1.36x faster                                                            |
| genshi_text              | 31.4 ms                                                      | 23.2 ms: 1.35x faster                                                            |
| pickle_pure_python       | 455 us                                                       | 338 us: 1.35x faster                                                             |
| nbody                    | 134 ms                                                       | 99.7 ms: 1.35x faster                                                            |
| deepcopy_reduce          | 4.01 us                                                      | 3.02 us: 1.33x faster                                                            |
| json_dumps               | 14.5 ms                                                      | 11.1 ms: 1.31x faster                                                            |
| sympy_sum                | 193 ms                                                       | 151 ms: 1.28x faster                                                             |
| fannkuch                 | 483 ms                                                       | 383 ms: 1.26x faster                                                             |
| sympy_integrate          | 28.2 ms                                                      | 22.4 ms: 1.26x faster                                                            |
| pathlib                  | 21.4 ms                                                      | 17.0 ms: 1.26x faster                                                            |
| nqueens                  | 115 ms                                                       | 92.5 ms: 1.24x faster                                                            |
| sympy_str                | 360 ms                                                       | 290 ms: 1.24x faster                                                             |
| 2to3                     | 350 ms                                                       | 286 ms: 1.22x faster                                                             |
| sympy_expand             | 600 ms                                                       | 497 ms: 1.21x faster                                                             |
| json_loads               | 30.3 us                                                      | 25.2 us: 1.21x faster                                                            |
| scimark_fft              | 361 ms                                                       | 303 ms: 1.19x faster                                                             |
| xml_etree_parse          | 160 ms                                                       | 134 ms: 1.19x faster                                                             |
| docutils                 | 3.41 sec                                                     | 2.91 sec: 1.17x faster                                                           |
| xml_etree_generate       | 92.3 ms                                                      | 78.9 ms: 1.17x faster                                                            |
| genshi_xml               | 63.3 ms                                                      | 54.2 ms: 1.17x faster                                                            |
| regex_dna                | 261 ms                                                       | 225 ms: 1.16x faster                                                             |
| regex_v8                 | 27.2 ms                                                      | 23.6 ms: 1.15x faster                                                            |
| meteor_contest           | 138 ms                                                       | 121 ms: 1.15x faster                                                             |
| xml_etree_iterparse      | 110 ms                                                       | 96.9 ms: 1.14x faster                                                            |
| json                     | 5.86 ms                                                      | 5.35 ms: 1.10x faster                                                            |
| pidigits                 | 271 ms                                                       | 255 ms: 1.06x faster                                                             |
| sqlite_synth             | 2.99 us                                                      | 2.93 us: 1.02x faster                                                            |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 5.00 ms: 1.02x faster                                                            |
| asyncio_websockets       | 390 ms                                                       | 387 ms: 1.01x faster                                                             |
| async_generators         | 421 ms                                                       | 444 ms: 1.05x slower                                                             |
| regex_effbot             | 3.09 ms                                                      | 3.67 ms: 1.19x slower                                                            |
| python_startup_no_site   | 7.33 ms                                                      | 8.86 ms: 1.21x slower                                                            |
| coverage                 | 63.3 ms                                                      | 80.3 ms: 1.27x slower                                                            |
| python_startup           | 11.5 ms                                                      | 15.4 ms: 1.34x slower                                                            |
| create_gc_cycles         | 1.76 ms                                                      | 2.84 ms: 1.61x slower                                                            |
| gc_traversal             | 3.42 ms                                                      | 6.48 ms: 1.90x slower                                                            |
| telco                    | 7.23 ms                                                      | 160 ms: 22.17x slower                                                            |
| Geometric mean           | (ref)                                                        | 1.33x faster                                                                     |
Ignored benchmarks (24) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, pycparser, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250708-3.15.0a0-73832b2-JIT/bm-20250708-pythonperf2-x86_64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.329x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: 1.40x