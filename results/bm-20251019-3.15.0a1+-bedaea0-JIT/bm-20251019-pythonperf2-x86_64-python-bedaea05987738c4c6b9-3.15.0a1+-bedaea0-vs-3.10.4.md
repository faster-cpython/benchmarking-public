# Results vs. 3.10.4

- fork: python
- ref: bedaea05987738c4c6b9
- machine: linux-x86_64
- commit hash: bedaea0
- commit date: 2025-10-19
- overall geometric mean: 1.338x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x faster
- Memory change: 1.41x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 281 ms: 1.24x faster                                                         |
| docutils       | 3.41 sec                                                     | 2.89 sec: 1.18x faster                                                       |
| html5lib       | 94.6 ms                                                      | 64.7 ms: 1.46x faster                                                        |
| Geometric mean | (ref)                                                        | 1.29x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 616 ms: 2.59x faster                                                         |
| async_tree_none         | 692 ms                                                       | 274 ms: 2.53x faster                                                         |
| async_tree_memoization  | 819 ms                                                       | 331 ms: 2.48x faster                                                         |
| async_tree_cpu_io_mixed | 936 ms                                                       | 500 ms: 1.87x faster                                                         |
| Geometric mean          | (ref)                                                        | 2.35x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 69.5 ms: 1.60x faster                                                        |
| nbody          | 134 ms                                                       | 96.9 ms: 1.38x faster                                                        |
| pidigits       | 271 ms                                                       | 255 ms: 1.06x faster                                                         |
| Geometric mean | (ref)                                                        | 1.33x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 133 ms: 1.43x faster                                                         |
| regex_dna      | 261 ms                                                       | 223 ms: 1.17x faster                                                         |
| regex_v8       | 27.2 ms                                                      | 24.0 ms: 1.13x faster                                                        |
| regex_effbot   | 3.09 ms                                                      | 3.40 ms: 1.10x slower                                                        |
| Geometric mean | (ref)                                                        | 1.15x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 194 us: 1.61x faster                                                         |
| tomli_loads          | 2.92 sec                                                     | 1.89 sec: 1.55x faster                                                       |
| json_dumps           | 14.5 ms                                                      | 10.1 ms: 1.44x faster                                                        |
| pickle_pure_python   | 455 us                                                       | 328 us: 1.39x faster                                                         |
| xml_etree_process    | 75.9 ms                                                      | 55.3 ms: 1.37x faster                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 79.4 ms: 1.16x faster                                                        |
| json_loads           | 30.3 us                                                      | 26.4 us: 1.15x faster                                                        |
| xml_etree_parse      | 160 ms                                                       | 140 ms: 1.14x faster                                                         |
| xml_etree_iterparse  | 110 ms                                                       | 98.4 ms: 1.12x faster                                                        |
| unpickle_list        | 4.65 us                                                      | 4.94 us: 1.06x slower                                                        |
| unpickle             | 13.5 us                                                      | 14.6 us: 1.08x slower                                                        |
| pickle_dict          | 29.5 us                                                      | 34.8 us: 1.18x slower                                                        |
| pickle_list          | 4.12 us                                                      | 4.99 us: 1.21x slower                                                        |
| pickle               | 9.89 us                                                      | 12.8 us: 1.30x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.13x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 8.82 ms: 1.20x slower                                                        |
| python_startup         | 11.5 ms                                                      | 15.4 ms: 1.33x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.27x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.82 ms: 1.50x faster                                                        |
| django_template | 50.2 ms                                                      | 34.6 ms: 1.45x faster                                                        |
| genshi_text     | 31.4 ms                                                      | 23.5 ms: 1.34x faster                                                        |
| genshi_xml      | 63.3 ms                                                      | 54.3 ms: 1.17x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.36x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 168 us: 3.20x faster                                                         |
| async_tree_io            | 1.60 sec                                                     | 616 ms: 2.59x faster                                                         |
| async_tree_none          | 692 ms                                                       | 274 ms: 2.53x faster                                                         |
| async_tree_memoization   | 819 ms                                                       | 331 ms: 2.48x faster                                                         |
| deltablue                | 7.50 ms                                                      | 3.16 ms: 2.38x faster                                                        |
| mdp                      | 3.01 sec                                                     | 1.29 sec: 2.33x faster                                                       |
| go                       | 262 ms                                                       | 118 ms: 2.21x faster                                                         |
| asyncio_tcp              | 779 ms                                                       | 370 ms: 2.10x faster                                                         |
| deepcopy_memo            | 49.8 us                                                      | 25.1 us: 1.99x faster                                                        |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.96x faster                                                       |
| generators               | 57.3 ms                                                      | 30.6 ms: 1.87x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 500 ms: 1.87x faster                                                         |
| chaos                    | 109 ms                                                       | 59.2 ms: 1.84x faster                                                        |
| pyflate                  | 733 ms                                                       | 400 ms: 1.83x faster                                                         |
| logging_silent           | 167 ns                                                       | 92.3 ns: 1.81x faster                                                        |
| deepcopy                 | 468 us                                                       | 259 us: 1.81x faster                                                         |
| pylint                   | 566 ms                                                       | 320 ms: 1.77x faster                                                         |
| scimark_lu               | 167 ms                                                       | 94.6 ms: 1.76x faster                                                        |
| richards_super           | 90.6 ms                                                      | 51.8 ms: 1.75x faster                                                        |
| scimark_sor              | 180 ms                                                       | 104 ms: 1.74x faster                                                         |
| raytrace                 | 489 ms                                                       | 281 ms: 1.74x faster                                                         |
| scimark_monte_carlo      | 107 ms                                                       | 62.4 ms: 1.72x faster                                                        |
| richards                 | 75.1 ms                                                      | 44.7 ms: 1.68x faster                                                        |
| unpickle_pure_python     | 312 us                                                       | 194 us: 1.61x faster                                                         |
| hexiom                   | 9.42 ms                                                      | 5.87 ms: 1.60x faster                                                        |
| float                    | 111 ms                                                       | 69.5 ms: 1.60x faster                                                        |
| spectral_norm            | 139 ms                                                       | 87.2 ms: 1.60x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 76.1 ms: 1.57x faster                                                        |
| tomli_loads              | 2.92 sec                                                     | 1.89 sec: 1.55x faster                                                       |
| logging_simple           | 8.88 us                                                      | 5.76 us: 1.54x faster                                                        |
| comprehensions           | 26.7 us                                                      | 17.4 us: 1.53x faster                                                        |
| logging_format           | 9.64 us                                                      | 6.42 us: 1.50x faster                                                        |
| mako                     | 14.7 ms                                                      | 9.82 ms: 1.50x faster                                                        |
| html5lib                 | 94.6 ms                                                      | 64.7 ms: 1.46x faster                                                        |
| pprint_pformat           | 2.15 sec                                                     | 1.48 sec: 1.46x faster                                                       |
| django_template          | 50.2 ms                                                      | 34.6 ms: 1.45x faster                                                        |
| json_dumps               | 14.5 ms                                                      | 10.1 ms: 1.44x faster                                                        |
| pprint_safe_repr         | 1.05 sec                                                     | 730 ms: 1.44x faster                                                         |
| regex_compile            | 190 ms                                                       | 133 ms: 1.43x faster                                                         |
| thrift                   | 1.18 ms                                                      | 834 us: 1.41x faster                                                         |
| deepcopy_reduce          | 4.01 us                                                      | 2.86 us: 1.40x faster                                                        |
| pathlib                  | 21.4 ms                                                      | 15.3 ms: 1.40x faster                                                        |
| pickle_pure_python       | 455 us                                                       | 328 us: 1.39x faster                                                         |
| nbody                    | 134 ms                                                       | 96.9 ms: 1.38x faster                                                        |
| xml_etree_process        | 75.9 ms                                                      | 55.3 ms: 1.37x faster                                                        |
| pycparser                | 1.67 sec                                                     | 1.22 sec: 1.37x faster                                                       |
| dulwich_log              | 81.1 ms                                                      | 60.0 ms: 1.35x faster                                                        |
| coroutines               | 30.3 ms                                                      | 22.6 ms: 1.34x faster                                                        |
| genshi_text              | 31.4 ms                                                      | 23.5 ms: 1.34x faster                                                        |
| fannkuch                 | 483 ms                                                       | 365 ms: 1.32x faster                                                         |
| scimark_fft              | 361 ms                                                       | 278 ms: 1.30x faster                                                         |
| sympy_sum                | 193 ms                                                       | 150 ms: 1.28x faster                                                         |
| sympy_integrate          | 28.2 ms                                                      | 22.2 ms: 1.27x faster                                                        |
| nqueens                  | 115 ms                                                       | 92.4 ms: 1.24x faster                                                        |
| 2to3                     | 350 ms                                                       | 281 ms: 1.24x faster                                                         |
| sympy_str                | 360 ms                                                       | 290 ms: 1.24x faster                                                         |
| bench_thread_pool        | 1.14 ms                                                      | 928 us: 1.23x faster                                                         |
| sympy_expand             | 600 ms                                                       | 497 ms: 1.21x faster                                                         |
| docutils                 | 3.41 sec                                                     | 2.89 sec: 1.18x faster                                                       |
| regex_dna                | 261 ms                                                       | 223 ms: 1.17x faster                                                         |
| genshi_xml               | 63.3 ms                                                      | 54.3 ms: 1.17x faster                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 79.4 ms: 1.16x faster                                                        |
| json_loads               | 30.3 us                                                      | 26.4 us: 1.15x faster                                                        |
| unpack_sequence          | 59.9 ns                                                      | 52.3 ns: 1.15x faster                                                        |
| meteor_contest           | 138 ms                                                       | 121 ms: 1.14x faster                                                         |
| xml_etree_parse          | 160 ms                                                       | 140 ms: 1.14x faster                                                         |
| regex_v8                 | 27.2 ms                                                      | 24.0 ms: 1.13x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 98.4 ms: 1.12x faster                                                        |
| sqlite_synth             | 2.99 us                                                      | 2.77 us: 1.08x faster                                                        |
| json                     | 5.86 ms                                                      | 5.44 ms: 1.08x faster                                                        |
| pidigits                 | 271 ms                                                       | 255 ms: 1.06x faster                                                         |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.85 ms: 1.05x faster                                                        |
| asyncio_websockets       | 390 ms                                                       | 409 ms: 1.05x slower                                                         |
| unpickle_list            | 4.65 us                                                      | 4.94 us: 1.06x slower                                                        |
| async_generators         | 421 ms                                                       | 447 ms: 1.06x slower                                                         |
| unpickle                 | 13.5 us                                                      | 14.6 us: 1.08x slower                                                        |
| regex_effbot             | 3.09 ms                                                      | 3.40 ms: 1.10x slower                                                        |
| pickle_dict              | 29.5 us                                                      | 34.8 us: 1.18x slower                                                        |
| python_startup_no_site   | 7.33 ms                                                      | 8.82 ms: 1.20x slower                                                        |
| pickle_list              | 4.12 us                                                      | 4.99 us: 1.21x slower                                                        |
| coverage                 | 63.3 ms                                                      | 77.8 ms: 1.23x slower                                                        |
| pickle                   | 9.89 us                                                      | 12.8 us: 1.30x slower                                                        |
| python_startup           | 11.5 ms                                                      | 15.4 ms: 1.33x slower                                                        |
| create_gc_cycles         | 1.76 ms                                                      | 2.85 ms: 1.62x slower                                                        |
| gc_traversal             | 3.42 ms                                                      | 6.49 ms: 1.90x slower                                                        |
| telco                    | 7.23 ms                                                      | 157 ms: 21.67x slower                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 2.74 sec: 429.74x slower                                                     |
| Geometric mean           | (ref)                                                        | 1.23x faster                                                                 |
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20251019-3.15.0a1+-bedaea0-JIT/bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.338x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.28x

# Memory
- memory change: 1.41x