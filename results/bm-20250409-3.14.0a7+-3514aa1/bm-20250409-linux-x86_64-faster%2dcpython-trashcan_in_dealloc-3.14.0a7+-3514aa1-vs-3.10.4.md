# Results vs. 3.10.4

- fork: faster-cpython
- ref: trashcan_in_dealloc
- machine: linux-x86_64
- commit hash: 3514aa1
- commit date: 2025-04-09
- overall geometric mean: 1.456x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.32x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250409-linux-x86_64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 252 ms: 1.38x faster                                                            |
| docutils       | 3.30 sec                                               | 2.60 sec: 1.27x faster                                                          |
| html5lib       | 88.9 ms                                                | 61.1 ms: 1.45x faster                                                           |
| Geometric mean | (ref)                                                  | 1.36x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250409-linux-x86_64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 615 ms: 2.87x faster                                                            |
| async_tree_none         | 728 ms                                                 | 261 ms: 2.79x faster                                                            |
| async_tree_memoization  | 870 ms                                                 | 313 ms: 2.78x faster                                                            |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 486 ms: 2.09x faster                                                            |
| Geometric mean          | (ref)                                                  | 2.61x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250409-linux-x86_64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 70.6 ms: 1.66x faster                                                           |
| nbody          | 154 ms                                                 | 94.6 ms: 1.62x faster                                                           |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                            |
| Geometric mean | (ref)                                                  | 1.40x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250409-linux-x86_64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 125 ms: 1.51x faster                                                            |
| regex_v8       | 27.8 ms                                                | 23.8 ms: 1.17x faster                                                           |
| regex_effbot   | 3.63 ms                                                | 3.26 ms: 1.11x faster                                                           |
| regex_dna      | 227 ms                                                 | 212 ms: 1.07x faster                                                            |
| Geometric mean | (ref)                                                  | 1.20x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250409-linux-x86_64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 2.00 sec: 1.57x faster                                                          |
| pickle_pure_python   | 484 us                                                 | 316 us: 1.53x faster                                                            |
| unpickle_pure_python | 331 us                                                 | 218 us: 1.51x faster                                                            |
| xml_etree_process    | 79.1 ms                                                | 58.9 ms: 1.34x faster                                                           |
| json_dumps           | 14.2 ms                                                | 11.6 ms: 1.22x faster                                                           |
| xml_etree_parse      | 168 ms                                                 | 142 ms: 1.19x faster                                                            |
| xml_etree_generate   | 99.4 ms                                                | 84.8 ms: 1.17x faster                                                           |
| xml_etree_iterparse  | 115 ms                                                 | 98.8 ms: 1.17x faster                                                           |
| json_loads           | 31.2 us                                                | 30.5 us: 1.02x faster                                                           |
| Geometric mean       | (ref)                                                  | 1.29x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250409-linux-x86_64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.2 ms: 1.10x faster                                                           |
| python_startup_no_site | 5.93 ms                                                | 8.23 ms: 1.39x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250409-linux-x86_64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 31.5 ms: 1.53x faster                                                           |
| genshi_text     | 31.8 ms                                                | 21.1 ms: 1.51x faster                                                           |
| mako            | 16.3 ms                                                | 11.5 ms: 1.42x faster                                                           |
| genshi_xml      | 66.0 ms                                                | 49.0 ms: 1.35x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250409-linux-x86_64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 166 us: 3.28x faster                                                            |
| async_tree_io            | 1.77 sec                                               | 615 ms: 2.87x faster                                                            |
| async_tree_none          | 728 ms                                                 | 261 ms: 2.79x faster                                                            |
| async_tree_memoization   | 870 ms                                                 | 313 ms: 2.78x faster                                                            |
| generators               | 80.1 ms                                                | 29.1 ms: 2.76x faster                                                           |
| deltablue                | 7.91 ms                                                | 3.33 ms: 2.38x faster                                                           |
| mdp                      | 2.85 sec                                               | 1.23 sec: 2.31x faster                                                          |
| go                       | 240 ms                                                 | 110 ms: 2.18x faster                                                            |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 486 ms: 2.09x faster                                                            |
| chaos                    | 115 ms                                                 | 57.0 ms: 2.02x faster                                                           |
| deepcopy_memo            | 58.5 us                                                | 29.4 us: 1.99x faster                                                           |
| pylint                   | 551 ms                                                 | 278 ms: 1.98x faster                                                            |
| richards_super           | 94.7 ms                                                | 48.5 ms: 1.95x faster                                                           |
| logging_silent           | 190 ns                                                 | 97.8 ns: 1.94x faster                                                           |
| raytrace                 | 507 ms                                                 | 264 ms: 1.92x faster                                                            |
| deepcopy                 | 479 us                                                 | 253 us: 1.89x faster                                                            |
| richards                 | 79.3 ms                                                | 42.5 ms: 1.86x faster                                                           |
| scimark_sor              | 220 ms                                                 | 120 ms: 1.84x faster                                                            |
| scimark_monte_carlo      | 118 ms                                                 | 65.9 ms: 1.79x faster                                                           |
| crypto_pyaes             | 128 ms                                                 | 74.4 ms: 1.72x faster                                                           |
| hexiom                   | 10.4 ms                                                | 6.12 ms: 1.70x faster                                                           |
| comprehensions           | 28.8 us                                                | 17.0 us: 1.69x faster                                                           |
| float                    | 117 ms                                                 | 70.6 ms: 1.66x faster                                                           |
| spectral_norm            | 170 ms                                                 | 104 ms: 1.63x faster                                                            |
| nbody                    | 154 ms                                                 | 94.6 ms: 1.62x faster                                                           |
| pyflate                  | 716 ms                                                 | 454 ms: 1.58x faster                                                            |
| deepcopy_reduce          | 4.17 us                                                | 2.65 us: 1.57x faster                                                           |
| tomli_loads              | 3.14 sec                                               | 2.00 sec: 1.57x faster                                                          |
| pickle_pure_python       | 484 us                                                 | 316 us: 1.53x faster                                                            |
| django_template          | 48.2 ms                                                | 31.5 ms: 1.53x faster                                                           |
| unpickle_pure_python     | 331 us                                                 | 218 us: 1.51x faster                                                            |
| genshi_text              | 31.8 ms                                                | 21.1 ms: 1.51x faster                                                           |
| logging_simple           | 8.30 us                                                | 5.49 us: 1.51x faster                                                           |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.51x faster                                                            |
| regex_compile            | 188 ms                                                 | 125 ms: 1.51x faster                                                            |
| coroutines               | 35.1 ms                                                | 23.4 ms: 1.50x faster                                                           |
| logging_format           | 9.09 us                                                | 6.06 us: 1.50x faster                                                           |
| html5lib                 | 88.9 ms                                                | 61.1 ms: 1.45x faster                                                           |
| pprint_pformat           | 2.10 sec                                               | 1.47 sec: 1.43x faster                                                          |
| pprint_safe_repr         | 1.02 sec                                               | 714 ms: 1.43x faster                                                            |
| mako                     | 16.3 ms                                                | 11.5 ms: 1.42x faster                                                           |
| pycparser                | 1.58 sec                                               | 1.11 sec: 1.42x faster                                                          |
| dulwich_log              | 84.3 ms                                                | 59.7 ms: 1.41x faster                                                           |
| 2to3                     | 348 ms                                                 | 252 ms: 1.38x faster                                                            |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.71 ms: 1.37x faster                                                           |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.0 ms: 1.37x faster                                                           |
| genshi_xml               | 66.0 ms                                                | 49.0 ms: 1.35x faster                                                           |
| xml_etree_process        | 79.1 ms                                                | 58.9 ms: 1.34x faster                                                           |
| sympy_integrate          | 25.8 ms                                                | 19.2 ms: 1.34x faster                                                           |
| sympy_sum                | 196 ms                                                 | 150 ms: 1.31x faster                                                            |
| scimark_fft              | 466 ms                                                 | 357 ms: 1.30x faster                                                            |
| nqueens                  | 106 ms                                                 | 81.5 ms: 1.30x faster                                                           |
| sqlalchemy_declarative   | 172 ms                                                 | 133 ms: 1.30x faster                                                            |
| sympy_str                | 346 ms                                                 | 269 ms: 1.29x faster                                                            |
| fannkuch                 | 532 ms                                                 | 415 ms: 1.28x faster                                                            |
| docutils                 | 3.30 sec                                               | 2.60 sec: 1.27x faster                                                          |
| sympy_expand             | 566 ms                                                 | 459 ms: 1.23x faster                                                            |
| json_dumps               | 14.2 ms                                                | 11.6 ms: 1.22x faster                                                           |
| pathlib                  | 20.5 ms                                                | 17.0 ms: 1.21x faster                                                           |
| xml_etree_parse          | 168 ms                                                 | 142 ms: 1.19x faster                                                            |
| xml_etree_generate       | 99.4 ms                                                | 84.8 ms: 1.17x faster                                                           |
| xml_etree_iterparse      | 115 ms                                                 | 98.8 ms: 1.17x faster                                                           |
| regex_v8                 | 27.8 ms                                                | 23.8 ms: 1.17x faster                                                           |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                            |
| bench_thread_pool        | 986 us                                                 | 884 us: 1.12x faster                                                            |
| regex_effbot             | 3.63 ms                                                | 3.26 ms: 1.11x faster                                                           |
| python_startup           | 14.6 ms                                                | 13.2 ms: 1.10x faster                                                           |
| async_generators         | 444 ms                                                 | 407 ms: 1.09x faster                                                            |
| sqlite_synth             | 3.02 us                                                | 2.81 us: 1.08x faster                                                           |
| regex_dna                | 227 ms                                                 | 212 ms: 1.07x faster                                                            |
| json                     | 5.69 ms                                                | 5.51 ms: 1.03x faster                                                           |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                            |
| json_loads               | 31.2 us                                                | 30.5 us: 1.02x faster                                                           |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                            |
| coverage                 | 79.4 ms                                                | 85.7 ms: 1.08x slower                                                           |
| telco                    | 7.27 ms                                                | 7.85 ms: 1.08x slower                                                           |
| gc_traversal             | 3.62 ms                                                | 5.03 ms: 1.39x slower                                                           |
| python_startup_no_site   | 5.93 ms                                                | 8.23 ms: 1.39x slower                                                           |
| create_gc_cycles         | 1.62 ms                                                | 2.47 ms: 1.52x slower                                                           |
| bench_mp_pool            | 24.0 ms                                                | 82.4 ms: 3.43x slower                                                           |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                                    |
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250409-3.14.0a7+-3514aa1/bm-20250409-linux-x86_64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.456x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.37x
- 95% likely to have a speedup of 1.35x
- 99% likely to have a speedup of 1.32x

# Memory
- memory change: 1.28x