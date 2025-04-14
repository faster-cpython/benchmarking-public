# Results vs. 3.10.4

- fork: mdboom
- ref: reorg_pyinterpreterf
- machine: linux-x86_64
- commit hash: 37fd664
- commit date: 2025-03-17
- overall geometric mean: 1.316x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250317-pythonperf2-x86_64-mdboom-reorg_pyinterpreterf-3.14.0a6+-37fd664 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 285 ms: 1.23x faster                                                         |
| docutils       | 3.41 sec                                                     | 2.91 sec: 1.17x faster                                                       |
| html5lib       | 94.6 ms                                                      | 69.4 ms: 1.36x faster                                                        |
| Geometric mean | (ref)                                                        | 1.25x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250317-pythonperf2-x86_64-mdboom-reorg_pyinterpreterf-3.14.0a6+-37fd664 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 645 ms: 2.48x faster                                                         |
| async_tree_none         | 692 ms                                                       | 292 ms: 2.36x faster                                                         |
| async_tree_memoization  | 819 ms                                                       | 351 ms: 2.34x faster                                                         |
| async_tree_cpu_io_mixed | 936 ms                                                       | 523 ms: 1.79x faster                                                         |
| Geometric mean          | (ref)                                                        | 2.22x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250317-pythonperf2-x86_64-mdboom-reorg_pyinterpreterf-3.14.0a6+-37fd664 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 72.9 ms: 1.52x faster                                                        |
| nbody          | 134 ms                                                       | 101 ms: 1.33x faster                                                         |
| pidigits       | 271 ms                                                       | 255 ms: 1.06x faster                                                         |
| Geometric mean | (ref)                                                        | 1.29x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250317-pythonperf2-x86_64-mdboom-reorg_pyinterpreterf-3.14.0a6+-37fd664 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 138 ms: 1.38x faster                                                         |
| regex_v8       | 27.2 ms                                                      | 23.7 ms: 1.15x faster                                                        |
| regex_dna      | 261 ms                                                       | 237 ms: 1.10x faster                                                         |
| regex_effbot   | 3.09 ms                                                      | 3.13 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                        | 1.15x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250317-pythonperf2-x86_64-mdboom-reorg_pyinterpreterf-3.14.0a6+-37fd664 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 225 us: 1.39x faster                                                         |
| pickle_pure_python   | 455 us                                                       | 338 us: 1.35x faster                                                         |
| tomli_loads          | 2.92 sec                                                     | 2.19 sec: 1.33x faster                                                       |
| json_dumps           | 14.5 ms                                                      | 11.4 ms: 1.28x faster                                                        |
| xml_etree_process    | 75.9 ms                                                      | 60.4 ms: 1.26x faster                                                        |
| json_loads           | 30.3 us                                                      | 25.5 us: 1.19x faster                                                        |
| xml_etree_parse      | 160 ms                                                       | 136 ms: 1.18x faster                                                         |
| xml_etree_iterparse  | 110 ms                                                       | 97.4 ms: 1.13x faster                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 85.0 ms: 1.09x faster                                                        |
| Geometric mean       | (ref)                                                        | 1.24x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250317-pythonperf2-x86_64-mdboom-reorg_pyinterpreterf-3.14.0a6+-37fd664 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 16.3 ms: 1.42x slower                                                        |
| python_startup_no_site | 7.33 ms                                                      | 10.5 ms: 1.43x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.42x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250317-pythonperf2-x86_64-mdboom-reorg_pyinterpreterf-3.14.0a6+-37fd664 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 36.8 ms: 1.36x faster                                                        |
| mako            | 14.7 ms                                                      | 11.0 ms: 1.34x faster                                                        |
| genshi_text     | 31.4 ms                                                      | 23.8 ms: 1.32x faster                                                        |
| genshi_xml      | 63.3 ms                                                      | 55.5 ms: 1.14x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.29x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250317-pythonperf2-x86_64-mdboom-reorg_pyinterpreterf-3.14.0a6+-37fd664 |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 168 us: 3.19x faster                                                         |
| async_tree_io            | 1.60 sec                                                     | 645 ms: 2.48x faster                                                         |
| async_tree_none          | 692 ms                                                       | 292 ms: 2.36x faster                                                         |
| async_tree_memoization   | 819 ms                                                       | 351 ms: 2.34x faster                                                         |
| deltablue                | 7.50 ms                                                      | 3.40 ms: 2.20x faster                                                        |
| go                       | 262 ms                                                       | 131 ms: 2.00x faster                                                         |
| generators               | 57.3 ms                                                      | 29.4 ms: 1.95x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 523 ms: 1.79x faster                                                         |
| pylint                   | 566 ms                                                       | 320 ms: 1.77x faster                                                         |
| logging_silent           | 167 ns                                                       | 95.0 ns: 1.76x faster                                                        |
| richards_super           | 90.6 ms                                                      | 53.6 ms: 1.69x faster                                                        |
| scimark_lu               | 167 ms                                                       | 99.1 ms: 1.68x faster                                                        |
| chaos                    | 109 ms                                                       | 64.5 ms: 1.68x faster                                                        |
| deepcopy_memo            | 49.8 us                                                      | 29.6 us: 1.68x faster                                                        |
| raytrace                 | 489 ms                                                       | 298 ms: 1.64x faster                                                         |
| scimark_sor              | 180 ms                                                       | 110 ms: 1.64x faster                                                         |
| pyflate                  | 733 ms                                                       | 452 ms: 1.62x faster                                                         |
| deepcopy                 | 468 us                                                       | 292 us: 1.60x faster                                                         |
| scimark_monte_carlo      | 107 ms                                                       | 68.1 ms: 1.58x faster                                                        |
| richards                 | 75.1 ms                                                      | 48.7 ms: 1.54x faster                                                        |
| float                    | 111 ms                                                       | 72.9 ms: 1.52x faster                                                        |
| spectral_norm            | 139 ms                                                       | 91.7 ms: 1.52x faster                                                        |
| comprehensions           | 26.7 us                                                      | 17.8 us: 1.50x faster                                                        |
| hexiom                   | 9.42 ms                                                      | 6.48 ms: 1.45x faster                                                        |
| coroutines               | 30.3 ms                                                      | 21.1 ms: 1.44x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 83.4 ms: 1.43x faster                                                        |
| unpickle_pure_python     | 312 us                                                       | 225 us: 1.39x faster                                                         |
| logging_simple           | 8.88 us                                                      | 6.41 us: 1.38x faster                                                        |
| regex_compile            | 190 ms                                                       | 138 ms: 1.38x faster                                                         |
| thrift                   | 1.18 ms                                                      | 859 us: 1.37x faster                                                         |
| django_template          | 50.2 ms                                                      | 36.8 ms: 1.36x faster                                                        |
| html5lib                 | 94.6 ms                                                      | 69.4 ms: 1.36x faster                                                        |
| logging_format           | 9.64 us                                                      | 7.13 us: 1.35x faster                                                        |
| pickle_pure_python       | 455 us                                                       | 338 us: 1.35x faster                                                         |
| mako                     | 14.7 ms                                                      | 11.0 ms: 1.34x faster                                                        |
| pycparser                | 1.67 sec                                                     | 1.25 sec: 1.34x faster                                                       |
| nbody                    | 134 ms                                                       | 101 ms: 1.33x faster                                                         |
| tomli_loads              | 2.92 sec                                                     | 2.19 sec: 1.33x faster                                                       |
| genshi_text              | 31.4 ms                                                      | 23.8 ms: 1.32x faster                                                        |
| deepcopy_reduce          | 4.01 us                                                      | 3.04 us: 1.32x faster                                                        |
| dulwich_log              | 81.1 ms                                                      | 62.6 ms: 1.30x faster                                                        |
| sqlalchemy_declarative   | 190 ms                                                       | 147 ms: 1.29x faster                                                         |
| json_dumps               | 14.5 ms                                                      | 11.4 ms: 1.28x faster                                                        |
| fannkuch                 | 483 ms                                                       | 378 ms: 1.28x faster                                                         |
| pprint_pformat           | 2.15 sec                                                     | 1.69 sec: 1.27x faster                                                       |
| sqlalchemy_imperative    | 22.7 ms                                                      | 18.0 ms: 1.26x faster                                                        |
| xml_etree_process        | 75.9 ms                                                      | 60.4 ms: 1.26x faster                                                        |
| pprint_safe_repr         | 1.05 sec                                                     | 838 ms: 1.25x faster                                                         |
| sympy_sum                | 193 ms                                                       | 156 ms: 1.23x faster                                                         |
| pathlib                  | 21.4 ms                                                      | 17.3 ms: 1.23x faster                                                        |
| 2to3                     | 350 ms                                                       | 285 ms: 1.23x faster                                                         |
| sympy_str                | 360 ms                                                       | 297 ms: 1.21x faster                                                         |
| sympy_integrate          | 28.2 ms                                                      | 23.4 ms: 1.20x faster                                                        |
| nqueens                  | 115 ms                                                       | 95.9 ms: 1.20x faster                                                        |
| json_loads               | 30.3 us                                                      | 25.5 us: 1.19x faster                                                        |
| sympy_expand             | 600 ms                                                       | 508 ms: 1.18x faster                                                         |
| bench_thread_pool        | 1.14 ms                                                      | 967 us: 1.18x faster                                                         |
| xml_etree_parse          | 160 ms                                                       | 136 ms: 1.18x faster                                                         |
| mdp                      | 3.01 sec                                                     | 2.56 sec: 1.17x faster                                                       |
| docutils                 | 3.41 sec                                                     | 2.91 sec: 1.17x faster                                                       |
| scimark_fft              | 361 ms                                                       | 314 ms: 1.15x faster                                                         |
| regex_v8                 | 27.2 ms                                                      | 23.7 ms: 1.15x faster                                                        |
| genshi_xml               | 63.3 ms                                                      | 55.5 ms: 1.14x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 97.4 ms: 1.13x faster                                                        |
| json                     | 5.86 ms                                                      | 5.24 ms: 1.12x faster                                                        |
| regex_dna                | 261 ms                                                       | 237 ms: 1.10x faster                                                         |
| xml_etree_generate       | 92.3 ms                                                      | 85.0 ms: 1.09x faster                                                        |
| meteor_contest           | 138 ms                                                       | 128 ms: 1.08x faster                                                         |
| pidigits                 | 271 ms                                                       | 255 ms: 1.06x faster                                                         |
| sqlite_synth             | 2.99 us                                                      | 2.82 us: 1.06x faster                                                        |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.86 ms: 1.05x faster                                                        |
| async_generators         | 421 ms                                                       | 413 ms: 1.02x faster                                                         |
| asyncio_websockets       | 390 ms                                                       | 384 ms: 1.02x faster                                                         |
| regex_effbot             | 3.09 ms                                                      | 3.13 ms: 1.01x slower                                                        |
| telco                    | 7.23 ms                                                      | 7.99 ms: 1.11x slower                                                        |
| coverage                 | 63.3 ms                                                      | 82.0 ms: 1.30x slower                                                        |
| python_startup           | 11.5 ms                                                      | 16.3 ms: 1.42x slower                                                        |
| python_startup_no_site   | 7.33 ms                                                      | 10.5 ms: 1.43x slower                                                        |
| create_gc_cycles         | 1.76 ms                                                      | 2.77 ms: 1.57x slower                                                        |
| gc_traversal             | 3.42 ms                                                      | 6.58 ms: 1.93x slower                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 1.74 sec: 273.58x slower                                                     |
| Geometric mean           | (ref)                                                        | 1.23x faster                                                                 |
Ignored benchmarks (19) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250317-3.14.0a6+-37fd664/bm-20250317-pythonperf2-x86_64-mdboom-reorg_pyinterpreterf-3.14.0a6+-37fd664.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.316x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: 1.28x