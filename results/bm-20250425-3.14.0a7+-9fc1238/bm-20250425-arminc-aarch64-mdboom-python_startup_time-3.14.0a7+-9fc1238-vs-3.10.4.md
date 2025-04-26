# Results vs. 3.10.4

- fork: mdboom
- ref: python_startup_time
- machine: linux-aarch64
- commit hash: 9fc1238
- commit date: 2025-04-25
- overall geometric mean: 1.360x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250425-arminc-aarch64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 298 ms: 1.28x faster                                                    |
| docutils       | 3.53 sec                                                              | 2.94 sec: 1.20x faster                                                  |
| html5lib       | 86.5 ms                                                               | 61.5 ms: 1.41x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.29x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250425-arminc-aarch64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 892 ms: 2.56x faster                                                    |
| async_tree_none         | 950 ms                                                                | 386 ms: 2.46x faster                                                    |
| async_tree_memoization  | 1.13 sec                                                              | 464 ms: 2.44x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 662 ms: 1.92x faster                                                    |
| Geometric mean          | (ref)                                                                 | 2.33x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250425-arminc-aarch64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 83.3 ms: 1.62x faster                                                   |
| nbody          | 166 ms                                                                | 119 ms: 1.39x faster                                                    |
| pidigits       | 235 ms                                                                | 234 ms: 1.00x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.31x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250425-arminc-aarch64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 120 ms: 1.47x faster                                                    |
| regex_v8       | 32.2 ms                                                               | 27.7 ms: 1.16x faster                                                   |
| regex_effbot   | 4.25 ms                                                               | 3.84 ms: 1.11x faster                                                   |
| regex_dna      | 257 ms                                                                | 236 ms: 1.09x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.20x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250425-arminc-aarch64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 379 us: 1.40x faster                                                    |
| unpickle_pure_python | 366 us                                                                | 263 us: 1.39x faster                                                    |
| tomli_loads          | 3.36 sec                                                              | 2.44 sec: 1.37x faster                                                  |
| xml_etree_process    | 99.5 ms                                                               | 80.2 ms: 1.24x faster                                                   |
| json_dumps           | 16.7 ms                                                               | 13.8 ms: 1.21x faster                                                   |
| xml_etree_parse      | 212 ms                                                                | 179 ms: 1.18x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 141 ms: 1.11x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 112 ms: 1.10x faster                                                    |
| json_loads           | 30.9 us                                                               | 34.2 us: 1.11x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.20x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250425-arminc-aarch64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 9.08 ms: 1.32x slower                                                   |
| python_startup         | 11.2 ms                                                               | 16.3 ms: 1.46x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.39x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250425-arminc-aarch64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.7 ms: 1.38x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 26.0 ms: 1.35x faster                                                   |
| django_template | 53.3 ms                                                               | 39.4 ms: 1.35x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 61.0 ms: 1.14x faster                                                   |
| Geometric mean  | (ref)                                                                 | 1.31x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250425-arminc-aarch64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 201 us: 3.30x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 892 ms: 2.56x faster                                                    |
| async_tree_none          | 950 ms                                                                | 386 ms: 2.46x faster                                                    |
| async_tree_memoization   | 1.13 sec                                                              | 464 ms: 2.44x faster                                                    |
| deltablue                | 8.94 ms                                                               | 3.92 ms: 2.28x faster                                                   |
| mdp                      | 3.70 sec                                                              | 1.62 sec: 2.28x faster                                                  |
| go                       | 264 ms                                                                | 131 ms: 2.01x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 662 ms: 1.92x faster                                                    |
| generators               | 68.1 ms                                                               | 36.5 ms: 1.87x faster                                                   |
| richards_super           | 107 ms                                                                | 58.8 ms: 1.82x faster                                                   |
| chaos                    | 121 ms                                                                | 66.5 ms: 1.82x faster                                                   |
| raytrace                 | 573 ms                                                                | 325 ms: 1.77x faster                                                    |
| richards                 | 91.7 ms                                                               | 52.9 ms: 1.73x faster                                                   |
| logging_silent           | 222 ns                                                                | 129 ns: 1.72x faster                                                    |
| scimark_sor              | 246 ms                                                                | 148 ms: 1.66x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 78.5 ms: 1.63x faster                                                   |
| crypto_pyaes             | 134 ms                                                                | 82.7 ms: 1.62x faster                                                   |
| float                    | 135 ms                                                                | 83.3 ms: 1.62x faster                                                   |
| deepcopy_memo            | 61.7 us                                                               | 38.2 us: 1.61x faster                                                   |
| comprehensions           | 33.1 us                                                               | 21.0 us: 1.58x faster                                                   |
| pylint                   | 485 ms                                                                | 312 ms: 1.56x faster                                                    |
| deepcopy                 | 511 us                                                                | 330 us: 1.55x faster                                                    |
| pyflate                  | 795 ms                                                                | 521 ms: 1.53x faster                                                    |
| scimark_lu               | 227 ms                                                                | 149 ms: 1.52x faster                                                    |
| spectral_norm            | 186 ms                                                                | 123 ms: 1.52x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 7.31 ms: 1.49x faster                                                   |
| regex_compile            | 177 ms                                                                | 120 ms: 1.47x faster                                                    |
| logging_simple           | 9.78 us                                                               | 6.90 us: 1.42x faster                                                   |
| html5lib                 | 86.5 ms                                                               | 61.5 ms: 1.41x faster                                                   |
| dulwich_log              | 73.5 ms                                                               | 52.6 ms: 1.40x faster                                                   |
| pickle_pure_python       | 529 us                                                                | 379 us: 1.40x faster                                                    |
| nbody                    | 166 ms                                                                | 119 ms: 1.39x faster                                                    |
| unpickle_pure_python     | 366 us                                                                | 263 us: 1.39x faster                                                    |
| mako                     | 18.9 ms                                                               | 13.7 ms: 1.38x faster                                                   |
| logging_format           | 10.6 us                                                               | 7.67 us: 1.38x faster                                                   |
| tomli_loads              | 3.36 sec                                                              | 2.44 sec: 1.37x faster                                                  |
| pycparser                | 1.69 sec                                                              | 1.24 sec: 1.36x faster                                                  |
| genshi_text              | 35.2 ms                                                               | 26.0 ms: 1.35x faster                                                   |
| django_template          | 53.3 ms                                                               | 39.4 ms: 1.35x faster                                                   |
| deepcopy_reduce          | 4.60 us                                                               | 3.40 us: 1.35x faster                                                   |
| sqlalchemy_declarative   | 197 ms                                                                | 147 ms: 1.34x faster                                                    |
| sqlalchemy_imperative    | 20.5 ms                                                               | 15.5 ms: 1.33x faster                                                   |
| sympy_integrate          | 26.5 ms                                                               | 20.0 ms: 1.32x faster                                                   |
| sympy_sum                | 184 ms                                                                | 142 ms: 1.29x faster                                                    |
| 2to3                     | 381 ms                                                                | 298 ms: 1.28x faster                                                    |
| pprint_safe_repr         | 1.15 sec                                                              | 898 ms: 1.28x faster                                                    |
| sympy_str                | 329 ms                                                                | 258 ms: 1.27x faster                                                    |
| pprint_pformat           | 2.36 sec                                                              | 1.87 sec: 1.26x faster                                                  |
| xml_etree_process        | 99.5 ms                                                               | 80.2 ms: 1.24x faster                                                   |
| coroutines               | 37.2 ms                                                               | 30.4 ms: 1.22x faster                                                   |
| nqueens                  | 117 ms                                                                | 96.3 ms: 1.22x faster                                                   |
| scimark_fft              | 500 ms                                                                | 413 ms: 1.21x faster                                                    |
| json_dumps               | 16.7 ms                                                               | 13.8 ms: 1.21x faster                                                   |
| docutils                 | 3.53 sec                                                              | 2.94 sec: 1.20x faster                                                  |
| sympy_expand             | 543 ms                                                                | 454 ms: 1.20x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 179 ms: 1.18x faster                                                    |
| regex_v8                 | 32.2 ms                                                               | 27.7 ms: 1.16x faster                                                   |
| bench_thread_pool        | 1.59 ms                                                               | 1.37 ms: 1.16x faster                                                   |
| fannkuch                 | 546 ms                                                                | 471 ms: 1.16x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 22.8 ms: 1.16x faster                                                   |
| genshi_xml               | 69.8 ms                                                               | 61.0 ms: 1.14x faster                                                   |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.77 ms: 1.13x faster                                                   |
| meteor_contest           | 126 ms                                                                | 113 ms: 1.12x faster                                                    |
| xml_etree_iterparse      | 156 ms                                                                | 141 ms: 1.11x faster                                                    |
| regex_effbot             | 4.25 ms                                                               | 3.84 ms: 1.11x faster                                                   |
| xml_etree_generate       | 123 ms                                                                | 112 ms: 1.10x faster                                                    |
| regex_dna                | 257 ms                                                                | 236 ms: 1.09x faster                                                    |
| sqlite_synth             | 4.12 us                                                               | 3.80 us: 1.08x faster                                                   |
| async_generators         | 452 ms                                                                | 446 ms: 1.02x faster                                                    |
| pidigits                 | 235 ms                                                                | 234 ms: 1.00x faster                                                    |
| asyncio_websockets       | 657 ms                                                                | 667 ms: 1.02x slower                                                    |
| telco                    | 8.49 ms                                                               | 9.32 ms: 1.10x slower                                                   |
| json_loads               | 30.9 us                                                               | 34.2 us: 1.11x slower                                                   |
| coverage                 | 83.6 ms                                                               | 102 ms: 1.22x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 9.08 ms: 1.32x slower                                                   |
| python_startup           | 11.2 ms                                                               | 16.3 ms: 1.46x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 6.59 ms: 1.59x slower                                                   |
| create_gc_cycles         | 2.26 ms                                                               | 3.58 ms: 1.59x slower                                                   |
| bench_mp_pool            | 14.5 ms                                                               | 4.67 sec: 321.53x slower                                                |
| Geometric mean           | (ref)                                                                 | 1.25x faster                                                            |

Benchmark hidden because not significant (1): json
Ignored benchmarks (19) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250425-3.14.0a7+-9fc1238/bm-20250425-arminc-aarch64-mdboom-python_startup_time-3.14.0a7+-9fc1238.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.360x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.31x