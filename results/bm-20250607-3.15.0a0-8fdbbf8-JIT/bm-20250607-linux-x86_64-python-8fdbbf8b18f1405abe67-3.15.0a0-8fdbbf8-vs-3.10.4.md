# Results vs. 3.10.4

- fork: python
- ref: 8fdbbf8b18f1405abe67
- machine: linux-x86_64
- commit hash: 8fdbbf8
- commit date: 2025-06-07
- overall geometric mean: 1.459x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.29x faster
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 259 ms: 1.34x faster                                                  |
| docutils       | 3.30 sec                                               | 2.65 sec: 1.24x faster                                                |
| html5lib       | 88.9 ms                                                | 62.7 ms: 1.42x faster                                                 |
| Geometric mean | (ref)                                                  | 1.33x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 599 ms: 2.95x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 312 ms: 2.79x faster                                                  |
| async_tree_none         | 728 ms                                                 | 261 ms: 2.79x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 489 ms: 2.08x faster                                                  |
| Geometric mean          | (ref)                                                  | 2.63x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 117 ms                                                 | 64.1 ms: 1.83x faster                                                 |
| nbody          | 154 ms                                                 | 91.9 ms: 1.67x faster                                                 |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.46x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 128 ms: 1.47x faster                                                  |
| regex_v8       | 27.8 ms                                                | 23.3 ms: 1.19x faster                                                 |
| regex_effbot   | 3.63 ms                                                | 3.36 ms: 1.08x faster                                                 |
| regex_dna      | 227 ms                                                 | 215 ms: 1.06x faster                                                  |
| Geometric mean | (ref)                                                  | 1.19x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.91 sec: 1.64x faster                                                |
| unpickle_pure_python | 331 us                                                 | 203 us: 1.62x faster                                                  |
| pickle_pure_python   | 484 us                                                 | 322 us: 1.51x faster                                                  |
| xml_etree_process    | 79.1 ms                                                | 56.0 ms: 1.41x faster                                                 |
| json_dumps           | 14.2 ms                                                | 11.0 ms: 1.29x faster                                                 |
| xml_etree_generate   | 99.4 ms                                                | 80.8 ms: 1.23x faster                                                 |
| xml_etree_parse      | 168 ms                                                 | 140 ms: 1.20x faster                                                  |
| xml_etree_iterparse  | 115 ms                                                 | 97.8 ms: 1.18x faster                                                 |
| json_loads           | 31.2 us                                                | 28.8 us: 1.08x faster                                                 |
| Geometric mean       | (ref)                                                  | 1.34x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.2 ms: 1.20x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 6.94 ms: 1.17x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.7 ms: 1.53x faster                                                 |
| genshi_text     | 31.8 ms                                                | 21.4 ms: 1.49x faster                                                 |
| django_template | 48.2 ms                                                | 32.4 ms: 1.49x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 50.2 ms: 1.32x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 169 us: 3.23x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 599 ms: 2.95x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 312 ms: 2.79x faster                                                  |
| async_tree_none          | 728 ms                                                 | 261 ms: 2.79x faster                                                  |
| generators               | 80.1 ms                                                | 31.5 ms: 2.55x faster                                                 |
| deltablue                | 7.91 ms                                                | 3.13 ms: 2.52x faster                                                 |
| richards_super           | 94.7 ms                                                | 39.8 ms: 2.38x faster                                                 |
| richards                 | 79.3 ms                                                | 34.1 ms: 2.33x faster                                                 |
| mdp                      | 2.85 sec                                               | 1.24 sec: 2.29x faster                                                |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 489 ms: 2.08x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 29.9 us: 1.96x faster                                                 |
| pylint                   | 551 ms                                                 | 283 ms: 1.95x faster                                                  |
| go                       | 240 ms                                                 | 125 ms: 1.91x faster                                                  |
| deepcopy                 | 479 us                                                 | 256 us: 1.87x faster                                                  |
| chaos                    | 115 ms                                                 | 62.3 ms: 1.85x faster                                                 |
| raytrace                 | 507 ms                                                 | 276 ms: 1.84x faster                                                  |
| float                    | 117 ms                                                 | 64.1 ms: 1.83x faster                                                 |
| scimark_sor              | 220 ms                                                 | 121 ms: 1.81x faster                                                  |
| scimark_monte_carlo      | 118 ms                                                 | 68.1 ms: 1.73x faster                                                 |
| djangocms                | 38.4 us                                                | 22.3 us: 1.72x faster                                                 |
| pyflate                  | 716 ms                                                 | 417 ms: 1.72x faster                                                  |
| crypto_pyaes             | 128 ms                                                 | 75.7 ms: 1.69x faster                                                 |
| comprehensions           | 28.8 us                                                | 17.2 us: 1.67x faster                                                 |
| nbody                    | 154 ms                                                 | 91.9 ms: 1.67x faster                                                 |
| tomli_loads              | 3.14 sec                                               | 1.91 sec: 1.64x faster                                                |
| unpickle_pure_python     | 331 us                                                 | 203 us: 1.62x faster                                                  |
| spectral_norm            | 170 ms                                                 | 105 ms: 1.62x faster                                                  |
| hexiom                   | 10.4 ms                                                | 6.47 ms: 1.61x faster                                                 |
| deepcopy_reduce          | 4.17 us                                                | 2.66 us: 1.57x faster                                                 |
| mako                     | 16.3 ms                                                | 10.7 ms: 1.53x faster                                                 |
| pickle_pure_python       | 484 us                                                 | 322 us: 1.51x faster                                                  |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.51x faster                                                  |
| genshi_text              | 31.8 ms                                                | 21.4 ms: 1.49x faster                                                 |
| django_template          | 48.2 ms                                                | 32.4 ms: 1.49x faster                                                 |
| regex_compile            | 188 ms                                                 | 128 ms: 1.47x faster                                                  |
| dulwich_log              | 84.3 ms                                                | 59.4 ms: 1.42x faster                                                 |
| html5lib                 | 88.9 ms                                                | 62.7 ms: 1.42x faster                                                 |
| xml_etree_process        | 79.1 ms                                                | 56.0 ms: 1.41x faster                                                 |
| thrift                   | 1.07 ms                                                | 764 us: 1.40x faster                                                  |
| scimark_fft              | 466 ms                                                 | 336 ms: 1.39x faster                                                  |
| coroutines               | 35.1 ms                                                | 25.5 ms: 1.38x faster                                                 |
| pycparser                | 1.58 sec                                               | 1.16 sec: 1.36x faster                                                |
| logging_simple           | 8.30 us                                                | 6.14 us: 1.35x faster                                                 |
| 2to3                     | 348 ms                                                 | 259 ms: 1.34x faster                                                  |
| logging_format           | 9.09 us                                                | 6.77 us: 1.34x faster                                                 |
| sympy_integrate          | 25.8 ms                                                | 19.3 ms: 1.34x faster                                                 |
| genshi_xml               | 66.0 ms                                                | 50.2 ms: 1.32x faster                                                 |
| sympy_sum                | 196 ms                                                 | 150 ms: 1.31x faster                                                  |
| json_dumps               | 14.2 ms                                                | 11.0 ms: 1.29x faster                                                 |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.03 ms: 1.29x faster                                                 |
| sympy_str                | 346 ms                                                 | 271 ms: 1.28x faster                                                  |
| fannkuch                 | 532 ms                                                 | 418 ms: 1.27x faster                                                  |
| nqueens                  | 106 ms                                                 | 83.7 ms: 1.26x faster                                                 |
| docutils                 | 3.30 sec                                               | 2.65 sec: 1.24x faster                                                |
| pprint_pformat           | 2.10 sec                                               | 1.69 sec: 1.24x faster                                                |
| xml_etree_generate       | 99.4 ms                                                | 80.8 ms: 1.23x faster                                                 |
| pprint_safe_repr         | 1.02 sec                                               | 830 ms: 1.23x faster                                                  |
| sympy_expand             | 566 ms                                                 | 465 ms: 1.22x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 140 ms: 1.20x faster                                                  |
| python_startup           | 14.6 ms                                                | 12.2 ms: 1.20x faster                                                 |
| regex_v8                 | 27.8 ms                                                | 23.3 ms: 1.19x faster                                                 |
| xml_etree_iterparse      | 115 ms                                                 | 97.8 ms: 1.18x faster                                                 |
| pathlib                  | 20.5 ms                                                | 17.3 ms: 1.18x faster                                                 |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                  |
| json_loads               | 31.2 us                                                | 28.8 us: 1.08x faster                                                 |
| sqlite_synth             | 3.02 us                                                | 2.80 us: 1.08x faster                                                 |
| regex_effbot             | 3.63 ms                                                | 3.36 ms: 1.08x faster                                                 |
| json                     | 5.69 ms                                                | 5.30 ms: 1.07x faster                                                 |
| regex_dna                | 227 ms                                                 | 215 ms: 1.06x faster                                                  |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                  |
| async_generators         | 444 ms                                                 | 437 ms: 1.02x faster                                                  |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                  |
| telco                    | 7.27 ms                                                | 7.82 ms: 1.08x slower                                                 |
| coverage                 | 79.4 ms                                                | 87.5 ms: 1.10x slower                                                 |
| python_startup_no_site   | 5.93 ms                                                | 6.94 ms: 1.17x slower                                                 |
| gc_traversal             | 3.62 ms                                                | 4.94 ms: 1.36x slower                                                 |
| create_gc_cycles         | 1.62 ms                                                | 2.58 ms: 1.59x slower                                                 |
| logging_silent           | 190 ns                                                 | 479 ns: 2.53x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                          |
Ignored benchmarks (23) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250607-3.15.0a0-8fdbbf8-JIT/bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.459x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.29x

# Memory
- memory change: 1.33x