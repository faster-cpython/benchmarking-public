# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_hot
- machine: linux-x86_64
- commit hash: 5606078
- commit date: 2025-06-11
- overall geometric mean: 1.342x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250611-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-5606078 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 259 ms: 1.35x faster                                              |
| docutils       | 3.30 sec                                               | 2.64 sec: 1.25x faster                                            |
| html5lib       | 88.9 ms                                                | 62.3 ms: 1.43x faster                                             |
| Geometric mean | (ref)                                                  | 1.34x faster                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250611-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-5606078 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 600 ms: 2.95x faster                                              |
| async_tree_memoization  | 870 ms                                                 | 314 ms: 2.77x faster                                              |
| async_tree_none         | 728 ms                                                 | 263 ms: 2.77x faster                                              |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 490 ms: 2.07x faster                                              |
| Geometric mean          | (ref)                                                  | 2.62x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250611-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-5606078 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 117 ms                                                 | 65.0 ms: 1.80x faster                                             |
| nbody          | 154 ms                                                 | 90.2 ms: 1.70x faster                                             |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                              |
| Geometric mean | (ref)                                                  | 1.46x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250611-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-5606078 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 127 ms: 1.48x faster                                              |
| regex_v8       | 27.8 ms                                                | 23.5 ms: 1.18x faster                                             |
| regex_effbot   | 3.63 ms                                                | 3.43 ms: 1.06x faster                                             |
| regex_dna      | 227 ms                                                 | 215 ms: 1.05x faster                                              |
| Geometric mean | (ref)                                                  | 1.18x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250611-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-5606078 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.86 sec: 1.69x faster                                            |
| unpickle_pure_python | 331 us                                                 | 196 us: 1.68x faster                                              |
| pickle_pure_python   | 484 us                                                 | 322 us: 1.51x faster                                              |
| xml_etree_process    | 79.1 ms                                                | 55.4 ms: 1.43x faster                                             |
| json_dumps           | 14.2 ms                                                | 11.0 ms: 1.29x faster                                             |
| xml_etree_generate   | 99.4 ms                                                | 80.2 ms: 1.24x faster                                             |
| xml_etree_parse      | 168 ms                                                 | 139 ms: 1.21x faster                                              |
| xml_etree_iterparse  | 115 ms                                                 | 98.0 ms: 1.18x faster                                             |
| json_loads           | 31.2 us                                                | 27.8 us: 1.12x faster                                             |
| Geometric mean       | (ref)                                                  | 1.36x faster                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250611-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-5606078 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.1 ms: 1.20x faster                                             |
| python_startup_no_site | 5.93 ms                                                | 6.91 ms: 1.16x slower                                             |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250611-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-5606078 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.5 ms: 1.55x faster                                             |
| genshi_text     | 31.8 ms                                                | 21.0 ms: 1.51x faster                                             |
| django_template | 48.2 ms                                                | 32.6 ms: 1.48x faster                                             |
| genshi_xml      | 66.0 ms                                                | 49.8 ms: 1.33x faster                                             |
| Geometric mean  | (ref)                                                  | 1.46x faster                                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250611-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-5606078 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 168 us: 3.24x faster                                              |
| async_tree_io            | 1.77 sec                                               | 600 ms: 2.95x faster                                              |
| async_tree_memoization   | 870 ms                                                 | 314 ms: 2.77x faster                                              |
| async_tree_none          | 728 ms                                                 | 263 ms: 2.77x faster                                              |
| generators               | 80.1 ms                                                | 30.0 ms: 2.67x faster                                             |
| deltablue                | 7.91 ms                                                | 3.07 ms: 2.58x faster                                             |
| richards_super           | 94.7 ms                                                | 38.0 ms: 2.49x faster                                             |
| richards                 | 79.3 ms                                                | 32.6 ms: 2.43x faster                                             |
| mdp                      | 2.85 sec                                               | 1.26 sec: 2.26x faster                                            |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 490 ms: 2.07x faster                                              |
| go                       | 240 ms                                                 | 116 ms: 2.06x faster                                              |
| deepcopy_memo            | 58.5 us                                                | 29.7 us: 1.97x faster                                             |
| pylint                   | 551 ms                                                 | 283 ms: 1.95x faster                                              |
| chaos                    | 115 ms                                                 | 61.7 ms: 1.87x faster                                             |
| raytrace                 | 507 ms                                                 | 274 ms: 1.85x faster                                              |
| deepcopy                 | 479 us                                                 | 262 us: 1.83x faster                                              |
| scimark_sor              | 220 ms                                                 | 120 ms: 1.83x faster                                              |
| scimark_monte_carlo      | 118 ms                                                 | 65.6 ms: 1.80x faster                                             |
| float                    | 117 ms                                                 | 65.0 ms: 1.80x faster                                             |
| pyflate                  | 716 ms                                                 | 412 ms: 1.74x faster                                              |
| crypto_pyaes             | 128 ms                                                 | 74.0 ms: 1.73x faster                                             |
| comprehensions           | 28.8 us                                                | 16.7 us: 1.72x faster                                             |
| spectral_norm            | 170 ms                                                 | 98.9 ms: 1.72x faster                                             |
| nbody                    | 154 ms                                                 | 90.2 ms: 1.70x faster                                             |
| tomli_loads              | 3.14 sec                                               | 1.86 sec: 1.69x faster                                            |
| unpickle_pure_python     | 331 us                                                 | 196 us: 1.68x faster                                              |
| hexiom                   | 10.4 ms                                                | 6.32 ms: 1.65x faster                                             |
| mako                     | 16.3 ms                                                | 10.5 ms: 1.55x faster                                             |
| deepcopy_reduce          | 4.17 us                                                | 2.75 us: 1.52x faster                                             |
| genshi_text              | 31.8 ms                                                | 21.0 ms: 1.51x faster                                             |
| pickle_pure_python       | 484 us                                                 | 322 us: 1.51x faster                                              |
| regex_compile            | 188 ms                                                 | 127 ms: 1.48x faster                                              |
| django_template          | 48.2 ms                                                | 32.6 ms: 1.48x faster                                             |
| scimark_lu               | 176 ms                                                 | 122 ms: 1.44x faster                                              |
| scimark_fft              | 466 ms                                                 | 323 ms: 1.44x faster                                              |
| xml_etree_process        | 79.1 ms                                                | 55.4 ms: 1.43x faster                                             |
| html5lib                 | 88.9 ms                                                | 62.3 ms: 1.43x faster                                             |
| coroutines               | 35.1 ms                                                | 24.7 ms: 1.42x faster                                             |
| dulwich_log              | 84.3 ms                                                | 61.8 ms: 1.37x faster                                             |
| pycparser                | 1.58 sec                                               | 1.16 sec: 1.36x faster                                            |
| logging_simple           | 8.30 us                                                | 6.15 us: 1.35x faster                                             |
| 2to3                     | 348 ms                                                 | 259 ms: 1.35x faster                                              |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.83 ms: 1.34x faster                                             |
| logging_format           | 9.09 us                                                | 6.82 us: 1.33x faster                                             |
| sympy_integrate          | 25.8 ms                                                | 19.4 ms: 1.33x faster                                             |
| genshi_xml               | 66.0 ms                                                | 49.8 ms: 1.33x faster                                             |
| fannkuch                 | 532 ms                                                 | 401 ms: 1.32x faster                                              |
| sympy_sum                | 196 ms                                                 | 151 ms: 1.30x faster                                              |
| pprint_safe_repr         | 1.02 sec                                               | 785 ms: 1.30x faster                                              |
| json_dumps               | 14.2 ms                                                | 11.0 ms: 1.29x faster                                             |
| pprint_pformat           | 2.10 sec                                               | 1.63 sec: 1.29x faster                                            |
| sympy_str                | 346 ms                                                 | 273 ms: 1.26x faster                                              |
| nqueens                  | 106 ms                                                 | 84.2 ms: 1.26x faster                                             |
| docutils                 | 3.30 sec                                               | 2.64 sec: 1.25x faster                                            |
| xml_etree_generate       | 99.4 ms                                                | 80.2 ms: 1.24x faster                                             |
| sympy_expand             | 566 ms                                                 | 469 ms: 1.21x faster                                              |
| xml_etree_parse          | 168 ms                                                 | 139 ms: 1.21x faster                                              |
| pathlib                  | 20.5 ms                                                | 17.0 ms: 1.20x faster                                             |
| python_startup           | 14.6 ms                                                | 12.1 ms: 1.20x faster                                             |
| regex_v8                 | 27.8 ms                                                | 23.5 ms: 1.18x faster                                             |
| xml_etree_iterparse      | 115 ms                                                 | 98.0 ms: 1.18x faster                                             |
| json_loads               | 31.2 us                                                | 27.8 us: 1.12x faster                                             |
| json                     | 5.69 ms                                                | 5.10 ms: 1.12x faster                                             |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.11x faster                                              |
| sqlite_synth             | 3.02 us                                                | 2.81 us: 1.08x faster                                             |
| regex_effbot             | 3.63 ms                                                | 3.43 ms: 1.06x faster                                             |
| regex_dna                | 227 ms                                                 | 215 ms: 1.05x faster                                              |
| async_generators         | 444 ms                                                 | 425 ms: 1.04x faster                                              |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                              |
| asyncio_websockets       | 559 ms                                                 | 553 ms: 1.01x faster                                              |
| telco                    | 7.27 ms                                                | 7.78 ms: 1.07x slower                                             |
| python_startup_no_site   | 5.93 ms                                                | 6.91 ms: 1.16x slower                                             |
| gc_traversal             | 3.62 ms                                                | 5.03 ms: 1.39x slower                                             |
| create_gc_cycles         | 1.62 ms                                                | 2.58 ms: 1.59x slower                                             |
| logging_silent           | 190 ns                                                 | 475 ns: 2.50x slower                                              |
| coverage                 | 79.4 ms                                                | 428 ms: 5.39x slower                                              |
| thrift                   | 1.07 ms                                                | 148 ms: 138.32x slower                                            |
| Geometric mean           | (ref)                                                  | 1.32x faster                                                      |
Ignored benchmarks (24) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250611-3.15.0a0-5606078-JIT/bm-20250611-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-5606078.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.342x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.33x