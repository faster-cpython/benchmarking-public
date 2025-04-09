# Results vs. 3.10.4

- fork: faster-cpython
- ref: trashcan_in_dealloc
- machine: linux-x86_64
- commit hash: 8aa20f2
- commit date: 2025-04-09
- overall geometric mean: 1.457x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.32x faster
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250409-linux-x86_64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 252 ms: 1.38x faster                                                            |
| docutils       | 3.30 sec                                               | 2.59 sec: 1.27x faster                                                          |
| html5lib       | 88.9 ms                                                | 61.0 ms: 1.46x faster                                                           |
| Geometric mean | (ref)                                                  | 1.37x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250409-linux-x86_64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 619 ms: 2.86x faster                                                            |
| async_tree_none         | 728 ms                                                 | 261 ms: 2.79x faster                                                            |
| async_tree_memoization  | 870 ms                                                 | 315 ms: 2.76x faster                                                            |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 490 ms: 2.07x faster                                                            |
| Geometric mean          | (ref)                                                  | 2.60x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250409-linux-x86_64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 89.3 ms: 1.72x faster                                                           |
| float          | 117 ms                                                 | 69.7 ms: 1.68x faster                                                           |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                            |
| Geometric mean | (ref)                                                  | 1.44x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250409-linux-x86_64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 126 ms: 1.50x faster                                                            |
| regex_v8       | 27.8 ms                                                | 22.0 ms: 1.26x faster                                                           |
| regex_effbot   | 3.63 ms                                                | 3.33 ms: 1.09x faster                                                           |
| regex_dna      | 227 ms                                                 | 213 ms: 1.07x faster                                                            |
| Geometric mean | (ref)                                                  | 1.22x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250409-linux-x86_64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.97 sec: 1.59x faster                                                          |
| pickle_pure_python   | 484 us                                                 | 314 us: 1.54x faster                                                            |
| unpickle_pure_python | 331 us                                                 | 218 us: 1.52x faster                                                            |
| xml_etree_process    | 79.1 ms                                                | 58.5 ms: 1.35x faster                                                           |
| json_dumps           | 14.2 ms                                                | 11.8 ms: 1.20x faster                                                           |
| xml_etree_parse      | 168 ms                                                 | 142 ms: 1.18x faster                                                            |
| xml_etree_generate   | 99.4 ms                                                | 84.3 ms: 1.18x faster                                                           |
| xml_etree_iterparse  | 115 ms                                                 | 98.7 ms: 1.17x faster                                                           |
| json_loads           | 31.2 us                                                | 30.3 us: 1.03x faster                                                           |
| Geometric mean       | (ref)                                                  | 1.29x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250409-linux-x86_64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.2 ms: 1.10x faster                                                           |
| python_startup_no_site | 5.93 ms                                                | 8.22 ms: 1.39x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250409-linux-x86_64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 20.9 ms: 1.52x faster                                                           |
| django_template | 48.2 ms                                                | 31.9 ms: 1.51x faster                                                           |
| mako            | 16.3 ms                                                | 11.1 ms: 1.48x faster                                                           |
| genshi_xml      | 66.0 ms                                                | 48.9 ms: 1.35x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.46x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250409-linux-x86_64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 162 us: 3.36x faster                                                            |
| async_tree_io            | 1.77 sec                                               | 619 ms: 2.86x faster                                                            |
| async_tree_none          | 728 ms                                                 | 261 ms: 2.79x faster                                                            |
| async_tree_memoization   | 870 ms                                                 | 315 ms: 2.76x faster                                                            |
| generators               | 80.1 ms                                                | 29.5 ms: 2.72x faster                                                           |
| deltablue                | 7.91 ms                                                | 3.28 ms: 2.41x faster                                                           |
| mdp                      | 2.85 sec                                               | 1.24 sec: 2.30x faster                                                          |
| go                       | 240 ms                                                 | 108 ms: 2.21x faster                                                            |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 490 ms: 2.07x faster                                                            |
| chaos                    | 115 ms                                                 | 58.1 ms: 1.99x faster                                                           |
| pylint                   | 551 ms                                                 | 278 ms: 1.98x faster                                                            |
| deepcopy_memo            | 58.5 us                                                | 29.7 us: 1.97x faster                                                           |
| richards_super           | 94.7 ms                                                | 48.6 ms: 1.95x faster                                                           |
| logging_silent           | 190 ns                                                 | 97.6 ns: 1.94x faster                                                           |
| raytrace                 | 507 ms                                                 | 266 ms: 1.91x faster                                                            |
| scimark_sor              | 220 ms                                                 | 117 ms: 1.88x faster                                                            |
| richards                 | 79.3 ms                                                | 42.5 ms: 1.87x faster                                                           |
| deepcopy                 | 479 us                                                 | 257 us: 1.86x faster                                                            |
| scimark_monte_carlo      | 118 ms                                                 | 66.7 ms: 1.77x faster                                                           |
| nbody                    | 154 ms                                                 | 89.3 ms: 1.72x faster                                                           |
| comprehensions           | 28.8 us                                                | 16.9 us: 1.71x faster                                                           |
| hexiom                   | 10.4 ms                                                | 6.12 ms: 1.70x faster                                                           |
| float                    | 117 ms                                                 | 69.7 ms: 1.68x faster                                                           |
| crypto_pyaes             | 128 ms                                                 | 76.0 ms: 1.68x faster                                                           |
| pyflate                  | 716 ms                                                 | 437 ms: 1.64x faster                                                            |
| spectral_norm            | 170 ms                                                 | 105 ms: 1.62x faster                                                            |
| tomli_loads              | 3.14 sec                                               | 1.97 sec: 1.59x faster                                                          |
| pickle_pure_python       | 484 us                                                 | 314 us: 1.54x faster                                                            |
| deepcopy_reduce          | 4.17 us                                                | 2.72 us: 1.53x faster                                                           |
| genshi_text              | 31.8 ms                                                | 20.9 ms: 1.52x faster                                                           |
| unpickle_pure_python     | 331 us                                                 | 218 us: 1.52x faster                                                            |
| django_template          | 48.2 ms                                                | 31.9 ms: 1.51x faster                                                           |
| regex_compile            | 188 ms                                                 | 126 ms: 1.50x faster                                                            |
| scimark_lu               | 176 ms                                                 | 118 ms: 1.49x faster                                                            |
| logging_simple           | 8.30 us                                                | 5.60 us: 1.48x faster                                                           |
| mako                     | 16.3 ms                                                | 11.1 ms: 1.48x faster                                                           |
| logging_format           | 9.09 us                                                | 6.21 us: 1.46x faster                                                           |
| coroutines               | 35.1 ms                                                | 24.0 ms: 1.46x faster                                                           |
| html5lib                 | 88.9 ms                                                | 61.0 ms: 1.46x faster                                                           |
| pprint_pformat           | 2.10 sec                                               | 1.48 sec: 1.42x faster                                                          |
| pprint_safe_repr         | 1.02 sec                                               | 721 ms: 1.41x faster                                                            |
| dulwich_log              | 84.3 ms                                                | 59.9 ms: 1.41x faster                                                           |
| 2to3                     | 348 ms                                                 | 252 ms: 1.38x faster                                                            |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.0 ms: 1.37x faster                                                           |
| pycparser                | 1.58 sec                                               | 1.15 sec: 1.37x faster                                                          |
| xml_etree_process        | 79.1 ms                                                | 58.5 ms: 1.35x faster                                                           |
| genshi_xml               | 66.0 ms                                                | 48.9 ms: 1.35x faster                                                           |
| sympy_integrate          | 25.8 ms                                                | 19.1 ms: 1.35x faster                                                           |
| sympy_sum                | 196 ms                                                 | 149 ms: 1.32x faster                                                            |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.92 ms: 1.32x faster                                                           |
| scimark_fft              | 466 ms                                                 | 356 ms: 1.31x faster                                                            |
| sqlalchemy_declarative   | 172 ms                                                 | 133 ms: 1.30x faster                                                            |
| nqueens                  | 106 ms                                                 | 81.6 ms: 1.30x faster                                                           |
| sympy_str                | 346 ms                                                 | 269 ms: 1.29x faster                                                            |
| fannkuch                 | 532 ms                                                 | 415 ms: 1.28x faster                                                            |
| docutils                 | 3.30 sec                                               | 2.59 sec: 1.27x faster                                                          |
| regex_v8                 | 27.8 ms                                                | 22.0 ms: 1.26x faster                                                           |
| sympy_expand             | 566 ms                                                 | 459 ms: 1.23x faster                                                            |
| pathlib                  | 20.5 ms                                                | 16.9 ms: 1.21x faster                                                           |
| json_dumps               | 14.2 ms                                                | 11.8 ms: 1.20x faster                                                           |
| xml_etree_parse          | 168 ms                                                 | 142 ms: 1.18x faster                                                            |
| xml_etree_generate       | 99.4 ms                                                | 84.3 ms: 1.18x faster                                                           |
| xml_etree_iterparse      | 115 ms                                                 | 98.7 ms: 1.17x faster                                                           |
| meteor_contest           | 120 ms                                                 | 105 ms: 1.14x faster                                                            |
| bench_thread_pool        | 986 us                                                 | 883 us: 1.12x faster                                                            |
| python_startup           | 14.6 ms                                                | 13.2 ms: 1.10x faster                                                           |
| async_generators         | 444 ms                                                 | 405 ms: 1.10x faster                                                            |
| regex_effbot             | 3.63 ms                                                | 3.33 ms: 1.09x faster                                                           |
| sqlite_synth             | 3.02 us                                                | 2.81 us: 1.08x faster                                                           |
| regex_dna                | 227 ms                                                 | 213 ms: 1.07x faster                                                            |
| json_loads               | 31.2 us                                                | 30.3 us: 1.03x faster                                                           |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                            |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                                            |
| json                     | 5.69 ms                                                | 5.63 ms: 1.01x faster                                                           |
| coverage                 | 79.4 ms                                                | 85.2 ms: 1.07x slower                                                           |
| telco                    | 7.27 ms                                                | 7.99 ms: 1.10x slower                                                           |
| gc_traversal             | 3.62 ms                                                | 4.79 ms: 1.32x slower                                                           |
| python_startup_no_site   | 5.93 ms                                                | 8.22 ms: 1.39x slower                                                           |
| create_gc_cycles         | 1.62 ms                                                | 2.47 ms: 1.52x slower                                                           |
| bench_mp_pool            | 24.0 ms                                                | 82.4 ms: 3.43x slower                                                           |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                                    |
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250409-3.14.0a7+-8aa20f2/bm-20250409-linux-x86_64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.457x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.36x
- 95% likely to have a speedup of 1.35x
- 99% likely to have a speedup of 1.32x

# Memory
- memory change: 1.27x