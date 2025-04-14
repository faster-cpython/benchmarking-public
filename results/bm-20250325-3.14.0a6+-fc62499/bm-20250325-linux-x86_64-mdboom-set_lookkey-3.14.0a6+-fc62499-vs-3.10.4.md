# Results vs. 3.10.4

- fork: mdboom
- ref: set_lookkey
- machine: linux-x86_64
- commit hash: fc62499
- commit date: 2025-03-25
- overall geometric mean: 1.431x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.29x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250325-linux-x86_64-mdboom-set_lookkey-3.14.0a6+-fc62499 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 257 ms: 1.36x faster                                          |
| docutils       | 3.30 sec                                               | 2.62 sec: 1.26x faster                                        |
| html5lib       | 88.9 ms                                                | 61.7 ms: 1.44x faster                                         |
| Geometric mean | (ref)                                                  | 1.35x faster                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250325-linux-x86_64-mdboom-set_lookkey-3.14.0a6+-fc62499 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 610 ms: 2.90x faster                                          |
| async_tree_none         | 728 ms                                                 | 257 ms: 2.83x faster                                          |
| async_tree_memoization  | 870 ms                                                 | 312 ms: 2.79x faster                                          |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 489 ms: 2.08x faster                                          |
| Geometric mean          | (ref)                                                  | 2.63x faster                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250325-linux-x86_64-mdboom-set_lookkey-3.14.0a6+-fc62499 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| float          | 117 ms                                                 | 70.0 ms: 1.67x faster                                         |
| nbody          | 154 ms                                                 | 99.9 ms: 1.54x faster                                         |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                          |
| Geometric mean | (ref)                                                  | 1.38x faster                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250325-linux-x86_64-mdboom-set_lookkey-3.14.0a6+-fc62499 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 127 ms: 1.48x faster                                          |
| regex_v8       | 27.8 ms                                                | 24.0 ms: 1.16x faster                                         |
| regex_effbot   | 3.63 ms                                                | 3.30 ms: 1.10x faster                                         |
| regex_dna      | 227 ms                                                 | 219 ms: 1.04x faster                                          |
| Geometric mean | (ref)                                                  | 1.18x faster                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250325-linux-x86_64-mdboom-set_lookkey-3.14.0a6+-fc62499 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 2.02 sec: 1.55x faster                                        |
| pickle_pure_python   | 484 us                                                 | 315 us: 1.54x faster                                          |
| unpickle_pure_python | 331 us                                                 | 221 us: 1.50x faster                                          |
| xml_etree_process    | 79.1 ms                                                | 58.7 ms: 1.35x faster                                         |
| json_dumps           | 14.2 ms                                                | 11.5 ms: 1.24x faster                                         |
| xml_etree_parse      | 168 ms                                                 | 140 ms: 1.20x faster                                          |
| xml_etree_generate   | 99.4 ms                                                | 84.2 ms: 1.18x faster                                         |
| xml_etree_iterparse  | 115 ms                                                 | 98.8 ms: 1.17x faster                                         |
| json_loads           | 31.2 us                                                | 30.0 us: 1.04x faster                                         |
| Geometric mean       | (ref)                                                  | 1.29x faster                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250325-linux-x86_64-mdboom-set_lookkey-3.14.0a6+-fc62499 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.2 ms: 1.10x faster                                         |
| python_startup_no_site | 5.93 ms                                                | 8.22 ms: 1.39x slower                                         |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250325-linux-x86_64-mdboom-set_lookkey-3.14.0a6+-fc62499 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 31.4 ms: 1.53x faster                                         |
| genshi_text     | 31.8 ms                                                | 21.2 ms: 1.50x faster                                         |
| mako            | 16.3 ms                                                | 11.2 ms: 1.46x faster                                         |
| genshi_xml      | 66.0 ms                                                | 49.2 ms: 1.34x faster                                         |
| Geometric mean  | (ref)                                                  | 1.46x faster                                                  |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250325-linux-x86_64-mdboom-set_lookkey-3.14.0a6+-fc62499 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 159 us: 3.42x faster                                          |
| async_tree_io            | 1.77 sec                                               | 610 ms: 2.90x faster                                          |
| async_tree_none          | 728 ms                                                 | 257 ms: 2.83x faster                                          |
| async_tree_memoization   | 870 ms                                                 | 312 ms: 2.79x faster                                          |
| generators               | 80.1 ms                                                | 28.9 ms: 2.77x faster                                         |
| deltablue                | 7.91 ms                                                | 3.08 ms: 2.57x faster                                         |
| go                       | 240 ms                                                 | 114 ms: 2.10x faster                                          |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 489 ms: 2.08x faster                                          |
| logging_silent           | 190 ns                                                 | 93.0 ns: 2.04x faster                                         |
| pylint                   | 551 ms                                                 | 279 ms: 1.98x faster                                          |
| deepcopy_memo            | 58.5 us                                                | 29.6 us: 1.97x faster                                         |
| chaos                    | 115 ms                                                 | 59.6 ms: 1.94x faster                                         |
| raytrace                 | 507 ms                                                 | 265 ms: 1.92x faster                                          |
| richards_super           | 94.7 ms                                                | 49.9 ms: 1.90x faster                                         |
| deepcopy                 | 479 us                                                 | 256 us: 1.87x faster                                          |
| scimark_sor              | 220 ms                                                 | 119 ms: 1.84x faster                                          |
| richards                 | 79.3 ms                                                | 43.6 ms: 1.82x faster                                         |
| comprehensions           | 28.8 us                                                | 16.6 us: 1.73x faster                                         |
| scimark_monte_carlo      | 118 ms                                                 | 68.2 ms: 1.73x faster                                         |
| float                    | 117 ms                                                 | 70.0 ms: 1.67x faster                                         |
| spectral_norm            | 170 ms                                                 | 102 ms: 1.66x faster                                          |
| crypto_pyaes             | 128 ms                                                 | 77.3 ms: 1.65x faster                                         |
| hexiom                   | 10.4 ms                                                | 6.33 ms: 1.64x faster                                         |
| tomli_loads              | 3.14 sec                                               | 2.02 sec: 1.55x faster                                        |
| deepcopy_reduce          | 4.17 us                                                | 2.70 us: 1.54x faster                                         |
| nbody                    | 154 ms                                                 | 99.9 ms: 1.54x faster                                         |
| pickle_pure_python       | 484 us                                                 | 315 us: 1.54x faster                                          |
| django_template          | 48.2 ms                                                | 31.4 ms: 1.53x faster                                         |
| pyflate                  | 716 ms                                                 | 470 ms: 1.53x faster                                          |
| scimark_lu               | 176 ms                                                 | 116 ms: 1.52x faster                                          |
| genshi_text              | 31.8 ms                                                | 21.2 ms: 1.50x faster                                         |
| unpickle_pure_python     | 331 us                                                 | 221 us: 1.50x faster                                          |
| regex_compile            | 188 ms                                                 | 127 ms: 1.48x faster                                          |
| logging_simple           | 8.30 us                                                | 5.60 us: 1.48x faster                                         |
| mako                     | 16.3 ms                                                | 11.2 ms: 1.46x faster                                         |
| coroutines               | 35.1 ms                                                | 24.2 ms: 1.45x faster                                         |
| logging_format           | 9.09 us                                                | 6.28 us: 1.45x faster                                         |
| html5lib                 | 88.9 ms                                                | 61.7 ms: 1.44x faster                                         |
| pprint_pformat           | 2.10 sec                                               | 1.49 sec: 1.41x faster                                        |
| dulwich_log              | 84.3 ms                                                | 60.1 ms: 1.40x faster                                         |
| pprint_safe_repr         | 1.02 sec                                               | 727 ms: 1.40x faster                                          |
| pycparser                | 1.58 sec                                               | 1.13 sec: 1.39x faster                                        |
| thrift                   | 1.07 ms                                                | 770 us: 1.39x faster                                          |
| 2to3                     | 348 ms                                                 | 257 ms: 1.36x faster                                          |
| xml_etree_process        | 79.1 ms                                                | 58.7 ms: 1.35x faster                                         |
| genshi_xml               | 66.0 ms                                                | 49.2 ms: 1.34x faster                                         |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.5 ms: 1.33x faster                                         |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.89 ms: 1.32x faster                                         |
| sympy_integrate          | 25.8 ms                                                | 19.7 ms: 1.31x faster                                         |
| sqlalchemy_declarative   | 172 ms                                                 | 132 ms: 1.30x faster                                          |
| scimark_fft              | 466 ms                                                 | 358 ms: 1.30x faster                                          |
| sympy_sum                | 196 ms                                                 | 152 ms: 1.30x faster                                          |
| sympy_str                | 346 ms                                                 | 269 ms: 1.28x faster                                          |
| nqueens                  | 106 ms                                                 | 84.2 ms: 1.26x faster                                         |
| docutils                 | 3.30 sec                                               | 2.62 sec: 1.26x faster                                        |
| sympy_expand             | 566 ms                                                 | 455 ms: 1.24x faster                                          |
| json_dumps               | 14.2 ms                                                | 11.5 ms: 1.24x faster                                         |
| pathlib                  | 20.5 ms                                                | 16.6 ms: 1.23x faster                                         |
| fannkuch                 | 532 ms                                                 | 437 ms: 1.22x faster                                          |
| xml_etree_parse          | 168 ms                                                 | 140 ms: 1.20x faster                                          |
| xml_etree_generate       | 99.4 ms                                                | 84.2 ms: 1.18x faster                                         |
| xml_etree_iterparse      | 115 ms                                                 | 98.8 ms: 1.17x faster                                         |
| regex_v8                 | 27.8 ms                                                | 24.0 ms: 1.16x faster                                         |
| mdp                      | 2.85 sec                                               | 2.51 sec: 1.13x faster                                        |
| bench_thread_pool        | 986 us                                                 | 880 us: 1.12x faster                                          |
| async_generators         | 444 ms                                                 | 398 ms: 1.12x faster                                          |
| python_startup           | 14.6 ms                                                | 13.2 ms: 1.10x faster                                         |
| regex_effbot             | 3.63 ms                                                | 3.30 ms: 1.10x faster                                         |
| sqlite_synth             | 3.02 us                                                | 2.77 us: 1.09x faster                                         |
| meteor_contest           | 120 ms                                                 | 110 ms: 1.09x faster                                          |
| json                     | 5.69 ms                                                | 5.35 ms: 1.06x faster                                         |
| json_loads               | 31.2 us                                                | 30.0 us: 1.04x faster                                         |
| regex_dna                | 227 ms                                                 | 219 ms: 1.04x faster                                          |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                          |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                          |
| telco                    | 7.27 ms                                                | 7.84 ms: 1.08x slower                                         |
| coverage                 | 79.4 ms                                                | 92.4 ms: 1.16x slower                                         |
| gc_traversal             | 3.62 ms                                                | 4.99 ms: 1.38x slower                                         |
| python_startup_no_site   | 5.93 ms                                                | 8.22 ms: 1.39x slower                                         |
| create_gc_cycles         | 1.62 ms                                                | 2.49 ms: 1.54x slower                                         |
| bench_mp_pool            | 24.0 ms                                                | 84.1 ms: 3.50x slower                                         |
| Geometric mean           | (ref)                                                  | 1.41x faster                                                  |
Ignored benchmarks (20) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250325-3.14.0a6+-fc62499/bm-20250325-linux-x86_64-mdboom-set_lookkey-3.14.0a6+-fc62499.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.431x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.29x

# Memory
- memory change: 1.28x