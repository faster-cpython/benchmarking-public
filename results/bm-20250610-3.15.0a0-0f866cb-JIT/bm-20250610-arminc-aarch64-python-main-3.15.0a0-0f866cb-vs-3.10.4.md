# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-aarch64
- commit hash: 0f866cb
- commit date: 2025-06-10
- overall geometric mean: 1.203x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: 1.40x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250610-arminc-aarch64-python-main-3.15.0a0-0f866cb |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 312 ms: 1.22x faster                                    |
| docutils       | 3.53 sec                                                              | 3.09 sec: 1.14x faster                                  |
| html5lib       | 86.5 ms                                                               | 63.2 ms: 1.37x faster                                   |
| Geometric mean | (ref)                                                                 | 1.24x faster                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250610-arminc-aarch64-python-main-3.15.0a0-0f866cb |
|-------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 897 ms: 2.55x faster                                    |
| async_tree_none         | 950 ms                                                                | 400 ms: 2.37x faster                                    |
| async_tree_memoization  | 1.13 sec                                                              | 478 ms: 2.37x faster                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 666 ms: 1.91x faster                                    |
| Geometric mean          | (ref)                                                                 | 2.29x faster                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250610-arminc-aarch64-python-main-3.15.0a0-0f866cb |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------:|
| float          | 135 ms                                                                | 82.8 ms: 1.63x faster                                   |
| nbody          | 166 ms                                                                | 119 ms: 1.40x faster                                    |
| Geometric mean | (ref)                                                                 | 1.32x faster                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250610-arminc-aarch64-python-main-3.15.0a0-0f866cb |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 122 ms: 1.45x faster                                    |
| regex_v8       | 32.2 ms                                                               | 27.1 ms: 1.18x faster                                   |
| regex_dna      | 257 ms                                                                | 223 ms: 1.15x faster                                    |
| regex_effbot   | 4.25 ms                                                               | 4.02 ms: 1.06x faster                                   |
| Geometric mean | (ref)                                                                 | 1.20x faster                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250610-arminc-aarch64-python-main-3.15.0a0-0f866cb |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 248 us: 1.48x faster                                    |
| tomli_loads          | 3.36 sec                                                              | 2.37 sec: 1.42x faster                                  |
| pickle_pure_python   | 529 us                                                                | 388 us: 1.37x faster                                    |
| xml_etree_process    | 99.5 ms                                                               | 79.2 ms: 1.26x faster                                   |
| json_dumps           | 16.7 ms                                                               | 13.9 ms: 1.20x faster                                   |
| xml_etree_parse      | 212 ms                                                                | 179 ms: 1.19x faster                                    |
| xml_etree_generate   | 123 ms                                                                | 110 ms: 1.12x faster                                    |
| xml_etree_iterparse  | 156 ms                                                                | 143 ms: 1.09x faster                                    |
| json_loads           | 30.9 us                                                               | 32.7 us: 1.06x slower                                   |
| Geometric mean       | (ref)                                                                 | 1.22x faster                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250610-arminc-aarch64-python-main-3.15.0a0-0f866cb |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.62 ms: 1.25x slower                                   |
| python_startup         | 11.2 ms                                                               | 15.1 ms: 1.35x slower                                   |
| Geometric mean         | (ref)                                                                 | 1.30x slower                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250610-arminc-aarch64-python-main-3.15.0a0-0f866cb |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.6 ms: 1.40x faster                                   |
| django_template | 53.3 ms                                                               | 41.7 ms: 1.28x faster                                   |
| genshi_text     | 35.2 ms                                                               | 27.7 ms: 1.27x faster                                   |
| genshi_xml      | 69.8 ms                                                               | 63.4 ms: 1.10x faster                                   |
| Geometric mean  | (ref)                                                                 | 1.26x faster                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250610-arminc-aarch64-python-main-3.15.0a0-0f866cb |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 205 us: 3.22x faster                                    |
| async_tree_io            | 2.28 sec                                                              | 897 ms: 2.55x faster                                    |
| async_tree_none          | 950 ms                                                                | 400 ms: 2.37x faster                                    |
| async_tree_memoization   | 1.13 sec                                                              | 478 ms: 2.37x faster                                    |
| deltablue                | 8.94 ms                                                               | 3.97 ms: 2.25x faster                                   |
| mdp                      | 3.70 sec                                                              | 1.68 sec: 2.20x faster                                  |
| richards_super           | 107 ms                                                                | 51.1 ms: 2.10x faster                                   |
| richards                 | 91.7 ms                                                               | 44.7 ms: 2.05x faster                                   |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 666 ms: 1.91x faster                                    |
| generators               | 68.1 ms                                                               | 35.9 ms: 1.89x faster                                   |
| chaos                    | 121 ms                                                                | 70.6 ms: 1.71x faster                                   |
| raytrace                 | 573 ms                                                                | 336 ms: 1.71x faster                                    |
| scimark_sor              | 246 ms                                                                | 145 ms: 1.70x faster                                    |
| go                       | 264 ms                                                                | 159 ms: 1.66x faster                                    |
| float                    | 135 ms                                                                | 82.8 ms: 1.63x faster                                   |
| deepcopy_memo            | 61.7 us                                                               | 38.2 us: 1.61x faster                                   |
| scimark_monte_carlo      | 128 ms                                                                | 82.9 ms: 1.54x faster                                   |
| pylint                   | 485 ms                                                                | 322 ms: 1.51x faster                                    |
| deepcopy                 | 511 us                                                                | 345 us: 1.48x faster                                    |
| unpickle_pure_python     | 366 us                                                                | 248 us: 1.48x faster                                    |
| scimark_lu               | 227 ms                                                                | 154 ms: 1.47x faster                                    |
| comprehensions           | 33.1 us                                                               | 22.7 us: 1.46x faster                                   |
| hexiom                   | 10.9 ms                                                               | 7.49 ms: 1.46x faster                                   |
| regex_compile            | 177 ms                                                                | 122 ms: 1.45x faster                                    |
| pyflate                  | 795 ms                                                                | 549 ms: 1.45x faster                                    |
| crypto_pyaes             | 134 ms                                                                | 92.8 ms: 1.44x faster                                   |
| tomli_loads              | 3.36 sec                                                              | 2.37 sec: 1.42x faster                                  |
| nbody                    | 166 ms                                                                | 119 ms: 1.40x faster                                    |
| spectral_norm            | 186 ms                                                                | 134 ms: 1.40x faster                                    |
| mako                     | 18.9 ms                                                               | 13.6 ms: 1.40x faster                                   |
| html5lib                 | 86.5 ms                                                               | 63.2 ms: 1.37x faster                                   |
| pickle_pure_python       | 529 us                                                                | 388 us: 1.37x faster                                    |
| dulwich_log              | 73.5 ms                                                               | 55.8 ms: 1.32x faster                                   |
| logging_simple           | 9.78 us                                                               | 7.57 us: 1.29x faster                                   |
| django_template          | 53.3 ms                                                               | 41.7 ms: 1.28x faster                                   |
| logging_format           | 10.6 us                                                               | 8.34 us: 1.27x faster                                   |
| genshi_text              | 35.2 ms                                                               | 27.7 ms: 1.27x faster                                   |
| deepcopy_reduce          | 4.60 us                                                               | 3.63 us: 1.27x faster                                   |
| coroutines               | 37.2 ms                                                               | 29.4 ms: 1.26x faster                                   |
| sympy_integrate          | 26.5 ms                                                               | 21.0 ms: 1.26x faster                                   |
| xml_etree_process        | 99.5 ms                                                               | 79.2 ms: 1.26x faster                                   |
| 2to3                     | 381 ms                                                                | 312 ms: 1.22x faster                                    |
| pycparser                | 1.69 sec                                                              | 1.40 sec: 1.21x faster                                  |
| json_dumps               | 16.7 ms                                                               | 13.9 ms: 1.20x faster                                   |
| sympy_sum                | 184 ms                                                                | 154 ms: 1.20x faster                                    |
| xml_etree_parse          | 212 ms                                                                | 179 ms: 1.19x faster                                    |
| regex_v8                 | 32.2 ms                                                               | 27.1 ms: 1.18x faster                                   |
| scimark_fft              | 500 ms                                                                | 424 ms: 1.18x faster                                    |
| nqueens                  | 117 ms                                                                | 101 ms: 1.16x faster                                    |
| sympy_str                | 329 ms                                                                | 284 ms: 1.16x faster                                    |
| regex_dna                | 257 ms                                                                | 223 ms: 1.15x faster                                    |
| docutils                 | 3.53 sec                                                              | 3.09 sec: 1.14x faster                                  |
| fannkuch                 | 546 ms                                                                | 483 ms: 1.13x faster                                    |
| pathlib                  | 26.3 ms                                                               | 23.5 ms: 1.12x faster                                   |
| xml_etree_generate       | 123 ms                                                                | 110 ms: 1.12x faster                                    |
| sqlite_synth             | 4.12 us                                                               | 3.71 us: 1.11x faster                                   |
| sympy_expand             | 543 ms                                                                | 490 ms: 1.11x faster                                    |
| genshi_xml               | 69.8 ms                                                               | 63.4 ms: 1.10x faster                                   |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.93 ms: 1.10x faster                                   |
| xml_etree_iterparse      | 156 ms                                                                | 143 ms: 1.09x faster                                    |
| meteor_contest           | 126 ms                                                                | 116 ms: 1.09x faster                                    |
| regex_effbot             | 4.25 ms                                                               | 4.02 ms: 1.06x faster                                   |
| json                     | 5.88 ms                                                               | 5.67 ms: 1.04x faster                                   |
| asyncio_websockets       | 657 ms                                                                | 666 ms: 1.01x slower                                    |
| async_generators         | 452 ms                                                                | 475 ms: 1.05x slower                                    |
| json_loads               | 30.9 us                                                               | 32.7 us: 1.06x slower                                   |
| pprint_safe_repr         | 1.15 sec                                                              | 1.25 sec: 1.09x slower                                  |
| pprint_pformat           | 2.36 sec                                                              | 2.58 sec: 1.10x slower                                  |
| telco                    | 8.49 ms                                                               | 9.45 ms: 1.11x slower                                   |
| python_startup_no_site   | 6.89 ms                                                               | 8.62 ms: 1.25x slower                                   |
| python_startup           | 11.2 ms                                                               | 15.1 ms: 1.35x slower                                   |
| create_gc_cycles         | 2.26 ms                                                               | 3.76 ms: 1.67x slower                                   |
| gc_traversal             | 4.15 ms                                                               | 7.06 ms: 1.70x slower                                   |
| logging_silent           | 222 ns                                                                | 606 ns: 2.73x slower                                    |
| coverage                 | 83.6 ms                                                               | 554 ms: 6.63x slower                                    |
| thrift                   | 1.26 ms                                                               | 191 ms: 151.23x slower                                  |
| Geometric mean           | (ref)                                                                 | 1.17x faster                                            |

Benchmark hidden because not significant (1): pidigits
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250610-3.15.0a0-0f866cb-JIT/bm-20250610-arminc-aarch64-python-main-3.15.0a0-0f866cb.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.203x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.22x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: 1.40x