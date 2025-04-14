# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_mcmodel_again
- machine: linux-x86_64
- commit hash: b13591a
- commit date: 2025-03-04
- overall geometric mean: 1.447x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.31x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250304-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a5+-b13591a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 260 ms: 1.34x faster                                                         |
| docutils       | 3.30 sec                                               | 2.66 sec: 1.24x faster                                                       |
| html5lib       | 88.9 ms                                                | 62.3 ms: 1.43x faster                                                        |
| Geometric mean | (ref)                                                  | 1.33x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250304-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a5+-b13591a |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 610 ms: 2.90x faster                                                         |
| async_tree_none         | 728 ms                                                 | 264 ms: 2.76x faster                                                         |
| async_tree_memoization  | 870 ms                                                 | 332 ms: 2.62x faster                                                         |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 494 ms: 2.06x faster                                                         |
| Geometric mean          | (ref)                                                  | 2.56x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250304-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a5+-b13591a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 86.7 ms: 1.77x faster                                                        |
| float          | 117 ms                                                 | 69.0 ms: 1.70x faster                                                        |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                         |
| Geometric mean | (ref)                                                  | 1.46x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250304-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a5+-b13591a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 127 ms: 1.48x faster                                                         |
| regex_v8       | 27.8 ms                                                | 25.6 ms: 1.08x faster                                                        |
| regex_effbot   | 3.63 ms                                                | 3.46 ms: 1.05x faster                                                        |
| regex_dna      | 227 ms                                                 | 225 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                  | 1.14x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250304-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a5+-b13591a |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.88 sec: 1.67x faster                                                       |
| unpickle_pure_python | 331 us                                                 | 206 us: 1.61x faster                                                         |
| pickle_pure_python   | 484 us                                                 | 325 us: 1.49x faster                                                         |
| xml_etree_process    | 79.1 ms                                                | 55.2 ms: 1.43x faster                                                        |
| xml_etree_generate   | 99.4 ms                                                | 79.1 ms: 1.26x faster                                                        |
| json_dumps           | 14.2 ms                                                | 11.3 ms: 1.25x faster                                                        |
| xml_etree_iterparse  | 115 ms                                                 | 99.0 ms: 1.17x faster                                                        |
| xml_etree_parse      | 168 ms                                                 | 146 ms: 1.15x faster                                                         |
| json_loads           | 31.2 us                                                | 29.8 us: 1.05x faster                                                        |
| Geometric mean       | (ref)                                                  | 1.33x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250304-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a5+-b13591a |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.9 ms: 1.13x faster                                                        |
| python_startup_no_site | 5.93 ms                                                | 7.12 ms: 1.20x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250304-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a5+-b13591a |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.5 ms: 1.55x faster                                                        |
| django_template | 48.2 ms                                                | 31.8 ms: 1.51x faster                                                        |
| genshi_text     | 31.8 ms                                                | 21.9 ms: 1.45x faster                                                        |
| genshi_xml      | 66.0 ms                                                | 49.8 ms: 1.33x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.46x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250304-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a5+-b13591a |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 161 us: 3.37x faster                                                         |
| async_tree_io            | 1.77 sec                                               | 610 ms: 2.90x faster                                                         |
| generators               | 80.1 ms                                                | 28.1 ms: 2.85x faster                                                        |
| async_tree_none          | 728 ms                                                 | 264 ms: 2.76x faster                                                         |
| async_tree_memoization   | 870 ms                                                 | 332 ms: 2.62x faster                                                         |
| deltablue                | 7.91 ms                                                | 3.30 ms: 2.40x faster                                                        |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 494 ms: 2.06x faster                                                         |
| go                       | 240 ms                                                 | 118 ms: 2.04x faster                                                         |
| deepcopy_memo            | 58.5 us                                                | 29.4 us: 1.99x faster                                                        |
| pylint                   | 551 ms                                                 | 279 ms: 1.98x faster                                                         |
| chaos                    | 115 ms                                                 | 59.2 ms: 1.95x faster                                                        |
| richards_super           | 94.7 ms                                                | 50.5 ms: 1.88x faster                                                        |
| raytrace                 | 507 ms                                                 | 272 ms: 1.86x faster                                                         |
| deepcopy                 | 479 us                                                 | 259 us: 1.85x faster                                                         |
| richards                 | 79.3 ms                                                | 43.9 ms: 1.81x faster                                                        |
| scimark_sor              | 220 ms                                                 | 123 ms: 1.78x faster                                                         |
| spectral_norm            | 170 ms                                                 | 95.4 ms: 1.78x faster                                                        |
| logging_silent           | 190 ns                                                 | 107 ns: 1.78x faster                                                         |
| nbody                    | 154 ms                                                 | 86.7 ms: 1.77x faster                                                        |
| scimark_monte_carlo      | 118 ms                                                 | 67.8 ms: 1.74x faster                                                        |
| crypto_pyaes             | 128 ms                                                 | 74.0 ms: 1.73x faster                                                        |
| float                    | 117 ms                                                 | 69.0 ms: 1.70x faster                                                        |
| sqlglot_parse            | 2.17 ms                                                | 1.28 ms: 1.69x faster                                                        |
| tomli_loads              | 3.14 sec                                               | 1.88 sec: 1.67x faster                                                       |
| hexiom                   | 10.4 ms                                                | 6.36 ms: 1.64x faster                                                        |
| comprehensions           | 28.8 us                                                | 17.6 us: 1.63x faster                                                        |
| sqlglot_transpile        | 2.57 ms                                                | 1.59 ms: 1.62x faster                                                        |
| unpickle_pure_python     | 331 us                                                 | 206 us: 1.61x faster                                                         |
| pyflate                  | 716 ms                                                 | 445 ms: 1.61x faster                                                         |
| mako                     | 16.3 ms                                                | 10.5 ms: 1.55x faster                                                        |
| deepcopy_reduce          | 4.17 us                                                | 2.70 us: 1.54x faster                                                        |
| django_template          | 48.2 ms                                                | 31.8 ms: 1.51x faster                                                        |
| scimark_lu               | 176 ms                                                 | 116 ms: 1.51x faster                                                         |
| logging_simple           | 8.30 us                                                | 5.49 us: 1.51x faster                                                        |
| scimark_fft              | 466 ms                                                 | 310 ms: 1.50x faster                                                         |
| pickle_pure_python       | 484 us                                                 | 325 us: 1.49x faster                                                         |
| regex_compile            | 188 ms                                                 | 127 ms: 1.48x faster                                                         |
| logging_format           | 9.09 us                                                | 6.15 us: 1.48x faster                                                        |
| coroutines               | 35.1 ms                                                | 23.9 ms: 1.47x faster                                                        |
| genshi_text              | 31.8 ms                                                | 21.9 ms: 1.45x faster                                                        |
| xml_etree_process        | 79.1 ms                                                | 55.2 ms: 1.43x faster                                                        |
| html5lib                 | 88.9 ms                                                | 62.3 ms: 1.43x faster                                                        |
| pprint_pformat           | 2.10 sec                                               | 1.48 sec: 1.42x faster                                                       |
| thrift                   | 1.07 ms                                                | 761 us: 1.41x faster                                                         |
| pprint_safe_repr         | 1.02 sec                                               | 725 ms: 1.40x faster                                                         |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.7 ms: 1.40x faster                                                        |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.69 ms: 1.38x faster                                                        |
| pycparser                | 1.58 sec                                               | 1.16 sec: 1.36x faster                                                       |
| sqlglot_normalize        | 143 ms                                                 | 106 ms: 1.35x faster                                                         |
| 2to3                     | 348 ms                                                 | 260 ms: 1.34x faster                                                         |
| genshi_xml               | 66.0 ms                                                | 49.8 ms: 1.33x faster                                                        |
| sqlalchemy_declarative   | 172 ms                                                 | 130 ms: 1.32x faster                                                         |
| fannkuch                 | 532 ms                                                 | 404 ms: 1.32x faster                                                         |
| sympy_sum                | 196 ms                                                 | 150 ms: 1.31x faster                                                         |
| nqueens                  | 106 ms                                                 | 81.0 ms: 1.31x faster                                                        |
| sqlglot_optimize         | 69.2 ms                                                | 53.2 ms: 1.30x faster                                                        |
| sympy_integrate          | 25.8 ms                                                | 20.1 ms: 1.28x faster                                                        |
| dulwich_log              | 84.3 ms                                                | 66.8 ms: 1.26x faster                                                        |
| sympy_str                | 346 ms                                                 | 274 ms: 1.26x faster                                                         |
| xml_etree_generate       | 99.4 ms                                                | 79.1 ms: 1.26x faster                                                        |
| json_dumps               | 14.2 ms                                                | 11.3 ms: 1.25x faster                                                        |
| docutils                 | 3.30 sec                                               | 2.66 sec: 1.24x faster                                                       |
| pathlib                  | 20.5 ms                                                | 16.8 ms: 1.22x faster                                                        |
| sympy_expand             | 566 ms                                                 | 469 ms: 1.21x faster                                                         |
| xml_etree_iterparse      | 115 ms                                                 | 99.0 ms: 1.17x faster                                                        |
| xml_etree_parse          | 168 ms                                                 | 146 ms: 1.15x faster                                                         |
| mdp                      | 2.85 sec                                               | 2.49 sec: 1.14x faster                                                       |
| bench_thread_pool        | 986 us                                                 | 874 us: 1.13x faster                                                         |
| python_startup           | 14.6 ms                                                | 12.9 ms: 1.13x faster                                                        |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                         |
| sqlite_synth             | 3.02 us                                                | 2.73 us: 1.11x faster                                                        |
| regex_v8                 | 27.8 ms                                                | 25.6 ms: 1.08x faster                                                        |
| json                     | 5.69 ms                                                | 5.31 ms: 1.07x faster                                                        |
| async_generators         | 444 ms                                                 | 414 ms: 1.07x faster                                                         |
| regex_effbot             | 3.63 ms                                                | 3.46 ms: 1.05x faster                                                        |
| json_loads               | 31.2 us                                                | 29.8 us: 1.05x faster                                                        |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                         |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                         |
| regex_dna                | 227 ms                                                 | 225 ms: 1.01x faster                                                         |
| telco                    | 7.27 ms                                                | 7.69 ms: 1.06x slower                                                        |
| coverage                 | 79.4 ms                                                | 85.2 ms: 1.07x slower                                                        |
| python_startup_no_site   | 5.93 ms                                                | 7.12 ms: 1.20x slower                                                        |
| gc_traversal             | 3.62 ms                                                | 4.63 ms: 1.28x slower                                                        |
| create_gc_cycles         | 1.62 ms                                                | 2.43 ms: 1.50x slower                                                        |
| bench_mp_pool            | 24.0 ms                                                | 81.8 ms: 3.41x slower                                                        |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                                 |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250304-3.14.0a5+-b13591a-JIT/bm-20250304-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a5+-b13591a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.447x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.33x
- 99% likely to have a speedup of 1.31x

# Memory
- memory change: 1.28x