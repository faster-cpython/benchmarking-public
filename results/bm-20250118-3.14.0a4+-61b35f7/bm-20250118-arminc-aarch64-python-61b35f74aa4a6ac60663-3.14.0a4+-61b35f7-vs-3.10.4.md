# Results vs. 3.10.4

- fork: python
- ref: 61b35f74aa4a6ac60663
- machine: linux-aarch64
- commit hash: 61b35f7
- commit date: 2025-01-18
- overall geometric mean: 1.327x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: 1.30x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 306 ms: 1.24x faster                                                     |
| docutils       | 3.53 sec                                                              | 3.01 sec: 1.17x faster                                                   |
| html5lib       | 86.5 ms                                                               | 62.9 ms: 1.37x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.26x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 895 ms: 2.55x faster                                                     |
| async_tree_none         | 950 ms                                                                | 385 ms: 2.47x faster                                                     |
| async_tree_memoization  | 1.13 sec                                                              | 490 ms: 2.31x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 678 ms: 1.88x faster                                                     |
| Geometric mean          | (ref)                                                                 | 2.29x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 86.7 ms: 1.55x faster                                                    |
| nbody          | 166 ms                                                                | 123 ms: 1.35x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.27x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 130 ms: 1.36x faster                                                     |
| regex_effbot   | 4.25 ms                                                               | 3.99 ms: 1.06x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.09x faster                                                             |

Benchmark hidden because not significant (2): regex_dna, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 266 us: 1.37x faster                                                     |
| pickle_pure_python   | 529 us                                                                | 393 us: 1.35x faster                                                     |
| tomli_loads          | 3.36 sec                                                              | 2.57 sec: 1.30x faster                                                   |
| xml_etree_process    | 99.5 ms                                                               | 82.2 ms: 1.21x faster                                                    |
| xml_etree_parse      | 212 ms                                                                | 184 ms: 1.15x faster                                                     |
| json_dumps           | 16.7 ms                                                               | 15.4 ms: 1.09x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 115 ms: 1.07x faster                                                     |
| xml_etree_iterparse  | 156 ms                                                                | 146 ms: 1.06x faster                                                     |
| unpickle_list        | 6.99 us                                                               | 6.65 us: 1.05x faster                                                    |
| json_loads           | 30.9 us                                                               | 33.8 us: 1.09x slower                                                    |
| pickle_dict          | 35.1 us                                                               | 39.6 us: 1.13x slower                                                    |
| pickle_list          | 5.24 us                                                               | 6.01 us: 1.15x slower                                                    |
| pickle               | 12.5 us                                                               | 16.0 us: 1.29x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.06x faster                                                             |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 9.15 ms: 1.33x slower                                                    |
| python_startup         | 11.2 ms                                                               | 16.4 ms: 1.47x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.40x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 53.3 ms                                                               | 39.4 ms: 1.35x faster                                                    |
| mako            | 18.9 ms                                                               | 14.6 ms: 1.30x faster                                                    |
| genshi_text     | 35.2 ms                                                               | 27.1 ms: 1.30x faster                                                    |
| genshi_xml      | 69.8 ms                                                               | 61.6 ms: 1.13x faster                                                    |
| Geometric mean  | (ref)                                                                 | 1.27x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 207 us: 3.20x faster                                                     |
| async_tree_io            | 2.28 sec                                                              | 895 ms: 2.55x faster                                                     |
| async_tree_none          | 950 ms                                                                | 385 ms: 2.47x faster                                                     |
| deltablue                | 8.94 ms                                                               | 3.86 ms: 2.32x faster                                                    |
| async_tree_memoization   | 1.13 sec                                                              | 490 ms: 2.31x faster                                                     |
| generators               | 68.1 ms                                                               | 36.1 ms: 1.89x faster                                                    |
| go                       | 264 ms                                                                | 140 ms: 1.88x faster                                                     |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 678 ms: 1.88x faster                                                     |
| raytrace                 | 573 ms                                                                | 315 ms: 1.82x faster                                                     |
| chaos                    | 121 ms                                                                | 67.8 ms: 1.79x faster                                                    |
| richards                 | 91.7 ms                                                               | 51.9 ms: 1.77x faster                                                    |
| richards_super           | 107 ms                                                                | 61.7 ms: 1.74x faster                                                    |
| scimark_lu               | 227 ms                                                                | 137 ms: 1.66x faster                                                     |
| asyncio_tcp              | 944 ms                                                                | 570 ms: 1.66x faster                                                     |
| sqlglot_parse            | 2.40 ms                                                               | 1.45 ms: 1.65x faster                                                    |
| scimark_sor              | 246 ms                                                                | 150 ms: 1.64x faster                                                     |
| logging_silent           | 222 ns                                                                | 139 ns: 1.60x faster                                                     |
| crypto_pyaes             | 134 ms                                                                | 84.4 ms: 1.59x faster                                                    |
| float                    | 135 ms                                                                | 86.7 ms: 1.55x faster                                                    |
| spectral_norm            | 186 ms                                                                | 121 ms: 1.54x faster                                                     |
| sqlglot_transpile        | 2.84 ms                                                               | 1.86 ms: 1.53x faster                                                    |
| pylint                   | 485 ms                                                                | 318 ms: 1.53x faster                                                     |
| comprehensions           | 33.1 us                                                               | 22.0 us: 1.51x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 41.0 us: 1.51x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 85.2 ms: 1.50x faster                                                    |
| deepcopy                 | 511 us                                                                | 349 us: 1.46x faster                                                     |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.26 sec: 1.45x faster                                                   |
| hexiom                   | 10.9 ms                                                               | 7.55 ms: 1.45x faster                                                    |
| pyflate                  | 795 ms                                                                | 567 ms: 1.40x faster                                                     |
| logging_simple           | 9.78 us                                                               | 6.99 us: 1.40x faster                                                    |
| html5lib                 | 86.5 ms                                                               | 62.9 ms: 1.37x faster                                                    |
| unpickle_pure_python     | 366 us                                                                | 266 us: 1.37x faster                                                     |
| logging_format           | 10.6 us                                                               | 7.75 us: 1.37x faster                                                    |
| regex_compile            | 177 ms                                                                | 130 ms: 1.36x faster                                                     |
| django_template          | 53.3 ms                                                               | 39.4 ms: 1.35x faster                                                    |
| nbody                    | 166 ms                                                                | 123 ms: 1.35x faster                                                     |
| pickle_pure_python       | 529 us                                                                | 393 us: 1.35x faster                                                     |
| sqlalchemy_declarative   | 197 ms                                                                | 148 ms: 1.33x faster                                                     |
| sqlalchemy_imperative    | 20.5 ms                                                               | 15.6 ms: 1.31x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.29 sec: 1.31x faster                                                   |
| tomli_loads              | 3.36 sec                                                              | 2.57 sec: 1.30x faster                                                   |
| mako                     | 18.9 ms                                                               | 14.6 ms: 1.30x faster                                                    |
| genshi_text              | 35.2 ms                                                               | 27.1 ms: 1.30x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 3.55 us: 1.29x faster                                                    |
| sympy_sum                | 184 ms                                                                | 146 ms: 1.26x faster                                                     |
| coroutines               | 37.2 ms                                                               | 29.5 ms: 1.26x faster                                                    |
| thrift                   | 1.26 ms                                                               | 1.00 ms: 1.26x faster                                                    |
| 2to3                     | 381 ms                                                                | 306 ms: 1.24x faster                                                     |
| sympy_integrate          | 26.5 ms                                                               | 21.7 ms: 1.22x faster                                                    |
| pprint_safe_repr         | 1.15 sec                                                              | 947 ms: 1.21x faster                                                     |
| xml_etree_process        | 99.5 ms                                                               | 82.2 ms: 1.21x faster                                                    |
| sympy_str                | 329 ms                                                                | 272 ms: 1.21x faster                                                     |
| pathlib                  | 26.3 ms                                                               | 21.8 ms: 1.20x faster                                                    |
| dulwich_log              | 73.5 ms                                                               | 61.4 ms: 1.20x faster                                                    |
| scimark_fft              | 500 ms                                                                | 418 ms: 1.20x faster                                                     |
| pprint_pformat           | 2.36 sec                                                              | 1.97 sec: 1.19x faster                                                   |
| sqlglot_normalize        | 156 ms                                                                | 131 ms: 1.19x faster                                                     |
| bench_thread_pool        | 1.59 ms                                                               | 1.34 ms: 1.19x faster                                                    |
| sqlglot_optimize         | 75.4 ms                                                               | 63.4 ms: 1.19x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.46 ms: 1.18x faster                                                    |
| nqueens                  | 117 ms                                                                | 99.7 ms: 1.18x faster                                                    |
| docutils                 | 3.53 sec                                                              | 3.01 sec: 1.17x faster                                                   |
| sympy_expand             | 543 ms                                                                | 471 ms: 1.15x faster                                                     |
| xml_etree_parse          | 212 ms                                                                | 184 ms: 1.15x faster                                                     |
| genshi_xml               | 69.8 ms                                                               | 61.6 ms: 1.13x faster                                                    |
| fannkuch                 | 546 ms                                                                | 484 ms: 1.13x faster                                                     |
| json_dumps               | 16.7 ms                                                               | 15.4 ms: 1.09x faster                                                    |
| mdp                      | 3.70 sec                                                              | 3.42 sec: 1.08x faster                                                   |
| xml_etree_generate       | 123 ms                                                                | 115 ms: 1.07x faster                                                     |
| regex_effbot             | 4.25 ms                                                               | 3.99 ms: 1.06x faster                                                    |
| xml_etree_iterparse      | 156 ms                                                                | 146 ms: 1.06x faster                                                     |
| unpickle_list            | 6.99 us                                                               | 6.65 us: 1.05x faster                                                    |
| asyncio_websockets       | 657 ms                                                                | 674 ms: 1.03x slower                                                     |
| json_loads               | 30.9 us                                                               | 33.8 us: 1.09x slower                                                    |
| telco                    | 8.49 ms                                                               | 9.53 ms: 1.12x slower                                                    |
| pickle_dict              | 35.1 us                                                               | 39.6 us: 1.13x slower                                                    |
| pickle_list              | 5.24 us                                                               | 6.01 us: 1.15x slower                                                    |
| coverage                 | 83.6 ms                                                               | 102 ms: 1.22x slower                                                     |
| pickle                   | 12.5 us                                                               | 16.0 us: 1.29x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 9.15 ms: 1.33x slower                                                    |
| python_startup           | 11.2 ms                                                               | 16.4 ms: 1.47x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 3.61 ms: 1.60x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 6.96 ms: 1.68x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 7.08 sec: 487.30x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.19x faster                                                             |

Benchmark hidden because not significant (8): meteor_contest, json, regex_dna, async_generators, sqlite_synth, pidigits, unpickle, regex_v8
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, tornado_http
Ignored benchmarks (12) of results/bm-20250118-3.14.0a4+-61b35f7/bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.327x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: 1.30x