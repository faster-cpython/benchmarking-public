# Results vs. 3.10.4

- fork: nelhage
- ref: computed_goto_nomerg
- machine: linux-aarch64
- commit hash: 4603470
- commit date: 2025-02-10
- overall geometric mean: 1.325x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.30x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250210-arminc-aarch64-nelhage-computed_goto_nomerg-3.14.0a4+-4603470 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 305 ms: 1.25x faster                                                      |
| docutils       | 3.53 sec                                                              | 3.02 sec: 1.17x faster                                                    |
| html5lib       | 86.5 ms                                                               | 65.9 ms: 1.31x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.24x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250210-arminc-aarch64-nelhage-computed_goto_nomerg-3.14.0a4+-4603470 |
|-------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 925 ms: 2.47x faster                                                      |
| async_tree_none         | 950 ms                                                                | 396 ms: 2.40x faster                                                      |
| async_tree_memoization  | 1.13 sec                                                              | 499 ms: 2.27x faster                                                      |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 686 ms: 1.85x faster                                                      |
| Geometric mean          | (ref)                                                                 | 2.23x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250210-arminc-aarch64-nelhage-computed_goto_nomerg-3.14.0a4+-4603470 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 87.0 ms: 1.55x faster                                                     |
| nbody          | 166 ms                                                                | 124 ms: 1.34x faster                                                      |
| Geometric mean | (ref)                                                                 | 1.26x faster                                                              |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250210-arminc-aarch64-nelhage-computed_goto_nomerg-3.14.0a4+-4603470 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 127 ms: 1.39x faster                                                      |
| regex_effbot   | 4.25 ms                                                               | 4.05 ms: 1.05x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.09x faster                                                              |

Benchmark hidden because not significant (2): regex_dna, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250210-arminc-aarch64-nelhage-computed_goto_nomerg-3.14.0a4+-4603470 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 263 us: 1.39x faster                                                      |
| pickle_pure_python   | 529 us                                                                | 395 us: 1.34x faster                                                      |
| tomli_loads          | 3.36 sec                                                              | 2.53 sec: 1.33x faster                                                    |
| xml_etree_process    | 99.5 ms                                                               | 82.9 ms: 1.20x faster                                                     |
| xml_etree_parse      | 212 ms                                                                | 183 ms: 1.16x faster                                                      |
| json_dumps           | 16.7 ms                                                               | 14.7 ms: 1.14x faster                                                     |
| json_loads           | 30.9 us                                                               | 34.8 us: 1.12x slower                                                     |
| Geometric mean       | (ref)                                                                 | 1.15x faster                                                              |

Benchmark hidden because not significant (2): xml_etree_generate, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250210-arminc-aarch64-nelhage-computed_goto_nomerg-3.14.0a4+-4603470 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 9.05 ms: 1.31x slower                                                     |
| python_startup         | 11.2 ms                                                               | 16.4 ms: 1.47x slower                                                     |
| Geometric mean         | (ref)                                                                 | 1.39x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250210-arminc-aarch64-nelhage-computed_goto_nomerg-3.14.0a4+-4603470 |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 14.0 ms: 1.36x faster                                                     |
| django_template | 53.3 ms                                                               | 40.2 ms: 1.33x faster                                                     |
| genshi_text     | 35.2 ms                                                               | 27.3 ms: 1.29x faster                                                     |
| genshi_xml      | 69.8 ms                                                               | 62.8 ms: 1.11x faster                                                     |
| Geometric mean  | (ref)                                                                 | 1.27x faster                                                              |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250210-arminc-aarch64-nelhage-computed_goto_nomerg-3.14.0a4+-4603470 |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 201 us: 3.29x faster                                                      |
| async_tree_io            | 2.28 sec                                                              | 925 ms: 2.47x faster                                                      |
| async_tree_none          | 950 ms                                                                | 396 ms: 2.40x faster                                                      |
| deltablue                | 8.94 ms                                                               | 3.90 ms: 2.29x faster                                                     |
| async_tree_memoization   | 1.13 sec                                                              | 499 ms: 2.27x faster                                                      |
| generators               | 68.1 ms                                                               | 36.6 ms: 1.86x faster                                                     |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 686 ms: 1.85x faster                                                      |
| go                       | 264 ms                                                                | 144 ms: 1.84x faster                                                      |
| raytrace                 | 573 ms                                                                | 319 ms: 1.79x faster                                                      |
| richards_super           | 107 ms                                                                | 60.0 ms: 1.79x faster                                                     |
| chaos                    | 121 ms                                                                | 68.6 ms: 1.76x faster                                                     |
| sqlglot_parse            | 2.40 ms                                                               | 1.41 ms: 1.71x faster                                                     |
| richards                 | 91.7 ms                                                               | 55.1 ms: 1.66x faster                                                     |
| scimark_lu               | 227 ms                                                                | 139 ms: 1.63x faster                                                      |
| pylint                   | 485 ms                                                                | 303 ms: 1.60x faster                                                      |
| sqlglot_transpile        | 2.84 ms                                                               | 1.77 ms: 1.60x faster                                                     |
| logging_silent           | 222 ns                                                                | 139 ns: 1.60x faster                                                      |
| scimark_sor              | 246 ms                                                                | 156 ms: 1.58x faster                                                      |
| crypto_pyaes             | 134 ms                                                                | 85.1 ms: 1.57x faster                                                     |
| spectral_norm            | 186 ms                                                                | 119 ms: 1.56x faster                                                      |
| comprehensions           | 33.1 us                                                               | 21.3 us: 1.56x faster                                                     |
| float                    | 135 ms                                                                | 87.0 ms: 1.55x faster                                                     |
| scimark_monte_carlo      | 128 ms                                                                | 83.6 ms: 1.53x faster                                                     |
| deepcopy_memo            | 61.7 us                                                               | 41.0 us: 1.50x faster                                                     |
| hexiom                   | 10.9 ms                                                               | 7.35 ms: 1.48x faster                                                     |
| deepcopy                 | 511 us                                                                | 347 us: 1.47x faster                                                      |
| pyflate                  | 795 ms                                                                | 562 ms: 1.42x faster                                                      |
| regex_compile            | 177 ms                                                                | 127 ms: 1.39x faster                                                      |
| unpickle_pure_python     | 366 us                                                                | 263 us: 1.39x faster                                                      |
| sqlalchemy_imperative    | 20.5 ms                                                               | 15.1 ms: 1.36x faster                                                     |
| mako                     | 18.9 ms                                                               | 14.0 ms: 1.36x faster                                                     |
| logging_format           | 10.6 us                                                               | 7.90 us: 1.34x faster                                                     |
| nbody                    | 166 ms                                                                | 124 ms: 1.34x faster                                                      |
| pickle_pure_python       | 529 us                                                                | 395 us: 1.34x faster                                                      |
| logging_simple           | 9.78 us                                                               | 7.31 us: 1.34x faster                                                     |
| sqlalchemy_declarative   | 197 ms                                                                | 148 ms: 1.34x faster                                                      |
| thrift                   | 1.26 ms                                                               | 947 us: 1.33x faster                                                      |
| tomli_loads              | 3.36 sec                                                              | 2.53 sec: 1.33x faster                                                    |
| django_template          | 53.3 ms                                                               | 40.2 ms: 1.33x faster                                                     |
| html5lib                 | 86.5 ms                                                               | 65.9 ms: 1.31x faster                                                     |
| pycparser                | 1.69 sec                                                              | 1.30 sec: 1.30x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 3.56 us: 1.29x faster                                                     |
| coroutines               | 37.2 ms                                                               | 28.8 ms: 1.29x faster                                                     |
| genshi_text              | 35.2 ms                                                               | 27.3 ms: 1.29x faster                                                     |
| sympy_sum                | 184 ms                                                                | 146 ms: 1.26x faster                                                      |
| sympy_str                | 329 ms                                                                | 261 ms: 1.26x faster                                                      |
| 2to3                     | 381 ms                                                                | 305 ms: 1.25x faster                                                      |
| dulwich_log              | 73.5 ms                                                               | 59.3 ms: 1.24x faster                                                     |
| sympy_integrate          | 26.5 ms                                                               | 21.6 ms: 1.23x faster                                                     |
| sqlglot_normalize        | 156 ms                                                                | 129 ms: 1.21x faster                                                      |
| bench_thread_pool        | 1.59 ms                                                               | 1.31 ms: 1.21x faster                                                     |
| scimark_fft              | 500 ms                                                                | 415 ms: 1.21x faster                                                      |
| sqlglot_optimize         | 75.4 ms                                                               | 62.8 ms: 1.20x faster                                                     |
| xml_etree_process        | 99.5 ms                                                               | 82.9 ms: 1.20x faster                                                     |
| pprint_pformat           | 2.36 sec                                                              | 1.97 sec: 1.20x faster                                                    |
| pprint_safe_repr         | 1.15 sec                                                              | 977 ms: 1.17x faster                                                      |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.52 ms: 1.17x faster                                                     |
| docutils                 | 3.53 sec                                                              | 3.02 sec: 1.17x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 183 ms: 1.16x faster                                                      |
| sympy_expand             | 543 ms                                                                | 470 ms: 1.16x faster                                                      |
| pathlib                  | 26.3 ms                                                               | 23.1 ms: 1.14x faster                                                     |
| json_dumps               | 16.7 ms                                                               | 14.7 ms: 1.14x faster                                                     |
| nqueens                  | 117 ms                                                                | 104 ms: 1.13x faster                                                      |
| fannkuch                 | 546 ms                                                                | 486 ms: 1.12x faster                                                      |
| genshi_xml               | 69.8 ms                                                               | 62.8 ms: 1.11x faster                                                     |
| meteor_contest           | 126 ms                                                                | 115 ms: 1.10x faster                                                      |
| mdp                      | 3.70 sec                                                              | 3.39 sec: 1.09x faster                                                    |
| regex_effbot             | 4.25 ms                                                               | 4.05 ms: 1.05x faster                                                     |
| json                     | 5.88 ms                                                               | 6.06 ms: 1.03x slower                                                     |
| json_loads               | 30.9 us                                                               | 34.8 us: 1.12x slower                                                     |
| telco                    | 8.49 ms                                                               | 9.65 ms: 1.14x slower                                                     |
| coverage                 | 83.6 ms                                                               | 105 ms: 1.26x slower                                                      |
| python_startup_no_site   | 6.89 ms                                                               | 9.05 ms: 1.31x slower                                                     |
| python_startup           | 11.2 ms                                                               | 16.4 ms: 1.47x slower                                                     |
| create_gc_cycles         | 2.26 ms                                                               | 3.59 ms: 1.59x slower                                                     |
| gc_traversal             | 4.15 ms                                                               | 6.76 ms: 1.63x slower                                                     |
| bench_mp_pool            | 14.5 ms                                                               | 3.99 sec: 274.71x slower                                                  |
| Geometric mean           | (ref)                                                                 | 1.21x faster                                                              |

Benchmark hidden because not significant (8): xml_etree_generate, sqlite_synth, async_generators, asyncio_websockets, regex_dna, regex_v8, xml_etree_iterparse, pidigits
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250210-3.14.0a4+-4603470/bm-20250210-arminc-aarch64-nelhage-computed_goto_nomerg-3.14.0a4+-4603470.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.325x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: 1.30x