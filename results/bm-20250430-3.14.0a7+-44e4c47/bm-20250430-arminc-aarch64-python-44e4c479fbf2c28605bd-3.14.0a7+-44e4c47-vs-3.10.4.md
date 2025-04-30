# Results vs. 3.10.4

- fork: python
- ref: 44e4c479fbf2c28605bd
- machine: linux-aarch64
- commit hash: 44e4c47
- commit date: 2025-04-30
- overall geometric mean: 1.344x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250430-arminc-aarch64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 298 ms: 1.28x faster                                                     |
| docutils       | 3.53 sec                                                              | 2.98 sec: 1.18x faster                                                   |
| html5lib       | 86.5 ms                                                               | 61.5 ms: 1.41x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.29x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250430-arminc-aarch64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 897 ms: 2.55x faster                                                     |
| async_tree_memoization  | 1.13 sec                                                              | 466 ms: 2.43x faster                                                     |
| async_tree_none         | 950 ms                                                                | 393 ms: 2.41x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 676 ms: 1.88x faster                                                     |
| Geometric mean          | (ref)                                                                 | 2.30x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250430-arminc-aarch64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 85.9 ms: 1.57x faster                                                    |
| nbody          | 166 ms                                                                | 123 ms: 1.35x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.28x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250430-arminc-aarch64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 124 ms: 1.42x faster                                                     |
| regex_v8       | 32.2 ms                                                               | 27.4 ms: 1.17x faster                                                    |
| regex_effbot   | 4.25 ms                                                               | 3.83 ms: 1.11x faster                                                    |
| regex_dna      | 257 ms                                                                | 236 ms: 1.09x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.19x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250430-arminc-aarch64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 383 us: 1.38x faster                                                     |
| unpickle_pure_python | 366 us                                                                | 265 us: 1.38x faster                                                     |
| tomli_loads          | 3.36 sec                                                              | 2.44 sec: 1.38x faster                                                   |
| xml_etree_process    | 99.5 ms                                                               | 79.6 ms: 1.25x faster                                                    |
| xml_etree_parse      | 212 ms                                                                | 176 ms: 1.20x faster                                                     |
| json_dumps           | 16.7 ms                                                               | 14.4 ms: 1.16x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 141 ms: 1.10x faster                                                     |
| xml_etree_generate   | 123 ms                                                                | 113 ms: 1.09x faster                                                     |
| json_loads           | 30.9 us                                                               | 35.5 us: 1.15x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.19x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250430-arminc-aarch64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.62 ms: 1.25x slower                                                    |
| python_startup         | 11.2 ms                                                               | 16.1 ms: 1.44x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.34x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250430-arminc-aarch64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 53.3 ms                                                               | 39.0 ms: 1.37x faster                                                    |
| mako            | 18.9 ms                                                               | 14.0 ms: 1.36x faster                                                    |
| genshi_text     | 35.2 ms                                                               | 26.5 ms: 1.33x faster                                                    |
| genshi_xml      | 69.8 ms                                                               | 62.7 ms: 1.11x faster                                                    |
| Geometric mean  | (ref)                                                                 | 1.29x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250430-arminc-aarch64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 199 us: 3.32x faster                                                     |
| async_tree_io            | 2.28 sec                                                              | 897 ms: 2.55x faster                                                     |
| async_tree_memoization   | 1.13 sec                                                              | 466 ms: 2.43x faster                                                     |
| async_tree_none          | 950 ms                                                                | 393 ms: 2.41x faster                                                     |
| deltablue                | 8.94 ms                                                               | 3.77 ms: 2.37x faster                                                    |
| mdp                      | 3.70 sec                                                              | 1.68 sec: 2.20x faster                                                   |
| go                       | 264 ms                                                                | 129 ms: 2.04x faster                                                     |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 676 ms: 1.88x faster                                                     |
| richards_super           | 107 ms                                                                | 57.1 ms: 1.88x faster                                                    |
| generators               | 68.1 ms                                                               | 36.7 ms: 1.85x faster                                                    |
| richards                 | 91.7 ms                                                               | 50.8 ms: 1.80x faster                                                    |
| chaos                    | 121 ms                                                                | 67.5 ms: 1.79x faster                                                    |
| raytrace                 | 573 ms                                                                | 322 ms: 1.78x faster                                                     |
| logging_silent           | 222 ns                                                                | 131 ns: 1.69x faster                                                     |
| scimark_sor              | 246 ms                                                                | 147 ms: 1.68x faster                                                     |
| deepcopy_memo            | 61.7 us                                                               | 38.1 us: 1.62x faster                                                    |
| comprehensions           | 33.1 us                                                               | 20.8 us: 1.59x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 80.4 ms: 1.59x faster                                                    |
| scimark_lu               | 227 ms                                                                | 144 ms: 1.58x faster                                                     |
| float                    | 135 ms                                                                | 85.9 ms: 1.57x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 6.96 ms: 1.57x faster                                                    |
| deepcopy                 | 511 us                                                                | 326 us: 1.56x faster                                                     |
| crypto_pyaes             | 134 ms                                                                | 85.7 ms: 1.56x faster                                                    |
| pylint                   | 485 ms                                                                | 323 ms: 1.50x faster                                                     |
| pyflate                  | 795 ms                                                                | 548 ms: 1.45x faster                                                     |
| regex_compile            | 177 ms                                                                | 124 ms: 1.42x faster                                                     |
| spectral_norm            | 186 ms                                                                | 132 ms: 1.41x faster                                                     |
| html5lib                 | 86.5 ms                                                               | 61.5 ms: 1.41x faster                                                    |
| logging_simple           | 9.78 us                                                               | 6.97 us: 1.40x faster                                                    |
| pickle_pure_python       | 529 us                                                                | 383 us: 1.38x faster                                                     |
| unpickle_pure_python     | 366 us                                                                | 265 us: 1.38x faster                                                     |
| tomli_loads              | 3.36 sec                                                              | 2.44 sec: 1.38x faster                                                   |
| logging_format           | 10.6 us                                                               | 7.72 us: 1.37x faster                                                    |
| django_template          | 53.3 ms                                                               | 39.0 ms: 1.37x faster                                                    |
| mako                     | 18.9 ms                                                               | 14.0 ms: 1.36x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.25 sec: 1.35x faster                                                   |
| nbody                    | 166 ms                                                                | 123 ms: 1.35x faster                                                     |
| sqlalchemy_declarative   | 197 ms                                                                | 148 ms: 1.33x faster                                                     |
| genshi_text              | 35.2 ms                                                               | 26.5 ms: 1.33x faster                                                    |
| sympy_integrate          | 26.5 ms                                                               | 20.1 ms: 1.32x faster                                                    |
| dulwich_log              | 73.5 ms                                                               | 56.0 ms: 1.31x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 3.53 us: 1.30x faster                                                    |
| sympy_sum                | 184 ms                                                                | 142 ms: 1.30x faster                                                     |
| sqlalchemy_imperative    | 20.5 ms                                                               | 16.0 ms: 1.28x faster                                                    |
| 2to3                     | 381 ms                                                                | 298 ms: 1.28x faster                                                     |
| pprint_pformat           | 2.36 sec                                                              | 1.85 sec: 1.27x faster                                                   |
| pprint_safe_repr         | 1.15 sec                                                              | 908 ms: 1.26x faster                                                     |
| coroutines               | 37.2 ms                                                               | 29.6 ms: 1.26x faster                                                    |
| xml_etree_process        | 99.5 ms                                                               | 79.6 ms: 1.25x faster                                                    |
| sympy_str                | 329 ms                                                                | 270 ms: 1.22x faster                                                     |
| xml_etree_parse          | 212 ms                                                                | 176 ms: 1.20x faster                                                     |
| nqueens                  | 117 ms                                                                | 98.4 ms: 1.19x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 22.2 ms: 1.19x faster                                                    |
| docutils                 | 3.53 sec                                                              | 2.98 sec: 1.18x faster                                                   |
| sympy_expand             | 543 ms                                                                | 460 ms: 1.18x faster                                                     |
| bench_thread_pool        | 1.59 ms                                                               | 1.35 ms: 1.17x faster                                                    |
| regex_v8                 | 32.2 ms                                                               | 27.4 ms: 1.17x faster                                                    |
| json_dumps               | 16.7 ms                                                               | 14.4 ms: 1.16x faster                                                    |
| scimark_fft              | 500 ms                                                                | 442 ms: 1.13x faster                                                     |
| fannkuch                 | 546 ms                                                                | 483 ms: 1.13x faster                                                     |
| meteor_contest           | 126 ms                                                                | 112 ms: 1.12x faster                                                     |
| genshi_xml               | 69.8 ms                                                               | 62.7 ms: 1.11x faster                                                    |
| regex_effbot             | 4.25 ms                                                               | 3.83 ms: 1.11x faster                                                    |
| xml_etree_iterparse      | 156 ms                                                                | 141 ms: 1.10x faster                                                     |
| xml_etree_generate       | 123 ms                                                                | 113 ms: 1.09x faster                                                     |
| regex_dna                | 257 ms                                                                | 236 ms: 1.09x faster                                                     |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 7.02 ms: 1.09x faster                                                    |
| sqlite_synth             | 4.12 us                                                               | 3.83 us: 1.07x faster                                                    |
| asyncio_websockets       | 657 ms                                                                | 673 ms: 1.02x slower                                                     |
| json                     | 5.88 ms                                                               | 6.10 ms: 1.04x slower                                                    |
| telco                    | 8.49 ms                                                               | 9.51 ms: 1.12x slower                                                    |
| json_loads               | 30.9 us                                                               | 35.5 us: 1.15x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 8.62 ms: 1.25x slower                                                    |
| coverage                 | 83.6 ms                                                               | 111 ms: 1.33x slower                                                     |
| python_startup           | 11.2 ms                                                               | 16.1 ms: 1.44x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 6.66 ms: 1.60x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 3.71 ms: 1.64x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 2.81 sec: 193.59x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.24x faster                                                             |

Benchmark hidden because not significant (2): pidigits, async_generators
Ignored benchmarks (19) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250430-3.14.0a7+-44e4c47/bm-20250430-arminc-aarch64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.344x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: 1.31x