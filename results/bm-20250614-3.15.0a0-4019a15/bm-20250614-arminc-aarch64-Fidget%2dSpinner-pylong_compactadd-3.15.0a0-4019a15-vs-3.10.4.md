# Results vs. 3.10.4

- fork: Fidget-Spinner
- ref: pylong_compactadd
- machine: linux-aarch64
- commit hash: 4019a15
- commit date: 2025-06-14
- overall geometric mean: 1.231x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: 1.37x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250614-arminc-aarch64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 300 ms: 1.27x faster                                                           |
| docutils       | 3.53 sec                                                              | 2.94 sec: 1.20x faster                                                         |
| html5lib       | 86.5 ms                                                               | 62.5 ms: 1.38x faster                                                          |
| Geometric mean | (ref)                                                                 | 1.28x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250614-arminc-aarch64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 900 ms: 2.54x faster                                                           |
| async_tree_memoization  | 1.13 sec                                                              | 467 ms: 2.43x faster                                                           |
| async_tree_none         | 950 ms                                                                | 398 ms: 2.39x faster                                                           |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 659 ms: 1.93x faster                                                           |
| Geometric mean          | (ref)                                                                 | 2.31x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250614-arminc-aarch64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 85.7 ms: 1.57x faster                                                          |
| nbody          | 166 ms                                                                | 119 ms: 1.39x faster                                                           |
| Geometric mean | (ref)                                                                 | 1.29x faster                                                                   |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250614-arminc-aarch64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 122 ms: 1.45x faster                                                           |
| regex_dna      | 257 ms                                                                | 220 ms: 1.17x faster                                                           |
| regex_v8       | 32.2 ms                                                               | 27.7 ms: 1.16x faster                                                          |
| regex_effbot   | 4.25 ms                                                               | 3.93 ms: 1.08x faster                                                          |
| Geometric mean | (ref)                                                                 | 1.21x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250614-arminc-aarch64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 379 us: 1.40x faster                                                           |
| tomli_loads          | 3.36 sec                                                              | 2.43 sec: 1.38x faster                                                         |
| unpickle_pure_python | 366 us                                                                | 265 us: 1.38x faster                                                           |
| xml_etree_process    | 99.5 ms                                                               | 79.2 ms: 1.26x faster                                                          |
| json_dumps           | 16.7 ms                                                               | 13.7 ms: 1.22x faster                                                          |
| xml_etree_parse      | 212 ms                                                                | 178 ms: 1.19x faster                                                           |
| xml_etree_generate   | 123 ms                                                                | 112 ms: 1.10x faster                                                           |
| xml_etree_iterparse  | 156 ms                                                                | 142 ms: 1.10x faster                                                           |
| json_loads           | 30.9 us                                                               | 32.9 us: 1.06x slower                                                          |
| Geometric mean       | (ref)                                                                 | 1.21x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250614-arminc-aarch64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.64 ms: 1.25x slower                                                          |
| python_startup         | 11.2 ms                                                               | 15.1 ms: 1.35x slower                                                          |
| Geometric mean         | (ref)                                                                 | 1.30x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250614-arminc-aarch64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.8 ms: 1.37x faster                                                          |
| django_template | 53.3 ms                                                               | 39.6 ms: 1.35x faster                                                          |
| genshi_text     | 35.2 ms                                                               | 27.6 ms: 1.27x faster                                                          |
| genshi_xml      | 69.8 ms                                                               | 60.5 ms: 1.15x faster                                                          |
| Geometric mean  | (ref)                                                                 | 1.28x faster                                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250614-arminc-aarch64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 196 us: 3.38x faster                                                           |
| async_tree_io            | 2.28 sec                                                              | 900 ms: 2.54x faster                                                           |
| async_tree_memoization   | 1.13 sec                                                              | 467 ms: 2.43x faster                                                           |
| async_tree_none          | 950 ms                                                                | 398 ms: 2.39x faster                                                           |
| mdp                      | 3.70 sec                                                              | 1.62 sec: 2.28x faster                                                         |
| deltablue                | 8.94 ms                                                               | 4.06 ms: 2.20x faster                                                          |
| go                       | 264 ms                                                                | 129 ms: 2.05x faster                                                           |
| generators               | 68.1 ms                                                               | 35.2 ms: 1.93x faster                                                          |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 659 ms: 1.93x faster                                                           |
| richards_super           | 107 ms                                                                | 58.2 ms: 1.84x faster                                                          |
| raytrace                 | 573 ms                                                                | 323 ms: 1.77x faster                                                           |
| chaos                    | 121 ms                                                                | 68.8 ms: 1.76x faster                                                          |
| richards                 | 91.7 ms                                                               | 52.9 ms: 1.73x faster                                                          |
| scimark_sor              | 246 ms                                                                | 147 ms: 1.68x faster                                                           |
| comprehensions           | 33.1 us                                                               | 20.3 us: 1.63x faster                                                          |
| deepcopy_memo            | 61.7 us                                                               | 38.2 us: 1.62x faster                                                          |
| crypto_pyaes             | 134 ms                                                                | 84.3 ms: 1.59x faster                                                          |
| hexiom                   | 10.9 ms                                                               | 6.92 ms: 1.58x faster                                                          |
| float                    | 135 ms                                                                | 85.7 ms: 1.57x faster                                                          |
| scimark_monte_carlo      | 128 ms                                                                | 82.0 ms: 1.56x faster                                                          |
| pylint                   | 485 ms                                                                | 315 ms: 1.54x faster                                                           |
| scimark_lu               | 227 ms                                                                | 147 ms: 1.54x faster                                                           |
| deepcopy                 | 511 us                                                                | 332 us: 1.54x faster                                                           |
| spectral_norm            | 186 ms                                                                | 125 ms: 1.49x faster                                                           |
| pyflate                  | 795 ms                                                                | 535 ms: 1.49x faster                                                           |
| regex_compile            | 177 ms                                                                | 122 ms: 1.45x faster                                                           |
| pickle_pure_python       | 529 us                                                                | 379 us: 1.40x faster                                                           |
| nbody                    | 166 ms                                                                | 119 ms: 1.39x faster                                                           |
| tomli_loads              | 3.36 sec                                                              | 2.43 sec: 1.38x faster                                                         |
| html5lib                 | 86.5 ms                                                               | 62.5 ms: 1.38x faster                                                          |
| dulwich_log              | 73.5 ms                                                               | 53.2 ms: 1.38x faster                                                          |
| unpickle_pure_python     | 366 us                                                                | 265 us: 1.38x faster                                                           |
| mako                     | 18.9 ms                                                               | 13.8 ms: 1.37x faster                                                          |
| pycparser                | 1.69 sec                                                              | 1.24 sec: 1.36x faster                                                         |
| django_template          | 53.3 ms                                                               | 39.6 ms: 1.35x faster                                                          |
| logging_simple           | 9.78 us                                                               | 7.45 us: 1.31x faster                                                          |
| logging_format           | 10.6 us                                                               | 8.10 us: 1.31x faster                                                          |
| sympy_integrate          | 26.5 ms                                                               | 20.6 ms: 1.29x faster                                                          |
| sympy_sum                | 184 ms                                                                | 143 ms: 1.28x faster                                                           |
| genshi_text              | 35.2 ms                                                               | 27.6 ms: 1.27x faster                                                          |
| 2to3                     | 381 ms                                                                | 300 ms: 1.27x faster                                                           |
| xml_etree_process        | 99.5 ms                                                               | 79.2 ms: 1.26x faster                                                          |
| deepcopy_reduce          | 4.60 us                                                               | 3.66 us: 1.25x faster                                                          |
| sympy_str                | 329 ms                                                                | 262 ms: 1.25x faster                                                           |
| coroutines               | 37.2 ms                                                               | 30.0 ms: 1.24x faster                                                          |
| json_dumps               | 16.7 ms                                                               | 13.7 ms: 1.22x faster                                                          |
| nqueens                  | 117 ms                                                                | 97.7 ms: 1.20x faster                                                          |
| docutils                 | 3.53 sec                                                              | 2.94 sec: 1.20x faster                                                         |
| pathlib                  | 26.3 ms                                                               | 22.1 ms: 1.19x faster                                                          |
| xml_etree_parse          | 212 ms                                                                | 178 ms: 1.19x faster                                                           |
| regex_dna                | 257 ms                                                                | 220 ms: 1.17x faster                                                           |
| pprint_pformat           | 2.36 sec                                                              | 2.02 sec: 1.17x faster                                                         |
| pprint_safe_repr         | 1.15 sec                                                              | 983 ms: 1.17x faster                                                           |
| regex_v8                 | 32.2 ms                                                               | 27.7 ms: 1.16x faster                                                          |
| meteor_contest           | 126 ms                                                                | 109 ms: 1.16x faster                                                           |
| sympy_expand             | 543 ms                                                                | 469 ms: 1.16x faster                                                           |
| genshi_xml               | 69.8 ms                                                               | 60.5 ms: 1.15x faster                                                          |
| scimark_fft              | 500 ms                                                                | 433 ms: 1.15x faster                                                           |
| fannkuch                 | 546 ms                                                                | 483 ms: 1.13x faster                                                           |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.92 ms: 1.10x faster                                                          |
| xml_etree_generate       | 123 ms                                                                | 112 ms: 1.10x faster                                                           |
| xml_etree_iterparse      | 156 ms                                                                | 142 ms: 1.10x faster                                                           |
| sqlite_synth             | 4.12 us                                                               | 3.77 us: 1.09x faster                                                          |
| regex_effbot             | 4.25 ms                                                               | 3.93 ms: 1.08x faster                                                          |
| asyncio_websockets       | 657 ms                                                                | 669 ms: 1.02x slower                                                           |
| json_loads               | 30.9 us                                                               | 32.9 us: 1.06x slower                                                          |
| telco                    | 8.49 ms                                                               | 9.32 ms: 1.10x slower                                                          |
| python_startup_no_site   | 6.89 ms                                                               | 8.64 ms: 1.25x slower                                                          |
| python_startup           | 11.2 ms                                                               | 15.1 ms: 1.35x slower                                                          |
| gc_traversal             | 4.15 ms                                                               | 7.02 ms: 1.69x slower                                                          |
| create_gc_cycles         | 2.26 ms                                                               | 3.97 ms: 1.76x slower                                                          |
| logging_silent           | 222 ns                                                                | 634 ns: 2.85x slower                                                           |
| coverage                 | 83.6 ms                                                               | 544 ms: 6.51x slower                                                           |
| thrift                   | 1.26 ms                                                               | 193 ms: 153.58x slower                                                         |
| Geometric mean           | (ref)                                                                 | 1.20x faster                                                                   |

Benchmark hidden because not significant (3): json, async_generators, pidigits
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250614-3.15.0a0-4019a15/bm-20250614-arminc-aarch64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.231x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: 1.37x