# Results vs. 3.10.4

- fork: mdboom
- ref: tuple_hash
- machine: linux-x86_64
- commit hash: 0a71905
- commit date: 2025-03-18
- overall geometric mean: 1.439x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.31x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250318-linux-x86_64-mdboom-tuple_hash-3.14.0a6+-0a71905 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 256 ms: 1.36x faster                                         |
| docutils       | 3.30 sec                                               | 2.62 sec: 1.26x faster                                       |
| html5lib       | 88.9 ms                                                | 61.3 ms: 1.45x faster                                        |
| Geometric mean | (ref)                                                  | 1.35x faster                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250318-linux-x86_64-mdboom-tuple_hash-3.14.0a6+-0a71905 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 610 ms: 2.90x faster                                         |
| async_tree_none         | 728 ms                                                 | 256 ms: 2.84x faster                                         |
| async_tree_memoization  | 870 ms                                                 | 315 ms: 2.76x faster                                         |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 487 ms: 2.09x faster                                         |
| Geometric mean          | (ref)                                                  | 2.62x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250318-linux-x86_64-mdboom-tuple_hash-3.14.0a6+-0a71905 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 117 ms                                                 | 70.0 ms: 1.67x faster                                        |
| nbody          | 154 ms                                                 | 98.1 ms: 1.57x faster                                        |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                         |
| Geometric mean | (ref)                                                  | 1.39x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250318-linux-x86_64-mdboom-tuple_hash-3.14.0a6+-0a71905 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 126 ms: 1.49x faster                                         |
| regex_v8       | 27.8 ms                                                | 24.2 ms: 1.15x faster                                        |
| regex_effbot   | 3.63 ms                                                | 3.26 ms: 1.11x faster                                        |
| regex_dna      | 227 ms                                                 | 221 ms: 1.03x faster                                         |
| Geometric mean | (ref)                                                  | 1.18x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250318-linux-x86_64-mdboom-tuple_hash-3.14.0a6+-0a71905 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 2.00 sec: 1.57x faster                                       |
| pickle_pure_python   | 484 us                                                 | 315 us: 1.54x faster                                         |
| unpickle_pure_python | 331 us                                                 | 218 us: 1.52x faster                                         |
| xml_etree_process    | 79.1 ms                                                | 58.3 ms: 1.36x faster                                        |
| json_dumps           | 14.2 ms                                                | 11.4 ms: 1.24x faster                                        |
| xml_etree_parse      | 168 ms                                                 | 142 ms: 1.19x faster                                         |
| xml_etree_generate   | 99.4 ms                                                | 84.2 ms: 1.18x faster                                        |
| xml_etree_iterparse  | 115 ms                                                 | 98.2 ms: 1.18x faster                                        |
| json_loads           | 31.2 us                                                | 30.1 us: 1.04x faster                                        |
| Geometric mean       | (ref)                                                  | 1.30x faster                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250318-linux-x86_64-mdboom-tuple_hash-3.14.0a6+-0a71905 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.1 ms: 1.11x faster                                        |
| python_startup_no_site | 5.93 ms                                                | 8.21 ms: 1.38x slower                                        |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250318-linux-x86_64-mdboom-tuple_hash-3.14.0a6+-0a71905 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 31.6 ms: 1.52x faster                                        |
| genshi_text     | 31.8 ms                                                | 21.5 ms: 1.48x faster                                        |
| mako            | 16.3 ms                                                | 11.3 ms: 1.44x faster                                        |
| genshi_xml      | 66.0 ms                                                | 49.4 ms: 1.34x faster                                        |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250318-linux-x86_64-mdboom-tuple_hash-3.14.0a6+-0a71905 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 166 us: 3.28x faster                                         |
| async_tree_io            | 1.77 sec                                               | 610 ms: 2.90x faster                                         |
| async_tree_none          | 728 ms                                                 | 256 ms: 2.84x faster                                         |
| generators               | 80.1 ms                                                | 28.6 ms: 2.80x faster                                        |
| async_tree_memoization   | 870 ms                                                 | 315 ms: 2.76x faster                                         |
| deltablue                | 7.91 ms                                                | 3.11 ms: 2.55x faster                                        |
| go                       | 240 ms                                                 | 113 ms: 2.12x faster                                         |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 487 ms: 2.09x faster                                         |
| logging_silent           | 190 ns                                                 | 94.2 ns: 2.01x faster                                        |
| deepcopy_memo            | 58.5 us                                                | 29.1 us: 2.01x faster                                        |
| pylint                   | 551 ms                                                 | 276 ms: 2.00x faster                                         |
| richards_super           | 94.7 ms                                                | 48.6 ms: 1.95x faster                                        |
| chaos                    | 115 ms                                                 | 59.8 ms: 1.93x faster                                        |
| raytrace                 | 507 ms                                                 | 265 ms: 1.91x faster                                         |
| richards                 | 79.3 ms                                                | 42.1 ms: 1.88x faster                                        |
| deepcopy                 | 479 us                                                 | 255 us: 1.88x faster                                         |
| scimark_sor              | 220 ms                                                 | 118 ms: 1.85x faster                                         |
| spectral_norm            | 170 ms                                                 | 97.7 ms: 1.74x faster                                        |
| scimark_monte_carlo      | 118 ms                                                 | 68.5 ms: 1.73x faster                                        |
| comprehensions           | 28.8 us                                                | 16.7 us: 1.72x faster                                        |
| crypto_pyaes             | 128 ms                                                 | 75.8 ms: 1.69x faster                                        |
| float                    | 117 ms                                                 | 70.0 ms: 1.67x faster                                        |
| hexiom                   | 10.4 ms                                                | 6.31 ms: 1.65x faster                                        |
| pyflate                  | 716 ms                                                 | 454 ms: 1.58x faster                                         |
| tomli_loads              | 3.14 sec                                               | 2.00 sec: 1.57x faster                                       |
| deepcopy_reduce          | 4.17 us                                                | 2.66 us: 1.57x faster                                        |
| nbody                    | 154 ms                                                 | 98.1 ms: 1.57x faster                                        |
| pickle_pure_python       | 484 us                                                 | 315 us: 1.54x faster                                         |
| scimark_lu               | 176 ms                                                 | 115 ms: 1.53x faster                                         |
| django_template          | 48.2 ms                                                | 31.6 ms: 1.52x faster                                        |
| unpickle_pure_python     | 331 us                                                 | 218 us: 1.52x faster                                         |
| logging_simple           | 8.30 us                                                | 5.54 us: 1.50x faster                                        |
| regex_compile            | 188 ms                                                 | 126 ms: 1.49x faster                                         |
| genshi_text              | 31.8 ms                                                | 21.5 ms: 1.48x faster                                        |
| logging_format           | 9.09 us                                                | 6.23 us: 1.46x faster                                        |
| coroutines               | 35.1 ms                                                | 24.2 ms: 1.45x faster                                        |
| html5lib                 | 88.9 ms                                                | 61.3 ms: 1.45x faster                                        |
| dulwich_log              | 84.3 ms                                                | 58.3 ms: 1.45x faster                                        |
| mako                     | 16.3 ms                                                | 11.3 ms: 1.44x faster                                        |
| pprint_pformat           | 2.10 sec                                               | 1.47 sec: 1.43x faster                                       |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.4 ms: 1.42x faster                                        |
| pprint_safe_repr         | 1.02 sec                                               | 725 ms: 1.40x faster                                         |
| pycparser                | 1.58 sec                                               | 1.13 sec: 1.39x faster                                       |
| thrift                   | 1.07 ms                                                | 776 us: 1.38x faster                                         |
| 2to3                     | 348 ms                                                 | 256 ms: 1.36x faster                                         |
| xml_etree_process        | 79.1 ms                                                | 58.3 ms: 1.36x faster                                        |
| genshi_xml               | 66.0 ms                                                | 49.4 ms: 1.34x faster                                        |
| sympy_sum                | 196 ms                                                 | 147 ms: 1.33x faster                                         |
| scimark_fft              | 466 ms                                                 | 350 ms: 1.33x faster                                         |
| sqlalchemy_declarative   | 172 ms                                                 | 131 ms: 1.32x faster                                         |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.94 ms: 1.31x faster                                        |
| sympy_integrate          | 25.8 ms                                                | 19.8 ms: 1.30x faster                                        |
| sympy_str                | 346 ms                                                 | 269 ms: 1.29x faster                                         |
| docutils                 | 3.30 sec                                               | 2.62 sec: 1.26x faster                                       |
| nqueens                  | 106 ms                                                 | 84.3 ms: 1.26x faster                                        |
| json_dumps               | 14.2 ms                                                | 11.4 ms: 1.24x faster                                        |
| sympy_expand             | 566 ms                                                 | 456 ms: 1.24x faster                                         |
| pathlib                  | 20.5 ms                                                | 16.5 ms: 1.24x faster                                        |
| fannkuch                 | 532 ms                                                 | 432 ms: 1.23x faster                                         |
| xml_etree_parse          | 168 ms                                                 | 142 ms: 1.19x faster                                         |
| xml_etree_generate       | 99.4 ms                                                | 84.2 ms: 1.18x faster                                        |
| xml_etree_iterparse      | 115 ms                                                 | 98.2 ms: 1.18x faster                                        |
| regex_v8                 | 27.8 ms                                                | 24.2 ms: 1.15x faster                                        |
| async_generators         | 444 ms                                                 | 390 ms: 1.14x faster                                         |
| bench_thread_pool        | 986 us                                                 | 869 us: 1.13x faster                                         |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.12x faster                                         |
| regex_effbot             | 3.63 ms                                                | 3.26 ms: 1.11x faster                                        |
| python_startup           | 14.6 ms                                                | 13.1 ms: 1.11x faster                                        |
| sqlite_synth             | 3.02 us                                                | 2.77 us: 1.09x faster                                        |
| mdp                      | 2.85 sec                                               | 2.66 sec: 1.07x faster                                       |
| json                     | 5.69 ms                                                | 5.32 ms: 1.07x faster                                        |
| json_loads               | 31.2 us                                                | 30.1 us: 1.04x faster                                        |
| regex_dna                | 227 ms                                                 | 221 ms: 1.03x faster                                         |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                         |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                         |
| telco                    | 7.27 ms                                                | 7.80 ms: 1.07x slower                                        |
| coverage                 | 79.4 ms                                                | 90.8 ms: 1.14x slower                                        |
| gc_traversal             | 3.62 ms                                                | 4.92 ms: 1.36x slower                                        |
| python_startup_no_site   | 5.93 ms                                                | 8.21 ms: 1.38x slower                                        |
| create_gc_cycles         | 1.62 ms                                                | 2.50 ms: 1.54x slower                                        |
| bench_mp_pool            | 24.0 ms                                                | 82.9 ms: 3.45x slower                                        |
| Geometric mean           | (ref)                                                  | 1.41x faster                                                 |
Ignored benchmarks (20) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250318-3.14.0a6+-0a71905/bm-20250318-linux-x86_64-mdboom-tuple_hash-3.14.0a6+-0a71905.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.439x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.35x
- 95% likely to have a speedup of 1.33x
- 99% likely to have a speedup of 1.31x

# Memory
- memory change: 1.28x