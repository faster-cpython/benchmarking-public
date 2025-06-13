# Results vs. 3.10.4

- fork: Fidget-Spinner
- ref: pylong_compactadd
- machine: linux-x86_64
- commit hash: 4019a15
- commit date: 2025-06-14
- overall geometric mean: 1.327x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.29x faster
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250614-linux-x86_64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 254 ms: 1.37x faster                                                         |
| docutils       | 3.30 sec                                               | 2.57 sec: 1.28x faster                                                       |
| html5lib       | 88.9 ms                                                | 61.7 ms: 1.44x faster                                                        |
| Geometric mean | (ref)                                                  | 1.36x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250614-linux-x86_64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 599 ms: 2.95x faster                                                         |
| async_tree_none         | 728 ms                                                 | 261 ms: 2.79x faster                                                         |
| async_tree_memoization  | 870 ms                                                 | 313 ms: 2.78x faster                                                         |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 487 ms: 2.08x faster                                                         |
| Geometric mean          | (ref)                                                  | 2.63x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250614-linux-x86_64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 72.4 ms: 1.62x faster                                                        |
| nbody          | 154 ms                                                 | 97.5 ms: 1.57x faster                                                        |
| pidigits       | 191 ms                                                 | 189 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                  | 1.37x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250614-linux-x86_64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 127 ms: 1.48x faster                                                         |
| regex_v8       | 27.8 ms                                                | 22.1 ms: 1.26x faster                                                        |
| regex_dna      | 227 ms                                                 | 183 ms: 1.24x faster                                                         |
| regex_effbot   | 3.63 ms                                                | 3.06 ms: 1.18x faster                                                        |
| Geometric mean | (ref)                                                  | 1.29x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250614-linux-x86_64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 2.01 sec: 1.56x faster                                                       |
| unpickle_pure_python | 331 us                                                 | 217 us: 1.52x faster                                                         |
| pickle_pure_python   | 484 us                                                 | 320 us: 1.51x faster                                                         |
| xml_etree_process    | 79.1 ms                                                | 60.0 ms: 1.32x faster                                                        |
| json_dumps           | 14.2 ms                                                | 11.0 ms: 1.29x faster                                                        |
| xml_etree_parse      | 168 ms                                                 | 143 ms: 1.17x faster                                                         |
| xml_etree_iterparse  | 115 ms                                                 | 98.5 ms: 1.17x faster                                                        |
| xml_etree_generate   | 99.4 ms                                                | 85.5 ms: 1.16x faster                                                        |
| json_loads           | 31.2 us                                                | 28.2 us: 1.11x faster                                                        |
| Geometric mean       | (ref)                                                  | 1.30x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250614-linux-x86_64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.1 ms: 1.20x faster                                                        |
| python_startup_no_site | 5.93 ms                                                | 6.90 ms: 1.16x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250614-linux-x86_64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 21.1 ms: 1.51x faster                                                        |
| django_template | 48.2 ms                                                | 32.6 ms: 1.48x faster                                                        |
| mako            | 16.3 ms                                                | 11.8 ms: 1.39x faster                                                        |
| genshi_xml      | 66.0 ms                                                | 49.2 ms: 1.34x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250614-linux-x86_64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 168 us: 3.23x faster                                                         |
| async_tree_io            | 1.77 sec                                               | 599 ms: 2.95x faster                                                         |
| async_tree_none          | 728 ms                                                 | 261 ms: 2.79x faster                                                         |
| async_tree_memoization   | 870 ms                                                 | 313 ms: 2.78x faster                                                         |
| generators               | 80.1 ms                                                | 30.3 ms: 2.64x faster                                                        |
| mdp                      | 2.85 sec                                               | 1.22 sec: 2.33x faster                                                       |
| deltablue                | 7.91 ms                                                | 3.50 ms: 2.26x faster                                                        |
| go                       | 240 ms                                                 | 111 ms: 2.17x faster                                                         |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 487 ms: 2.08x faster                                                         |
| deepcopy_memo            | 58.5 us                                                | 29.2 us: 2.00x faster                                                        |
| pylint                   | 551 ms                                                 | 279 ms: 1.98x faster                                                         |
| richards_super           | 94.7 ms                                                | 49.3 ms: 1.92x faster                                                        |
| scimark_sor              | 220 ms                                                 | 116 ms: 1.90x faster                                                         |
| chaos                    | 115 ms                                                 | 61.1 ms: 1.89x faster                                                        |
| deepcopy                 | 479 us                                                 | 254 us: 1.89x faster                                                         |
| raytrace                 | 507 ms                                                 | 273 ms: 1.86x faster                                                         |
| richards                 | 79.3 ms                                                | 43.3 ms: 1.83x faster                                                        |
| comprehensions           | 28.8 us                                                | 15.9 us: 1.81x faster                                                        |
| scimark_monte_carlo      | 118 ms                                                 | 67.2 ms: 1.76x faster                                                        |
| hexiom                   | 10.4 ms                                                | 6.03 ms: 1.72x faster                                                        |
| crypto_pyaes             | 128 ms                                                 | 75.6 ms: 1.69x faster                                                        |
| pyflate                  | 716 ms                                                 | 427 ms: 1.68x faster                                                         |
| spectral_norm            | 170 ms                                                 | 104 ms: 1.63x faster                                                         |
| float                    | 117 ms                                                 | 72.4 ms: 1.62x faster                                                        |
| nbody                    | 154 ms                                                 | 97.5 ms: 1.57x faster                                                        |
| tomli_loads              | 3.14 sec                                               | 2.01 sec: 1.56x faster                                                       |
| deepcopy_reduce          | 4.17 us                                                | 2.69 us: 1.55x faster                                                        |
| unpickle_pure_python     | 331 us                                                 | 217 us: 1.52x faster                                                         |
| pickle_pure_python       | 484 us                                                 | 320 us: 1.51x faster                                                         |
| genshi_text              | 31.8 ms                                                | 21.1 ms: 1.51x faster                                                        |
| regex_compile            | 188 ms                                                 | 127 ms: 1.48x faster                                                         |
| django_template          | 48.2 ms                                                | 32.6 ms: 1.48x faster                                                        |
| scimark_lu               | 176 ms                                                 | 119 ms: 1.48x faster                                                         |
| html5lib                 | 88.9 ms                                                | 61.7 ms: 1.44x faster                                                        |
| coroutines               | 35.1 ms                                                | 24.5 ms: 1.43x faster                                                        |
| dulwich_log              | 84.3 ms                                                | 59.2 ms: 1.42x faster                                                        |
| pycparser                | 1.58 sec                                               | 1.12 sec: 1.41x faster                                                       |
| mako                     | 16.3 ms                                                | 11.8 ms: 1.39x faster                                                        |
| 2to3                     | 348 ms                                                 | 254 ms: 1.37x faster                                                         |
| sympy_integrate          | 25.8 ms                                                | 19.0 ms: 1.36x faster                                                        |
| logging_simple           | 8.30 us                                                | 6.13 us: 1.35x faster                                                        |
| genshi_xml               | 66.0 ms                                                | 49.2 ms: 1.34x faster                                                        |
| sympy_sum                | 196 ms                                                 | 149 ms: 1.32x faster                                                         |
| xml_etree_process        | 79.1 ms                                                | 60.0 ms: 1.32x faster                                                        |
| logging_format           | 9.09 us                                                | 6.94 us: 1.31x faster                                                        |
| nqueens                  | 106 ms                                                 | 81.3 ms: 1.30x faster                                                        |
| sympy_str                | 346 ms                                                 | 267 ms: 1.29x faster                                                         |
| json_dumps               | 14.2 ms                                                | 11.0 ms: 1.29x faster                                                        |
| fannkuch                 | 532 ms                                                 | 412 ms: 1.29x faster                                                         |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.02 ms: 1.29x faster                                                        |
| docutils                 | 3.30 sec                                               | 2.57 sec: 1.28x faster                                                       |
| scimark_fft              | 466 ms                                                 | 367 ms: 1.27x faster                                                         |
| pprint_pformat           | 2.10 sec                                               | 1.66 sec: 1.26x faster                                                       |
| regex_v8                 | 27.8 ms                                                | 22.1 ms: 1.26x faster                                                        |
| pprint_safe_repr         | 1.02 sec                                               | 813 ms: 1.25x faster                                                         |
| sympy_expand             | 566 ms                                                 | 452 ms: 1.25x faster                                                         |
| regex_dna                | 227 ms                                                 | 183 ms: 1.24x faster                                                         |
| python_startup           | 14.6 ms                                                | 12.1 ms: 1.20x faster                                                        |
| pathlib                  | 20.5 ms                                                | 17.0 ms: 1.20x faster                                                        |
| regex_effbot             | 3.63 ms                                                | 3.06 ms: 1.18x faster                                                        |
| xml_etree_parse          | 168 ms                                                 | 143 ms: 1.17x faster                                                         |
| xml_etree_iterparse      | 115 ms                                                 | 98.5 ms: 1.17x faster                                                        |
| xml_etree_generate       | 99.4 ms                                                | 85.5 ms: 1.16x faster                                                        |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                         |
| json_loads               | 31.2 us                                                | 28.2 us: 1.11x faster                                                        |
| json                     | 5.69 ms                                                | 5.27 ms: 1.08x faster                                                        |
| async_generators         | 444 ms                                                 | 418 ms: 1.06x faster                                                         |
| sqlite_synth             | 3.02 us                                                | 2.88 us: 1.05x faster                                                        |
| asyncio_websockets       | 559 ms                                                 | 553 ms: 1.01x faster                                                         |
| pidigits                 | 191 ms                                                 | 189 ms: 1.01x faster                                                         |
| telco                    | 7.27 ms                                                | 7.99 ms: 1.10x slower                                                        |
| python_startup_no_site   | 5.93 ms                                                | 6.90 ms: 1.16x slower                                                        |
| gc_traversal             | 3.62 ms                                                | 4.90 ms: 1.35x slower                                                        |
| create_gc_cycles         | 1.62 ms                                                | 2.58 ms: 1.59x slower                                                        |
| logging_silent           | 190 ns                                                 | 473 ns: 2.49x slower                                                         |
| coverage                 | 79.4 ms                                                | 423 ms: 5.32x slower                                                         |
| thrift                   | 1.07 ms                                                | 147 ms: 137.58x slower                                                       |
| Geometric mean           | (ref)                                                  | 1.31x faster                                                                 |
Ignored benchmarks (24) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250614-3.15.0a0-4019a15/bm-20250614-linux-x86_64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.327x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.29x

# Memory
- memory change: 1.31x