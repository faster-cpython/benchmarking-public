# Results vs. 3.10.4

- fork: kumaraditya303
- ref: gc
- machine: linux-x86_64
- commit hash: e537b8b
- commit date: 2025-01-17
- overall geometric mean: 1.453x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.32x faster
- Memory change: 1.26x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4+-e537b8b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 253 ms: 1.38x faster                                         |
| docutils       | 3.30 sec                                               | 2.59 sec: 1.27x faster                                       |
| html5lib       | 88.9 ms                                                | 59.8 ms: 1.49x faster                                        |
| Geometric mean | (ref)                                                  | 1.38x faster                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4+-e537b8b |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 604 ms: 2.93x faster                                         |
| async_tree_none         | 728 ms                                                 | 259 ms: 2.81x faster                                         |
| async_tree_memoization  | 870 ms                                                 | 324 ms: 2.68x faster                                         |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 482 ms: 2.11x faster                                         |
| Geometric mean          | (ref)                                                  | 2.61x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4+-e537b8b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 117 ms                                                 | 70.3 ms: 1.66x faster                                        |
| nbody          | 154 ms                                                 | 94.3 ms: 1.63x faster                                        |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                         |
| Geometric mean | (ref)                                                  | 1.41x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4+-e537b8b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 125 ms: 1.50x faster                                         |
| regex_effbot   | 3.63 ms                                                | 3.29 ms: 1.10x faster                                        |
| regex_dna      | 227 ms                                                 | 211 ms: 1.08x faster                                         |
| regex_v8       | 27.8 ms                                                | 26.1 ms: 1.06x faster                                        |
| Geometric mean | (ref)                                                  | 1.17x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4+-e537b8b |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.94 sec: 1.62x faster                                       |
| unpickle_pure_python | 331 us                                                 | 218 us: 1.52x faster                                         |
| pickle_pure_python   | 484 us                                                 | 321 us: 1.51x faster                                         |
| xml_etree_process    | 79.1 ms                                                | 59.1 ms: 1.34x faster                                        |
| xml_etree_parse      | 168 ms                                                 | 139 ms: 1.21x faster                                         |
| xml_etree_iterparse  | 115 ms                                                 | 97.7 ms: 1.18x faster                                        |
| json_dumps           | 14.2 ms                                                | 12.0 ms: 1.18x faster                                        |
| xml_etree_generate   | 99.4 ms                                                | 84.5 ms: 1.18x faster                                        |
| json_loads           | 31.2 us                                                | 29.8 us: 1.05x faster                                        |
| Geometric mean       | (ref)                                                  | 1.30x faster                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4+-e537b8b |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.8 ms: 1.14x faster                                        |
| python_startup_no_site | 5.93 ms                                                | 7.05 ms: 1.19x slower                                        |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4+-e537b8b |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 31.9 ms: 1.51x faster                                        |
| genshi_text     | 31.8 ms                                                | 21.4 ms: 1.49x faster                                        |
| mako            | 16.3 ms                                                | 11.2 ms: 1.45x faster                                        |
| genshi_xml      | 66.0 ms                                                | 48.7 ms: 1.36x faster                                        |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4+-e537b8b |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 160 us: 3.40x faster                                         |
| async_tree_io            | 1.77 sec                                               | 604 ms: 2.93x faster                                         |
| generators               | 80.1 ms                                                | 28.0 ms: 2.86x faster                                        |
| async_tree_none          | 728 ms                                                 | 259 ms: 2.81x faster                                         |
| async_tree_memoization   | 870 ms                                                 | 324 ms: 2.68x faster                                         |
| deltablue                | 7.91 ms                                                | 3.22 ms: 2.46x faster                                        |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 482 ms: 2.11x faster                                         |
| go                       | 240 ms                                                 | 117 ms: 2.06x faster                                         |
| pylint                   | 551 ms                                                 | 274 ms: 2.02x faster                                         |
| chaos                    | 115 ms                                                 | 58.1 ms: 1.99x faster                                        |
| deepcopy_memo            | 58.5 us                                                | 30.4 us: 1.92x faster                                        |
| richards_super           | 94.7 ms                                                | 49.9 ms: 1.90x faster                                        |
| deepcopy                 | 479 us                                                 | 256 us: 1.87x faster                                         |
| raytrace                 | 507 ms                                                 | 271 ms: 1.87x faster                                         |
| richards                 | 79.3 ms                                                | 43.4 ms: 1.83x faster                                        |
| spectral_norm            | 170 ms                                                 | 93.5 ms: 1.82x faster                                        |
| scimark_sor              | 220 ms                                                 | 122 ms: 1.80x faster                                         |
| logging_silent           | 190 ns                                                 | 106 ns: 1.79x faster                                         |
| crypto_pyaes             | 128 ms                                                 | 71.7 ms: 1.78x faster                                        |
| scimark_monte_carlo      | 118 ms                                                 | 68.1 ms: 1.74x faster                                        |
| sqlglot_parse            | 2.17 ms                                                | 1.25 ms: 1.73x faster                                        |
| comprehensions           | 28.8 us                                                | 17.0 us: 1.69x faster                                        |
| hexiom                   | 10.4 ms                                                | 6.24 ms: 1.67x faster                                        |
| float                    | 117 ms                                                 | 70.3 ms: 1.66x faster                                        |
| sqlglot_transpile        | 2.57 ms                                                | 1.56 ms: 1.65x faster                                        |
| nbody                    | 154 ms                                                 | 94.3 ms: 1.63x faster                                        |
| tomli_loads              | 3.14 sec                                               | 1.94 sec: 1.62x faster                                       |
| deepcopy_reduce          | 4.17 us                                                | 2.60 us: 1.60x faster                                        |
| logging_simple           | 8.30 us                                                | 5.41 us: 1.54x faster                                        |
| coroutines               | 35.1 ms                                                | 23.0 ms: 1.53x faster                                        |
| scimark_lu               | 176 ms                                                 | 116 ms: 1.52x faster                                         |
| unpickle_pure_python     | 331 us                                                 | 218 us: 1.52x faster                                         |
| logging_format           | 9.09 us                                                | 6.01 us: 1.51x faster                                        |
| pickle_pure_python       | 484 us                                                 | 321 us: 1.51x faster                                         |
| django_template          | 48.2 ms                                                | 31.9 ms: 1.51x faster                                        |
| pyflate                  | 716 ms                                                 | 474 ms: 1.51x faster                                         |
| regex_compile            | 188 ms                                                 | 125 ms: 1.50x faster                                         |
| genshi_text              | 31.8 ms                                                | 21.4 ms: 1.49x faster                                        |
| html5lib                 | 88.9 ms                                                | 59.8 ms: 1.49x faster                                        |
| mako                     | 16.3 ms                                                | 11.2 ms: 1.45x faster                                        |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.2 ms: 1.44x faster                                        |
| pprint_pformat           | 2.10 sec                                               | 1.48 sec: 1.42x faster                                       |
| pprint_safe_repr         | 1.02 sec                                               | 719 ms: 1.42x faster                                         |
| thrift                   | 1.07 ms                                                | 761 us: 1.41x faster                                         |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.63 ms: 1.40x faster                                        |
| 2to3                     | 348 ms                                                 | 253 ms: 1.38x faster                                         |
| sqlglot_normalize        | 143 ms                                                 | 105 ms: 1.36x faster                                         |
| pycparser                | 1.58 sec                                               | 1.16 sec: 1.36x faster                                       |
| scimark_fft              | 466 ms                                                 | 343 ms: 1.36x faster                                         |
| genshi_xml               | 66.0 ms                                                | 48.7 ms: 1.36x faster                                        |
| sympy_sum                | 196 ms                                                 | 146 ms: 1.35x faster                                         |
| sqlalchemy_declarative   | 172 ms                                                 | 128 ms: 1.34x faster                                         |
| xml_etree_process        | 79.1 ms                                                | 59.1 ms: 1.34x faster                                        |
| nqueens                  | 106 ms                                                 | 79.8 ms: 1.33x faster                                        |
| fannkuch                 | 532 ms                                                 | 401 ms: 1.32x faster                                         |
| dulwich_log              | 84.3 ms                                                | 63.8 ms: 1.32x faster                                        |
| sqlglot_optimize         | 69.2 ms                                                | 52.4 ms: 1.32x faster                                        |
| sympy_str                | 346 ms                                                 | 263 ms: 1.31x faster                                         |
| sympy_integrate          | 25.8 ms                                                | 19.7 ms: 1.31x faster                                        |
| docutils                 | 3.30 sec                                               | 2.59 sec: 1.27x faster                                       |
| pathlib                  | 20.5 ms                                                | 16.1 ms: 1.27x faster                                        |
| sympy_expand             | 566 ms                                                 | 446 ms: 1.27x faster                                         |
| xml_etree_parse          | 168 ms                                                 | 139 ms: 1.21x faster                                         |
| xml_etree_iterparse      | 115 ms                                                 | 97.7 ms: 1.18x faster                                        |
| json_dumps               | 14.2 ms                                                | 12.0 ms: 1.18x faster                                        |
| xml_etree_generate       | 99.4 ms                                                | 84.5 ms: 1.18x faster                                        |
| async_generators         | 444 ms                                                 | 382 ms: 1.16x faster                                         |
| mdp                      | 2.85 sec                                               | 2.47 sec: 1.15x faster                                       |
| bench_thread_pool        | 986 us                                                 | 863 us: 1.14x faster                                         |
| python_startup           | 14.6 ms                                                | 12.8 ms: 1.14x faster                                        |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                         |
| regex_effbot             | 3.63 ms                                                | 3.29 ms: 1.10x faster                                        |
| sqlite_synth             | 3.02 us                                                | 2.77 us: 1.09x faster                                        |
| json                     | 5.69 ms                                                | 5.26 ms: 1.08x faster                                        |
| regex_dna                | 227 ms                                                 | 211 ms: 1.08x faster                                         |
| regex_v8                 | 27.8 ms                                                | 26.1 ms: 1.06x faster                                        |
| json_loads               | 31.2 us                                                | 29.8 us: 1.05x faster                                        |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                         |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                         |
| telco                    | 7.27 ms                                                | 7.77 ms: 1.07x slower                                        |
| coverage                 | 79.4 ms                                                | 90.7 ms: 1.14x slower                                        |
| python_startup_no_site   | 5.93 ms                                                | 7.05 ms: 1.19x slower                                        |
| gc_traversal             | 3.62 ms                                                | 4.78 ms: 1.32x slower                                        |
| create_gc_cycles         | 1.62 ms                                                | 2.45 ms: 1.51x slower                                        |
| bench_mp_pool            | 24.0 ms                                                | 81.2 ms: 3.38x slower                                        |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                 |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250117-3.14.0a4+-e537b8b/bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4+-e537b8b.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.453x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.35x
- 95% likely to have a speedup of 1.34x
- 99% likely to have a speedup of 1.32x

# Memory
- memory change: 1.26x