# Results vs. 3.10.4

- fork: python
- ref: d783d7b51d31db568de6
- machine: linux-aarch64
- commit hash: d783d7b
- commit date: 2025-03-18
- overall geometric mean: 1.316x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250318-arminc-aarch64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 297 ms: 1.28x faster                                                     |
| docutils       | 3.53 sec                                                              | 2.97 sec: 1.19x faster                                                   |
| html5lib       | 86.5 ms                                                               | 64.2 ms: 1.35x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.27x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250318-arminc-aarch64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 890 ms: 2.57x faster                                                     |
| async_tree_none         | 950 ms                                                                | 386 ms: 2.46x faster                                                     |
| async_tree_memoization  | 1.13 sec                                                              | 468 ms: 2.42x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 658 ms: 1.93x faster                                                     |
| Geometric mean          | (ref)                                                                 | 2.33x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250318-arminc-aarch64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 87.4 ms: 1.54x faster                                                    |
| nbody          | 166 ms                                                                | 128 ms: 1.29x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.26x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250318-arminc-aarch64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 125 ms: 1.41x faster                                                     |
| regex_v8       | 32.2 ms                                                               | 28.1 ms: 1.15x faster                                                    |
| regex_effbot   | 4.25 ms                                                               | 3.98 ms: 1.07x faster                                                    |
| regex_dna      | 257 ms                                                                | 244 ms: 1.05x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.16x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250318-arminc-aarch64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 269 us: 1.36x faster                                                     |
| tomli_loads          | 3.36 sec                                                              | 2.48 sec: 1.36x faster                                                   |
| pickle_pure_python   | 529 us                                                                | 398 us: 1.33x faster                                                     |
| xml_etree_process    | 99.5 ms                                                               | 82.2 ms: 1.21x faster                                                    |
| xml_etree_parse      | 212 ms                                                                | 176 ms: 1.20x faster                                                     |
| json_dumps           | 16.7 ms                                                               | 14.2 ms: 1.18x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 141 ms: 1.10x faster                                                     |
| xml_etree_generate   | 123 ms                                                                | 115 ms: 1.07x faster                                                     |
| json_loads           | 30.9 us                                                               | 34.6 us: 1.12x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.18x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250318-arminc-aarch64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 16.1 ms: 1.44x slower                                                    |
| python_startup_no_site | 6.89 ms                                                               | 10.2 ms: 1.47x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.46x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250318-arminc-aarch64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 14.2 ms: 1.33x faster                                                    |
| django_template | 53.3 ms                                                               | 40.6 ms: 1.31x faster                                                    |
| genshi_text     | 35.2 ms                                                               | 27.0 ms: 1.31x faster                                                    |
| genshi_xml      | 69.8 ms                                                               | 61.0 ms: 1.15x faster                                                    |
| Geometric mean  | (ref)                                                                 | 1.27x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250318-arminc-aarch64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 199 us: 3.32x faster                                                     |
| async_tree_io            | 2.28 sec                                                              | 890 ms: 2.57x faster                                                     |
| async_tree_none          | 950 ms                                                                | 386 ms: 2.46x faster                                                     |
| async_tree_memoization   | 1.13 sec                                                              | 468 ms: 2.42x faster                                                     |
| deltablue                | 8.94 ms                                                               | 3.97 ms: 2.25x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 658 ms: 1.93x faster                                                     |
| generators               | 68.1 ms                                                               | 35.7 ms: 1.91x faster                                                    |
| go                       | 264 ms                                                                | 140 ms: 1.89x faster                                                     |
| richards_super           | 107 ms                                                                | 59.8 ms: 1.79x faster                                                    |
| raytrace                 | 573 ms                                                                | 323 ms: 1.77x faster                                                     |
| richards                 | 91.7 ms                                                               | 51.8 ms: 1.77x faster                                                    |
| logging_silent           | 222 ns                                                                | 132 ns: 1.68x faster                                                     |
| chaos                    | 121 ms                                                                | 72.5 ms: 1.67x faster                                                    |
| scimark_sor              | 246 ms                                                                | 149 ms: 1.66x faster                                                     |
| deepcopy_memo            | 61.7 us                                                               | 38.2 us: 1.61x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 86.7 ms: 1.55x faster                                                    |
| float                    | 135 ms                                                                | 87.4 ms: 1.54x faster                                                    |
| deepcopy                 | 511 us                                                                | 331 us: 1.54x faster                                                     |
| comprehensions           | 33.1 us                                                               | 21.6 us: 1.53x faster                                                    |
| scimark_lu               | 227 ms                                                                | 149 ms: 1.52x faster                                                     |
| hexiom                   | 10.9 ms                                                               | 7.33 ms: 1.49x faster                                                    |
| spectral_norm            | 186 ms                                                                | 126 ms: 1.48x faster                                                     |
| scimark_monte_carlo      | 128 ms                                                                | 87.4 ms: 1.46x faster                                                    |
| pylint                   | 485 ms                                                                | 334 ms: 1.45x faster                                                     |
| pyflate                  | 795 ms                                                                | 548 ms: 1.45x faster                                                     |
| dulwich_log              | 73.5 ms                                                               | 51.9 ms: 1.42x faster                                                    |
| regex_compile            | 177 ms                                                                | 125 ms: 1.41x faster                                                     |
| logging_simple           | 9.78 us                                                               | 7.07 us: 1.38x faster                                                    |
| unpickle_pure_python     | 366 us                                                                | 269 us: 1.36x faster                                                     |
| tomli_loads              | 3.36 sec                                                              | 2.48 sec: 1.36x faster                                                   |
| logging_format           | 10.6 us                                                               | 7.84 us: 1.35x faster                                                    |
| html5lib                 | 86.5 ms                                                               | 64.2 ms: 1.35x faster                                                    |
| sqlalchemy_declarative   | 197 ms                                                                | 147 ms: 1.34x faster                                                     |
| pycparser                | 1.69 sec                                                              | 1.27 sec: 1.34x faster                                                   |
| mako                     | 18.9 ms                                                               | 14.2 ms: 1.33x faster                                                    |
| pickle_pure_python       | 529 us                                                                | 398 us: 1.33x faster                                                     |
| thrift                   | 1.26 ms                                                               | 949 us: 1.33x faster                                                     |
| django_template          | 53.3 ms                                                               | 40.6 ms: 1.31x faster                                                    |
| genshi_text              | 35.2 ms                                                               | 27.0 ms: 1.31x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 3.53 us: 1.30x faster                                                    |
| nbody                    | 166 ms                                                                | 128 ms: 1.29x faster                                                     |
| sqlalchemy_imperative    | 20.5 ms                                                               | 15.9 ms: 1.29x faster                                                    |
| sympy_sum                | 184 ms                                                                | 143 ms: 1.28x faster                                                     |
| 2to3                     | 381 ms                                                                | 297 ms: 1.28x faster                                                     |
| coroutines               | 37.2 ms                                                               | 29.1 ms: 1.28x faster                                                    |
| sympy_str                | 329 ms                                                                | 267 ms: 1.23x faster                                                     |
| sympy_integrate          | 26.5 ms                                                               | 21.6 ms: 1.23x faster                                                    |
| xml_etree_process        | 99.5 ms                                                               | 82.2 ms: 1.21x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 176 ms: 1.20x faster                                                     |
| pprint_pformat           | 2.36 sec                                                              | 1.97 sec: 1.20x faster                                                   |
| pprint_safe_repr         | 1.15 sec                                                              | 959 ms: 1.20x faster                                                     |
| bench_thread_pool        | 1.59 ms                                                               | 1.34 ms: 1.19x faster                                                    |
| docutils                 | 3.53 sec                                                              | 2.97 sec: 1.19x faster                                                   |
| scimark_fft              | 500 ms                                                                | 424 ms: 1.18x faster                                                     |
| json_dumps               | 16.7 ms                                                               | 14.2 ms: 1.18x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 22.5 ms: 1.17x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.59 ms: 1.16x faster                                                    |
| sympy_expand             | 543 ms                                                                | 470 ms: 1.15x faster                                                     |
| regex_v8                 | 32.2 ms                                                               | 28.1 ms: 1.15x faster                                                    |
| genshi_xml               | 69.8 ms                                                               | 61.0 ms: 1.15x faster                                                    |
| nqueens                  | 117 ms                                                                | 104 ms: 1.13x faster                                                     |
| meteor_contest           | 126 ms                                                                | 113 ms: 1.12x faster                                                     |
| mdp                      | 3.70 sec                                                              | 3.31 sec: 1.12x faster                                                   |
| xml_etree_iterparse      | 156 ms                                                                | 141 ms: 1.10x faster                                                     |
| fannkuch                 | 546 ms                                                                | 508 ms: 1.07x faster                                                     |
| regex_effbot             | 4.25 ms                                                               | 3.98 ms: 1.07x faster                                                    |
| xml_etree_generate       | 123 ms                                                                | 115 ms: 1.07x faster                                                     |
| sqlite_synth             | 4.12 us                                                               | 3.87 us: 1.06x faster                                                    |
| regex_dna                | 257 ms                                                                | 244 ms: 1.05x faster                                                     |
| json                     | 5.88 ms                                                               | 5.79 ms: 1.02x faster                                                    |
| asyncio_websockets       | 657 ms                                                                | 667 ms: 1.02x slower                                                     |
| json_loads               | 30.9 us                                                               | 34.6 us: 1.12x slower                                                    |
| telco                    | 8.49 ms                                                               | 9.89 ms: 1.17x slower                                                    |
| coverage                 | 83.6 ms                                                               | 98.7 ms: 1.18x slower                                                    |
| python_startup           | 11.2 ms                                                               | 16.1 ms: 1.44x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 10.2 ms: 1.47x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 6.56 ms: 1.58x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 3.68 ms: 1.63x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 2.47 sec: 170.04x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.22x faster                                                             |

Benchmark hidden because not significant (2): pidigits, async_generators
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250318-3.14.0a6+-d783d7b/bm-20250318-arminc-aarch64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.316x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: 1.31x