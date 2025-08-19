# Results vs. 3.10.4

- fork: faster-cpython
- ref: jit_trampoline
- machine: linux-x86_64
- commit hash: 14080cb
- commit date: 2025-08-19
- overall geometric mean: 1.338x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: 1.40x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250819-pythonperf2-x86_64-faster%2dcpython-jit_trampoline-3.15.0a0-14080cb |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 286 ms: 1.22x faster                                                            |
| docutils       | 3.41 sec                                                     | 2.91 sec: 1.17x faster                                                          |
| html5lib       | 94.6 ms                                                      | 68.1 ms: 1.39x faster                                                           |
| Geometric mean | (ref)                                                        | 1.26x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250819-pythonperf2-x86_64-faster%2dcpython-jit_trampoline-3.15.0a0-14080cb |
|-------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 617 ms: 2.59x faster                                                            |
| async_tree_none         | 692 ms                                                       | 270 ms: 2.56x faster                                                            |
| async_tree_memoization  | 819 ms                                                       | 327 ms: 2.51x faster                                                            |
| async_tree_cpu_io_mixed | 936 ms                                                       | 499 ms: 1.88x faster                                                            |
| Geometric mean          | (ref)                                                        | 2.36x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250819-pythonperf2-x86_64-faster%2dcpython-jit_trampoline-3.15.0a0-14080cb |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 64.0 ms: 1.74x faster                                                           |
| nbody          | 134 ms                                                       | 106 ms: 1.27x faster                                                            |
| pidigits       | 271 ms                                                       | 255 ms: 1.06x faster                                                            |
| Geometric mean | (ref)                                                        | 1.33x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250819-pythonperf2-x86_64-faster%2dcpython-jit_trampoline-3.15.0a0-14080cb |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 133 ms: 1.43x faster                                                            |
| regex_v8       | 27.2 ms                                                      | 23.3 ms: 1.17x faster                                                           |
| regex_dna      | 261 ms                                                       | 228 ms: 1.15x faster                                                            |
| regex_effbot   | 3.09 ms                                                      | 3.58 ms: 1.16x slower                                                           |
| Geometric mean | (ref)                                                        | 1.13x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250819-pythonperf2-x86_64-faster%2dcpython-jit_trampoline-3.15.0a0-14080cb |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 191 us: 1.63x faster                                                            |
| tomli_loads          | 2.92 sec                                                     | 1.92 sec: 1.52x faster                                                          |
| json_dumps           | 14.5 ms                                                      | 10.0 ms: 1.45x faster                                                           |
| pickle_pure_python   | 455 us                                                       | 328 us: 1.39x faster                                                            |
| xml_etree_process    | 75.9 ms                                                      | 55.0 ms: 1.38x faster                                                           |
| json_loads           | 30.3 us                                                      | 25.1 us: 1.21x faster                                                           |
| xml_etree_generate   | 92.3 ms                                                      | 78.4 ms: 1.18x faster                                                           |
| xml_etree_iterparse  | 110 ms                                                       | 98.0 ms: 1.13x faster                                                           |
| xml_etree_parse      | 160 ms                                                       | 143 ms: 1.12x faster                                                            |
| Geometric mean       | (ref)                                                        | 1.32x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250819-pythonperf2-x86_64-faster%2dcpython-jit_trampoline-3.15.0a0-14080cb |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 8.83 ms: 1.21x slower                                                           |
| python_startup         | 11.5 ms                                                      | 15.4 ms: 1.34x slower                                                           |
| Geometric mean         | (ref)                                                        | 1.27x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250819-pythonperf2-x86_64-faster%2dcpython-jit_trampoline-3.15.0a0-14080cb |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.79 ms: 1.50x faster                                                           |
| django_template | 50.2 ms                                                      | 35.0 ms: 1.44x faster                                                           |
| genshi_text     | 31.4 ms                                                      | 23.4 ms: 1.34x faster                                                           |
| genshi_xml      | 63.3 ms                                                      | 56.6 ms: 1.12x faster                                                           |
| Geometric mean  | (ref)                                                        | 1.34x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250819-pythonperf2-x86_64-faster%2dcpython-jit_trampoline-3.15.0a0-14080cb |
|--------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 170 us: 3.15x faster                                                            |
| deltablue                | 7.50 ms                                                      | 2.86 ms: 2.62x faster                                                           |
| async_tree_io            | 1.60 sec                                                     | 617 ms: 2.59x faster                                                            |
| async_tree_none          | 692 ms                                                       | 270 ms: 2.56x faster                                                            |
| async_tree_memoization   | 819 ms                                                       | 327 ms: 2.51x faster                                                            |
| mdp                      | 3.01 sec                                                     | 1.30 sec: 2.31x faster                                                          |
| richards_super           | 90.6 ms                                                      | 39.3 ms: 2.31x faster                                                           |
| richards                 | 75.1 ms                                                      | 34.2 ms: 2.19x faster                                                           |
| go                       | 262 ms                                                       | 124 ms: 2.11x faster                                                            |
| generators               | 57.3 ms                                                      | 30.3 ms: 1.89x faster                                                           |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 499 ms: 1.88x faster                                                            |
| chaos                    | 109 ms                                                       | 59.1 ms: 1.84x faster                                                           |
| logging_silent           | 167 ns                                                       | 91.8 ns: 1.82x faster                                                           |
| spectral_norm            | 139 ms                                                       | 77.6 ms: 1.79x faster                                                           |
| scimark_sor              | 180 ms                                                       | 101 ms: 1.78x faster                                                            |
| deepcopy_memo            | 49.8 us                                                      | 27.9 us: 1.78x faster                                                           |
| pyflate                  | 733 ms                                                       | 414 ms: 1.77x faster                                                            |
| raytrace                 | 489 ms                                                       | 281 ms: 1.74x faster                                                            |
| pylint                   | 566 ms                                                       | 326 ms: 1.74x faster                                                            |
| float                    | 111 ms                                                       | 64.0 ms: 1.74x faster                                                           |
| scimark_monte_carlo      | 107 ms                                                       | 62.2 ms: 1.73x faster                                                           |
| scimark_lu               | 167 ms                                                       | 97.7 ms: 1.71x faster                                                           |
| deepcopy                 | 468 us                                                       | 280 us: 1.67x faster                                                            |
| unpickle_pure_python     | 312 us                                                       | 191 us: 1.63x faster                                                            |
| comprehensions           | 26.7 us                                                      | 17.1 us: 1.56x faster                                                           |
| hexiom                   | 9.42 ms                                                      | 6.06 ms: 1.55x faster                                                           |
| crypto_pyaes             | 119 ms                                                       | 77.0 ms: 1.55x faster                                                           |
| tomli_loads              | 2.92 sec                                                     | 1.92 sec: 1.52x faster                                                          |
| mako                     | 14.7 ms                                                      | 9.79 ms: 1.50x faster                                                           |
| logging_simple           | 8.88 us                                                      | 5.92 us: 1.50x faster                                                           |
| logging_format           | 9.64 us                                                      | 6.52 us: 1.48x faster                                                           |
| pprint_pformat           | 2.15 sec                                                     | 1.48 sec: 1.46x faster                                                          |
| json_dumps               | 14.5 ms                                                      | 10.0 ms: 1.45x faster                                                           |
| django_template          | 50.2 ms                                                      | 35.0 ms: 1.44x faster                                                           |
| regex_compile            | 190 ms                                                       | 133 ms: 1.43x faster                                                            |
| pprint_safe_repr         | 1.05 sec                                                     | 737 ms: 1.42x faster                                                            |
| thrift                   | 1.18 ms                                                      | 842 us: 1.40x faster                                                            |
| html5lib                 | 94.6 ms                                                      | 68.1 ms: 1.39x faster                                                           |
| pickle_pure_python       | 455 us                                                       | 328 us: 1.39x faster                                                            |
| xml_etree_process        | 75.9 ms                                                      | 55.0 ms: 1.38x faster                                                           |
| dulwich_log              | 81.1 ms                                                      | 59.2 ms: 1.37x faster                                                           |
| coroutines               | 30.3 ms                                                      | 22.4 ms: 1.35x faster                                                           |
| genshi_text              | 31.4 ms                                                      | 23.4 ms: 1.34x faster                                                           |
| pycparser                | 1.67 sec                                                     | 1.25 sec: 1.34x faster                                                          |
| deepcopy_reduce          | 4.01 us                                                      | 3.03 us: 1.32x faster                                                           |
| fannkuch                 | 483 ms                                                       | 367 ms: 1.31x faster                                                            |
| sympy_sum                | 193 ms                                                       | 152 ms: 1.27x faster                                                            |
| pathlib                  | 21.4 ms                                                      | 16.8 ms: 1.27x faster                                                           |
| nbody                    | 134 ms                                                       | 106 ms: 1.27x faster                                                            |
| sympy_integrate          | 28.2 ms                                                      | 22.4 ms: 1.26x faster                                                           |
| nqueens                  | 115 ms                                                       | 91.8 ms: 1.25x faster                                                           |
| sympy_str                | 360 ms                                                       | 292 ms: 1.23x faster                                                            |
| 2to3                     | 350 ms                                                       | 286 ms: 1.22x faster                                                            |
| scimark_fft              | 361 ms                                                       | 299 ms: 1.21x faster                                                            |
| json_loads               | 30.3 us                                                      | 25.1 us: 1.21x faster                                                           |
| sympy_expand             | 600 ms                                                       | 502 ms: 1.19x faster                                                            |
| xml_etree_generate       | 92.3 ms                                                      | 78.4 ms: 1.18x faster                                                           |
| docutils                 | 3.41 sec                                                     | 2.91 sec: 1.17x faster                                                          |
| regex_v8                 | 27.2 ms                                                      | 23.3 ms: 1.17x faster                                                           |
| meteor_contest           | 138 ms                                                       | 120 ms: 1.15x faster                                                            |
| regex_dna                | 261 ms                                                       | 228 ms: 1.15x faster                                                            |
| xml_etree_iterparse      | 110 ms                                                       | 98.0 ms: 1.13x faster                                                           |
| xml_etree_parse          | 160 ms                                                       | 143 ms: 1.12x faster                                                            |
| genshi_xml               | 63.3 ms                                                      | 56.6 ms: 1.12x faster                                                           |
| json                     | 5.86 ms                                                      | 5.47 ms: 1.07x faster                                                           |
| pidigits                 | 271 ms                                                       | 255 ms: 1.06x faster                                                            |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.79 ms: 1.06x faster                                                           |
| sqlite_synth             | 2.99 us                                                      | 2.82 us: 1.06x faster                                                           |
| asyncio_websockets       | 390 ms                                                       | 384 ms: 1.02x faster                                                            |
| async_generators         | 421 ms                                                       | 443 ms: 1.05x slower                                                            |
| regex_effbot             | 3.09 ms                                                      | 3.58 ms: 1.16x slower                                                           |
| python_startup_no_site   | 7.33 ms                                                      | 8.83 ms: 1.21x slower                                                           |
| python_startup           | 11.5 ms                                                      | 15.4 ms: 1.34x slower                                                           |
| coverage                 | 63.3 ms                                                      | 86.3 ms: 1.36x slower                                                           |
| create_gc_cycles         | 1.76 ms                                                      | 2.92 ms: 1.65x slower                                                           |
| gc_traversal             | 3.42 ms                                                      | 6.65 ms: 1.95x slower                                                           |
| telco                    | 7.23 ms                                                      | 160 ms: 22.18x slower                                                           |
| Geometric mean           | (ref)                                                        | 1.34x faster                                                                    |
Ignored benchmarks (23) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250819-3.15.0a0-14080cb-JIT/bm-20250819-pythonperf2-x86_64-faster%2dcpython-jit_trampoline-3.15.0a0-14080cb.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.338x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: 1.40x