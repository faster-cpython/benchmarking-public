# Results vs. 3.10.4

- fork: faster-cpython
- ref: immortal_stickiness
- machine: linux-aarch64
- commit hash: 2a08194
- commit date: 2025-03-12
- overall geometric mean: 1.324x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250312-arminc-aarch64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 297 ms: 1.28x faster                                                              |
| docutils       | 3.53 sec                                                              | 2.96 sec: 1.19x faster                                                            |
| html5lib       | 86.5 ms                                                               | 64.2 ms: 1.35x faster                                                             |
| Geometric mean | (ref)                                                                 | 1.27x faster                                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250312-arminc-aarch64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|-------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 881 ms: 2.59x faster                                                              |
| async_tree_none         | 950 ms                                                                | 386 ms: 2.46x faster                                                              |
| async_tree_memoization  | 1.13 sec                                                              | 474 ms: 2.39x faster                                                              |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 657 ms: 1.94x faster                                                              |
| Geometric mean          | (ref)                                                                 | 2.33x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250312-arminc-aarch64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 87.5 ms: 1.54x faster                                                             |
| nbody          | 166 ms                                                                | 126 ms: 1.32x faster                                                              |
| Geometric mean | (ref)                                                                 | 1.26x faster                                                                      |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250312-arminc-aarch64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 125 ms: 1.41x faster                                                              |
| regex_v8       | 32.2 ms                                                               | 28.5 ms: 1.13x faster                                                             |
| regex_effbot   | 4.25 ms                                                               | 3.98 ms: 1.07x faster                                                             |
| regex_dna      | 257 ms                                                                | 241 ms: 1.07x faster                                                              |
| Geometric mean | (ref)                                                                 | 1.16x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250312-arminc-aarch64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 264 us: 1.39x faster                                                              |
| tomli_loads          | 3.36 sec                                                              | 2.42 sec: 1.39x faster                                                            |
| pickle_pure_python   | 529 us                                                                | 395 us: 1.34x faster                                                              |
| xml_etree_process    | 99.5 ms                                                               | 79.2 ms: 1.26x faster                                                             |
| json_dumps           | 16.7 ms                                                               | 13.8 ms: 1.21x faster                                                             |
| xml_etree_parse      | 212 ms                                                                | 176 ms: 1.20x faster                                                              |
| xml_etree_generate   | 123 ms                                                                | 111 ms: 1.11x faster                                                              |
| xml_etree_iterparse  | 156 ms                                                                | 141 ms: 1.11x faster                                                              |
| json_loads           | 30.9 us                                                               | 33.9 us: 1.10x slower                                                             |
| Geometric mean       | (ref)                                                                 | 1.20x faster                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250312-arminc-aarch64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 16.2 ms: 1.45x slower                                                             |
| python_startup_no_site | 6.89 ms                                                               | 10.3 ms: 1.49x slower                                                             |
| Geometric mean         | (ref)                                                                 | 1.47x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250312-arminc-aarch64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 14.0 ms: 1.35x faster                                                             |
| genshi_text     | 35.2 ms                                                               | 26.8 ms: 1.31x faster                                                             |
| django_template | 53.3 ms                                                               | 41.5 ms: 1.28x faster                                                             |
| genshi_xml      | 69.8 ms                                                               | 60.4 ms: 1.16x faster                                                             |
| Geometric mean  | (ref)                                                                 | 1.27x faster                                                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250312-arminc-aarch64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 196 us: 3.37x faster                                                              |
| async_tree_io            | 2.28 sec                                                              | 881 ms: 2.59x faster                                                              |
| async_tree_none          | 950 ms                                                                | 386 ms: 2.46x faster                                                              |
| async_tree_memoization   | 1.13 sec                                                              | 474 ms: 2.39x faster                                                              |
| deltablue                | 8.94 ms                                                               | 4.04 ms: 2.22x faster                                                             |
| go                       | 264 ms                                                                | 136 ms: 1.94x faster                                                              |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 657 ms: 1.94x faster                                                              |
| generators               | 68.1 ms                                                               | 35.6 ms: 1.91x faster                                                             |
| richards_super           | 107 ms                                                                | 59.8 ms: 1.79x faster                                                             |
| raytrace                 | 573 ms                                                                | 322 ms: 1.78x faster                                                              |
| richards                 | 91.7 ms                                                               | 51.8 ms: 1.77x faster                                                             |
| chaos                    | 121 ms                                                                | 69.0 ms: 1.75x faster                                                             |
| logging_silent           | 222 ns                                                                | 130 ns: 1.71x faster                                                              |
| scimark_sor              | 246 ms                                                                | 152 ms: 1.62x faster                                                              |
| deepcopy_memo            | 61.7 us                                                               | 38.2 us: 1.62x faster                                                             |
| pylint                   | 485 ms                                                                | 310 ms: 1.57x faster                                                              |
| comprehensions           | 33.1 us                                                               | 21.2 us: 1.56x faster                                                             |
| deepcopy                 | 511 us                                                                | 329 us: 1.55x faster                                                              |
| crypto_pyaes             | 134 ms                                                                | 86.7 ms: 1.55x faster                                                             |
| float                    | 135 ms                                                                | 87.5 ms: 1.54x faster                                                             |
| scimark_monte_carlo      | 128 ms                                                                | 84.4 ms: 1.52x faster                                                             |
| scimark_lu               | 227 ms                                                                | 150 ms: 1.51x faster                                                              |
| spectral_norm            | 186 ms                                                                | 124 ms: 1.50x faster                                                              |
| hexiom                   | 10.9 ms                                                               | 7.35 ms: 1.48x faster                                                             |
| dulwich_log              | 73.5 ms                                                               | 51.5 ms: 1.43x faster                                                             |
| regex_compile            | 177 ms                                                                | 125 ms: 1.41x faster                                                              |
| logging_simple           | 9.78 us                                                               | 6.96 us: 1.41x faster                                                             |
| unpickle_pure_python     | 366 us                                                                | 264 us: 1.39x faster                                                              |
| tomli_loads              | 3.36 sec                                                              | 2.42 sec: 1.39x faster                                                            |
| pyflate                  | 795 ms                                                                | 574 ms: 1.39x faster                                                              |
| logging_format           | 10.6 us                                                               | 7.72 us: 1.37x faster                                                             |
| deepcopy_reduce          | 4.60 us                                                               | 3.39 us: 1.36x faster                                                             |
| mako                     | 18.9 ms                                                               | 14.0 ms: 1.35x faster                                                             |
| sqlalchemy_imperative    | 20.5 ms                                                               | 15.2 ms: 1.35x faster                                                             |
| sqlalchemy_declarative   | 197 ms                                                                | 146 ms: 1.35x faster                                                              |
| html5lib                 | 86.5 ms                                                               | 64.2 ms: 1.35x faster                                                             |
| pickle_pure_python       | 529 us                                                                | 395 us: 1.34x faster                                                              |
| thrift                   | 1.26 ms                                                               | 943 us: 1.34x faster                                                              |
| pycparser                | 1.69 sec                                                              | 1.27 sec: 1.33x faster                                                            |
| nbody                    | 166 ms                                                                | 126 ms: 1.32x faster                                                              |
| genshi_text              | 35.2 ms                                                               | 26.8 ms: 1.31x faster                                                             |
| sympy_sum                | 184 ms                                                                | 142 ms: 1.29x faster                                                              |
| django_template          | 53.3 ms                                                               | 41.5 ms: 1.28x faster                                                             |
| 2to3                     | 381 ms                                                                | 297 ms: 1.28x faster                                                              |
| coroutines               | 37.2 ms                                                               | 29.4 ms: 1.26x faster                                                             |
| xml_etree_process        | 99.5 ms                                                               | 79.2 ms: 1.26x faster                                                             |
| sympy_str                | 329 ms                                                                | 267 ms: 1.23x faster                                                              |
| pprint_pformat           | 2.36 sec                                                              | 1.92 sec: 1.23x faster                                                            |
| sympy_integrate          | 26.5 ms                                                               | 21.6 ms: 1.23x faster                                                             |
| pprint_safe_repr         | 1.15 sec                                                              | 940 ms: 1.22x faster                                                              |
| json_dumps               | 16.7 ms                                                               | 13.8 ms: 1.21x faster                                                             |
| xml_etree_parse          | 212 ms                                                                | 176 ms: 1.20x faster                                                              |
| docutils                 | 3.53 sec                                                              | 2.96 sec: 1.19x faster                                                            |
| bench_thread_pool        | 1.59 ms                                                               | 1.35 ms: 1.18x faster                                                             |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.51 ms: 1.17x faster                                                             |
| pathlib                  | 26.3 ms                                                               | 22.5 ms: 1.17x faster                                                             |
| nqueens                  | 117 ms                                                                | 101 ms: 1.17x faster                                                              |
| sympy_expand             | 543 ms                                                                | 467 ms: 1.16x faster                                                              |
| scimark_fft              | 500 ms                                                                | 432 ms: 1.16x faster                                                              |
| genshi_xml               | 69.8 ms                                                               | 60.4 ms: 1.16x faster                                                             |
| regex_v8                 | 32.2 ms                                                               | 28.5 ms: 1.13x faster                                                             |
| meteor_contest           | 126 ms                                                                | 113 ms: 1.12x faster                                                              |
| mdp                      | 3.70 sec                                                              | 3.32 sec: 1.11x faster                                                            |
| fannkuch                 | 546 ms                                                                | 493 ms: 1.11x faster                                                              |
| xml_etree_generate       | 123 ms                                                                | 111 ms: 1.11x faster                                                              |
| xml_etree_iterparse      | 156 ms                                                                | 141 ms: 1.11x faster                                                              |
| sqlite_synth             | 4.12 us                                                               | 3.76 us: 1.09x faster                                                             |
| regex_effbot             | 4.25 ms                                                               | 3.98 ms: 1.07x faster                                                             |
| regex_dna                | 257 ms                                                                | 241 ms: 1.07x faster                                                              |
| async_generators         | 452 ms                                                                | 444 ms: 1.02x faster                                                              |
| json_loads               | 30.9 us                                                               | 33.9 us: 1.10x slower                                                             |
| coverage                 | 83.6 ms                                                               | 97.8 ms: 1.17x slower                                                             |
| telco                    | 8.49 ms                                                               | 10.0 ms: 1.18x slower                                                             |
| python_startup           | 11.2 ms                                                               | 16.2 ms: 1.45x slower                                                             |
| python_startup_no_site   | 6.89 ms                                                               | 10.3 ms: 1.49x slower                                                             |
| create_gc_cycles         | 2.26 ms                                                               | 3.69 ms: 1.63x slower                                                             |
| gc_traversal             | 4.15 ms                                                               | 6.79 ms: 1.63x slower                                                             |
| bench_mp_pool            | 14.5 ms                                                               | 4.02 sec: 276.84x slower                                                          |
| Geometric mean           | (ref)                                                                 | 1.22x faster                                                                      |

Benchmark hidden because not significant (3): asyncio_websockets, pidigits, json
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250312-3.14.0a5+-2a08194/bm-20250312-arminc-aarch64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.324x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: 1.31x