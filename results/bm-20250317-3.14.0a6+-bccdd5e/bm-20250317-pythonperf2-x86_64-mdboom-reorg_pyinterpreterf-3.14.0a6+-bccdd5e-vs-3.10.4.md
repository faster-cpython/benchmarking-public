# Results vs. 3.10.4

- fork: mdboom
- ref: reorg_pyinterpreterf
- machine: linux-x86_64
- commit hash: bccdd5e
- commit date: 2025-03-17
- overall geometric mean: 1.313x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250317-pythonperf2-x86_64-mdboom-reorg_pyinterpreterf-3.14.0a6+-bccdd5e |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 285 ms: 1.23x faster                                                         |
| docutils       | 3.41 sec                                                     | 2.93 sec: 1.16x faster                                                       |
| html5lib       | 94.6 ms                                                      | 69.6 ms: 1.36x faster                                                        |
| Geometric mean | (ref)                                                        | 1.25x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250317-pythonperf2-x86_64-mdboom-reorg_pyinterpreterf-3.14.0a6+-bccdd5e |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 642 ms: 2.49x faster                                                         |
| async_tree_none         | 692 ms                                                       | 292 ms: 2.37x faster                                                         |
| async_tree_memoization  | 819 ms                                                       | 350 ms: 2.34x faster                                                         |
| async_tree_cpu_io_mixed | 936 ms                                                       | 523 ms: 1.79x faster                                                         |
| Geometric mean          | (ref)                                                        | 2.23x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250317-pythonperf2-x86_64-mdboom-reorg_pyinterpreterf-3.14.0a6+-bccdd5e |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 71.6 ms: 1.55x faster                                                        |
| nbody          | 134 ms                                                       | 108 ms: 1.24x faster                                                         |
| pidigits       | 271 ms                                                       | 254 ms: 1.07x faster                                                         |
| Geometric mean | (ref)                                                        | 1.27x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250317-pythonperf2-x86_64-mdboom-reorg_pyinterpreterf-3.14.0a6+-bccdd5e |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 136 ms: 1.40x faster                                                         |
| regex_v8       | 27.2 ms                                                      | 23.5 ms: 1.15x faster                                                        |
| regex_dna      | 261 ms                                                       | 234 ms: 1.12x faster                                                         |
| regex_effbot   | 3.09 ms                                                      | 3.14 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                        | 1.15x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250317-pythonperf2-x86_64-mdboom-reorg_pyinterpreterf-3.14.0a6+-bccdd5e |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 226 us: 1.38x faster                                                         |
| pickle_pure_python   | 455 us                                                       | 335 us: 1.36x faster                                                         |
| tomli_loads          | 2.92 sec                                                     | 2.20 sec: 1.33x faster                                                       |
| json_dumps           | 14.5 ms                                                      | 11.4 ms: 1.28x faster                                                        |
| xml_etree_process    | 75.9 ms                                                      | 60.2 ms: 1.26x faster                                                        |
| json_loads           | 30.3 us                                                      | 25.7 us: 1.18x faster                                                        |
| xml_etree_parse      | 160 ms                                                       | 141 ms: 1.14x faster                                                         |
| xml_etree_iterparse  | 110 ms                                                       | 101 ms: 1.10x faster                                                         |
| xml_etree_generate   | 92.3 ms                                                      | 84.8 ms: 1.09x faster                                                        |
| Geometric mean       | (ref)                                                        | 1.23x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250317-pythonperf2-x86_64-mdboom-reorg_pyinterpreterf-3.14.0a6+-bccdd5e |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 16.4 ms: 1.42x slower                                                        |
| python_startup_no_site | 7.33 ms                                                      | 10.5 ms: 1.43x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.43x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250317-pythonperf2-x86_64-mdboom-reorg_pyinterpreterf-3.14.0a6+-bccdd5e |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 37.0 ms: 1.36x faster                                                        |
| mako            | 14.7 ms                                                      | 11.1 ms: 1.32x faster                                                        |
| genshi_text     | 31.4 ms                                                      | 24.3 ms: 1.30x faster                                                        |
| genshi_xml      | 63.3 ms                                                      | 56.2 ms: 1.13x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.27x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250317-pythonperf2-x86_64-mdboom-reorg_pyinterpreterf-3.14.0a6+-bccdd5e |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 174 us: 3.08x faster                                                         |
| async_tree_io            | 1.60 sec                                                     | 642 ms: 2.49x faster                                                         |
| async_tree_none          | 692 ms                                                       | 292 ms: 2.37x faster                                                         |
| async_tree_memoization   | 819 ms                                                       | 350 ms: 2.34x faster                                                         |
| deltablue                | 7.50 ms                                                      | 3.39 ms: 2.21x faster                                                        |
| generators               | 57.3 ms                                                      | 28.2 ms: 2.03x faster                                                        |
| go                       | 262 ms                                                       | 133 ms: 1.96x faster                                                         |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 523 ms: 1.79x faster                                                         |
| pylint                   | 566 ms                                                       | 321 ms: 1.77x faster                                                         |
| logging_silent           | 167 ns                                                       | 95.7 ns: 1.75x faster                                                        |
| chaos                    | 109 ms                                                       | 64.3 ms: 1.69x faster                                                        |
| richards_super           | 90.6 ms                                                      | 54.0 ms: 1.68x faster                                                        |
| deepcopy_memo            | 49.8 us                                                      | 29.7 us: 1.67x faster                                                        |
| raytrace                 | 489 ms                                                       | 297 ms: 1.65x faster                                                         |
| scimark_lu               | 167 ms                                                       | 102 ms: 1.64x faster                                                         |
| scimark_monte_carlo      | 107 ms                                                       | 66.0 ms: 1.63x faster                                                        |
| scimark_sor              | 180 ms                                                       | 111 ms: 1.63x faster                                                         |
| deepcopy                 | 468 us                                                       | 295 us: 1.58x faster                                                         |
| richards                 | 75.1 ms                                                      | 47.8 ms: 1.57x faster                                                        |
| pyflate                  | 733 ms                                                       | 470 ms: 1.56x faster                                                         |
| float                    | 111 ms                                                       | 71.6 ms: 1.55x faster                                                        |
| spectral_norm            | 139 ms                                                       | 90.1 ms: 1.54x faster                                                        |
| comprehensions           | 26.7 us                                                      | 17.7 us: 1.51x faster                                                        |
| hexiom                   | 9.42 ms                                                      | 6.44 ms: 1.46x faster                                                        |
| coroutines               | 30.3 ms                                                      | 21.1 ms: 1.44x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 83.6 ms: 1.43x faster                                                        |
| logging_simple           | 8.88 us                                                      | 6.33 us: 1.40x faster                                                        |
| regex_compile            | 190 ms                                                       | 136 ms: 1.40x faster                                                         |
| unpickle_pure_python     | 312 us                                                       | 226 us: 1.38x faster                                                         |
| logging_format           | 9.64 us                                                      | 7.05 us: 1.37x faster                                                        |
| thrift                   | 1.18 ms                                                      | 860 us: 1.37x faster                                                         |
| html5lib                 | 94.6 ms                                                      | 69.6 ms: 1.36x faster                                                        |
| pickle_pure_python       | 455 us                                                       | 335 us: 1.36x faster                                                         |
| django_template          | 50.2 ms                                                      | 37.0 ms: 1.36x faster                                                        |
| deepcopy_reduce          | 4.01 us                                                      | 3.01 us: 1.33x faster                                                        |
| tomli_loads              | 2.92 sec                                                     | 2.20 sec: 1.33x faster                                                       |
| mako                     | 14.7 ms                                                      | 11.1 ms: 1.32x faster                                                        |
| sqlalchemy_declarative   | 190 ms                                                       | 146 ms: 1.30x faster                                                         |
| genshi_text              | 31.4 ms                                                      | 24.3 ms: 1.30x faster                                                        |
| dulwich_log              | 81.1 ms                                                      | 62.7 ms: 1.29x faster                                                        |
| pycparser                | 1.67 sec                                                     | 1.29 sec: 1.29x faster                                                       |
| pprint_pformat           | 2.15 sec                                                     | 1.68 sec: 1.28x faster                                                       |
| pprint_safe_repr         | 1.05 sec                                                     | 822 ms: 1.28x faster                                                         |
| json_dumps               | 14.5 ms                                                      | 11.4 ms: 1.28x faster                                                        |
| xml_etree_process        | 75.9 ms                                                      | 60.2 ms: 1.26x faster                                                        |
| sqlalchemy_imperative    | 22.7 ms                                                      | 18.3 ms: 1.24x faster                                                        |
| pathlib                  | 21.4 ms                                                      | 17.2 ms: 1.24x faster                                                        |
| nbody                    | 134 ms                                                       | 108 ms: 1.24x faster                                                         |
| sympy_sum                | 193 ms                                                       | 156 ms: 1.24x faster                                                         |
| fannkuch                 | 483 ms                                                       | 393 ms: 1.23x faster                                                         |
| 2to3                     | 350 ms                                                       | 285 ms: 1.23x faster                                                         |
| sympy_str                | 360 ms                                                       | 296 ms: 1.22x faster                                                         |
| mdp                      | 3.01 sec                                                     | 2.50 sec: 1.20x faster                                                       |
| bench_thread_pool        | 1.14 ms                                                      | 950 us: 1.20x faster                                                         |
| sympy_integrate          | 28.2 ms                                                      | 23.5 ms: 1.20x faster                                                        |
| nqueens                  | 115 ms                                                       | 96.3 ms: 1.19x faster                                                        |
| sympy_expand             | 600 ms                                                       | 503 ms: 1.19x faster                                                         |
| json_loads               | 30.3 us                                                      | 25.7 us: 1.18x faster                                                        |
| docutils                 | 3.41 sec                                                     | 2.93 sec: 1.16x faster                                                       |
| regex_v8                 | 27.2 ms                                                      | 23.5 ms: 1.15x faster                                                        |
| xml_etree_parse          | 160 ms                                                       | 141 ms: 1.14x faster                                                         |
| scimark_fft              | 361 ms                                                       | 319 ms: 1.13x faster                                                         |
| genshi_xml               | 63.3 ms                                                      | 56.2 ms: 1.13x faster                                                        |
| regex_dna                | 261 ms                                                       | 234 ms: 1.12x faster                                                         |
| json                     | 5.86 ms                                                      | 5.27 ms: 1.11x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 101 ms: 1.10x faster                                                         |
| xml_etree_generate       | 92.3 ms                                                      | 84.8 ms: 1.09x faster                                                        |
| meteor_contest           | 138 ms                                                       | 128 ms: 1.08x faster                                                         |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.71 ms: 1.08x faster                                                        |
| pidigits                 | 271 ms                                                       | 254 ms: 1.07x faster                                                         |
| sqlite_synth             | 2.99 us                                                      | 2.82 us: 1.06x faster                                                        |
| asyncio_websockets       | 390 ms                                                       | 383 ms: 1.02x faster                                                         |
| async_generators         | 421 ms                                                       | 416 ms: 1.01x faster                                                         |
| regex_effbot             | 3.09 ms                                                      | 3.14 ms: 1.02x slower                                                        |
| telco                    | 7.23 ms                                                      | 7.98 ms: 1.10x slower                                                        |
| coverage                 | 63.3 ms                                                      | 82.6 ms: 1.31x slower                                                        |
| python_startup           | 11.5 ms                                                      | 16.4 ms: 1.42x slower                                                        |
| python_startup_no_site   | 7.33 ms                                                      | 10.5 ms: 1.43x slower                                                        |
| create_gc_cycles         | 1.76 ms                                                      | 2.82 ms: 1.60x slower                                                        |
| gc_traversal             | 3.42 ms                                                      | 6.58 ms: 1.93x slower                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 1.69 sec: 265.72x slower                                                     |
| Geometric mean           | (ref)                                                        | 1.22x faster                                                                 |
Ignored benchmarks (19) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250317-3.14.0a6+-bccdd5e/bm-20250317-pythonperf2-x86_64-mdboom-reorg_pyinterpreterf-3.14.0a6+-bccdd5e.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.313x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.28x