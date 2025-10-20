# Results vs. 3.10.4

- fork: python
- ref: bedaea05987738c4c6b9
- machine: linux-x86_64
- commit hash: bedaea0
- commit date: 2025-10-19
- overall geometric mean: 1.345x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x faster
- Memory change: 1.39x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 277 ms: 1.27x faster                                                         |
| docutils       | 3.41 sec                                                     | 2.83 sec: 1.20x faster                                                       |
| html5lib       | 94.6 ms                                                      | 66.3 ms: 1.43x faster                                                        |
| Geometric mean | (ref)                                                        | 1.30x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 614 ms: 2.60x faster                                                         |
| async_tree_none         | 692 ms                                                       | 269 ms: 2.57x faster                                                         |
| async_tree_memoization  | 819 ms                                                       | 325 ms: 2.52x faster                                                         |
| async_tree_cpu_io_mixed | 936 ms                                                       | 500 ms: 1.87x faster                                                         |
| Geometric mean          | (ref)                                                        | 2.37x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 68.0 ms: 1.64x faster                                                        |
| nbody          | 134 ms                                                       | 96.5 ms: 1.39x faster                                                        |
| pidigits       | 271 ms                                                       | 254 ms: 1.07x faster                                                         |
| Geometric mean | (ref)                                                        | 1.34x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 131 ms: 1.45x faster                                                         |
| regex_dna      | 261 ms                                                       | 218 ms: 1.20x faster                                                         |
| regex_v8       | 27.2 ms                                                      | 23.9 ms: 1.13x faster                                                        |
| regex_effbot   | 3.09 ms                                                      | 3.41 ms: 1.11x slower                                                        |
| Geometric mean | (ref)                                                        | 1.16x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 203 us: 1.54x faster                                                         |
| tomli_loads          | 2.92 sec                                                     | 1.97 sec: 1.48x faster                                                       |
| json_dumps           | 14.5 ms                                                      | 10.2 ms: 1.43x faster                                                        |
| pickle_pure_python   | 455 us                                                       | 324 us: 1.40x faster                                                         |
| xml_etree_process    | 75.9 ms                                                      | 57.9 ms: 1.31x faster                                                        |
| json_loads           | 30.3 us                                                      | 26.4 us: 1.15x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 96.7 ms: 1.14x faster                                                        |
| xml_etree_parse      | 160 ms                                                       | 140 ms: 1.14x faster                                                         |
| xml_etree_generate   | 92.3 ms                                                      | 83.6 ms: 1.10x faster                                                        |
| unpickle_list        | 4.65 us                                                      | 4.98 us: 1.07x slower                                                        |
| unpickle             | 13.5 us                                                      | 15.1 us: 1.12x slower                                                        |
| pickle_dict          | 29.5 us                                                      | 35.1 us: 1.19x slower                                                        |
| pickle_list          | 4.12 us                                                      | 5.03 us: 1.22x slower                                                        |
| pickle               | 9.89 us                                                      | 12.4 us: 1.25x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.11x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 8.84 ms: 1.21x slower                                                        |
| python_startup         | 11.5 ms                                                      | 15.4 ms: 1.34x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.27x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 35.1 ms: 1.43x faster                                                        |
| mako            | 14.7 ms                                                      | 10.7 ms: 1.38x faster                                                        |
| genshi_text     | 31.4 ms                                                      | 23.1 ms: 1.36x faster                                                        |
| genshi_xml      | 63.3 ms                                                      | 54.2 ms: 1.17x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.33x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 166 us: 3.23x faster                                                         |
| async_tree_io            | 1.60 sec                                                     | 614 ms: 2.60x faster                                                         |
| async_tree_none          | 692 ms                                                       | 269 ms: 2.57x faster                                                         |
| async_tree_memoization   | 819 ms                                                       | 325 ms: 2.52x faster                                                         |
| mdp                      | 3.01 sec                                                     | 1.25 sec: 2.40x faster                                                       |
| deltablue                | 7.50 ms                                                      | 3.14 ms: 2.39x faster                                                        |
| go                       | 262 ms                                                       | 116 ms: 2.25x faster                                                         |
| asyncio_tcp              | 779 ms                                                       | 369 ms: 2.11x faster                                                         |
| generators               | 57.3 ms                                                      | 28.4 ms: 2.02x faster                                                        |
| deepcopy_memo            | 49.8 us                                                      | 24.8 us: 2.00x faster                                                        |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.96x faster                                                       |
| chaos                    | 109 ms                                                       | 57.8 ms: 1.88x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 500 ms: 1.87x faster                                                         |
| scimark_monte_carlo      | 107 ms                                                       | 58.2 ms: 1.85x faster                                                        |
| pyflate                  | 733 ms                                                       | 399 ms: 1.84x faster                                                         |
| deepcopy                 | 468 us                                                       | 257 us: 1.82x faster                                                         |
| logging_silent           | 167 ns                                                       | 92.7 ns: 1.81x faster                                                        |
| scimark_lu               | 167 ms                                                       | 92.7 ms: 1.80x faster                                                        |
| richards_super           | 90.6 ms                                                      | 50.4 ms: 1.80x faster                                                        |
| raytrace                 | 489 ms                                                       | 274 ms: 1.78x faster                                                         |
| pylint                   | 566 ms                                                       | 318 ms: 1.78x faster                                                         |
| scimark_sor              | 180 ms                                                       | 101 ms: 1.78x faster                                                         |
| richards                 | 75.1 ms                                                      | 44.1 ms: 1.70x faster                                                        |
| comprehensions           | 26.7 us                                                      | 16.0 us: 1.67x faster                                                        |
| hexiom                   | 9.42 ms                                                      | 5.72 ms: 1.65x faster                                                        |
| float                    | 111 ms                                                       | 68.0 ms: 1.64x faster                                                        |
| spectral_norm            | 139 ms                                                       | 86.9 ms: 1.60x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 75.9 ms: 1.57x faster                                                        |
| logging_simple           | 8.88 us                                                      | 5.74 us: 1.55x faster                                                        |
| unpickle_pure_python     | 312 us                                                       | 203 us: 1.54x faster                                                         |
| logging_format           | 9.64 us                                                      | 6.37 us: 1.51x faster                                                        |
| tomli_loads              | 2.92 sec                                                     | 1.97 sec: 1.48x faster                                                       |
| regex_compile            | 190 ms                                                       | 131 ms: 1.45x faster                                                         |
| json_dumps               | 14.5 ms                                                      | 10.2 ms: 1.43x faster                                                        |
| django_template          | 50.2 ms                                                      | 35.1 ms: 1.43x faster                                                        |
| html5lib                 | 94.6 ms                                                      | 66.3 ms: 1.43x faster                                                        |
| pathlib                  | 21.4 ms                                                      | 15.0 ms: 1.42x faster                                                        |
| thrift                   | 1.18 ms                                                      | 834 us: 1.41x faster                                                         |
| deepcopy_reduce          | 4.01 us                                                      | 2.85 us: 1.41x faster                                                        |
| pickle_pure_python       | 455 us                                                       | 324 us: 1.40x faster                                                         |
| nbody                    | 134 ms                                                       | 96.5 ms: 1.39x faster                                                        |
| unpack_sequence          | 59.9 ns                                                      | 43.2 ns: 1.39x faster                                                        |
| pprint_safe_repr         | 1.05 sec                                                     | 758 ms: 1.39x faster                                                         |
| pprint_pformat           | 2.15 sec                                                     | 1.55 sec: 1.39x faster                                                       |
| mako                     | 14.7 ms                                                      | 10.7 ms: 1.38x faster                                                        |
| dulwich_log              | 81.1 ms                                                      | 59.0 ms: 1.38x faster                                                        |
| pycparser                | 1.67 sec                                                     | 1.22 sec: 1.37x faster                                                       |
| coroutines               | 30.3 ms                                                      | 22.2 ms: 1.36x faster                                                        |
| genshi_text              | 31.4 ms                                                      | 23.1 ms: 1.36x faster                                                        |
| fannkuch                 | 483 ms                                                       | 358 ms: 1.35x faster                                                         |
| xml_etree_process        | 75.9 ms                                                      | 57.9 ms: 1.31x faster                                                        |
| sympy_sum                | 193 ms                                                       | 148 ms: 1.30x faster                                                         |
| scimark_fft              | 361 ms                                                       | 281 ms: 1.29x faster                                                         |
| sympy_integrate          | 28.2 ms                                                      | 22.0 ms: 1.28x faster                                                        |
| sympy_str                | 360 ms                                                       | 284 ms: 1.27x faster                                                         |
| 2to3                     | 350 ms                                                       | 277 ms: 1.27x faster                                                         |
| bench_thread_pool        | 1.14 ms                                                      | 920 us: 1.24x faster                                                         |
| sympy_expand             | 600 ms                                                       | 485 ms: 1.24x faster                                                         |
| nqueens                  | 115 ms                                                       | 94.0 ms: 1.22x faster                                                        |
| docutils                 | 3.41 sec                                                     | 2.83 sec: 1.20x faster                                                       |
| regex_dna                | 261 ms                                                       | 218 ms: 1.20x faster                                                         |
| genshi_xml               | 63.3 ms                                                      | 54.2 ms: 1.17x faster                                                        |
| meteor_contest           | 138 ms                                                       | 120 ms: 1.15x faster                                                         |
| json_loads               | 30.3 us                                                      | 26.4 us: 1.15x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 96.7 ms: 1.14x faster                                                        |
| xml_etree_parse          | 160 ms                                                       | 140 ms: 1.14x faster                                                         |
| regex_v8                 | 27.2 ms                                                      | 23.9 ms: 1.13x faster                                                        |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.51 ms: 1.13x faster                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 83.6 ms: 1.10x faster                                                        |
| json                     | 5.86 ms                                                      | 5.45 ms: 1.08x faster                                                        |
| pidigits                 | 271 ms                                                       | 254 ms: 1.07x faster                                                         |
| sqlite_synth             | 2.99 us                                                      | 2.84 us: 1.05x faster                                                        |
| async_generators         | 421 ms                                                       | 423 ms: 1.01x slower                                                         |
| asyncio_websockets       | 390 ms                                                       | 410 ms: 1.05x slower                                                         |
| unpickle_list            | 4.65 us                                                      | 4.98 us: 1.07x slower                                                        |
| regex_effbot             | 3.09 ms                                                      | 3.41 ms: 1.11x slower                                                        |
| unpickle                 | 13.5 us                                                      | 15.1 us: 1.12x slower                                                        |
| pickle_dict              | 29.5 us                                                      | 35.1 us: 1.19x slower                                                        |
| python_startup_no_site   | 7.33 ms                                                      | 8.84 ms: 1.21x slower                                                        |
| pickle_list              | 4.12 us                                                      | 5.03 us: 1.22x slower                                                        |
| pickle                   | 9.89 us                                                      | 12.4 us: 1.25x slower                                                        |
| coverage                 | 63.3 ms                                                      | 83.2 ms: 1.32x slower                                                        |
| python_startup           | 11.5 ms                                                      | 15.4 ms: 1.34x slower                                                        |
| create_gc_cycles         | 1.76 ms                                                      | 2.82 ms: 1.60x slower                                                        |
| gc_traversal             | 3.42 ms                                                      | 6.52 ms: 1.91x slower                                                        |
| telco                    | 7.23 ms                                                      | 155 ms: 21.41x slower                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 2.36 sec: 370.61x slower                                                     |
| Geometric mean           | (ref)                                                        | 1.24x faster                                                                 |
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20251019-3.15.0a1+-bedaea0/bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.345x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.28x

# Memory
- memory change: 1.39x