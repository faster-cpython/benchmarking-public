# Results vs. 3.10.4

- fork: faster-cpython
- ref: specialize_for_iter_
- machine: linux-x86_64
- commit hash: 08419ee
- commit date: 2025-05-29
- overall geometric mean: 1.299x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x faster
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250529-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-08419ee |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 256 ms: 1.36x faster                                                            |
| docutils       | 3.30 sec                                               | 2.57 sec: 1.28x faster                                                          |
| html5lib       | 88.9 ms                                                | 61.7 ms: 1.44x faster                                                           |
| Geometric mean | (ref)                                                  | 1.36x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250529-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-08419ee |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 602 ms: 2.94x faster                                                            |
| async_tree_none         | 728 ms                                                 | 262 ms: 2.78x faster                                                            |
| async_tree_memoization  | 870 ms                                                 | 314 ms: 2.77x faster                                                            |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 495 ms: 2.05x faster                                                            |
| Geometric mean          | (ref)                                                  | 2.61x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250529-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-08419ee |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 73.0 ms: 1.60x faster                                                           |
| nbody          | 154 ms                                                 | 100 ms: 1.53x faster                                                            |
| pidigits       | 191 ms                                                 | 188 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                  | 1.36x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250529-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-08419ee |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 128 ms: 1.48x faster                                                            |
| regex_v8       | 27.8 ms                                                | 23.2 ms: 1.20x faster                                                           |
| regex_effbot   | 3.63 ms                                                | 3.23 ms: 1.12x faster                                                           |
| regex_dna      | 227 ms                                                 | 209 ms: 1.09x faster                                                            |
| Geometric mean | (ref)                                                  | 1.21x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250529-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-08419ee |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 2.01 sec: 1.56x faster                                                          |
| pickle_pure_python   | 484 us                                                 | 319 us: 1.52x faster                                                            |
| unpickle_pure_python | 331 us                                                 | 219 us: 1.51x faster                                                            |
| xml_etree_process    | 79.1 ms                                                | 59.5 ms: 1.33x faster                                                           |
| json_dumps           | 14.2 ms                                                | 11.2 ms: 1.26x faster                                                           |
| xml_etree_parse      | 168 ms                                                 | 143 ms: 1.17x faster                                                            |
| xml_etree_generate   | 99.4 ms                                                | 84.8 ms: 1.17x faster                                                           |
| xml_etree_iterparse  | 115 ms                                                 | 99.2 ms: 1.16x faster                                                           |
| json_loads           | 31.2 us                                                | 29.8 us: 1.05x faster                                                           |
| Geometric mean       | (ref)                                                  | 1.29x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250529-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-08419ee |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.2 ms: 1.20x faster                                                           |
| python_startup_no_site | 5.93 ms                                                | 6.92 ms: 1.17x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250529-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-08419ee |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 32.3 ms: 1.49x faster                                                           |
| genshi_text     | 31.8 ms                                                | 21.3 ms: 1.49x faster                                                           |
| mako            | 16.3 ms                                                | 11.3 ms: 1.45x faster                                                           |
| genshi_xml      | 66.0 ms                                                | 49.0 ms: 1.35x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250529-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-08419ee |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 168 us: 3.24x faster                                                            |
| async_tree_io            | 1.77 sec                                               | 602 ms: 2.94x faster                                                            |
| async_tree_none          | 728 ms                                                 | 262 ms: 2.78x faster                                                            |
| async_tree_memoization   | 870 ms                                                 | 314 ms: 2.77x faster                                                            |
| generators               | 80.1 ms                                                | 29.8 ms: 2.69x faster                                                           |
| mdp                      | 2.85 sec                                               | 1.23 sec: 2.32x faster                                                          |
| deltablue                | 7.91 ms                                                | 3.55 ms: 2.23x faster                                                           |
| go                       | 240 ms                                                 | 114 ms: 2.11x faster                                                            |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 495 ms: 2.05x faster                                                            |
| pylint                   | 551 ms                                                 | 278 ms: 1.98x faster                                                            |
| deepcopy_memo            | 58.5 us                                                | 29.6 us: 1.98x faster                                                           |
| chaos                    | 115 ms                                                 | 59.6 ms: 1.94x faster                                                           |
| richards_super           | 94.7 ms                                                | 49.8 ms: 1.90x faster                                                           |
| deepcopy                 | 479 us                                                 | 257 us: 1.87x faster                                                            |
| raytrace                 | 507 ms                                                 | 272 ms: 1.86x faster                                                            |
| richards                 | 79.3 ms                                                | 43.6 ms: 1.82x faster                                                           |
| scimark_sor              | 220 ms                                                 | 121 ms: 1.81x faster                                                            |
| comprehensions           | 28.8 us                                                | 16.2 us: 1.77x faster                                                           |
| scimark_monte_carlo      | 118 ms                                                 | 67.8 ms: 1.74x faster                                                           |
| crypto_pyaes             | 128 ms                                                 | 73.9 ms: 1.73x faster                                                           |
| hexiom                   | 10.4 ms                                                | 6.09 ms: 1.71x faster                                                           |
| pyflate                  | 716 ms                                                 | 429 ms: 1.67x faster                                                            |
| float                    | 117 ms                                                 | 73.0 ms: 1.60x faster                                                           |
| tomli_loads              | 3.14 sec                                               | 2.01 sec: 1.56x faster                                                          |
| spectral_norm            | 170 ms                                                 | 110 ms: 1.54x faster                                                            |
| nbody                    | 154 ms                                                 | 100 ms: 1.53x faster                                                            |
| deepcopy_reduce          | 4.17 us                                                | 2.74 us: 1.52x faster                                                           |
| pickle_pure_python       | 484 us                                                 | 319 us: 1.52x faster                                                            |
| unpickle_pure_python     | 331 us                                                 | 219 us: 1.51x faster                                                            |
| django_template          | 48.2 ms                                                | 32.3 ms: 1.49x faster                                                           |
| genshi_text              | 31.8 ms                                                | 21.3 ms: 1.49x faster                                                           |
| scimark_lu               | 176 ms                                                 | 119 ms: 1.48x faster                                                            |
| regex_compile            | 188 ms                                                 | 128 ms: 1.48x faster                                                            |
| mako                     | 16.3 ms                                                | 11.3 ms: 1.45x faster                                                           |
| html5lib                 | 88.9 ms                                                | 61.7 ms: 1.44x faster                                                           |
| dulwich_log              | 84.3 ms                                                | 59.9 ms: 1.41x faster                                                           |
| logging_simple           | 8.30 us                                                | 6.06 us: 1.37x faster                                                           |
| 2to3                     | 348 ms                                                 | 256 ms: 1.36x faster                                                            |
| coroutines               | 35.1 ms                                                | 25.7 ms: 1.36x faster                                                           |
| sympy_integrate          | 25.8 ms                                                | 19.0 ms: 1.36x faster                                                           |
| pycparser                | 1.58 sec                                               | 1.16 sec: 1.36x faster                                                          |
| logging_format           | 9.09 us                                                | 6.74 us: 1.35x faster                                                           |
| genshi_xml               | 66.0 ms                                                | 49.0 ms: 1.35x faster                                                           |
| xml_etree_process        | 79.1 ms                                                | 59.5 ms: 1.33x faster                                                           |
| sympy_sum                | 196 ms                                                 | 149 ms: 1.32x faster                                                            |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.93 ms: 1.31x faster                                                           |
| nqueens                  | 106 ms                                                 | 81.0 ms: 1.31x faster                                                           |
| fannkuch                 | 532 ms                                                 | 408 ms: 1.30x faster                                                            |
| sympy_str                | 346 ms                                                 | 266 ms: 1.30x faster                                                            |
| docutils                 | 3.30 sec                                               | 2.57 sec: 1.28x faster                                                          |
| pprint_pformat           | 2.10 sec                                               | 1.64 sec: 1.28x faster                                                          |
| pprint_safe_repr         | 1.02 sec                                               | 800 ms: 1.27x faster                                                            |
| json_dumps               | 14.2 ms                                                | 11.2 ms: 1.26x faster                                                           |
| sympy_expand             | 566 ms                                                 | 450 ms: 1.26x faster                                                            |
| pathlib                  | 20.5 ms                                                | 16.7 ms: 1.22x faster                                                           |
| scimark_fft              | 466 ms                                                 | 381 ms: 1.22x faster                                                            |
| regex_v8                 | 27.8 ms                                                | 23.2 ms: 1.20x faster                                                           |
| python_startup           | 14.6 ms                                                | 12.2 ms: 1.20x faster                                                           |
| xml_etree_parse          | 168 ms                                                 | 143 ms: 1.17x faster                                                            |
| xml_etree_generate       | 99.4 ms                                                | 84.8 ms: 1.17x faster                                                           |
| xml_etree_iterparse      | 115 ms                                                 | 99.2 ms: 1.16x faster                                                           |
| meteor_contest           | 120 ms                                                 | 105 ms: 1.14x faster                                                            |
| regex_effbot             | 3.63 ms                                                | 3.23 ms: 1.12x faster                                                           |
| bench_thread_pool        | 986 us                                                 | 887 us: 1.11x faster                                                            |
| regex_dna                | 227 ms                                                 | 209 ms: 1.09x faster                                                            |
| async_generators         | 444 ms                                                 | 411 ms: 1.08x faster                                                            |
| sqlite_synth             | 3.02 us                                                | 2.88 us: 1.05x faster                                                           |
| json                     | 5.69 ms                                                | 5.44 ms: 1.05x faster                                                           |
| json_loads               | 31.2 us                                                | 29.8 us: 1.05x faster                                                           |
| pidigits                 | 191 ms                                                 | 188 ms: 1.02x faster                                                            |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                            |
| telco                    | 7.27 ms                                                | 7.97 ms: 1.10x slower                                                           |
| python_startup_no_site   | 5.93 ms                                                | 6.92 ms: 1.17x slower                                                           |
| gc_traversal             | 3.62 ms                                                | 5.08 ms: 1.40x slower                                                           |
| create_gc_cycles         | 1.62 ms                                                | 2.57 ms: 1.59x slower                                                           |
| dask                     | 441 ms                                                 | 912 ms: 2.07x slower                                                            |
| logging_silent           | 190 ns                                                 | 477 ns: 2.51x slower                                                            |
| bench_mp_pool            | 24.0 ms                                                | 93.1 ms: 3.88x slower                                                           |
| coverage                 | 79.4 ms                                                | 428 ms: 5.39x slower                                                            |
| thrift                   | 1.07 ms                                                | 148 ms: 138.56x slower                                                          |
| Geometric mean           | (ref)                                                  | 1.25x faster                                                                    |
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (23) of results/bm-20250529-3.15.0a0-08419ee/bm-20250529-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-08419ee.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.299x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.28x

# Memory
- memory change: 1.31x