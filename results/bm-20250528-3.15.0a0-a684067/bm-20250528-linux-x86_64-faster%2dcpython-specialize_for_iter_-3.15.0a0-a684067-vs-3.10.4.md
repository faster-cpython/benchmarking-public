# Results vs. 3.10.4

- fork: faster-cpython
- ref: specialize_for_iter_
- machine: linux-x86_64
- commit hash: a684067
- commit date: 2025-05-28
- overall geometric mean: 1.306x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.29x faster
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250528-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 254 ms: 1.37x faster                                                            |
| docutils       | 3.30 sec                                               | 2.57 sec: 1.28x faster                                                          |
| html5lib       | 88.9 ms                                                | 61.3 ms: 1.45x faster                                                           |
| Geometric mean | (ref)                                                  | 1.37x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250528-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 600 ms: 2.95x faster                                                            |
| async_tree_none         | 728 ms                                                 | 263 ms: 2.77x faster                                                            |
| async_tree_memoization  | 870 ms                                                 | 315 ms: 2.76x faster                                                            |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 493 ms: 2.06x faster                                                            |
| Geometric mean          | (ref)                                                  | 2.61x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250528-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 71.4 ms: 1.64x faster                                                           |
| nbody          | 154 ms                                                 | 100 ms: 1.53x faster                                                            |
| pidigits       | 191 ms                                                 | 188 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                  | 1.37x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250528-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 127 ms: 1.48x faster                                                            |
| regex_v8       | 27.8 ms                                                | 23.5 ms: 1.18x faster                                                           |
| regex_effbot   | 3.63 ms                                                | 3.22 ms: 1.13x faster                                                           |
| regex_dna      | 227 ms                                                 | 210 ms: 1.08x faster                                                            |
| Geometric mean | (ref)                                                  | 1.21x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250528-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.98 sec: 1.58x faster                                                          |
| pickle_pure_python   | 484 us                                                 | 316 us: 1.53x faster                                                            |
| unpickle_pure_python | 331 us                                                 | 217 us: 1.53x faster                                                            |
| xml_etree_process    | 79.1 ms                                                | 59.9 ms: 1.32x faster                                                           |
| json_dumps           | 14.2 ms                                                | 11.0 ms: 1.29x faster                                                           |
| xml_etree_parse      | 168 ms                                                 | 141 ms: 1.20x faster                                                            |
| xml_etree_generate   | 99.4 ms                                                | 84.4 ms: 1.18x faster                                                           |
| xml_etree_iterparse  | 115 ms                                                 | 99.0 ms: 1.17x faster                                                           |
| json_loads           | 31.2 us                                                | 29.0 us: 1.08x faster                                                           |
| Geometric mean       | (ref)                                                  | 1.31x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250528-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.2 ms: 1.20x faster                                                           |
| python_startup_no_site | 5.93 ms                                                | 6.92 ms: 1.17x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250528-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 21.5 ms: 1.48x faster                                                           |
| django_template | 48.2 ms                                                | 32.8 ms: 1.47x faster                                                           |
| mako            | 16.3 ms                                                | 11.3 ms: 1.45x faster                                                           |
| genshi_xml      | 66.0 ms                                                | 49.2 ms: 1.34x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250528-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 169 us: 3.22x faster                                                            |
| async_tree_io            | 1.77 sec                                               | 600 ms: 2.95x faster                                                            |
| async_tree_none          | 728 ms                                                 | 263 ms: 2.77x faster                                                            |
| async_tree_memoization   | 870 ms                                                 | 315 ms: 2.76x faster                                                            |
| generators               | 80.1 ms                                                | 29.6 ms: 2.71x faster                                                           |
| mdp                      | 2.85 sec                                               | 1.22 sec: 2.34x faster                                                          |
| deltablue                | 7.91 ms                                                | 3.43 ms: 2.31x faster                                                           |
| go                       | 240 ms                                                 | 111 ms: 2.15x faster                                                            |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 493 ms: 2.06x faster                                                            |
| pylint                   | 551 ms                                                 | 277 ms: 1.99x faster                                                            |
| deepcopy_memo            | 58.5 us                                                | 29.5 us: 1.98x faster                                                           |
| richards_super           | 94.7 ms                                                | 49.2 ms: 1.93x faster                                                           |
| chaos                    | 115 ms                                                 | 60.1 ms: 1.92x faster                                                           |
| deepcopy                 | 479 us                                                 | 254 us: 1.89x faster                                                            |
| raytrace                 | 507 ms                                                 | 269 ms: 1.88x faster                                                            |
| richards                 | 79.3 ms                                                | 42.8 ms: 1.85x faster                                                           |
| scimark_sor              | 220 ms                                                 | 120 ms: 1.82x faster                                                            |
| comprehensions           | 28.8 us                                                | 16.1 us: 1.78x faster                                                           |
| hexiom                   | 10.4 ms                                                | 5.99 ms: 1.74x faster                                                           |
| scimark_monte_carlo      | 118 ms                                                 | 68.1 ms: 1.74x faster                                                           |
| crypto_pyaes             | 128 ms                                                 | 74.0 ms: 1.73x faster                                                           |
| pyflate                  | 716 ms                                                 | 423 ms: 1.69x faster                                                            |
| float                    | 117 ms                                                 | 71.4 ms: 1.64x faster                                                           |
| tomli_loads              | 3.14 sec                                               | 1.98 sec: 1.58x faster                                                          |
| spectral_norm            | 170 ms                                                 | 109 ms: 1.56x faster                                                            |
| deepcopy_reduce          | 4.17 us                                                | 2.68 us: 1.55x faster                                                           |
| nbody                    | 154 ms                                                 | 100 ms: 1.53x faster                                                            |
| pickle_pure_python       | 484 us                                                 | 316 us: 1.53x faster                                                            |
| unpickle_pure_python     | 331 us                                                 | 217 us: 1.53x faster                                                            |
| genshi_text              | 31.8 ms                                                | 21.5 ms: 1.48x faster                                                           |
| regex_compile            | 188 ms                                                 | 127 ms: 1.48x faster                                                            |
| django_template          | 48.2 ms                                                | 32.8 ms: 1.47x faster                                                           |
| scimark_lu               | 176 ms                                                 | 120 ms: 1.47x faster                                                            |
| html5lib                 | 88.9 ms                                                | 61.3 ms: 1.45x faster                                                           |
| mako                     | 16.3 ms                                                | 11.3 ms: 1.45x faster                                                           |
| pycparser                | 1.58 sec                                               | 1.11 sec: 1.41x faster                                                          |
| dulwich_log              | 84.3 ms                                                | 60.0 ms: 1.40x faster                                                           |
| 2to3                     | 348 ms                                                 | 254 ms: 1.37x faster                                                            |
| coroutines               | 35.1 ms                                                | 25.6 ms: 1.37x faster                                                           |
| sympy_integrate          | 25.8 ms                                                | 18.9 ms: 1.37x faster                                                           |
| logging_simple           | 8.30 us                                                | 6.11 us: 1.36x faster                                                           |
| logging_format           | 9.09 us                                                | 6.71 us: 1.35x faster                                                           |
| genshi_xml               | 66.0 ms                                                | 49.2 ms: 1.34x faster                                                           |
| sympy_sum                | 196 ms                                                 | 147 ms: 1.34x faster                                                            |
| xml_etree_process        | 79.1 ms                                                | 59.9 ms: 1.32x faster                                                           |
| nqueens                  | 106 ms                                                 | 80.2 ms: 1.32x faster                                                           |
| pprint_pformat           | 2.10 sec                                               | 1.61 sec: 1.31x faster                                                          |
| sympy_str                | 346 ms                                                 | 265 ms: 1.31x faster                                                            |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.98 ms: 1.30x faster                                                           |
| pprint_safe_repr         | 1.02 sec                                               | 787 ms: 1.29x faster                                                            |
| fannkuch                 | 532 ms                                                 | 413 ms: 1.29x faster                                                            |
| json_dumps               | 14.2 ms                                                | 11.0 ms: 1.29x faster                                                           |
| docutils                 | 3.30 sec                                               | 2.57 sec: 1.28x faster                                                          |
| sympy_expand             | 566 ms                                                 | 448 ms: 1.26x faster                                                            |
| scimark_fft              | 466 ms                                                 | 372 ms: 1.25x faster                                                            |
| python_startup           | 14.6 ms                                                | 12.2 ms: 1.20x faster                                                           |
| pathlib                  | 20.5 ms                                                | 17.1 ms: 1.20x faster                                                           |
| xml_etree_parse          | 168 ms                                                 | 141 ms: 1.20x faster                                                            |
| regex_v8                 | 27.8 ms                                                | 23.5 ms: 1.18x faster                                                           |
| xml_etree_generate       | 99.4 ms                                                | 84.4 ms: 1.18x faster                                                           |
| xml_etree_iterparse      | 115 ms                                                 | 99.0 ms: 1.17x faster                                                           |
| meteor_contest           | 120 ms                                                 | 104 ms: 1.15x faster                                                            |
| regex_effbot             | 3.63 ms                                                | 3.22 ms: 1.13x faster                                                           |
| bench_thread_pool        | 986 us                                                 | 886 us: 1.11x faster                                                            |
| json                     | 5.69 ms                                                | 5.14 ms: 1.11x faster                                                           |
| async_generators         | 444 ms                                                 | 403 ms: 1.10x faster                                                            |
| regex_dna                | 227 ms                                                 | 210 ms: 1.08x faster                                                            |
| json_loads               | 31.2 us                                                | 29.0 us: 1.08x faster                                                           |
| sqlite_synth             | 3.02 us                                                | 2.88 us: 1.05x faster                                                           |
| pidigits                 | 191 ms                                                 | 188 ms: 1.02x faster                                                            |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                            |
| telco                    | 7.27 ms                                                | 7.99 ms: 1.10x slower                                                           |
| python_startup_no_site   | 5.93 ms                                                | 6.92 ms: 1.17x slower                                                           |
| gc_traversal             | 3.62 ms                                                | 5.18 ms: 1.43x slower                                                           |
| create_gc_cycles         | 1.62 ms                                                | 2.59 ms: 1.60x slower                                                           |
| dask                     | 441 ms                                                 | 909 ms: 2.06x slower                                                            |
| logging_silent           | 190 ns                                                 | 471 ns: 2.49x slower                                                            |
| bench_mp_pool            | 24.0 ms                                                | 92.9 ms: 3.87x slower                                                           |
| coverage                 | 79.4 ms                                                | 423 ms: 5.32x slower                                                            |
| thrift                   | 1.07 ms                                                | 149 ms: 138.66x slower                                                          |
| Geometric mean           | (ref)                                                  | 1.26x faster                                                                    |
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (23) of results/bm-20250528-3.15.0a0-a684067/bm-20250528-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.306x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.29x

# Memory
- memory change: 1.31x