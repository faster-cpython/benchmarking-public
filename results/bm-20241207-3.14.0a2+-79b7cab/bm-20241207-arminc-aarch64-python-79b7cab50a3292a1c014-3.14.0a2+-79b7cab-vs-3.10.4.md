# Results vs. 3.10.4

- fork: python
- ref: 79b7cab50a3292a1c014
- machine: linux-aarch64
- commit hash: 79b7cab
- commit date: 2024-12-07
- overall geometric mean: 1.308x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.29x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 307 ms: 1.24x faster                                                     |
| docutils       | 3.53 sec                                                              | 3.05 sec: 1.16x faster                                                   |
| html5lib       | 86.5 ms                                                               | 63.8 ms: 1.35x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.25x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 917 ms: 2.49x faster                                                     |
| async_tree_none         | 950 ms                                                                | 401 ms: 2.37x faster                                                     |
| async_tree_memoization  | 1.13 sec                                                              | 528 ms: 2.15x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 690 ms: 1.84x faster                                                     |
| Geometric mean          | (ref)                                                                 | 2.20x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 95.8 ms: 1.41x faster                                                    |
| nbody          | 166 ms                                                                | 120 ms: 1.38x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.24x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 128 ms: 1.38x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.09x faster                                                             |

Benchmark hidden because not significant (3): regex_effbot, regex_dna, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 386 us: 1.37x faster                                                     |
| unpickle_pure_python | 366 us                                                                | 268 us: 1.36x faster                                                     |
| tomli_loads          | 3.36 sec                                                              | 2.76 sec: 1.21x faster                                                   |
| xml_etree_process    | 99.5 ms                                                               | 83.6 ms: 1.19x faster                                                    |
| json_dumps           | 16.7 ms                                                               | 14.2 ms: 1.17x faster                                                    |
| xml_etree_parse      | 212 ms                                                                | 184 ms: 1.15x faster                                                     |
| xml_etree_iterparse  | 156 ms                                                                | 140 ms: 1.11x faster                                                     |
| xml_etree_generate   | 123 ms                                                                | 116 ms: 1.06x faster                                                     |
| json_loads           | 30.9 us                                                               | 32.0 us: 1.03x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.17x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 9.08 ms: 1.32x slower                                                    |
| python_startup         | 11.2 ms                                                               | 16.2 ms: 1.45x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.38x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 14.4 ms: 1.32x faster                                                    |
| django_template | 53.3 ms                                                               | 40.5 ms: 1.32x faster                                                    |
| genshi_text     | 35.2 ms                                                               | 29.4 ms: 1.20x faster                                                    |
| genshi_xml      | 69.8 ms                                                               | 63.3 ms: 1.10x faster                                                    |
| Geometric mean  | (ref)                                                                 | 1.23x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 205 us: 3.23x faster                                                     |
| async_tree_io            | 2.28 sec                                                              | 917 ms: 2.49x faster                                                     |
| async_tree_none          | 950 ms                                                                | 401 ms: 2.37x faster                                                     |
| deltablue                | 8.94 ms                                                               | 3.98 ms: 2.24x faster                                                    |
| async_tree_memoization   | 1.13 sec                                                              | 528 ms: 2.15x faster                                                     |
| generators               | 68.1 ms                                                               | 36.6 ms: 1.86x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 690 ms: 1.84x faster                                                     |
| go                       | 264 ms                                                                | 144 ms: 1.84x faster                                                     |
| raytrace                 | 573 ms                                                                | 321 ms: 1.79x faster                                                     |
| richards_super           | 107 ms                                                                | 61.8 ms: 1.74x faster                                                    |
| chaos                    | 121 ms                                                                | 71.1 ms: 1.70x faster                                                    |
| richards                 | 91.7 ms                                                               | 55.0 ms: 1.67x faster                                                    |
| sqlglot_parse            | 2.40 ms                                                               | 1.45 ms: 1.66x faster                                                    |
| scimark_lu               | 227 ms                                                                | 137 ms: 1.65x faster                                                     |
| sqlglot_transpile        | 2.84 ms                                                               | 1.78 ms: 1.59x faster                                                    |
| comprehensions           | 33.1 us                                                               | 21.0 us: 1.58x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 85.2 ms: 1.57x faster                                                    |
| logging_silent           | 222 ns                                                                | 143 ns: 1.55x faster                                                     |
| deepcopy_memo            | 61.7 us                                                               | 40.3 us: 1.53x faster                                                    |
| pylint                   | 485 ms                                                                | 318 ms: 1.53x faster                                                     |
| hexiom                   | 10.9 ms                                                               | 7.25 ms: 1.51x faster                                                    |
| scimark_sor              | 246 ms                                                                | 164 ms: 1.50x faster                                                     |
| scimark_monte_carlo      | 128 ms                                                                | 85.4 ms: 1.50x faster                                                    |
| deepcopy                 | 511 us                                                                | 344 us: 1.48x faster                                                     |
| float                    | 135 ms                                                                | 95.8 ms: 1.41x faster                                                    |
| regex_compile            | 177 ms                                                                | 128 ms: 1.38x faster                                                     |
| nbody                    | 166 ms                                                                | 120 ms: 1.38x faster                                                     |
| pycparser                | 1.69 sec                                                              | 1.23 sec: 1.38x faster                                                   |
| pickle_pure_python       | 529 us                                                                | 386 us: 1.37x faster                                                     |
| logging_format           | 10.6 us                                                               | 7.74 us: 1.37x faster                                                    |
| unpickle_pure_python     | 366 us                                                                | 268 us: 1.36x faster                                                     |
| sqlalchemy_declarative   | 197 ms                                                                | 145 ms: 1.36x faster                                                     |
| html5lib                 | 86.5 ms                                                               | 63.8 ms: 1.35x faster                                                    |
| logging_simple           | 9.78 us                                                               | 7.24 us: 1.35x faster                                                    |
| sqlalchemy_imperative    | 20.5 ms                                                               | 15.5 ms: 1.32x faster                                                    |
| mako                     | 18.9 ms                                                               | 14.4 ms: 1.32x faster                                                    |
| django_template          | 53.3 ms                                                               | 40.5 ms: 1.32x faster                                                    |
| pyflate                  | 795 ms                                                                | 605 ms: 1.31x faster                                                     |
| thrift                   | 1.26 ms                                                               | 977 us: 1.29x faster                                                     |
| sympy_sum                | 184 ms                                                                | 143 ms: 1.29x faster                                                     |
| coroutines               | 37.2 ms                                                               | 29.1 ms: 1.28x faster                                                    |
| spectral_norm            | 186 ms                                                                | 146 ms: 1.28x faster                                                     |
| deepcopy_reduce          | 4.60 us                                                               | 3.62 us: 1.27x faster                                                    |
| 2to3                     | 381 ms                                                                | 307 ms: 1.24x faster                                                     |
| tomli_loads              | 3.36 sec                                                              | 2.76 sec: 1.21x faster                                                   |
| sympy_integrate          | 26.5 ms                                                               | 21.9 ms: 1.21x faster                                                    |
| dulwich_log              | 73.5 ms                                                               | 60.6 ms: 1.21x faster                                                    |
| pprint_pformat           | 2.36 sec                                                              | 1.95 sec: 1.21x faster                                                   |
| pprint_safe_repr         | 1.15 sec                                                              | 952 ms: 1.21x faster                                                     |
| bench_thread_pool        | 1.59 ms                                                               | 1.33 ms: 1.20x faster                                                    |
| sqlglot_optimize         | 75.4 ms                                                               | 62.9 ms: 1.20x faster                                                    |
| genshi_text              | 35.2 ms                                                               | 29.4 ms: 1.20x faster                                                    |
| xml_etree_process        | 99.5 ms                                                               | 83.6 ms: 1.19x faster                                                    |
| sympy_str                | 329 ms                                                                | 278 ms: 1.18x faster                                                     |
| json_dumps               | 16.7 ms                                                               | 14.2 ms: 1.17x faster                                                    |
| sqlglot_normalize        | 156 ms                                                                | 134 ms: 1.17x faster                                                     |
| docutils                 | 3.53 sec                                                              | 3.05 sec: 1.16x faster                                                   |
| xml_etree_parse          | 212 ms                                                                | 184 ms: 1.15x faster                                                     |
| sympy_expand             | 543 ms                                                                | 471 ms: 1.15x faster                                                     |
| pathlib                  | 26.3 ms                                                               | 23.1 ms: 1.14x faster                                                    |
| fannkuch                 | 546 ms                                                                | 490 ms: 1.11x faster                                                     |
| xml_etree_iterparse      | 156 ms                                                                | 140 ms: 1.11x faster                                                     |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.86 ms: 1.11x faster                                                    |
| scimark_fft              | 500 ms                                                                | 453 ms: 1.10x faster                                                     |
| genshi_xml               | 69.8 ms                                                               | 63.3 ms: 1.10x faster                                                    |
| nqueens                  | 117 ms                                                                | 107 ms: 1.10x faster                                                     |
| mdp                      | 3.70 sec                                                              | 3.44 sec: 1.07x faster                                                   |
| meteor_contest           | 126 ms                                                                | 118 ms: 1.07x faster                                                     |
| xml_etree_generate       | 123 ms                                                                | 116 ms: 1.06x faster                                                     |
| json_loads               | 30.9 us                                                               | 32.0 us: 1.03x slower                                                    |
| async_generators         | 452 ms                                                                | 510 ms: 1.13x slower                                                     |
| telco                    | 8.49 ms                                                               | 10.00 ms: 1.18x slower                                                   |
| coverage                 | 83.6 ms                                                               | 98.7 ms: 1.18x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 9.08 ms: 1.32x slower                                                    |
| python_startup           | 11.2 ms                                                               | 16.2 ms: 1.45x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 3.30 ms: 1.46x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 6.92 ms: 1.67x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 3.66 sec: 252.13x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.20x faster                                                             |

Benchmark hidden because not significant (7): regex_effbot, json, regex_dna, sqlite_synth, regex_v8, pidigits, asyncio_websockets
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20241207-3.14.0a2+-79b7cab/bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.308x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.29x