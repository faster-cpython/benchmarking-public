# Results vs. 3.10.4

- fork: Fidget-Spinner
- ref: decref_for_nbody
- machine: linux-x86_64
- commit hash: 96ee078
- commit date: 2025-06-25
- overall geometric mean: 1.471x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250625-linux-x86_64-Fidget%2dSpinner-decref_for_nbody-3.15.0a0-96ee078 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 260 ms: 1.34x faster                                                        |
| docutils       | 3.30 sec                                               | 2.65 sec: 1.24x faster                                                      |
| html5lib       | 88.9 ms                                                | 61.6 ms: 1.44x faster                                                       |
| Geometric mean | (ref)                                                  | 1.34x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250625-linux-x86_64-Fidget%2dSpinner-decref_for_nbody-3.15.0a0-96ee078 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 599 ms: 2.95x faster                                                        |
| async_tree_none         | 728 ms                                                 | 260 ms: 2.80x faster                                                        |
| async_tree_memoization  | 870 ms                                                 | 312 ms: 2.79x faster                                                        |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 494 ms: 2.06x faster                                                        |
| Geometric mean          | (ref)                                                  | 2.62x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250625-linux-x86_64-Fidget%2dSpinner-decref_for_nbody-3.15.0a0-96ee078 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 65.5 ms: 1.79x faster                                                       |
| nbody          | 154 ms                                                 | 90.3 ms: 1.70x faster                                                       |
| pidigits       | 191 ms                                                 | 188 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                  | 1.45x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250625-linux-x86_64-Fidget%2dSpinner-decref_for_nbody-3.15.0a0-96ee078 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 127 ms: 1.48x faster                                                        |
| regex_v8       | 27.8 ms                                                | 24.0 ms: 1.15x faster                                                       |
| regex_dna      | 227 ms                                                 | 210 ms: 1.08x faster                                                        |
| regex_effbot   | 3.63 ms                                                | 3.38 ms: 1.07x faster                                                       |
| Geometric mean | (ref)                                                  | 1.19x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250625-linux-x86_64-Fidget%2dSpinner-decref_for_nbody-3.15.0a0-96ee078 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.83 sec: 1.71x faster                                                      |
| unpickle_pure_python | 331 us                                                 | 201 us: 1.65x faster                                                        |
| pickle_pure_python   | 484 us                                                 | 323 us: 1.50x faster                                                        |
| xml_etree_process    | 79.1 ms                                                | 56.0 ms: 1.41x faster                                                       |
| json_dumps           | 14.2 ms                                                | 10.9 ms: 1.29x faster                                                       |
| xml_etree_generate   | 99.4 ms                                                | 80.6 ms: 1.23x faster                                                       |
| xml_etree_parse      | 168 ms                                                 | 141 ms: 1.19x faster                                                        |
| xml_etree_iterparse  | 115 ms                                                 | 98.0 ms: 1.18x faster                                                       |
| json_loads           | 31.2 us                                                | 28.8 us: 1.08x faster                                                       |
| Geometric mean       | (ref)                                                  | 1.35x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250625-linux-x86_64-Fidget%2dSpinner-decref_for_nbody-3.15.0a0-96ee078 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.2 ms: 1.19x faster                                                       |
| python_startup_no_site | 5.93 ms                                                | 6.97 ms: 1.17x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250625-linux-x86_64-Fidget%2dSpinner-decref_for_nbody-3.15.0a0-96ee078 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.8 ms: 1.52x faster                                                       |
| genshi_text     | 31.8 ms                                                | 21.5 ms: 1.48x faster                                                       |
| django_template | 48.2 ms                                                | 32.7 ms: 1.47x faster                                                       |
| genshi_xml      | 66.0 ms                                                | 51.2 ms: 1.29x faster                                                       |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250625-linux-x86_64-Fidget%2dSpinner-decref_for_nbody-3.15.0a0-96ee078 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 167 us: 3.25x faster                                                        |
| async_tree_io            | 1.77 sec                                               | 599 ms: 2.95x faster                                                        |
| async_tree_none          | 728 ms                                                 | 260 ms: 2.80x faster                                                        |
| async_tree_memoization   | 870 ms                                                 | 312 ms: 2.79x faster                                                        |
| generators               | 80.1 ms                                                | 30.0 ms: 2.67x faster                                                       |
| deltablue                | 7.91 ms                                                | 3.13 ms: 2.53x faster                                                       |
| richards_super           | 94.7 ms                                                | 39.7 ms: 2.39x faster                                                       |
| richards                 | 79.3 ms                                                | 33.7 ms: 2.35x faster                                                       |
| mdp                      | 2.85 sec                                               | 1.24 sec: 2.29x faster                                                      |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 494 ms: 2.06x faster                                                        |
| deepcopy_memo            | 58.5 us                                                | 29.3 us: 2.00x faster                                                       |
| go                       | 240 ms                                                 | 120 ms: 1.99x faster                                                        |
| pylint                   | 551 ms                                                 | 283 ms: 1.95x faster                                                        |
| chaos                    | 115 ms                                                 | 60.6 ms: 1.90x faster                                                       |
| deepcopy                 | 479 us                                                 | 257 us: 1.86x faster                                                        |
| scimark_sor              | 220 ms                                                 | 118 ms: 1.86x faster                                                        |
| raytrace                 | 507 ms                                                 | 273 ms: 1.85x faster                                                        |
| scimark_monte_carlo      | 118 ms                                                 | 65.2 ms: 1.81x faster                                                       |
| spectral_norm            | 170 ms                                                 | 94.2 ms: 1.80x faster                                                       |
| float                    | 117 ms                                                 | 65.5 ms: 1.79x faster                                                       |
| djangocms                | 38.4 us                                                | 22.3 us: 1.72x faster                                                       |
| tomli_loads              | 3.14 sec                                               | 1.83 sec: 1.71x faster                                                      |
| nbody                    | 154 ms                                                 | 90.3 ms: 1.70x faster                                                       |
| pyflate                  | 716 ms                                                 | 423 ms: 1.69x faster                                                        |
| crypto_pyaes             | 128 ms                                                 | 75.5 ms: 1.69x faster                                                       |
| comprehensions           | 28.8 us                                                | 17.0 us: 1.69x faster                                                       |
| unpickle_pure_python     | 331 us                                                 | 201 us: 1.65x faster                                                        |
| hexiom                   | 10.4 ms                                                | 6.45 ms: 1.61x faster                                                       |
| deepcopy_reduce          | 4.17 us                                                | 2.66 us: 1.57x faster                                                       |
| mako                     | 16.3 ms                                                | 10.8 ms: 1.52x faster                                                       |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.50x faster                                                        |
| pickle_pure_python       | 484 us                                                 | 323 us: 1.50x faster                                                        |
| regex_compile            | 188 ms                                                 | 127 ms: 1.48x faster                                                        |
| scimark_fft              | 466 ms                                                 | 314 ms: 1.48x faster                                                        |
| genshi_text              | 31.8 ms                                                | 21.5 ms: 1.48x faster                                                       |
| django_template          | 48.2 ms                                                | 32.7 ms: 1.47x faster                                                       |
| html5lib                 | 88.9 ms                                                | 61.6 ms: 1.44x faster                                                       |
| dulwich_log              | 84.3 ms                                                | 59.4 ms: 1.42x faster                                                       |
| xml_etree_process        | 79.1 ms                                                | 56.0 ms: 1.41x faster                                                       |
| thrift                   | 1.07 ms                                                | 762 us: 1.41x faster                                                        |
| coroutines               | 35.1 ms                                                | 25.5 ms: 1.38x faster                                                       |
| logging_simple           | 8.30 us                                                | 6.15 us: 1.35x faster                                                       |
| pycparser                | 1.58 sec                                               | 1.17 sec: 1.35x faster                                                      |
| logging_format           | 9.09 us                                                | 6.77 us: 1.34x faster                                                       |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.82 ms: 1.34x faster                                                       |
| 2to3                     | 348 ms                                                 | 260 ms: 1.34x faster                                                        |
| fannkuch                 | 532 ms                                                 | 397 ms: 1.34x faster                                                        |
| sympy_integrate          | 25.8 ms                                                | 19.4 ms: 1.33x faster                                                       |
| sympy_sum                | 196 ms                                                 | 150 ms: 1.31x faster                                                        |
| json_dumps               | 14.2 ms                                                | 10.9 ms: 1.29x faster                                                       |
| nqueens                  | 106 ms                                                 | 81.7 ms: 1.29x faster                                                       |
| genshi_xml               | 66.0 ms                                                | 51.2 ms: 1.29x faster                                                       |
| pprint_pformat           | 2.10 sec                                               | 1.66 sec: 1.27x faster                                                      |
| sympy_str                | 346 ms                                                 | 273 ms: 1.27x faster                                                        |
| pprint_safe_repr         | 1.02 sec                                               | 803 ms: 1.27x faster                                                        |
| docutils                 | 3.30 sec                                               | 2.65 sec: 1.24x faster                                                      |
| xml_etree_generate       | 99.4 ms                                                | 80.6 ms: 1.23x faster                                                       |
| sympy_expand             | 566 ms                                                 | 469 ms: 1.21x faster                                                        |
| pathlib                  | 20.5 ms                                                | 17.1 ms: 1.20x faster                                                       |
| xml_etree_parse          | 168 ms                                                 | 141 ms: 1.19x faster                                                        |
| python_startup           | 14.6 ms                                                | 12.2 ms: 1.19x faster                                                       |
| xml_etree_iterparse      | 115 ms                                                 | 98.0 ms: 1.18x faster                                                       |
| regex_v8                 | 27.8 ms                                                | 24.0 ms: 1.15x faster                                                       |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                        |
| json_loads               | 31.2 us                                                | 28.8 us: 1.08x faster                                                       |
| sqlite_synth             | 3.02 us                                                | 2.80 us: 1.08x faster                                                       |
| regex_dna                | 227 ms                                                 | 210 ms: 1.08x faster                                                        |
| regex_effbot             | 3.63 ms                                                | 3.38 ms: 1.07x faster                                                       |
| json                     | 5.69 ms                                                | 5.31 ms: 1.07x faster                                                       |
| async_generators         | 444 ms                                                 | 430 ms: 1.03x faster                                                        |
| pidigits                 | 191 ms                                                 | 188 ms: 1.01x faster                                                        |
| asyncio_websockets       | 559 ms                                                 | 554 ms: 1.01x faster                                                        |
| telco                    | 7.27 ms                                                | 7.65 ms: 1.05x slower                                                       |
| coverage                 | 79.4 ms                                                | 87.6 ms: 1.10x slower                                                       |
| python_startup_no_site   | 5.93 ms                                                | 6.97 ms: 1.17x slower                                                       |
| gc_traversal             | 3.62 ms                                                | 4.75 ms: 1.31x slower                                                       |
| create_gc_cycles         | 1.62 ms                                                | 2.60 ms: 1.60x slower                                                       |
| logging_silent           | 190 ns                                                 | 473 ns: 2.49x slower                                                        |
| Geometric mean           | (ref)                                                  | 1.45x faster                                                                |
Ignored benchmarks (23) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250625-3.15.0a0-96ee078-JIT/bm-20250625-linux-x86_64-Fidget%2dSpinner-decref_for_nbody-3.15.0a0-96ee078.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.471x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.33x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.33x