# Results vs. 3.10.4

- fork: brandtbucher
- ref: jit_oz
- machine: linux-x86_64
- commit hash: 6448067
- commit date: 2025-06-28
- overall geometric mean: 1.356x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: 1.39x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250628-pythonperf2-x86_64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 286 ms: 1.22x faster                                                |
| docutils       | 3.41 sec                                                     | 2.91 sec: 1.17x faster                                              |
| html5lib       | 94.6 ms                                                      | 68.2 ms: 1.39x faster                                               |
| Geometric mean | (ref)                                                        | 1.26x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250628-pythonperf2-x86_64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|-------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 627 ms: 2.55x faster                                                |
| async_tree_memoization  | 819 ms                                                       | 332 ms: 2.47x faster                                                |
| async_tree_none         | 692 ms                                                       | 284 ms: 2.44x faster                                                |
| async_tree_cpu_io_mixed | 936 ms                                                       | 503 ms: 1.86x faster                                                |
| Geometric mean          | (ref)                                                        | 2.31x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250628-pythonperf2-x86_64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 111 ms                                                       | 66.0 ms: 1.68x faster                                               |
| nbody          | 134 ms                                                       | 102 ms: 1.31x faster                                                |
| pidigits       | 271 ms                                                       | 258 ms: 1.05x faster                                                |
| Geometric mean | (ref)                                                        | 1.32x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250628-pythonperf2-x86_64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 137 ms: 1.39x faster                                                |
| regex_dna      | 261 ms                                                       | 220 ms: 1.19x faster                                                |
| regex_v8       | 27.2 ms                                                      | 23.0 ms: 1.18x faster                                               |
| regex_effbot   | 3.09 ms                                                      | 3.49 ms: 1.13x slower                                               |
| Geometric mean | (ref)                                                        | 1.14x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250628-pythonperf2-x86_64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 215 us: 1.45x faster                                                |
| tomli_loads          | 2.92 sec                                                     | 2.11 sec: 1.38x faster                                              |
| pickle_pure_python   | 455 us                                                       | 340 us: 1.34x faster                                                |
| xml_etree_process    | 75.9 ms                                                      | 58.0 ms: 1.31x faster                                               |
| json_dumps           | 14.5 ms                                                      | 11.2 ms: 1.30x faster                                               |
| json_loads           | 30.3 us                                                      | 25.1 us: 1.21x faster                                               |
| xml_etree_parse      | 160 ms                                                       | 136 ms: 1.18x faster                                                |
| xml_etree_iterparse  | 110 ms                                                       | 95.9 ms: 1.15x faster                                               |
| xml_etree_generate   | 92.3 ms                                                      | 82.9 ms: 1.11x faster                                               |
| Geometric mean       | (ref)                                                        | 1.26x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250628-pythonperf2-x86_64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 8.85 ms: 1.21x slower                                               |
| python_startup         | 11.5 ms                                                      | 15.3 ms: 1.33x slower                                               |
| Geometric mean         | (ref)                                                        | 1.27x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250628-pythonperf2-x86_64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 36.2 ms: 1.39x faster                                               |
| genshi_text     | 31.4 ms                                                      | 23.0 ms: 1.36x faster                                               |
| mako            | 14.7 ms                                                      | 11.0 ms: 1.34x faster                                               |
| genshi_xml      | 63.3 ms                                                      | 55.4 ms: 1.14x faster                                               |
| Geometric mean  | (ref)                                                        | 1.30x faster                                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250628-pythonperf2-x86_64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|--------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 172 us: 3.12x faster                                                |
| async_tree_io            | 1.60 sec                                                     | 627 ms: 2.55x faster                                                |
| deltablue                | 7.50 ms                                                      | 3.01 ms: 2.49x faster                                               |
| async_tree_memoization   | 819 ms                                                       | 332 ms: 2.47x faster                                                |
| async_tree_none          | 692 ms                                                       | 284 ms: 2.44x faster                                                |
| mdp                      | 3.01 sec                                                     | 1.31 sec: 2.29x faster                                              |
| richards_super           | 90.6 ms                                                      | 41.8 ms: 2.17x faster                                               |
| richards                 | 75.1 ms                                                      | 35.8 ms: 2.10x faster                                               |
| go                       | 262 ms                                                       | 131 ms: 1.99x faster                                                |
| generators               | 57.3 ms                                                      | 29.5 ms: 1.94x faster                                               |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 503 ms: 1.86x faster                                                |
| chaos                    | 109 ms                                                       | 59.6 ms: 1.82x faster                                               |
| logging_silent           | 167 ns                                                       | 94.4 ns: 1.77x faster                                               |
| deepcopy_memo            | 49.8 us                                                      | 28.3 us: 1.76x faster                                               |
| scimark_sor              | 180 ms                                                       | 103 ms: 1.76x faster                                                |
| pylint                   | 566 ms                                                       | 322 ms: 1.76x faster                                                |
| scimark_lu               | 167 ms                                                       | 95.7 ms: 1.74x faster                                               |
| pyflate                  | 733 ms                                                       | 425 ms: 1.72x faster                                                |
| raytrace                 | 489 ms                                                       | 288 ms: 1.70x faster                                                |
| float                    | 111 ms                                                       | 66.0 ms: 1.68x faster                                               |
| scimark_monte_carlo      | 107 ms                                                       | 64.3 ms: 1.67x faster                                               |
| deepcopy                 | 468 us                                                       | 281 us: 1.67x faster                                                |
| logging_simple           | 8.88 us                                                      | 6.05 us: 1.47x faster                                               |
| logging_format           | 9.64 us                                                      | 6.62 us: 1.46x faster                                               |
| comprehensions           | 26.7 us                                                      | 18.4 us: 1.45x faster                                               |
| unpickle_pure_python     | 312 us                                                       | 215 us: 1.45x faster                                                |
| hexiom                   | 9.42 ms                                                      | 6.52 ms: 1.45x faster                                               |
| crypto_pyaes             | 119 ms                                                       | 83.3 ms: 1.43x faster                                               |
| thrift                   | 1.18 ms                                                      | 840 us: 1.40x faster                                                |
| django_template          | 50.2 ms                                                      | 36.2 ms: 1.39x faster                                               |
| regex_compile            | 190 ms                                                       | 137 ms: 1.39x faster                                                |
| html5lib                 | 94.6 ms                                                      | 68.2 ms: 1.39x faster                                               |
| dulwich_log              | 81.1 ms                                                      | 58.7 ms: 1.38x faster                                               |
| tomli_loads              | 2.92 sec                                                     | 2.11 sec: 1.38x faster                                              |
| genshi_text              | 31.4 ms                                                      | 23.0 ms: 1.36x faster                                               |
| spectral_norm            | 139 ms                                                       | 102 ms: 1.36x faster                                                |
| coroutines               | 30.3 ms                                                      | 22.3 ms: 1.36x faster                                               |
| deepcopy_reduce          | 4.01 us                                                      | 2.99 us: 1.34x faster                                               |
| pickle_pure_python       | 455 us                                                       | 340 us: 1.34x faster                                                |
| mako                     | 14.7 ms                                                      | 11.0 ms: 1.34x faster                                               |
| pycparser                | 1.67 sec                                                     | 1.26 sec: 1.33x faster                                              |
| pprint_pformat           | 2.15 sec                                                     | 1.64 sec: 1.32x faster                                              |
| nbody                    | 134 ms                                                       | 102 ms: 1.31x faster                                                |
| xml_etree_process        | 75.9 ms                                                      | 58.0 ms: 1.31x faster                                               |
| pprint_safe_repr         | 1.05 sec                                                     | 808 ms: 1.30x faster                                                |
| json_dumps               | 14.5 ms                                                      | 11.2 ms: 1.30x faster                                               |
| sympy_sum                | 193 ms                                                       | 152 ms: 1.26x faster                                                |
| pathlib                  | 21.4 ms                                                      | 17.0 ms: 1.25x faster                                               |
| sympy_integrate          | 28.2 ms                                                      | 22.5 ms: 1.25x faster                                               |
| sympy_str                | 360 ms                                                       | 292 ms: 1.23x faster                                                |
| 2to3                     | 350 ms                                                       | 286 ms: 1.22x faster                                                |
| json_loads               | 30.3 us                                                      | 25.1 us: 1.21x faster                                               |
| sympy_expand             | 600 ms                                                       | 500 ms: 1.20x faster                                                |
| nqueens                  | 115 ms                                                       | 96.6 ms: 1.19x faster                                               |
| regex_dna                | 261 ms                                                       | 220 ms: 1.19x faster                                                |
| regex_v8                 | 27.2 ms                                                      | 23.0 ms: 1.18x faster                                               |
| xml_etree_parse          | 160 ms                                                       | 136 ms: 1.18x faster                                                |
| docutils                 | 3.41 sec                                                     | 2.91 sec: 1.17x faster                                              |
| xml_etree_iterparse      | 110 ms                                                       | 95.9 ms: 1.15x faster                                               |
| genshi_xml               | 63.3 ms                                                      | 55.4 ms: 1.14x faster                                               |
| xml_etree_generate       | 92.3 ms                                                      | 82.9 ms: 1.11x faster                                               |
| fannkuch                 | 483 ms                                                       | 437 ms: 1.10x faster                                                |
| json                     | 5.86 ms                                                      | 5.31 ms: 1.10x faster                                               |
| meteor_contest           | 138 ms                                                       | 126 ms: 1.10x faster                                                |
| sqlite_synth             | 2.99 us                                                      | 2.81 us: 1.07x faster                                               |
| scimark_fft              | 361 ms                                                       | 343 ms: 1.05x faster                                                |
| pidigits                 | 271 ms                                                       | 258 ms: 1.05x faster                                                |
| asyncio_websockets       | 390 ms                                                       | 386 ms: 1.01x faster                                                |
| async_generators         | 421 ms                                                       | 448 ms: 1.06x slower                                                |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 5.44 ms: 1.07x slower                                               |
| telco                    | 7.23 ms                                                      | 8.14 ms: 1.13x slower                                               |
| regex_effbot             | 3.09 ms                                                      | 3.49 ms: 1.13x slower                                               |
| python_startup_no_site   | 7.33 ms                                                      | 8.85 ms: 1.21x slower                                               |
| coverage                 | 63.3 ms                                                      | 78.9 ms: 1.25x slower                                               |
| python_startup           | 11.5 ms                                                      | 15.3 ms: 1.33x slower                                               |
| create_gc_cycles         | 1.76 ms                                                      | 2.83 ms: 1.61x slower                                               |
| gc_traversal             | 3.42 ms                                                      | 6.47 ms: 1.89x slower                                               |
| Geometric mean           | (ref)                                                        | 1.36x faster                                                        |
Ignored benchmarks (23) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250628-3.15.0a0-6448067-JIT/bm-20250628-pythonperf2-x86_64-brandtbucher-jit_oz-3.15.0a0-6448067.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.356x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: 1.39x