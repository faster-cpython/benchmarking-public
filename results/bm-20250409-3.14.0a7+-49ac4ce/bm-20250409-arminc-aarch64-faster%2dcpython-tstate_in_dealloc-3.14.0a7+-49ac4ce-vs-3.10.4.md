# Results vs. 3.10.4

- fork: faster-cpython
- ref: tstate_in_dealloc
- machine: linux-aarch64
- commit hash: 49ac4ce
- commit date: 2025-04-09
- overall geometric mean: 1.344x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250409-arminc-aarch64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 300 ms: 1.27x faster                                                            |
| docutils       | 3.53 sec                                                              | 2.92 sec: 1.21x faster                                                          |
| html5lib       | 86.5 ms                                                               | 63.2 ms: 1.37x faster                                                           |
| Geometric mean | (ref)                                                                 | 1.28x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250409-arminc-aarch64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|-------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 878 ms: 2.60x faster                                                            |
| async_tree_memoization  | 1.13 sec                                                              | 464 ms: 2.44x faster                                                            |
| async_tree_none         | 950 ms                                                                | 389 ms: 2.44x faster                                                            |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 665 ms: 1.91x faster                                                            |
| Geometric mean          | (ref)                                                                 | 2.33x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250409-arminc-aarch64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 86.0 ms: 1.57x faster                                                           |
| nbody          | 166 ms                                                                | 123 ms: 1.35x faster                                                            |
| Geometric mean | (ref)                                                                 | 1.28x faster                                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250409-arminc-aarch64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 123 ms: 1.43x faster                                                            |
| regex_v8       | 32.2 ms                                                               | 28.0 ms: 1.15x faster                                                           |
| regex_effbot   | 4.25 ms                                                               | 3.94 ms: 1.08x faster                                                           |
| regex_dna      | 257 ms                                                                | 242 ms: 1.06x faster                                                            |
| Geometric mean | (ref)                                                                 | 1.17x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250409-arminc-aarch64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 371 us: 1.43x faster                                                            |
| tomli_loads          | 3.36 sec                                                              | 2.45 sec: 1.37x faster                                                          |
| unpickle_pure_python | 366 us                                                                | 268 us: 1.36x faster                                                            |
| xml_etree_process    | 99.5 ms                                                               | 81.1 ms: 1.23x faster                                                           |
| xml_etree_parse      | 212 ms                                                                | 175 ms: 1.21x faster                                                            |
| json_dumps           | 16.7 ms                                                               | 13.9 ms: 1.20x faster                                                           |
| xml_etree_iterparse  | 156 ms                                                                | 141 ms: 1.10x faster                                                            |
| xml_etree_generate   | 123 ms                                                                | 113 ms: 1.08x faster                                                            |
| json_loads           | 30.9 us                                                               | 34.9 us: 1.13x slower                                                           |
| Geometric mean       | (ref)                                                                 | 1.20x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250409-arminc-aarch64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 16.1 ms: 1.44x slower                                                           |
| python_startup_no_site | 6.89 ms                                                               | 10.2 ms: 1.47x slower                                                           |
| Geometric mean         | (ref)                                                                 | 1.46x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250409-arminc-aarch64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 14.1 ms: 1.34x faster                                                           |
| django_template | 53.3 ms                                                               | 39.9 ms: 1.34x faster                                                           |
| genshi_text     | 35.2 ms                                                               | 27.5 ms: 1.28x faster                                                           |
| genshi_xml      | 69.8 ms                                                               | 61.8 ms: 1.13x faster                                                           |
| Geometric mean  | (ref)                                                                 | 1.27x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250409-arminc-aarch64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 198 us: 3.35x faster                                                            |
| async_tree_io            | 2.28 sec                                                              | 878 ms: 2.60x faster                                                            |
| async_tree_memoization   | 1.13 sec                                                              | 464 ms: 2.44x faster                                                            |
| async_tree_none          | 950 ms                                                                | 389 ms: 2.44x faster                                                            |
| deltablue                | 8.94 ms                                                               | 3.83 ms: 2.34x faster                                                           |
| mdp                      | 3.70 sec                                                              | 1.66 sec: 2.23x faster                                                          |
| go                       | 264 ms                                                                | 132 ms: 2.01x faster                                                            |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 665 ms: 1.91x faster                                                            |
| generators               | 68.1 ms                                                               | 36.0 ms: 1.89x faster                                                           |
| richards_super           | 107 ms                                                                | 58.5 ms: 1.83x faster                                                           |
| chaos                    | 121 ms                                                                | 67.8 ms: 1.79x faster                                                           |
| richards                 | 91.7 ms                                                               | 51.8 ms: 1.77x faster                                                           |
| raytrace                 | 573 ms                                                                | 324 ms: 1.77x faster                                                            |
| logging_silent           | 222 ns                                                                | 127 ns: 1.75x faster                                                            |
| scimark_sor              | 246 ms                                                                | 149 ms: 1.66x faster                                                            |
| deepcopy_memo            | 61.7 us                                                               | 38.0 us: 1.63x faster                                                           |
| scimark_lu               | 227 ms                                                                | 140 ms: 1.62x faster                                                            |
| scimark_monte_carlo      | 128 ms                                                                | 80.6 ms: 1.59x faster                                                           |
| float                    | 135 ms                                                                | 86.0 ms: 1.57x faster                                                           |
| crypto_pyaes             | 134 ms                                                                | 85.9 ms: 1.56x faster                                                           |
| deepcopy                 | 511 us                                                                | 328 us: 1.56x faster                                                            |
| comprehensions           | 33.1 us                                                               | 21.5 us: 1.54x faster                                                           |
| pylint                   | 485 ms                                                                | 321 ms: 1.51x faster                                                            |
| hexiom                   | 10.9 ms                                                               | 7.28 ms: 1.50x faster                                                           |
| spectral_norm            | 186 ms                                                                | 126 ms: 1.48x faster                                                            |
| pyflate                  | 795 ms                                                                | 547 ms: 1.45x faster                                                            |
| regex_compile            | 177 ms                                                                | 123 ms: 1.43x faster                                                            |
| pickle_pure_python       | 529 us                                                                | 371 us: 1.43x faster                                                            |
| dulwich_log              | 73.5 ms                                                               | 52.7 ms: 1.39x faster                                                           |
| logging_simple           | 9.78 us                                                               | 7.07 us: 1.38x faster                                                           |
| tomli_loads              | 3.36 sec                                                              | 2.45 sec: 1.37x faster                                                          |
| html5lib                 | 86.5 ms                                                               | 63.2 ms: 1.37x faster                                                           |
| unpickle_pure_python     | 366 us                                                                | 268 us: 1.36x faster                                                            |
| logging_format           | 10.6 us                                                               | 7.79 us: 1.36x faster                                                           |
| nbody                    | 166 ms                                                                | 123 ms: 1.35x faster                                                            |
| deepcopy_reduce          | 4.60 us                                                               | 3.42 us: 1.34x faster                                                           |
| pycparser                | 1.69 sec                                                              | 1.26 sec: 1.34x faster                                                          |
| mako                     | 18.9 ms                                                               | 14.1 ms: 1.34x faster                                                           |
| django_template          | 53.3 ms                                                               | 39.9 ms: 1.34x faster                                                           |
| sqlalchemy_declarative   | 197 ms                                                                | 148 ms: 1.33x faster                                                            |
| sympy_integrate          | 26.5 ms                                                               | 20.1 ms: 1.32x faster                                                           |
| sqlalchemy_imperative    | 20.5 ms                                                               | 15.6 ms: 1.31x faster                                                           |
| sympy_sum                | 184 ms                                                                | 141 ms: 1.30x faster                                                            |
| genshi_text              | 35.2 ms                                                               | 27.5 ms: 1.28x faster                                                           |
| pprint_safe_repr         | 1.15 sec                                                              | 902 ms: 1.27x faster                                                            |
| 2to3                     | 381 ms                                                                | 300 ms: 1.27x faster                                                            |
| pprint_pformat           | 2.36 sec                                                              | 1.86 sec: 1.27x faster                                                          |
| coroutines               | 37.2 ms                                                               | 30.2 ms: 1.23x faster                                                           |
| sympy_str                | 329 ms                                                                | 268 ms: 1.23x faster                                                            |
| xml_etree_process        | 99.5 ms                                                               | 81.1 ms: 1.23x faster                                                           |
| xml_etree_parse          | 212 ms                                                                | 175 ms: 1.21x faster                                                            |
| docutils                 | 3.53 sec                                                              | 2.92 sec: 1.21x faster                                                          |
| json_dumps               | 16.7 ms                                                               | 13.9 ms: 1.20x faster                                                           |
| sympy_expand             | 543 ms                                                                | 458 ms: 1.19x faster                                                            |
| bench_thread_pool        | 1.59 ms                                                               | 1.35 ms: 1.18x faster                                                           |
| nqueens                  | 117 ms                                                                | 100 ms: 1.17x faster                                                            |
| scimark_fft              | 500 ms                                                                | 433 ms: 1.15x faster                                                            |
| pathlib                  | 26.3 ms                                                               | 22.9 ms: 1.15x faster                                                           |
| regex_v8                 | 32.2 ms                                                               | 28.0 ms: 1.15x faster                                                           |
| fannkuch                 | 546 ms                                                                | 479 ms: 1.14x faster                                                            |
| genshi_xml               | 69.8 ms                                                               | 61.8 ms: 1.13x faster                                                           |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.82 ms: 1.12x faster                                                           |
| meteor_contest           | 126 ms                                                                | 113 ms: 1.12x faster                                                            |
| xml_etree_iterparse      | 156 ms                                                                | 141 ms: 1.10x faster                                                            |
| xml_etree_generate       | 123 ms                                                                | 113 ms: 1.08x faster                                                            |
| regex_effbot             | 4.25 ms                                                               | 3.94 ms: 1.08x faster                                                           |
| sqlite_synth             | 4.12 us                                                               | 3.85 us: 1.07x faster                                                           |
| regex_dna                | 257 ms                                                                | 242 ms: 1.06x faster                                                            |
| asyncio_websockets       | 657 ms                                                                | 667 ms: 1.02x slower                                                            |
| json                     | 5.88 ms                                                               | 5.99 ms: 1.02x slower                                                           |
| telco                    | 8.49 ms                                                               | 9.37 ms: 1.10x slower                                                           |
| json_loads               | 30.9 us                                                               | 34.9 us: 1.13x slower                                                           |
| coverage                 | 83.6 ms                                                               | 103 ms: 1.24x slower                                                            |
| python_startup           | 11.2 ms                                                               | 16.1 ms: 1.44x slower                                                           |
| python_startup_no_site   | 6.89 ms                                                               | 10.2 ms: 1.47x slower                                                           |
| create_gc_cycles         | 2.26 ms                                                               | 3.64 ms: 1.61x slower                                                           |
| gc_traversal             | 4.15 ms                                                               | 6.72 ms: 1.62x slower                                                           |
| bench_mp_pool            | 14.5 ms                                                               | 2.46 sec: 169.37x slower                                                        |
| Geometric mean           | (ref)                                                                 | 1.24x faster                                                                    |

Benchmark hidden because not significant (2): pidigits, async_generators
Ignored benchmarks (19) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250409-3.14.0a7+-49ac4ce/bm-20250409-arminc-aarch64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.344x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: 1.31x