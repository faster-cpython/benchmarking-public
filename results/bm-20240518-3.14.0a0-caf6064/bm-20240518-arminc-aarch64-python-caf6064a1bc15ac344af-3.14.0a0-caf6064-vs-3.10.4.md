# Results vs. 3.10.4

- fork: python
- ref: caf6064a1bc15ac344af
- machine: linux-aarch64
- commit hash: caf6064
- commit date: 2024-05-18
- overall geometric mean: 1.24x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 303 ms: 1.26x faster                                                    |
| chameleon      | 10.8 ms                                                               | 9.03 ms: 1.20x faster                                                   |
| docutils       | 3.53 sec                                                              | 3.09 sec: 1.14x faster                                                  |
| html5lib       | 86.5 ms                                                               | 68.3 ms: 1.27x faster                                                   |
| tornado_http   | 178 ms                                                                | 131 ms: 1.36x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.24x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 486 ms: 1.96x faster                                                    |
| async_tree_io           | 2.28 sec                                                              | 1.22 sec: 1.87x faster                                                  |
| async_tree_memoization  | 1.13 sec                                                              | 642 ms: 1.77x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 785 ms: 1.62x faster                                                    |
| Geometric mean          | (ref)                                                                 | 1.80x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 90.6 ms: 1.49x faster                                                   |
| nbody          | 166 ms                                                                | 113 ms: 1.47x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.30x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 131 ms: 1.35x faster                                                    |
| regex_dna      | 257 ms                                                                | 247 ms: 1.04x faster                                                    |
| regex_v8       | 32.2 ms                                                               | 31.1 ms: 1.03x faster                                                   |
| regex_effbot   | 4.25 ms                                                               | 4.88 ms: 1.15x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.06x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 358 us: 1.48x faster                                                    |
| unpickle_pure_python | 366 us                                                                | 254 us: 1.44x faster                                                    |
| tomli_loads          | 3.36 sec                                                              | 2.56 sec: 1.31x faster                                                  |
| json_dumps           | 16.7 ms                                                               | 13.3 ms: 1.26x faster                                                   |
| xml_etree_process    | 99.5 ms                                                               | 80.3 ms: 1.24x faster                                                   |
| xml_etree_parse      | 212 ms                                                                | 192 ms: 1.10x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 112 ms: 1.10x faster                                                    |
| unpickle_list        | 6.99 us                                                               | 6.63 us: 1.05x faster                                                   |
| pickle_list          | 5.24 us                                                               | 5.19 us: 1.01x faster                                                   |
| json_loads           | 30.9 us                                                               | 32.3 us: 1.04x slower                                                   |
| pickle_dict          | 35.1 us                                                               | 37.4 us: 1.06x slower                                                   |
| pickle               | 12.5 us                                                               | 13.8 us: 1.10x slower                                                   |
| unpickle             | 17.5 us                                                               | 19.7 us: 1.13x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.11x faster                                                            |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 12.3 ms: 1.10x slower                                                   |
| python_startup_no_site | 6.89 ms                                                               | 8.48 ms: 1.23x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.17x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.5 ms: 1.40x faster                                                   |
| django_template | 53.3 ms                                                               | 41.7 ms: 1.28x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 28.6 ms: 1.23x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 61.2 ms: 1.14x faster                                                   |
| Geometric mean  | (ref)                                                                 | 1.26x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 197 us: 3.36x faster                                                    |
| deltablue                | 8.94 ms                                                               | 3.88 ms: 2.31x faster                                                   |
| bench_mp_pool            | 14.5 ms                                                               | 7.41 ms: 1.96x faster                                                   |
| async_tree_none          | 950 ms                                                                | 486 ms: 1.96x faster                                                    |
| raytrace                 | 573 ms                                                                | 297 ms: 1.93x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 1.22 sec: 1.87x faster                                                  |
| chaos                    | 121 ms                                                                | 67.6 ms: 1.79x faster                                                   |
| richards_super           | 107 ms                                                                | 60.1 ms: 1.78x faster                                                   |
| async_tree_memoization   | 1.13 sec                                                              | 642 ms: 1.77x faster                                                    |
| generators               | 68.1 ms                                                               | 39.0 ms: 1.74x faster                                                   |
| richards                 | 91.7 ms                                                               | 53.3 ms: 1.72x faster                                                   |
| sqlglot_parse            | 2.40 ms                                                               | 1.40 ms: 1.71x faster                                                   |
| logging_silent           | 222 ns                                                                | 133 ns: 1.67x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 81.5 ms: 1.64x faster                                                   |
| asyncio_tcp              | 944 ms                                                                | 574 ms: 1.64x faster                                                    |
| sqlglot_transpile        | 2.84 ms                                                               | 1.73 ms: 1.64x faster                                                   |
| scimark_lu               | 227 ms                                                                | 139 ms: 1.64x faster                                                    |
| go                       | 264 ms                                                                | 161 ms: 1.64x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 785 ms: 1.62x faster                                                    |
| comprehensions           | 33.1 us                                                               | 20.7 us: 1.60x faster                                                   |
| hexiom                   | 10.9 ms                                                               | 7.03 ms: 1.55x faster                                                   |
| scimark_sor              | 246 ms                                                                | 159 ms: 1.55x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 83.0 ms: 1.54x faster                                                   |
| float                    | 135 ms                                                                | 90.6 ms: 1.49x faster                                                   |
| pickle_pure_python       | 529 us                                                                | 358 us: 1.48x faster                                                    |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.22 sec: 1.48x faster                                                  |
| nbody                    | 166 ms                                                                | 113 ms: 1.47x faster                                                    |
| unpickle_pure_python     | 366 us                                                                | 254 us: 1.44x faster                                                    |
| pylint                   | 485 ms                                                                | 342 ms: 1.42x faster                                                    |
| mako                     | 18.9 ms                                                               | 13.5 ms: 1.40x faster                                                   |
| logging_simple           | 9.78 us                                                               | 7.00 us: 1.40x faster                                                   |
| pycparser                | 1.69 sec                                                              | 1.22 sec: 1.39x faster                                                  |
| pyflate                  | 795 ms                                                                | 578 ms: 1.38x faster                                                    |
| tornado_http             | 178 ms                                                                | 131 ms: 1.36x faster                                                    |
| logging_format           | 10.6 us                                                               | 7.85 us: 1.35x faster                                                   |
| regex_compile            | 177 ms                                                                | 131 ms: 1.35x faster                                                    |
| thrift                   | 1.26 ms                                                               | 942 us: 1.34x faster                                                    |
| spectral_norm            | 186 ms                                                                | 141 ms: 1.32x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 2.56 sec: 1.31x faster                                                  |
| coroutines               | 37.2 ms                                                               | 29.0 ms: 1.28x faster                                                   |
| django_template          | 53.3 ms                                                               | 41.7 ms: 1.28x faster                                                   |
| sympy_sum                | 184 ms                                                                | 144 ms: 1.28x faster                                                    |
| html5lib                 | 86.5 ms                                                               | 68.3 ms: 1.27x faster                                                   |
| dulwich_log              | 73.5 ms                                                               | 58.3 ms: 1.26x faster                                                   |
| 2to3                     | 381 ms                                                                | 303 ms: 1.26x faster                                                    |
| json_dumps               | 16.7 ms                                                               | 13.3 ms: 1.26x faster                                                   |
| sympy_integrate          | 26.5 ms                                                               | 21.1 ms: 1.26x faster                                                   |
| xml_etree_process        | 99.5 ms                                                               | 80.3 ms: 1.24x faster                                                   |
| pprint_pformat           | 2.36 sec                                                              | 1.91 sec: 1.24x faster                                                  |
| bench_thread_pool        | 1.59 ms                                                               | 1.29 ms: 1.23x faster                                                   |
| genshi_text              | 35.2 ms                                                               | 28.6 ms: 1.23x faster                                                   |
| sympy_str                | 329 ms                                                                | 268 ms: 1.23x faster                                                    |
| pprint_safe_repr         | 1.15 sec                                                              | 935 ms: 1.23x faster                                                    |
| sqlglot_normalize        | 156 ms                                                                | 128 ms: 1.22x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 21.8 ms: 1.21x faster                                                   |
| dask                     | 450 ms                                                                | 373 ms: 1.21x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 51.3 us: 1.20x faster                                                   |
| chameleon                | 10.8 ms                                                               | 9.03 ms: 1.20x faster                                                   |
| sqlglot_optimize         | 75.4 ms                                                               | 63.0 ms: 1.20x faster                                                   |
| nqueens                  | 117 ms                                                                | 99.0 ms: 1.19x faster                                                   |
| fannkuch                 | 546 ms                                                                | 463 ms: 1.18x faster                                                    |
| sympy_expand             | 543 ms                                                                | 462 ms: 1.18x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.53 ms: 1.17x faster                                                   |
| docutils                 | 3.53 sec                                                              | 3.09 sec: 1.14x faster                                                  |
| genshi_xml               | 69.8 ms                                                               | 61.2 ms: 1.14x faster                                                   |
| deepcopy                 | 511 us                                                                | 450 us: 1.14x faster                                                    |
| scimark_fft              | 500 ms                                                                | 443 ms: 1.13x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 4.07 us: 1.13x faster                                                   |
| meteor_contest           | 126 ms                                                                | 113 ms: 1.11x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 192 ms: 1.10x faster                                                    |
| mdp                      | 3.70 sec                                                              | 3.37 sec: 1.10x faster                                                  |
| xml_etree_generate       | 123 ms                                                                | 112 ms: 1.10x faster                                                    |
| sqlite_synth             | 4.12 us                                                               | 3.90 us: 1.06x faster                                                   |
| unpickle_list            | 6.99 us                                                               | 6.63 us: 1.05x faster                                                   |
| regex_dna                | 257 ms                                                                | 247 ms: 1.04x faster                                                    |
| regex_v8                 | 32.2 ms                                                               | 31.1 ms: 1.03x faster                                                   |
| json                     | 5.88 ms                                                               | 5.68 ms: 1.03x faster                                                   |
| pickle_list              | 5.24 us                                                               | 5.19 us: 1.01x faster                                                   |
| json_loads               | 30.9 us                                                               | 32.3 us: 1.04x slower                                                   |
| pickle_dict              | 35.1 us                                                               | 37.4 us: 1.06x slower                                                   |
| create_gc_cycles         | 2.26 ms                                                               | 2.42 ms: 1.07x slower                                                   |
| async_generators         | 452 ms                                                                | 496 ms: 1.10x slower                                                    |
| pickle                   | 12.5 us                                                               | 13.8 us: 1.10x slower                                                   |
| python_startup           | 11.2 ms                                                               | 12.3 ms: 1.10x slower                                                   |
| unpickle                 | 17.5 us                                                               | 19.7 us: 1.13x slower                                                   |
| regex_effbot             | 4.25 ms                                                               | 4.88 ms: 1.15x slower                                                   |
| coverage                 | 83.6 ms                                                               | 99.5 ms: 1.19x slower                                                   |
| python_startup_no_site   | 6.89 ms                                                               | 8.48 ms: 1.23x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 5.29 ms: 1.27x slower                                                   |
| telco                    | 8.49 ms                                                               | 166 ms: 19.51x slower                                                   |
| Geometric mean           | (ref)                                                                 | 1.24x faster                                                            |

Benchmark hidden because not significant (4): xml_etree_iterparse, flaskblogging, pidigits, asyncio_websockets
Ignored benchmarks (5) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240518-3.14.0a0-caf6064/bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.13x