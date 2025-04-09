# Results vs. 3.10.4

- fork: python
- ref: c5e856a5dc8eed4813ec
- machine: linux-aarch64
- commit hash: c5e856a
- commit date: 2025-04-08
- overall geometric mean: 1.356x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250408-arminc-aarch64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 291 ms: 1.31x faster                                                     |
| docutils       | 3.53 sec                                                              | 2.93 sec: 1.20x faster                                                   |
| html5lib       | 86.5 ms                                                               | 62.9 ms: 1.38x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.29x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250408-arminc-aarch64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 875 ms: 2.61x faster                                                     |
| async_tree_memoization  | 1.13 sec                                                              | 457 ms: 2.48x faster                                                     |
| async_tree_none         | 950 ms                                                                | 385 ms: 2.47x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 658 ms: 1.93x faster                                                     |
| Geometric mean          | (ref)                                                                 | 2.36x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250408-arminc-aarch64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 83.8 ms: 1.61x faster                                                    |
| nbody          | 166 ms                                                                | 120 ms: 1.38x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.30x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250408-arminc-aarch64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 122 ms: 1.45x faster                                                     |
| regex_v8       | 32.2 ms                                                               | 28.0 ms: 1.15x faster                                                    |
| regex_effbot   | 4.25 ms                                                               | 3.95 ms: 1.07x faster                                                    |
| regex_dna      | 257 ms                                                                | 251 ms: 1.03x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.16x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250408-arminc-aarch64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 263 us: 1.39x faster                                                     |
| tomli_loads          | 3.36 sec                                                              | 2.43 sec: 1.38x faster                                                   |
| pickle_pure_python   | 529 us                                                                | 387 us: 1.37x faster                                                     |
| xml_etree_process    | 99.5 ms                                                               | 78.9 ms: 1.26x faster                                                    |
| xml_etree_parse      | 212 ms                                                                | 173 ms: 1.22x faster                                                     |
| json_dumps           | 16.7 ms                                                               | 13.9 ms: 1.20x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 139 ms: 1.12x faster                                                     |
| xml_etree_generate   | 123 ms                                                                | 110 ms: 1.11x faster                                                     |
| json_loads           | 30.9 us                                                               | 33.9 us: 1.10x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.21x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250408-arminc-aarch64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 16.1 ms: 1.44x slower                                                    |
| python_startup_no_site | 6.89 ms                                                               | 10.2 ms: 1.48x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.46x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250408-arminc-aarch64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.9 ms: 1.36x faster                                                    |
| genshi_text     | 35.2 ms                                                               | 26.2 ms: 1.34x faster                                                    |
| django_template | 53.3 ms                                                               | 40.1 ms: 1.33x faster                                                    |
| genshi_xml      | 69.8 ms                                                               | 59.6 ms: 1.17x faster                                                    |
| Geometric mean  | (ref)                                                                 | 1.30x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250408-arminc-aarch64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 197 us: 3.36x faster                                                     |
| async_tree_io            | 2.28 sec                                                              | 875 ms: 2.61x faster                                                     |
| async_tree_memoization   | 1.13 sec                                                              | 457 ms: 2.48x faster                                                     |
| async_tree_none          | 950 ms                                                                | 385 ms: 2.47x faster                                                     |
| deltablue                | 8.94 ms                                                               | 3.79 ms: 2.36x faster                                                    |
| mdp                      | 3.70 sec                                                              | 1.61 sec: 2.29x faster                                                   |
| go                       | 264 ms                                                                | 129 ms: 2.05x faster                                                     |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 658 ms: 1.93x faster                                                     |
| generators               | 68.1 ms                                                               | 36.5 ms: 1.86x faster                                                    |
| richards_super           | 107 ms                                                                | 58.7 ms: 1.83x faster                                                    |
| raytrace                 | 573 ms                                                                | 315 ms: 1.82x faster                                                     |
| chaos                    | 121 ms                                                                | 66.8 ms: 1.81x faster                                                    |
| richards                 | 91.7 ms                                                               | 52.1 ms: 1.76x faster                                                    |
| logging_silent           | 222 ns                                                                | 129 ns: 1.73x faster                                                     |
| deepcopy_memo            | 61.7 us                                                               | 37.5 us: 1.64x faster                                                    |
| scimark_sor              | 246 ms                                                                | 150 ms: 1.64x faster                                                     |
| crypto_pyaes             | 134 ms                                                                | 83.3 ms: 1.61x faster                                                    |
| float                    | 135 ms                                                                | 83.8 ms: 1.61x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 79.8 ms: 1.60x faster                                                    |
| deepcopy                 | 511 us                                                                | 320 us: 1.59x faster                                                     |
| pylint                   | 485 ms                                                                | 307 ms: 1.58x faster                                                     |
| hexiom                   | 10.9 ms                                                               | 6.99 ms: 1.56x faster                                                    |
| comprehensions           | 33.1 us                                                               | 21.6 us: 1.54x faster                                                    |
| spectral_norm            | 186 ms                                                                | 124 ms: 1.50x faster                                                     |
| scimark_lu               | 227 ms                                                                | 152 ms: 1.49x faster                                                     |
| pyflate                  | 795 ms                                                                | 547 ms: 1.45x faster                                                     |
| regex_compile            | 177 ms                                                                | 122 ms: 1.45x faster                                                     |
| dulwich_log              | 73.5 ms                                                               | 52.1 ms: 1.41x faster                                                    |
| unpickle_pure_python     | 366 us                                                                | 263 us: 1.39x faster                                                     |
| tomli_loads              | 3.36 sec                                                              | 2.43 sec: 1.38x faster                                                   |
| logging_simple           | 9.78 us                                                               | 7.07 us: 1.38x faster                                                    |
| nbody                    | 166 ms                                                                | 120 ms: 1.38x faster                                                     |
| html5lib                 | 86.5 ms                                                               | 62.9 ms: 1.38x faster                                                    |
| pickle_pure_python       | 529 us                                                                | 387 us: 1.37x faster                                                     |
| logging_format           | 10.6 us                                                               | 7.79 us: 1.36x faster                                                    |
| mako                     | 18.9 ms                                                               | 13.9 ms: 1.36x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 3.38 us: 1.36x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.25 sec: 1.35x faster                                                   |
| genshi_text              | 35.2 ms                                                               | 26.2 ms: 1.34x faster                                                    |
| sqlalchemy_declarative   | 197 ms                                                                | 147 ms: 1.34x faster                                                     |
| django_template          | 53.3 ms                                                               | 40.1 ms: 1.33x faster                                                    |
| sqlalchemy_imperative    | 20.5 ms                                                               | 15.6 ms: 1.31x faster                                                    |
| 2to3                     | 381 ms                                                                | 291 ms: 1.31x faster                                                     |
| sympy_integrate          | 26.5 ms                                                               | 20.4 ms: 1.30x faster                                                    |
| pprint_pformat           | 2.36 sec                                                              | 1.85 sec: 1.28x faster                                                   |
| sympy_sum                | 184 ms                                                                | 144 ms: 1.27x faster                                                     |
| pprint_safe_repr         | 1.15 sec                                                              | 910 ms: 1.26x faster                                                     |
| xml_etree_process        | 99.5 ms                                                               | 78.9 ms: 1.26x faster                                                    |
| sympy_str                | 329 ms                                                                | 262 ms: 1.25x faster                                                     |
| coroutines               | 37.2 ms                                                               | 30.3 ms: 1.23x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 173 ms: 1.22x faster                                                     |
| pathlib                  | 26.3 ms                                                               | 21.6 ms: 1.22x faster                                                    |
| scimark_fft              | 500 ms                                                                | 412 ms: 1.21x faster                                                     |
| json_dumps               | 16.7 ms                                                               | 13.9 ms: 1.20x faster                                                    |
| docutils                 | 3.53 sec                                                              | 2.93 sec: 1.20x faster                                                   |
| bench_thread_pool        | 1.59 ms                                                               | 1.34 ms: 1.19x faster                                                    |
| nqueens                  | 117 ms                                                                | 99.2 ms: 1.18x faster                                                    |
| sympy_expand             | 543 ms                                                                | 462 ms: 1.17x faster                                                     |
| genshi_xml               | 69.8 ms                                                               | 59.6 ms: 1.17x faster                                                    |
| fannkuch                 | 546 ms                                                                | 475 ms: 1.15x faster                                                     |
| regex_v8                 | 32.2 ms                                                               | 28.0 ms: 1.15x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.65 ms: 1.15x faster                                                    |
| meteor_contest           | 126 ms                                                                | 112 ms: 1.13x faster                                                     |
| xml_etree_iterparse      | 156 ms                                                                | 139 ms: 1.12x faster                                                     |
| xml_etree_generate       | 123 ms                                                                | 110 ms: 1.11x faster                                                     |
| regex_effbot             | 4.25 ms                                                               | 3.95 ms: 1.07x faster                                                    |
| sqlite_synth             | 4.12 us                                                               | 3.91 us: 1.05x faster                                                    |
| regex_dna                | 257 ms                                                                | 251 ms: 1.03x faster                                                     |
| telco                    | 8.49 ms                                                               | 9.08 ms: 1.07x slower                                                    |
| json_loads               | 30.9 us                                                               | 33.9 us: 1.10x slower                                                    |
| coverage                 | 83.6 ms                                                               | 101 ms: 1.21x slower                                                     |
| python_startup           | 11.2 ms                                                               | 16.1 ms: 1.44x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 10.2 ms: 1.48x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 3.49 ms: 1.54x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 6.73 ms: 1.62x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 2.07 sec: 142.20x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.26x faster                                                             |

Benchmark hidden because not significant (4): async_generators, json, pidigits, asyncio_websockets
Ignored benchmarks (19) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250408-3.14.0a7+-c5e856a/bm-20250408-arminc-aarch64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.356x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.31x