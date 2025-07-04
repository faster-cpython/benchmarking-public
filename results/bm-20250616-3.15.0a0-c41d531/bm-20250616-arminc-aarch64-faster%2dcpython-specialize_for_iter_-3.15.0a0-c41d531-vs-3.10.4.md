# Results vs. 3.10.4

- fork: faster-cpython
- ref: specialize_for_iter_
- machine: linux-aarch64
- commit hash: c41d531
- commit date: 2025-06-16
- overall geometric mean: 1.231x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: 1.37x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250616-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 303 ms: 1.26x faster                                                              |
| docutils       | 3.53 sec                                                              | 2.93 sec: 1.20x faster                                                            |
| html5lib       | 86.5 ms                                                               | 61.2 ms: 1.41x faster                                                             |
| Geometric mean | (ref)                                                                 | 1.29x faster                                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250616-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|-------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 892 ms: 2.56x faster                                                              |
| async_tree_none         | 950 ms                                                                | 385 ms: 2.47x faster                                                              |
| async_tree_memoization  | 1.13 sec                                                              | 460 ms: 2.46x faster                                                              |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 649 ms: 1.96x faster                                                              |
| Geometric mean          | (ref)                                                                 | 2.35x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250616-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 85.4 ms: 1.58x faster                                                             |
| nbody          | 166 ms                                                                | 125 ms: 1.33x faster                                                              |
| Geometric mean | (ref)                                                                 | 1.28x faster                                                                      |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250616-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 124 ms: 1.42x faster                                                              |
| regex_v8       | 32.2 ms                                                               | 27.4 ms: 1.17x faster                                                             |
| regex_dna      | 257 ms                                                                | 223 ms: 1.15x faster                                                              |
| regex_effbot   | 4.25 ms                                                               | 4.01 ms: 1.06x faster                                                             |
| Geometric mean | (ref)                                                                 | 1.19x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250616-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 263 us: 1.39x faster                                                              |
| tomli_loads          | 3.36 sec                                                              | 2.44 sec: 1.38x faster                                                            |
| pickle_pure_python   | 529 us                                                                | 387 us: 1.37x faster                                                              |
| xml_etree_process    | 99.5 ms                                                               | 79.5 ms: 1.25x faster                                                             |
| json_dumps           | 16.7 ms                                                               | 13.5 ms: 1.24x faster                                                             |
| xml_etree_parse      | 212 ms                                                                | 183 ms: 1.16x faster                                                              |
| xml_etree_generate   | 123 ms                                                                | 112 ms: 1.09x faster                                                              |
| xml_etree_iterparse  | 156 ms                                                                | 143 ms: 1.09x faster                                                              |
| json_loads           | 30.9 us                                                               | 32.7 us: 1.06x slower                                                             |
| Geometric mean       | (ref)                                                                 | 1.20x faster                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250616-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.61 ms: 1.25x slower                                                             |
| python_startup         | 11.2 ms                                                               | 15.1 ms: 1.35x slower                                                             |
| Geometric mean         | (ref)                                                                 | 1.30x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250616-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| django_template | 53.3 ms                                                               | 39.9 ms: 1.34x faster                                                             |
| mako            | 18.9 ms                                                               | 14.2 ms: 1.34x faster                                                             |
| genshi_text     | 35.2 ms                                                               | 28.0 ms: 1.26x faster                                                             |
| genshi_xml      | 69.8 ms                                                               | 60.3 ms: 1.16x faster                                                             |
| Geometric mean  | (ref)                                                                 | 1.27x faster                                                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250616-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 191 us: 3.46x faster                                                              |
| async_tree_io            | 2.28 sec                                                              | 892 ms: 2.56x faster                                                              |
| async_tree_none          | 950 ms                                                                | 385 ms: 2.47x faster                                                              |
| async_tree_memoization   | 1.13 sec                                                              | 460 ms: 2.46x faster                                                              |
| deltablue                | 8.94 ms                                                               | 3.94 ms: 2.27x faster                                                             |
| mdp                      | 3.70 sec                                                              | 1.64 sec: 2.26x faster                                                            |
| go                       | 264 ms                                                                | 128 ms: 2.06x faster                                                              |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 649 ms: 1.96x faster                                                              |
| generators               | 68.1 ms                                                               | 36.1 ms: 1.89x faster                                                             |
| richards_super           | 107 ms                                                                | 58.9 ms: 1.82x faster                                                             |
| chaos                    | 121 ms                                                                | 68.4 ms: 1.77x faster                                                             |
| richards                 | 91.7 ms                                                               | 52.6 ms: 1.74x faster                                                             |
| raytrace                 | 573 ms                                                                | 330 ms: 1.73x faster                                                              |
| deepcopy_memo            | 61.7 us                                                               | 36.2 us: 1.70x faster                                                             |
| scimark_sor              | 246 ms                                                                | 148 ms: 1.67x faster                                                              |
| crypto_pyaes             | 134 ms                                                                | 81.2 ms: 1.65x faster                                                             |
| hexiom                   | 10.9 ms                                                               | 6.72 ms: 1.62x faster                                                             |
| comprehensions           | 33.1 us                                                               | 20.8 us: 1.59x faster                                                             |
| float                    | 135 ms                                                                | 85.4 ms: 1.58x faster                                                             |
| deepcopy                 | 511 us                                                                | 324 us: 1.57x faster                                                              |
| scimark_monte_carlo      | 128 ms                                                                | 81.8 ms: 1.56x faster                                                             |
| pylint                   | 485 ms                                                                | 317 ms: 1.53x faster                                                              |
| scimark_lu               | 227 ms                                                                | 148 ms: 1.53x faster                                                              |
| pyflate                  | 795 ms                                                                | 523 ms: 1.52x faster                                                              |
| spectral_norm            | 186 ms                                                                | 128 ms: 1.46x faster                                                              |
| regex_compile            | 177 ms                                                                | 124 ms: 1.42x faster                                                              |
| html5lib                 | 86.5 ms                                                               | 61.2 ms: 1.41x faster                                                             |
| unpickle_pure_python     | 366 us                                                                | 263 us: 1.39x faster                                                              |
| tomli_loads              | 3.36 sec                                                              | 2.44 sec: 1.38x faster                                                            |
| pickle_pure_python       | 529 us                                                                | 387 us: 1.37x faster                                                              |
| dulwich_log              | 73.5 ms                                                               | 54.0 ms: 1.36x faster                                                             |
| pycparser                | 1.69 sec                                                              | 1.25 sec: 1.35x faster                                                            |
| django_template          | 53.3 ms                                                               | 39.9 ms: 1.34x faster                                                             |
| mako                     | 18.9 ms                                                               | 14.2 ms: 1.34x faster                                                             |
| nbody                    | 166 ms                                                                | 125 ms: 1.33x faster                                                              |
| sympy_integrate          | 26.5 ms                                                               | 20.2 ms: 1.31x faster                                                             |
| sympy_sum                | 184 ms                                                                | 141 ms: 1.30x faster                                                              |
| deepcopy_reduce          | 4.60 us                                                               | 3.54 us: 1.30x faster                                                             |
| logging_simple           | 9.78 us                                                               | 7.62 us: 1.28x faster                                                             |
| logging_format           | 10.6 us                                                               | 8.30 us: 1.28x faster                                                             |
| coroutines               | 37.2 ms                                                               | 29.2 ms: 1.27x faster                                                             |
| 2to3                     | 381 ms                                                                | 303 ms: 1.26x faster                                                              |
| genshi_text              | 35.2 ms                                                               | 28.0 ms: 1.26x faster                                                             |
| xml_etree_process        | 99.5 ms                                                               | 79.5 ms: 1.25x faster                                                             |
| sympy_str                | 329 ms                                                                | 264 ms: 1.24x faster                                                              |
| json_dumps               | 16.7 ms                                                               | 13.5 ms: 1.24x faster                                                             |
| docutils                 | 3.53 sec                                                              | 2.93 sec: 1.20x faster                                                            |
| nqueens                  | 117 ms                                                                | 98.2 ms: 1.20x faster                                                             |
| regex_v8                 | 32.2 ms                                                               | 27.4 ms: 1.17x faster                                                             |
| pprint_pformat           | 2.36 sec                                                              | 2.01 sec: 1.17x faster                                                            |
| meteor_contest           | 126 ms                                                                | 108 ms: 1.17x faster                                                              |
| sympy_expand             | 543 ms                                                                | 466 ms: 1.16x faster                                                              |
| pprint_safe_repr         | 1.15 sec                                                              | 988 ms: 1.16x faster                                                              |
| genshi_xml               | 69.8 ms                                                               | 60.3 ms: 1.16x faster                                                             |
| xml_etree_parse          | 212 ms                                                                | 183 ms: 1.16x faster                                                              |
| regex_dna                | 257 ms                                                                | 223 ms: 1.15x faster                                                              |
| scimark_fft              | 500 ms                                                                | 439 ms: 1.14x faster                                                              |
| pathlib                  | 26.3 ms                                                               | 23.1 ms: 1.14x faster                                                             |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.69 ms: 1.14x faster                                                             |
| fannkuch                 | 546 ms                                                                | 480 ms: 1.14x faster                                                              |
| xml_etree_generate       | 123 ms                                                                | 112 ms: 1.09x faster                                                              |
| xml_etree_iterparse      | 156 ms                                                                | 143 ms: 1.09x faster                                                              |
| sqlite_synth             | 4.12 us                                                               | 3.80 us: 1.08x faster                                                             |
| regex_effbot             | 4.25 ms                                                               | 4.01 ms: 1.06x faster                                                             |
| json                     | 5.88 ms                                                               | 5.63 ms: 1.04x faster                                                             |
| asyncio_websockets       | 657 ms                                                                | 667 ms: 1.02x slower                                                              |
| json_loads               | 30.9 us                                                               | 32.7 us: 1.06x slower                                                             |
| telco                    | 8.49 ms                                                               | 9.20 ms: 1.08x slower                                                             |
| python_startup_no_site   | 6.89 ms                                                               | 8.61 ms: 1.25x slower                                                             |
| python_startup           | 11.2 ms                                                               | 15.1 ms: 1.35x slower                                                             |
| gc_traversal             | 4.15 ms                                                               | 6.96 ms: 1.68x slower                                                             |
| create_gc_cycles         | 2.26 ms                                                               | 3.83 ms: 1.70x slower                                                             |
| logging_silent           | 222 ns                                                                | 609 ns: 2.74x slower                                                              |
| coverage                 | 83.6 ms                                                               | 545 ms: 6.52x slower                                                              |
| thrift                   | 1.26 ms                                                               | 194 ms: 153.88x slower                                                            |
| Geometric mean           | (ref)                                                                 | 1.20x faster                                                                      |

Benchmark hidden because not significant (2): async_generators, pidigits
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250616-3.15.0a0-c41d531/bm-20250616-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.231x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: 1.37x