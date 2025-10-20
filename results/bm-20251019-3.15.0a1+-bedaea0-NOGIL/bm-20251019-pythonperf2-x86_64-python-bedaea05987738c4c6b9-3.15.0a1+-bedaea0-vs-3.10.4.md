# Results vs. 3.10.4

- fork: python
- ref: bedaea05987738c4c6b9
- machine: linux-x86_64
- commit hash: bedaea0
- commit date: 2025-10-19
- overall geometric mean: 1.213x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x faster
- Memory change: 1.69x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 313 ms: 1.12x faster                                                         |
| docutils       | 3.41 sec                                                     | 2.86 sec: 1.19x faster                                                       |
| html5lib       | 94.6 ms                                                      | 70.4 ms: 1.34x faster                                                        |
| Geometric mean | (ref)                                                        | 1.22x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 555 ms: 2.88x faster                                                         |
| async_tree_none         | 692 ms                                                       | 261 ms: 2.65x faster                                                         |
| async_tree_memoization  | 819 ms                                                       | 318 ms: 2.58x faster                                                         |
| async_tree_cpu_io_mixed | 936 ms                                                       | 491 ms: 1.91x faster                                                         |
| Geometric mean          | (ref)                                                        | 2.48x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 71.5 ms: 1.55x faster                                                        |
| nbody          | 134 ms                                                       | 124 ms: 1.08x faster                                                         |
| pidigits       | 271 ms                                                       | 251 ms: 1.08x faster                                                         |
| Geometric mean | (ref)                                                        | 1.22x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 153 ms: 1.24x faster                                                         |
| regex_dna      | 261 ms                                                       | 219 ms: 1.19x faster                                                         |
| regex_v8       | 27.2 ms                                                      | 23.1 ms: 1.18x faster                                                        |
| regex_effbot   | 3.09 ms                                                      | 3.36 ms: 1.09x slower                                                        |
| Geometric mean | (ref)                                                        | 1.12x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.92 sec                                                     | 2.16 sec: 1.35x faster                                                       |
| unpickle_pure_python | 312 us                                                       | 237 us: 1.32x faster                                                         |
| pickle_pure_python   | 455 us                                                       | 360 us: 1.26x faster                                                         |
| json_dumps           | 14.5 ms                                                      | 11.5 ms: 1.26x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 88.4 ms: 1.25x faster                                                        |
| xml_etree_parse      | 160 ms                                                       | 139 ms: 1.16x faster                                                         |
| xml_etree_process    | 75.9 ms                                                      | 69.3 ms: 1.10x faster                                                        |
| json_loads           | 30.3 us                                                      | 28.0 us: 1.08x faster                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 97.3 ms: 1.05x slower                                                        |
| pickle_dict          | 29.5 us                                                      | 34.0 us: 1.15x slower                                                        |
| unpickle_list        | 4.65 us                                                      | 5.64 us: 1.21x slower                                                        |
| pickle               | 9.89 us                                                      | 12.1 us: 1.22x slower                                                        |
| unpickle             | 13.5 us                                                      | 16.5 us: 1.22x slower                                                        |
| pickle_list          | 4.12 us                                                      | 5.08 us: 1.23x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.04x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 11.7 ms: 1.60x slower                                                        |
| python_startup         | 11.5 ms                                                      | 19.1 ms: 1.66x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.63x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 43.7 ms: 1.15x faster                                                        |
| genshi_text     | 31.4 ms                                                      | 29.9 ms: 1.05x faster                                                        |
| genshi_xml      | 63.3 ms                                                      | 66.0 ms: 1.04x slower                                                        |
| mako            | 14.7 ms                                                      | 17.3 ms: 1.17x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.00x slower                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io            | 1.60 sec                                                     | 555 ms: 2.88x faster                                                         |
| async_tree_none          | 692 ms                                                       | 261 ms: 2.65x faster                                                         |
| typing_runtime_protocols | 537 us                                                       | 203 us: 2.64x faster                                                         |
| async_tree_memoization   | 819 ms                                                       | 318 ms: 2.58x faster                                                         |
| deltablue                | 7.50 ms                                                      | 3.61 ms: 2.08x faster                                                        |
| mdp                      | 3.01 sec                                                     | 1.45 sec: 2.08x faster                                                       |
| asyncio_tcp              | 779 ms                                                       | 381 ms: 2.04x faster                                                         |
| generators               | 57.3 ms                                                      | 29.8 ms: 1.92x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 491 ms: 1.91x faster                                                         |
| go                       | 262 ms                                                       | 139 ms: 1.88x faster                                                         |
| logging_silent           | 167 ns                                                       | 97.1 ns: 1.72x faster                                                        |
| pylint                   | 566 ms                                                       | 335 ms: 1.69x faster                                                         |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.88 sec: 1.65x faster                                                       |
| deepcopy_memo            | 49.8 us                                                      | 30.3 us: 1.64x faster                                                        |
| chaos                    | 109 ms                                                       | 66.7 ms: 1.63x faster                                                        |
| deepcopy                 | 468 us                                                       | 294 us: 1.59x faster                                                         |
| float                    | 111 ms                                                       | 71.5 ms: 1.55x faster                                                        |
| pyflate                  | 733 ms                                                       | 472 ms: 1.55x faster                                                         |
| raytrace                 | 489 ms                                                       | 315 ms: 1.55x faster                                                         |
| gc_traversal             | 3.42 ms                                                      | 2.20 ms: 1.55x faster                                                        |
| scimark_sor              | 180 ms                                                       | 117 ms: 1.55x faster                                                         |
| comprehensions           | 26.7 us                                                      | 18.1 us: 1.48x faster                                                        |
| hexiom                   | 9.42 ms                                                      | 6.51 ms: 1.45x faster                                                        |
| scimark_lu               | 167 ms                                                       | 116 ms: 1.43x faster                                                         |
| richards_super           | 90.6 ms                                                      | 63.8 ms: 1.42x faster                                                        |
| pathlib                  | 21.4 ms                                                      | 15.4 ms: 1.39x faster                                                        |
| spectral_norm            | 139 ms                                                       | 101 ms: 1.38x faster                                                         |
| richards                 | 75.1 ms                                                      | 55.4 ms: 1.36x faster                                                        |
| coroutines               | 30.3 ms                                                      | 22.4 ms: 1.35x faster                                                        |
| tomli_loads              | 2.92 sec                                                     | 2.16 sec: 1.35x faster                                                       |
| pycparser                | 1.67 sec                                                     | 1.24 sec: 1.35x faster                                                       |
| html5lib                 | 94.6 ms                                                      | 70.4 ms: 1.34x faster                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 81.2 ms: 1.32x faster                                                        |
| unpickle_pure_python     | 312 us                                                       | 237 us: 1.32x faster                                                         |
| dulwich_log              | 81.1 ms                                                      | 61.7 ms: 1.31x faster                                                        |
| logging_simple           | 8.88 us                                                      | 6.90 us: 1.29x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 93.4 ms: 1.28x faster                                                        |
| pickle_pure_python       | 455 us                                                       | 360 us: 1.26x faster                                                         |
| json_dumps               | 14.5 ms                                                      | 11.5 ms: 1.26x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 88.4 ms: 1.25x faster                                                        |
| regex_compile            | 190 ms                                                       | 153 ms: 1.24x faster                                                         |
| logging_format           | 9.64 us                                                      | 7.78 us: 1.24x faster                                                        |
| deepcopy_reduce          | 4.01 us                                                      | 3.32 us: 1.21x faster                                                        |
| docutils                 | 3.41 sec                                                     | 2.86 sec: 1.19x faster                                                       |
| regex_dna                | 261 ms                                                       | 219 ms: 1.19x faster                                                         |
| pprint_safe_repr         | 1.05 sec                                                     | 887 ms: 1.18x faster                                                         |
| thrift                   | 1.18 ms                                                      | 993 us: 1.18x faster                                                         |
| pprint_pformat           | 2.15 sec                                                     | 1.83 sec: 1.18x faster                                                       |
| regex_v8                 | 27.2 ms                                                      | 23.1 ms: 1.18x faster                                                        |
| sqlite_synth             | 2.99 us                                                      | 2.56 us: 1.17x faster                                                        |
| xml_etree_parse          | 160 ms                                                       | 139 ms: 1.16x faster                                                         |
| django_template          | 50.2 ms                                                      | 43.7 ms: 1.15x faster                                                        |
| sympy_sum                | 193 ms                                                       | 169 ms: 1.14x faster                                                         |
| scimark_fft              | 361 ms                                                       | 317 ms: 1.14x faster                                                         |
| sympy_integrate          | 28.2 ms                                                      | 24.9 ms: 1.13x faster                                                        |
| 2to3                     | 350 ms                                                       | 313 ms: 1.12x faster                                                         |
| sympy_str                | 360 ms                                                       | 323 ms: 1.11x faster                                                         |
| unpack_sequence          | 59.9 ns                                                      | 54.2 ns: 1.11x faster                                                        |
| xml_etree_process        | 75.9 ms                                                      | 69.3 ms: 1.10x faster                                                        |
| sympy_expand             | 600 ms                                                       | 550 ms: 1.09x faster                                                         |
| json_loads               | 30.3 us                                                      | 28.0 us: 1.08x faster                                                        |
| nbody                    | 134 ms                                                       | 124 ms: 1.08x faster                                                         |
| pidigits                 | 271 ms                                                       | 251 ms: 1.08x faster                                                         |
| nqueens                  | 115 ms                                                       | 107 ms: 1.07x faster                                                         |
| json                     | 5.86 ms                                                      | 5.52 ms: 1.06x faster                                                        |
| asyncio_websockets       | 390 ms                                                       | 370 ms: 1.05x faster                                                         |
| genshi_text              | 31.4 ms                                                      | 29.9 ms: 1.05x faster                                                        |
| fannkuch                 | 483 ms                                                       | 460 ms: 1.05x faster                                                         |
| genshi_xml               | 63.3 ms                                                      | 66.0 ms: 1.04x slower                                                        |
| meteor_contest           | 138 ms                                                       | 146 ms: 1.05x slower                                                         |
| xml_etree_generate       | 92.3 ms                                                      | 97.3 ms: 1.05x slower                                                        |
| regex_effbot             | 3.09 ms                                                      | 3.36 ms: 1.09x slower                                                        |
| create_gc_cycles         | 1.76 ms                                                      | 1.97 ms: 1.12x slower                                                        |
| async_generators         | 421 ms                                                       | 474 ms: 1.13x slower                                                         |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 5.76 ms: 1.13x slower                                                        |
| pickle_dict              | 29.5 us                                                      | 34.0 us: 1.15x slower                                                        |
| mako                     | 14.7 ms                                                      | 17.3 ms: 1.17x slower                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 1.34 ms: 1.18x slower                                                        |
| unpickle_list            | 4.65 us                                                      | 5.64 us: 1.21x slower                                                        |
| pickle                   | 9.89 us                                                      | 12.1 us: 1.22x slower                                                        |
| unpickle                 | 13.5 us                                                      | 16.5 us: 1.22x slower                                                        |
| pickle_list              | 4.12 us                                                      | 5.08 us: 1.23x slower                                                        |
| python_startup_no_site   | 7.33 ms                                                      | 11.7 ms: 1.60x slower                                                        |
| python_startup           | 11.5 ms                                                      | 19.1 ms: 1.66x slower                                                        |
| coverage                 | 63.3 ms                                                      | 119 ms: 1.88x slower                                                         |
| telco                    | 7.23 ms                                                      | 168 ms: 23.27x slower                                                        |
| Geometric mean           | (ref)                                                        | 1.20x faster                                                                 |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (15) of results/bm-20251019-3.15.0a1+-bedaea0-NOGIL/bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.213x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.17x
- 99% likely to have a speedup of 1.14x

# Memory
- memory change: 1.69x