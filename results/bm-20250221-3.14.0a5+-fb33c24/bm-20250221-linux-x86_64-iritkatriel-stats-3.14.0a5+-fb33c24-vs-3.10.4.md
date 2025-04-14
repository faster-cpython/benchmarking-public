# Results vs. 3.10.4

- fork: iritkatriel
- ref: stats
- machine: linux-x86_64
- commit hash: fb33c24
- commit date: 2025-02-21
- overall geometric mean: 1.439x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.31x faster
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250221-linux-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 256 ms: 1.36x faster                                         |
| docutils       | 3.30 sec                                               | 2.62 sec: 1.26x faster                                       |
| html5lib       | 88.9 ms                                                | 61.6 ms: 1.44x faster                                        |
| Geometric mean | (ref)                                                  | 1.35x faster                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250221-linux-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 611 ms: 2.89x faster                                         |
| async_tree_none         | 728 ms                                                 | 260 ms: 2.80x faster                                         |
| async_tree_memoization  | 870 ms                                                 | 320 ms: 2.72x faster                                         |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 493 ms: 2.06x faster                                         |
| Geometric mean          | (ref)                                                  | 2.60x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250221-linux-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 117 ms                                                 | 72.7 ms: 1.61x faster                                        |
| nbody          | 154 ms                                                 | 97.6 ms: 1.57x faster                                        |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                         |
| Geometric mean | (ref)                                                  | 1.37x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250221-linux-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 126 ms: 1.49x faster                                         |
| regex_v8       | 27.8 ms                                                | 23.3 ms: 1.19x faster                                        |
| regex_effbot   | 3.63 ms                                                | 3.46 ms: 1.05x faster                                        |
| regex_dna      | 227 ms                                                 | 221 ms: 1.02x faster                                         |
| Geometric mean | (ref)                                                  | 1.18x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250221-linux-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.96 sec: 1.60x faster                                       |
| pickle_pure_python   | 484 us                                                 | 319 us: 1.52x faster                                         |
| unpickle_pure_python | 331 us                                                 | 222 us: 1.49x faster                                         |
| xml_etree_process    | 79.1 ms                                                | 58.7 ms: 1.35x faster                                        |
| xml_etree_parse      | 168 ms                                                 | 139 ms: 1.21x faster                                         |
| json_dumps           | 14.2 ms                                                | 11.8 ms: 1.20x faster                                        |
| xml_etree_generate   | 99.4 ms                                                | 83.9 ms: 1.18x faster                                        |
| xml_etree_iterparse  | 115 ms                                                 | 98.1 ms: 1.18x faster                                        |
| json_loads           | 31.2 us                                                | 29.7 us: 1.05x faster                                        |
| Geometric mean       | (ref)                                                  | 1.30x faster                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250221-linux-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.9 ms: 1.13x faster                                        |
| python_startup_no_site | 5.93 ms                                                | 7.06 ms: 1.19x slower                                        |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250221-linux-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 31.8 ms: 1.51x faster                                        |
| mako            | 16.3 ms                                                | 11.2 ms: 1.45x faster                                        |
| genshi_text     | 31.8 ms                                                | 21.9 ms: 1.45x faster                                        |
| genshi_xml      | 66.0 ms                                                | 49.5 ms: 1.33x faster                                        |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250221-linux-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 160 us: 3.41x faster                                         |
| async_tree_io            | 1.77 sec                                               | 611 ms: 2.89x faster                                         |
| generators               | 80.1 ms                                                | 28.0 ms: 2.86x faster                                        |
| async_tree_none          | 728 ms                                                 | 260 ms: 2.80x faster                                         |
| async_tree_memoization   | 870 ms                                                 | 320 ms: 2.72x faster                                         |
| deltablue                | 7.91 ms                                                | 3.12 ms: 2.54x faster                                        |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 493 ms: 2.06x faster                                         |
| go                       | 240 ms                                                 | 118 ms: 2.04x faster                                         |
| pylint                   | 551 ms                                                 | 275 ms: 2.01x faster                                         |
| chaos                    | 115 ms                                                 | 59.4 ms: 1.94x faster                                        |
| deepcopy_memo            | 58.5 us                                                | 30.1 us: 1.94x faster                                        |
| deepcopy                 | 479 us                                                 | 257 us: 1.87x faster                                         |
| richards_super           | 94.7 ms                                                | 50.7 ms: 1.87x faster                                        |
| raytrace                 | 507 ms                                                 | 273 ms: 1.85x faster                                         |
| logging_silent           | 190 ns                                                 | 105 ns: 1.81x faster                                         |
| scimark_sor              | 220 ms                                                 | 123 ms: 1.79x faster                                         |
| richards                 | 79.3 ms                                                | 44.4 ms: 1.79x faster                                        |
| comprehensions           | 28.8 us                                                | 16.4 us: 1.75x faster                                        |
| spectral_norm            | 170 ms                                                 | 97.4 ms: 1.74x faster                                        |
| scimark_monte_carlo      | 118 ms                                                 | 67.8 ms: 1.74x faster                                        |
| crypto_pyaes             | 128 ms                                                 | 74.7 ms: 1.71x faster                                        |
| hexiom                   | 10.4 ms                                                | 6.23 ms: 1.67x faster                                        |
| float                    | 117 ms                                                 | 72.7 ms: 1.61x faster                                        |
| tomli_loads              | 3.14 sec                                               | 1.96 sec: 1.60x faster                                       |
| nbody                    | 154 ms                                                 | 97.6 ms: 1.57x faster                                        |
| deepcopy_reduce          | 4.17 us                                                | 2.66 us: 1.57x faster                                        |
| scimark_lu               | 176 ms                                                 | 115 ms: 1.53x faster                                         |
| pyflate                  | 716 ms                                                 | 470 ms: 1.52x faster                                         |
| pickle_pure_python       | 484 us                                                 | 319 us: 1.52x faster                                         |
| django_template          | 48.2 ms                                                | 31.8 ms: 1.51x faster                                        |
| regex_compile            | 188 ms                                                 | 126 ms: 1.49x faster                                         |
| logging_simple           | 8.30 us                                                | 5.56 us: 1.49x faster                                        |
| unpickle_pure_python     | 331 us                                                 | 222 us: 1.49x faster                                         |
| coroutines               | 35.1 ms                                                | 23.8 ms: 1.47x faster                                        |
| logging_format           | 9.09 us                                                | 6.22 us: 1.46x faster                                        |
| mako                     | 16.3 ms                                                | 11.2 ms: 1.45x faster                                        |
| genshi_text              | 31.8 ms                                                | 21.9 ms: 1.45x faster                                        |
| html5lib                 | 88.9 ms                                                | 61.6 ms: 1.44x faster                                        |
| pprint_pformat           | 2.10 sec                                               | 1.47 sec: 1.43x faster                                       |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.4 ms: 1.42x faster                                        |
| pprint_safe_repr         | 1.02 sec                                               | 723 ms: 1.41x faster                                         |
| thrift                   | 1.07 ms                                                | 764 us: 1.40x faster                                         |
| 2to3                     | 348 ms                                                 | 256 ms: 1.36x faster                                         |
| xml_etree_process        | 79.1 ms                                                | 58.7 ms: 1.35x faster                                        |
| pycparser                | 1.58 sec                                               | 1.17 sec: 1.35x faster                                       |
| sqlalchemy_declarative   | 172 ms                                                 | 128 ms: 1.35x faster                                         |
| scimark_fft              | 466 ms                                                 | 348 ms: 1.34x faster                                         |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.83 ms: 1.34x faster                                        |
| sympy_sum                | 196 ms                                                 | 147 ms: 1.34x faster                                         |
| genshi_xml               | 66.0 ms                                                | 49.5 ms: 1.33x faster                                        |
| dulwich_log              | 84.3 ms                                                | 64.0 ms: 1.32x faster                                        |
| sympy_integrate          | 25.8 ms                                                | 19.7 ms: 1.31x faster                                        |
| nqueens                  | 106 ms                                                 | 81.6 ms: 1.30x faster                                        |
| sympy_str                | 346 ms                                                 | 267 ms: 1.29x faster                                         |
| fannkuch                 | 532 ms                                                 | 415 ms: 1.28x faster                                         |
| docutils                 | 3.30 sec                                               | 2.62 sec: 1.26x faster                                       |
| sympy_expand             | 566 ms                                                 | 454 ms: 1.25x faster                                         |
| pathlib                  | 20.5 ms                                                | 16.7 ms: 1.22x faster                                        |
| xml_etree_parse          | 168 ms                                                 | 139 ms: 1.21x faster                                         |
| json_dumps               | 14.2 ms                                                | 11.8 ms: 1.20x faster                                        |
| regex_v8                 | 27.8 ms                                                | 23.3 ms: 1.19x faster                                        |
| xml_etree_generate       | 99.4 ms                                                | 83.9 ms: 1.18x faster                                        |
| xml_etree_iterparse      | 115 ms                                                 | 98.1 ms: 1.18x faster                                        |
| async_generators         | 444 ms                                                 | 387 ms: 1.15x faster                                         |
| mdp                      | 2.85 sec                                               | 2.50 sec: 1.14x faster                                       |
| bench_thread_pool        | 986 us                                                 | 867 us: 1.14x faster                                         |
| python_startup           | 14.6 ms                                                | 12.9 ms: 1.13x faster                                        |
| sqlite_synth             | 3.02 us                                                | 2.76 us: 1.10x faster                                        |
| meteor_contest           | 120 ms                                                 | 109 ms: 1.09x faster                                         |
| json                     | 5.69 ms                                                | 5.32 ms: 1.07x faster                                        |
| regex_effbot             | 3.63 ms                                                | 3.46 ms: 1.05x faster                                        |
| json_loads               | 31.2 us                                                | 29.7 us: 1.05x faster                                        |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                         |
| regex_dna                | 227 ms                                                 | 221 ms: 1.02x faster                                         |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                         |
| telco                    | 7.27 ms                                                | 7.84 ms: 1.08x slower                                        |
| coverage                 | 79.4 ms                                                | 91.0 ms: 1.15x slower                                        |
| python_startup_no_site   | 5.93 ms                                                | 7.06 ms: 1.19x slower                                        |
| gc_traversal             | 3.62 ms                                                | 4.78 ms: 1.32x slower                                        |
| create_gc_cycles         | 1.62 ms                                                | 2.48 ms: 1.53x slower                                        |
| bench_mp_pool            | 24.0 ms                                                | 83.5 ms: 3.48x slower                                        |
| Geometric mean           | (ref)                                                  | 1.41x faster                                                 |
Ignored benchmarks (20) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-linux-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.439x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.33x
- 99% likely to have a speedup of 1.31x

# Memory
- memory change: 1.27x