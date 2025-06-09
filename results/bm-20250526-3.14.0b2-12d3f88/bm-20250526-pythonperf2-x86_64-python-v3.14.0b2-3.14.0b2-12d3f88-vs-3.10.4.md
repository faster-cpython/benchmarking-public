# Results vs. 3.10.4

- fork: python
- ref: v3.14.0b2
- machine: linux-x86_64
- commit hash: 12d3f88
- commit date: 2025-05-26
- overall geometric mean: 1.353x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: 1.32x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250526-pythonperf2-x86_64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 284 ms: 1.23x faster                                             |
| docutils       | 3.41 sec                                                     | 2.90 sec: 1.18x faster                                           |
| html5lib       | 94.6 ms                                                      | 66.8 ms: 1.42x faster                                            |
| Geometric mean | (ref)                                                        | 1.27x faster                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250526-pythonperf2-x86_64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 626 ms: 2.55x faster                                             |
| async_tree_memoization  | 819 ms                                                       | 332 ms: 2.47x faster                                             |
| async_tree_none         | 692 ms                                                       | 286 ms: 2.41x faster                                             |
| async_tree_cpu_io_mixed | 936 ms                                                       | 506 ms: 1.85x faster                                             |
| Geometric mean          | (ref)                                                        | 2.30x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250526-pythonperf2-x86_64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 111 ms                                                       | 69.0 ms: 1.61x faster                                            |
| nbody          | 134 ms                                                       | 94.6 ms: 1.42x faster                                            |
| pidigits       | 271 ms                                                       | 257 ms: 1.05x faster                                             |
| Geometric mean | (ref)                                                        | 1.34x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250526-pythonperf2-x86_64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 133 ms: 1.43x faster                                             |
| regex_v8       | 27.2 ms                                                      | 24.3 ms: 1.12x faster                                            |
| regex_dna      | 261 ms                                                       | 235 ms: 1.11x faster                                             |
| regex_effbot   | 3.09 ms                                                      | 3.46 ms: 1.12x slower                                            |
| Geometric mean | (ref)                                                        | 1.12x faster                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250526-pythonperf2-x86_64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 211 us: 1.48x faster                                             |
| tomli_loads          | 2.92 sec                                                     | 2.08 sec: 1.40x faster                                           |
| pickle_pure_python   | 455 us                                                       | 333 us: 1.37x faster                                             |
| xml_etree_process    | 75.9 ms                                                      | 59.3 ms: 1.28x faster                                            |
| json_dumps           | 14.5 ms                                                      | 11.4 ms: 1.28x faster                                            |
| xml_etree_parse      | 160 ms                                                       | 138 ms: 1.16x faster                                             |
| xml_etree_iterparse  | 110 ms                                                       | 96.9 ms: 1.14x faster                                            |
| json_loads           | 30.3 us                                                      | 27.1 us: 1.12x faster                                            |
| xml_etree_generate   | 92.3 ms                                                      | 86.2 ms: 1.07x faster                                            |
| Geometric mean       | (ref)                                                        | 1.25x faster                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250526-pythonperf2-x86_64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 8.79 ms: 1.20x slower                                            |
| python_startup         | 11.5 ms                                                      | 16.3 ms: 1.41x slower                                            |
| Geometric mean         | (ref)                                                        | 1.30x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250526-pythonperf2-x86_64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 36.0 ms: 1.39x faster                                            |
| mako            | 14.7 ms                                                      | 10.8 ms: 1.37x faster                                            |
| genshi_text     | 31.4 ms                                                      | 23.5 ms: 1.34x faster                                            |
| genshi_xml      | 63.3 ms                                                      | 53.8 ms: 1.18x faster                                            |
| Geometric mean  | (ref)                                                        | 1.31x faster                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250526-pythonperf2-x86_64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 178 us: 3.02x faster                                             |
| async_tree_io            | 1.60 sec                                                     | 626 ms: 2.55x faster                                             |
| async_tree_memoization   | 819 ms                                                       | 332 ms: 2.47x faster                                             |
| async_tree_none          | 692 ms                                                       | 286 ms: 2.41x faster                                             |
| deltablue                | 7.50 ms                                                      | 3.12 ms: 2.41x faster                                            |
| mdp                      | 3.01 sec                                                     | 1.31 sec: 2.29x faster                                           |
| go                       | 262 ms                                                       | 123 ms: 2.12x faster                                             |
| generators               | 57.3 ms                                                      | 28.9 ms: 1.99x faster                                            |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 506 ms: 1.85x faster                                             |
| chaos                    | 109 ms                                                       | 60.1 ms: 1.81x faster                                            |
| deepcopy_memo            | 49.8 us                                                      | 27.9 us: 1.79x faster                                            |
| richards_super           | 90.6 ms                                                      | 51.2 ms: 1.77x faster                                            |
| pylint                   | 566 ms                                                       | 326 ms: 1.74x faster                                             |
| scimark_lu               | 167 ms                                                       | 96.7 ms: 1.73x faster                                            |
| scimark_monte_carlo      | 107 ms                                                       | 62.4 ms: 1.72x faster                                            |
| pyflate                  | 733 ms                                                       | 426 ms: 1.72x faster                                             |
| raytrace                 | 489 ms                                                       | 285 ms: 1.72x faster                                             |
| deepcopy                 | 468 us                                                       | 278 us: 1.68x faster                                             |
| scimark_sor              | 180 ms                                                       | 108 ms: 1.67x faster                                             |
| richards                 | 75.1 ms                                                      | 44.9 ms: 1.67x faster                                            |
| float                    | 111 ms                                                       | 69.0 ms: 1.61x faster                                            |
| hexiom                   | 9.42 ms                                                      | 5.97 ms: 1.58x faster                                            |
| comprehensions           | 26.7 us                                                      | 17.3 us: 1.54x faster                                            |
| crypto_pyaes             | 119 ms                                                       | 78.3 ms: 1.52x faster                                            |
| spectral_norm            | 139 ms                                                       | 92.7 ms: 1.50x faster                                            |
| unpickle_pure_python     | 312 us                                                       | 211 us: 1.48x faster                                             |
| regex_compile            | 190 ms                                                       | 133 ms: 1.43x faster                                             |
| nbody                    | 134 ms                                                       | 94.6 ms: 1.42x faster                                            |
| html5lib                 | 94.6 ms                                                      | 66.8 ms: 1.42x faster                                            |
| tomli_loads              | 2.92 sec                                                     | 2.08 sec: 1.40x faster                                           |
| django_template          | 50.2 ms                                                      | 36.0 ms: 1.39x faster                                            |
| pprint_pformat           | 2.15 sec                                                     | 1.57 sec: 1.37x faster                                           |
| pickle_pure_python       | 455 us                                                       | 333 us: 1.37x faster                                             |
| mako                     | 14.7 ms                                                      | 10.8 ms: 1.37x faster                                            |
| pycparser                | 1.67 sec                                                     | 1.23 sec: 1.36x faster                                           |
| pprint_safe_repr         | 1.05 sec                                                     | 775 ms: 1.35x faster                                             |
| deepcopy_reduce          | 4.01 us                                                      | 2.96 us: 1.35x faster                                            |
| logging_simple           | 8.88 us                                                      | 6.61 us: 1.34x faster                                            |
| coroutines               | 30.3 ms                                                      | 22.6 ms: 1.34x faster                                            |
| genshi_text              | 31.4 ms                                                      | 23.5 ms: 1.34x faster                                            |
| dulwich_log              | 81.1 ms                                                      | 61.9 ms: 1.31x faster                                            |
| fannkuch                 | 483 ms                                                       | 369 ms: 1.31x faster                                             |
| logging_format           | 9.64 us                                                      | 7.41 us: 1.30x faster                                            |
| xml_etree_process        | 75.9 ms                                                      | 59.3 ms: 1.28x faster                                            |
| sympy_sum                | 193 ms                                                       | 151 ms: 1.28x faster                                             |
| json_dumps               | 14.5 ms                                                      | 11.4 ms: 1.28x faster                                            |
| sympy_integrate          | 28.2 ms                                                      | 22.2 ms: 1.27x faster                                            |
| sqlalchemy_declarative   | 190 ms                                                       | 151 ms: 1.26x faster                                             |
| pathlib                  | 21.4 ms                                                      | 17.1 ms: 1.25x faster                                            |
| nqueens                  | 115 ms                                                       | 92.0 ms: 1.25x faster                                            |
| sympy_str                | 360 ms                                                       | 290 ms: 1.24x faster                                             |
| 2to3                     | 350 ms                                                       | 284 ms: 1.23x faster                                             |
| sympy_expand             | 600 ms                                                       | 496 ms: 1.21x faster                                             |
| sqlalchemy_imperative    | 22.7 ms                                                      | 19.0 ms: 1.20x faster                                            |
| genshi_xml               | 63.3 ms                                                      | 53.8 ms: 1.18x faster                                            |
| docutils                 | 3.41 sec                                                     | 2.90 sec: 1.18x faster                                           |
| scimark_fft              | 361 ms                                                       | 308 ms: 1.17x faster                                             |
| xml_etree_parse          | 160 ms                                                       | 138 ms: 1.16x faster                                             |
| xml_etree_iterparse      | 110 ms                                                       | 96.9 ms: 1.14x faster                                            |
| json_loads               | 30.3 us                                                      | 27.1 us: 1.12x faster                                            |
| regex_v8                 | 27.2 ms                                                      | 24.3 ms: 1.12x faster                                            |
| meteor_contest           | 138 ms                                                       | 124 ms: 1.11x faster                                             |
| regex_dna                | 261 ms                                                       | 235 ms: 1.11x faster                                             |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.70 ms: 1.08x faster                                            |
| xml_etree_generate       | 92.3 ms                                                      | 86.2 ms: 1.07x faster                                            |
| json                     | 5.86 ms                                                      | 5.57 ms: 1.05x faster                                            |
| pidigits                 | 271 ms                                                       | 257 ms: 1.05x faster                                             |
| sqlite_synth             | 2.99 us                                                      | 2.91 us: 1.03x faster                                            |
| asyncio_websockets       | 390 ms                                                       | 382 ms: 1.02x faster                                             |
| async_generators         | 421 ms                                                       | 433 ms: 1.03x slower                                             |
| telco                    | 7.23 ms                                                      | 7.84 ms: 1.08x slower                                            |
| regex_effbot             | 3.09 ms                                                      | 3.46 ms: 1.12x slower                                            |
| python_startup_no_site   | 7.33 ms                                                      | 8.79 ms: 1.20x slower                                            |
| coverage                 | 63.3 ms                                                      | 85.6 ms: 1.35x slower                                            |
| python_startup           | 11.5 ms                                                      | 16.3 ms: 1.41x slower                                            |
| create_gc_cycles         | 1.76 ms                                                      | 2.81 ms: 1.59x slower                                            |
| gc_traversal             | 3.42 ms                                                      | 6.21 ms: 1.82x slower                                            |
| logging_silent           | 167 ns                                                       | 518 ns: 3.10x slower                                             |
| Geometric mean           | (ref)                                                        | 1.33x faster                                                     |
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250526-3.14.0b2-12d3f88/bm-20250526-pythonperf2-x86_64-python-v3.14.0b2-3.14.0b2-12d3f88.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.353x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: 1.32x