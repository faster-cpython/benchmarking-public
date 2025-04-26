# Results vs. 3.10.4

- fork: JelleZijlstra
- ref: sunder_io
- machine: linux-aarch64
- commit hash: dac50cc
- commit date: 2025-04-25
- overall geometric mean: 1.355x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: 1.32x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250425-arminc-aarch64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 295 ms: 1.29x faster                                                 |
| docutils       | 3.53 sec                                                              | 2.95 sec: 1.20x faster                                               |
| html5lib       | 86.5 ms                                                               | 61.7 ms: 1.40x faster                                                |
| Geometric mean | (ref)                                                                 | 1.29x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250425-arminc-aarch64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|-------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 894 ms: 2.56x faster                                                 |
| async_tree_none         | 950 ms                                                                | 385 ms: 2.47x faster                                                 |
| async_tree_memoization  | 1.13 sec                                                              | 461 ms: 2.46x faster                                                 |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 658 ms: 1.93x faster                                                 |
| Geometric mean          | (ref)                                                                 | 2.34x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250425-arminc-aarch64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 135 ms                                                                | 84.8 ms: 1.59x faster                                                |
| nbody          | 166 ms                                                                | 120 ms: 1.39x faster                                                 |
| Geometric mean | (ref)                                                                 | 1.30x faster                                                         |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250425-arminc-aarch64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 120 ms: 1.47x faster                                                 |
| regex_v8       | 32.2 ms                                                               | 27.4 ms: 1.18x faster                                                |
| regex_effbot   | 4.25 ms                                                               | 3.82 ms: 1.11x faster                                                |
| regex_dna      | 257 ms                                                                | 236 ms: 1.09x faster                                                 |
| Geometric mean | (ref)                                                                 | 1.20x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250425-arminc-aarch64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|----------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 380 us: 1.39x faster                                                 |
| unpickle_pure_python | 366 us                                                                | 264 us: 1.38x faster                                                 |
| tomli_loads          | 3.36 sec                                                              | 2.44 sec: 1.38x faster                                               |
| xml_etree_process    | 99.5 ms                                                               | 79.5 ms: 1.25x faster                                                |
| xml_etree_parse      | 212 ms                                                                | 180 ms: 1.18x faster                                                 |
| json_dumps           | 16.7 ms                                                               | 14.4 ms: 1.16x faster                                                |
| xml_etree_generate   | 123 ms                                                                | 113 ms: 1.09x faster                                                 |
| xml_etree_iterparse  | 156 ms                                                                | 144 ms: 1.09x faster                                                 |
| json_loads           | 30.9 us                                                               | 35.1 us: 1.13x slower                                                |
| Geometric mean       | (ref)                                                                 | 1.19x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250425-arminc-aarch64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.59 ms: 1.25x slower                                                |
| python_startup         | 11.2 ms                                                               | 16.2 ms: 1.45x slower                                                |
| Geometric mean         | (ref)                                                                 | 1.34x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250425-arminc-aarch64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|-----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 14.0 ms: 1.35x faster                                                |
| django_template | 53.3 ms                                                               | 39.6 ms: 1.35x faster                                                |
| genshi_text     | 35.2 ms                                                               | 26.4 ms: 1.33x faster                                                |
| genshi_xml      | 69.8 ms                                                               | 60.1 ms: 1.16x faster                                                |
| Geometric mean  | (ref)                                                                 | 1.30x faster                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250425-arminc-aarch64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|--------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 206 us: 3.20x faster                                                 |
| async_tree_io            | 2.28 sec                                                              | 894 ms: 2.56x faster                                                 |
| async_tree_none          | 950 ms                                                                | 385 ms: 2.47x faster                                                 |
| async_tree_memoization   | 1.13 sec                                                              | 461 ms: 2.46x faster                                                 |
| deltablue                | 8.94 ms                                                               | 3.93 ms: 2.27x faster                                                |
| mdp                      | 3.70 sec                                                              | 1.64 sec: 2.25x faster                                               |
| go                       | 264 ms                                                                | 134 ms: 1.98x faster                                                 |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 658 ms: 1.93x faster                                                 |
| generators               | 68.1 ms                                                               | 36.5 ms: 1.86x faster                                                |
| richards_super           | 107 ms                                                                | 59.2 ms: 1.81x faster                                                |
| chaos                    | 121 ms                                                                | 67.8 ms: 1.79x faster                                                |
| richards                 | 91.7 ms                                                               | 51.6 ms: 1.78x faster                                                |
| raytrace                 | 573 ms                                                                | 325 ms: 1.76x faster                                                 |
| scimark_sor              | 246 ms                                                                | 148 ms: 1.67x faster                                                 |
| logging_silent           | 222 ns                                                                | 133 ns: 1.66x faster                                                 |
| scimark_monte_carlo      | 128 ms                                                                | 78.9 ms: 1.62x faster                                                |
| crypto_pyaes             | 134 ms                                                                | 82.8 ms: 1.62x faster                                                |
| deepcopy_memo            | 61.7 us                                                               | 38.6 us: 1.60x faster                                                |
| float                    | 135 ms                                                                | 84.8 ms: 1.59x faster                                                |
| comprehensions           | 33.1 us                                                               | 20.8 us: 1.59x faster                                                |
| pylint                   | 485 ms                                                                | 314 ms: 1.55x faster                                                 |
| deepcopy                 | 511 us                                                                | 334 us: 1.53x faster                                                 |
| hexiom                   | 10.9 ms                                                               | 7.18 ms: 1.52x faster                                                |
| scimark_lu               | 227 ms                                                                | 150 ms: 1.51x faster                                                 |
| spectral_norm            | 186 ms                                                                | 125 ms: 1.50x faster                                                 |
| regex_compile            | 177 ms                                                                | 120 ms: 1.47x faster                                                 |
| pyflate                  | 795 ms                                                                | 548 ms: 1.45x faster                                                 |
| dulwich_log              | 73.5 ms                                                               | 52.0 ms: 1.41x faster                                                |
| html5lib                 | 86.5 ms                                                               | 61.7 ms: 1.40x faster                                                |
| logging_simple           | 9.78 us                                                               | 7.00 us: 1.40x faster                                                |
| pickle_pure_python       | 529 us                                                                | 380 us: 1.39x faster                                                 |
| nbody                    | 166 ms                                                                | 120 ms: 1.39x faster                                                 |
| logging_format           | 10.6 us                                                               | 7.65 us: 1.39x faster                                                |
| unpickle_pure_python     | 366 us                                                                | 264 us: 1.38x faster                                                 |
| tomli_loads              | 3.36 sec                                                              | 2.44 sec: 1.38x faster                                               |
| mako                     | 18.9 ms                                                               | 14.0 ms: 1.35x faster                                                |
| django_template          | 53.3 ms                                                               | 39.6 ms: 1.35x faster                                                |
| pycparser                | 1.69 sec                                                              | 1.26 sec: 1.35x faster                                               |
| sqlalchemy_declarative   | 197 ms                                                                | 148 ms: 1.34x faster                                                 |
| genshi_text              | 35.2 ms                                                               | 26.4 ms: 1.33x faster                                                |
| sqlalchemy_imperative    | 20.5 ms                                                               | 15.5 ms: 1.33x faster                                                |
| sympy_integrate          | 26.5 ms                                                               | 20.4 ms: 1.30x faster                                                |
| deepcopy_reduce          | 4.60 us                                                               | 3.55 us: 1.30x faster                                                |
| 2to3                     | 381 ms                                                                | 295 ms: 1.29x faster                                                 |
| pprint_pformat           | 2.36 sec                                                              | 1.84 sec: 1.28x faster                                               |
| sympy_sum                | 184 ms                                                                | 145 ms: 1.27x faster                                                 |
| sympy_str                | 329 ms                                                                | 259 ms: 1.27x faster                                                 |
| pprint_safe_repr         | 1.15 sec                                                              | 906 ms: 1.27x faster                                                 |
| xml_etree_process        | 99.5 ms                                                               | 79.5 ms: 1.25x faster                                                |
| coroutines               | 37.2 ms                                                               | 29.8 ms: 1.25x faster                                                |
| nqueens                  | 117 ms                                                                | 97.5 ms: 1.20x faster                                                |
| docutils                 | 3.53 sec                                                              | 2.95 sec: 1.20x faster                                               |
| scimark_fft              | 500 ms                                                                | 421 ms: 1.19x faster                                                 |
| sympy_expand             | 543 ms                                                                | 459 ms: 1.18x faster                                                 |
| xml_etree_parse          | 212 ms                                                                | 180 ms: 1.18x faster                                                 |
| regex_v8                 | 32.2 ms                                                               | 27.4 ms: 1.18x faster                                                |
| pathlib                  | 26.3 ms                                                               | 22.4 ms: 1.17x faster                                                |
| genshi_xml               | 69.8 ms                                                               | 60.1 ms: 1.16x faster                                                |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.56 ms: 1.16x faster                                                |
| json_dumps               | 16.7 ms                                                               | 14.4 ms: 1.16x faster                                                |
| bench_thread_pool        | 1.59 ms                                                               | 1.38 ms: 1.16x faster                                                |
| fannkuch                 | 546 ms                                                                | 478 ms: 1.14x faster                                                 |
| meteor_contest           | 126 ms                                                                | 113 ms: 1.12x faster                                                 |
| regex_effbot             | 4.25 ms                                                               | 3.82 ms: 1.11x faster                                                |
| sqlite_synth             | 4.12 us                                                               | 3.75 us: 1.10x faster                                                |
| regex_dna                | 257 ms                                                                | 236 ms: 1.09x faster                                                 |
| xml_etree_generate       | 123 ms                                                                | 113 ms: 1.09x faster                                                 |
| xml_etree_iterparse      | 156 ms                                                                | 144 ms: 1.09x faster                                                 |
| asyncio_websockets       | 657 ms                                                                | 667 ms: 1.02x slower                                                 |
| telco                    | 8.49 ms                                                               | 9.00 ms: 1.06x slower                                                |
| json_loads               | 30.9 us                                                               | 35.1 us: 1.13x slower                                                |
| coverage                 | 83.6 ms                                                               | 100 ms: 1.20x slower                                                 |
| python_startup_no_site   | 6.89 ms                                                               | 8.59 ms: 1.25x slower                                                |
| python_startup           | 11.2 ms                                                               | 16.2 ms: 1.45x slower                                                |
| create_gc_cycles         | 2.26 ms                                                               | 3.55 ms: 1.57x slower                                                |
| gc_traversal             | 4.15 ms                                                               | 6.56 ms: 1.58x slower                                                |
| bench_mp_pool            | 14.5 ms                                                               | 2.22 sec: 152.77x slower                                             |
| Geometric mean           | (ref)                                                                 | 1.26x faster                                                         |

Benchmark hidden because not significant (3): async_generators, pidigits, json
Ignored benchmarks (19) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250425-3.14.0a7+-dac50cc/bm-20250425-arminc-aarch64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.355x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: 1.32x