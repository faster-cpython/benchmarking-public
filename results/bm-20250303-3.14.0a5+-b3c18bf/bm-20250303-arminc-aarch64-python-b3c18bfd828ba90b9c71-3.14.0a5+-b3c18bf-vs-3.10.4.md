# Results vs. 3.10.4

- fork: python
- ref: b3c18bfd828ba90b9c71
- machine: linux-aarch64
- commit hash: b3c18bf
- commit date: 2025-03-03
- overall geometric mean: 1.363x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.30x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250303-arminc-aarch64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 290 ms: 1.31x faster                                                     |
| docutils       | 3.53 sec                                                              | 2.90 sec: 1.22x faster                                                   |
| html5lib       | 86.5 ms                                                               | 60.4 ms: 1.43x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.32x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250303-arminc-aarch64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 878 ms: 2.60x faster                                                     |
| async_tree_none         | 950 ms                                                                | 375 ms: 2.53x faster                                                     |
| async_tree_memoization  | 1.13 sec                                                              | 463 ms: 2.45x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 653 ms: 1.95x faster                                                     |
| Geometric mean          | (ref)                                                                 | 2.37x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250303-arminc-aarch64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 84.4 ms: 1.60x faster                                                    |
| nbody          | 166 ms                                                                | 118 ms: 1.41x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.31x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250303-arminc-aarch64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 120 ms: 1.47x faster                                                     |
| regex_effbot   | 4.25 ms                                                               | 4.03 ms: 1.05x faster                                                    |
| regex_dna      | 257 ms                                                                | 245 ms: 1.05x faster                                                     |
| regex_v8       | 32.2 ms                                                               | 30.9 ms: 1.04x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.14x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250303-arminc-aarch64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 252 us: 1.45x faster                                                     |
| tomli_loads          | 3.36 sec                                                              | 2.42 sec: 1.39x faster                                                   |
| pickle_pure_python   | 529 us                                                                | 381 us: 1.39x faster                                                     |
| xml_etree_process    | 99.5 ms                                                               | 77.5 ms: 1.28x faster                                                    |
| json_dumps           | 16.7 ms                                                               | 13.9 ms: 1.21x faster                                                    |
| xml_etree_parse      | 212 ms                                                                | 181 ms: 1.17x faster                                                     |
| xml_etree_generate   | 123 ms                                                                | 108 ms: 1.14x faster                                                     |
| xml_etree_iterparse  | 156 ms                                                                | 141 ms: 1.11x faster                                                     |
| json_loads           | 30.9 us                                                               | 34.5 us: 1.12x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.21x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250303-arminc-aarch64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.79 ms: 1.28x slower                                                    |
| python_startup         | 11.2 ms                                                               | 15.9 ms: 1.42x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.35x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250303-arminc-aarch64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.6 ms: 1.39x faster                                                    |
| django_template | 53.3 ms                                                               | 39.4 ms: 1.35x faster                                                    |
| genshi_text     | 35.2 ms                                                               | 26.4 ms: 1.33x faster                                                    |
| genshi_xml      | 69.8 ms                                                               | 59.1 ms: 1.18x faster                                                    |
| Geometric mean  | (ref)                                                                 | 1.31x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250303-arminc-aarch64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 190 us: 3.48x faster                                                     |
| async_tree_io            | 2.28 sec                                                              | 878 ms: 2.60x faster                                                     |
| async_tree_none          | 950 ms                                                                | 375 ms: 2.53x faster                                                     |
| async_tree_memoization   | 1.13 sec                                                              | 463 ms: 2.45x faster                                                     |
| deltablue                | 8.94 ms                                                               | 3.78 ms: 2.37x faster                                                    |
| go                       | 264 ms                                                                | 134 ms: 1.98x faster                                                     |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 653 ms: 1.95x faster                                                     |
| generators               | 68.1 ms                                                               | 35.1 ms: 1.94x faster                                                    |
| richards_super           | 107 ms                                                                | 57.1 ms: 1.88x faster                                                    |
| raytrace                 | 573 ms                                                                | 307 ms: 1.87x faster                                                     |
| chaos                    | 121 ms                                                                | 65.6 ms: 1.85x faster                                                    |
| richards                 | 91.7 ms                                                               | 50.2 ms: 1.83x faster                                                    |
| sqlglot_parse            | 2.40 ms                                                               | 1.36 ms: 1.77x faster                                                    |
| logging_silent           | 222 ns                                                                | 130 ns: 1.71x faster                                                     |
| scimark_sor              | 246 ms                                                                | 147 ms: 1.67x faster                                                     |
| scimark_lu               | 227 ms                                                                | 137 ms: 1.66x faster                                                     |
| deepcopy_memo            | 61.7 us                                                               | 37.3 us: 1.66x faster                                                    |
| sqlglot_transpile        | 2.84 ms                                                               | 1.73 ms: 1.64x faster                                                    |
| comprehensions           | 33.1 us                                                               | 20.4 us: 1.62x faster                                                    |
| spectral_norm            | 186 ms                                                                | 115 ms: 1.62x faster                                                     |
| scimark_monte_carlo      | 128 ms                                                                | 79.6 ms: 1.61x faster                                                    |
| float                    | 135 ms                                                                | 84.4 ms: 1.60x faster                                                    |
| pylint                   | 485 ms                                                                | 306 ms: 1.59x faster                                                     |
| hexiom                   | 10.9 ms                                                               | 6.93 ms: 1.57x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 85.1 ms: 1.57x faster                                                    |
| deepcopy                 | 511 us                                                                | 330 us: 1.55x faster                                                     |
| regex_compile            | 177 ms                                                                | 120 ms: 1.47x faster                                                     |
| unpickle_pure_python     | 366 us                                                                | 252 us: 1.45x faster                                                     |
| logging_simple           | 9.78 us                                                               | 6.77 us: 1.44x faster                                                    |
| pyflate                  | 795 ms                                                                | 554 ms: 1.44x faster                                                     |
| html5lib                 | 86.5 ms                                                               | 60.4 ms: 1.43x faster                                                    |
| logging_format           | 10.6 us                                                               | 7.47 us: 1.42x faster                                                    |
| sqlalchemy_declarative   | 197 ms                                                                | 139 ms: 1.42x faster                                                     |
| nbody                    | 166 ms                                                                | 118 ms: 1.41x faster                                                     |
| mako                     | 18.9 ms                                                               | 13.6 ms: 1.39x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.22 sec: 1.39x faster                                                   |
| tomli_loads              | 3.36 sec                                                              | 2.42 sec: 1.39x faster                                                   |
| pickle_pure_python       | 529 us                                                                | 381 us: 1.39x faster                                                     |
| sqlalchemy_imperative    | 20.5 ms                                                               | 14.9 ms: 1.38x faster                                                    |
| thrift                   | 1.26 ms                                                               | 926 us: 1.36x faster                                                     |
| django_template          | 53.3 ms                                                               | 39.4 ms: 1.35x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 3.45 us: 1.33x faster                                                    |
| genshi_text              | 35.2 ms                                                               | 26.4 ms: 1.33x faster                                                    |
| sympy_sum                | 184 ms                                                                | 139 ms: 1.32x faster                                                     |
| coroutines               | 37.2 ms                                                               | 28.3 ms: 1.32x faster                                                    |
| 2to3                     | 381 ms                                                                | 290 ms: 1.31x faster                                                     |
| sympy_str                | 329 ms                                                                | 255 ms: 1.29x faster                                                     |
| xml_etree_process        | 99.5 ms                                                               | 77.5 ms: 1.28x faster                                                    |
| pprint_safe_repr         | 1.15 sec                                                              | 895 ms: 1.28x faster                                                     |
| dulwich_log              | 73.5 ms                                                               | 57.4 ms: 1.28x faster                                                    |
| sympy_integrate          | 26.5 ms                                                               | 20.9 ms: 1.27x faster                                                    |
| pprint_pformat           | 2.36 sec                                                              | 1.87 sec: 1.26x faster                                                   |
| sqlglot_optimize         | 75.4 ms                                                               | 60.2 ms: 1.25x faster                                                    |
| sqlglot_normalize        | 156 ms                                                                | 125 ms: 1.25x faster                                                     |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.13 ms: 1.24x faster                                                    |
| scimark_fft              | 500 ms                                                                | 410 ms: 1.22x faster                                                     |
| bench_thread_pool        | 1.59 ms                                                               | 1.31 ms: 1.22x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 21.6 ms: 1.22x faster                                                    |
| docutils                 | 3.53 sec                                                              | 2.90 sec: 1.22x faster                                                   |
| json_dumps               | 16.7 ms                                                               | 13.9 ms: 1.21x faster                                                    |
| sympy_expand             | 543 ms                                                                | 451 ms: 1.20x faster                                                     |
| nqueens                  | 117 ms                                                                | 98.2 ms: 1.20x faster                                                    |
| genshi_xml               | 69.8 ms                                                               | 59.1 ms: 1.18x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 181 ms: 1.17x faster                                                     |
| fannkuch                 | 546 ms                                                                | 476 ms: 1.15x faster                                                     |
| xml_etree_generate       | 123 ms                                                                | 108 ms: 1.14x faster                                                     |
| meteor_contest           | 126 ms                                                                | 112 ms: 1.13x faster                                                     |
| mdp                      | 3.70 sec                                                              | 3.29 sec: 1.12x faster                                                   |
| xml_etree_iterparse      | 156 ms                                                                | 141 ms: 1.11x faster                                                     |
| sqlite_synth             | 4.12 us                                                               | 3.83 us: 1.08x faster                                                    |
| regex_effbot             | 4.25 ms                                                               | 4.03 ms: 1.05x faster                                                    |
| async_generators         | 452 ms                                                                | 431 ms: 1.05x faster                                                     |
| regex_dna                | 257 ms                                                                | 245 ms: 1.05x faster                                                     |
| regex_v8                 | 32.2 ms                                                               | 30.9 ms: 1.04x faster                                                    |
| telco                    | 8.49 ms                                                               | 9.40 ms: 1.11x slower                                                    |
| json_loads               | 30.9 us                                                               | 34.5 us: 1.12x slower                                                    |
| coverage                 | 83.6 ms                                                               | 100 ms: 1.20x slower                                                     |
| python_startup_no_site   | 6.89 ms                                                               | 8.79 ms: 1.28x slower                                                    |
| python_startup           | 11.2 ms                                                               | 15.9 ms: 1.42x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 3.49 ms: 1.55x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 6.49 ms: 1.56x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 4.45 sec: 305.94x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.26x faster                                                             |

Benchmark hidden because not significant (3): json, asyncio_websockets, pidigits
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250303-3.14.0a5+-b3c18bf/bm-20250303-arminc-aarch64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.363x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.30x