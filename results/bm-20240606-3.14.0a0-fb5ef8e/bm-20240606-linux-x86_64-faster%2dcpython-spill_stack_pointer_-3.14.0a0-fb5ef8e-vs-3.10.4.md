# Results vs. 3.10.4

- fork: faster-cpython
- ref: spill_stack_pointer_
- machine: linux-x86_64
- commit hash: fb5ef8e
- commit date: 2024-06-06
- overall geometric mean: 1.34x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240606-linux-x86_64-faster%2dcpython-spill_stack_pointer_-3.14.0a0-fb5ef8e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 271 ms: 1.28x faster                                                            |
| docutils       | 3.30 sec                                               | 2.80 sec: 1.18x faster                                                          |
| html5lib       | 88.9 ms                                                | 67.7 ms: 1.31x faster                                                           |
| tornado_http   | 136 ms                                                 | 94.9 ms: 1.44x faster                                                           |
| Geometric mean | (ref)                                                  | 1.30x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240606-linux-x86_64-faster%2dcpython-spill_stack_pointer_-3.14.0a0-fb5ef8e |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 391 ms: 1.86x faster                                                            |
| async_tree_io           | 1.77 sec                                               | 960 ms: 1.84x faster                                                            |
| async_tree_memoization  | 870 ms                                                 | 477 ms: 1.82x faster                                                            |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 621 ms: 1.64x faster                                                            |
| Geometric mean          | (ref)                                                  | 1.79x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240606-linux-x86_64-faster%2dcpython-spill_stack_pointer_-3.14.0a0-fb5ef8e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 92.1 ms: 1.67x faster                                                           |
| float          | 117 ms                                                 | 79.3 ms: 1.48x faster                                                           |
| pidigits       | 191 ms                                                 | 189 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                  | 1.35x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240606-linux-x86_64-faster%2dcpython-spill_stack_pointer_-3.14.0a0-fb5ef8e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 136 ms: 1.39x faster                                                            |
| regex_v8       | 27.8 ms                                                | 24.8 ms: 1.12x faster                                                           |
| regex_dna      | 227 ms                                                 | 223 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                  | 1.12x faster                                                                    |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240606-linux-x86_64-faster%2dcpython-spill_stack_pointer_-3.14.0a0-fb5ef8e |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 302 us: 1.60x faster                                                            |
| unpickle_pure_python | 331 us                                                 | 223 us: 1.48x faster                                                            |
| tomli_loads          | 3.14 sec                                               | 2.19 sec: 1.44x faster                                                          |
| json_dumps           | 14.2 ms                                                | 10.6 ms: 1.34x faster                                                           |
| xml_etree_process    | 79.1 ms                                                | 60.3 ms: 1.31x faster                                                           |
| xml_etree_generate   | 99.4 ms                                                | 87.0 ms: 1.14x faster                                                           |
| xml_etree_iterparse  | 115 ms                                                 | 106 ms: 1.08x faster                                                            |
| json_loads           | 31.2 us                                                | 28.8 us: 1.08x faster                                                           |
| xml_etree_parse      | 168 ms                                                 | 158 ms: 1.06x faster                                                            |
| pickle_list          | 5.08 us                                                | 5.04 us: 1.01x faster                                                           |
| unpickle_list        | 5.20 us                                                | 5.40 us: 1.04x slower                                                           |
| unpickle             | 14.4 us                                                | 15.3 us: 1.06x slower                                                           |
| pickle               | 10.7 us                                                | 11.7 us: 1.10x slower                                                           |
| pickle_dict          | 29.6 us                                                | 35.3 us: 1.19x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.14x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240606-linux-x86_64-faster%2dcpython-spill_stack_pointer_-3.14.0a0-fb5ef8e |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.6 ms: 1.37x faster                                                           |
| python_startup_no_site | 5.93 ms                                                | 7.13 ms: 1.20x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240606-linux-x86_64-faster%2dcpython-spill_stack_pointer_-3.14.0a0-fb5ef8e |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.9 ms: 1.49x faster                                                           |
| genshi_text     | 31.8 ms                                                | 23.6 ms: 1.35x faster                                                           |
| django_template | 48.2 ms                                                | 36.1 ms: 1.34x faster                                                           |
| genshi_xml      | 66.0 ms                                                | 50.5 ms: 1.31x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.37x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240606-linux-x86_64-faster%2dcpython-spill_stack_pointer_-3.14.0a0-fb5ef8e |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 168 us: 3.23x faster                                                            |
| generators               | 80.1 ms                                                | 27.9 ms: 2.87x faster                                                           |
| deltablue                | 7.91 ms                                                | 3.26 ms: 2.43x faster                                                           |
| raytrace                 | 507 ms                                                 | 264 ms: 1.92x faster                                                            |
| chaos                    | 115 ms                                                 | 60.8 ms: 1.90x faster                                                           |
| async_tree_none          | 728 ms                                                 | 391 ms: 1.86x faster                                                            |
| async_tree_io            | 1.77 sec                                               | 960 ms: 1.84x faster                                                            |
| logging_silent           | 190 ns                                                 | 104 ns: 1.83x faster                                                            |
| async_tree_memoization   | 870 ms                                                 | 477 ms: 1.82x faster                                                            |
| asyncio_tcp              | 922 ms                                                 | 509 ms: 1.81x faster                                                            |
| richards_super           | 94.7 ms                                                | 54.0 ms: 1.75x faster                                                           |
| pylint                   | 551 ms                                                 | 316 ms: 1.74x faster                                                            |
| scimark_sor              | 220 ms                                                 | 126 ms: 1.74x faster                                                            |
| scimark_monte_carlo      | 118 ms                                                 | 68.5 ms: 1.72x faster                                                           |
| comprehensions           | 28.8 us                                                | 16.9 us: 1.70x faster                                                           |
| hexiom                   | 10.4 ms                                                | 6.16 ms: 1.69x faster                                                           |
| crypto_pyaes             | 128 ms                                                 | 76.4 ms: 1.67x faster                                                           |
| nbody                    | 154 ms                                                 | 92.1 ms: 1.67x faster                                                           |
| go                       | 240 ms                                                 | 145 ms: 1.66x faster                                                            |
| richards                 | 79.3 ms                                                | 48.3 ms: 1.64x faster                                                           |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 621 ms: 1.64x faster                                                            |
| sqlglot_parse            | 2.17 ms                                                | 1.34 ms: 1.62x faster                                                           |
| pickle_pure_python       | 484 us                                                 | 302 us: 1.60x faster                                                            |
| sqlglot_transpile        | 2.57 ms                                                | 1.64 ms: 1.57x faster                                                           |
| scimark_lu               | 176 ms                                                 | 116 ms: 1.52x faster                                                            |
| coroutines               | 35.1 ms                                                | 23.1 ms: 1.52x faster                                                           |
| mako                     | 16.3 ms                                                | 10.9 ms: 1.49x faster                                                           |
| unpickle_pure_python     | 331 us                                                 | 223 us: 1.48x faster                                                            |
| deepcopy_memo            | 58.5 us                                                | 39.5 us: 1.48x faster                                                           |
| float                    | 117 ms                                                 | 79.3 ms: 1.48x faster                                                           |
| pyflate                  | 716 ms                                                 | 486 ms: 1.47x faster                                                            |
| spectral_norm            | 170 ms                                                 | 116 ms: 1.46x faster                                                            |
| tornado_http             | 136 ms                                                 | 94.9 ms: 1.44x faster                                                           |
| tomli_loads              | 3.14 sec                                               | 2.19 sec: 1.44x faster                                                          |
| logging_simple           | 8.30 us                                                | 5.89 us: 1.41x faster                                                           |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.85 sec: 1.39x faster                                                          |
| regex_compile            | 188 ms                                                 | 136 ms: 1.39x faster                                                            |
| logging_format           | 9.09 us                                                | 6.55 us: 1.39x faster                                                           |
| pprint_pformat           | 2.10 sec                                               | 1.53 sec: 1.38x faster                                                          |
| python_startup           | 14.6 ms                                                | 10.6 ms: 1.37x faster                                                           |
| pprint_safe_repr         | 1.02 sec                                               | 745 ms: 1.37x faster                                                            |
| genshi_text              | 31.8 ms                                                | 23.6 ms: 1.35x faster                                                           |
| pycparser                | 1.58 sec                                               | 1.17 sec: 1.35x faster                                                          |
| json_dumps               | 14.2 ms                                                | 10.6 ms: 1.34x faster                                                           |
| django_template          | 48.2 ms                                                | 36.1 ms: 1.34x faster                                                           |
| fannkuch                 | 532 ms                                                 | 399 ms: 1.33x faster                                                            |
| thrift                   | 1.07 ms                                                | 812 us: 1.32x faster                                                            |
| html5lib                 | 88.9 ms                                                | 67.7 ms: 1.31x faster                                                           |
| xml_etree_process        | 79.1 ms                                                | 60.3 ms: 1.31x faster                                                           |
| deepcopy                 | 479 us                                                 | 366 us: 1.31x faster                                                            |
| genshi_xml               | 66.0 ms                                                | 50.5 ms: 1.31x faster                                                           |
| nqueens                  | 106 ms                                                 | 81.3 ms: 1.30x faster                                                           |
| sqlglot_normalize        | 143 ms                                                 | 111 ms: 1.29x faster                                                            |
| 2to3                     | 348 ms                                                 | 271 ms: 1.28x faster                                                            |
| dulwich_log              | 84.3 ms                                                | 65.8 ms: 1.28x faster                                                           |
| pathlib                  | 20.5 ms                                                | 16.1 ms: 1.27x faster                                                           |
| deepcopy_reduce          | 4.17 us                                                | 3.30 us: 1.27x faster                                                           |
| sympy_integrate          | 25.8 ms                                                | 20.5 ms: 1.26x faster                                                           |
| sympy_sum                | 196 ms                                                 | 157 ms: 1.26x faster                                                            |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.17 ms: 1.25x faster                                                           |
| sqlglot_optimize         | 69.2 ms                                                | 55.4 ms: 1.25x faster                                                           |
| scimark_fft              | 466 ms                                                 | 379 ms: 1.23x faster                                                            |
| sympy_str                | 346 ms                                                 | 282 ms: 1.22x faster                                                            |
| bench_thread_pool        | 986 us                                                 | 828 us: 1.19x faster                                                            |
| sympy_expand             | 566 ms                                                 | 476 ms: 1.19x faster                                                            |
| dask                     | 441 ms                                                 | 372 ms: 1.18x faster                                                            |
| docutils                 | 3.30 sec                                               | 2.80 sec: 1.18x faster                                                          |
| xml_etree_generate       | 99.4 ms                                                | 87.0 ms: 1.14x faster                                                           |
| regex_v8                 | 27.8 ms                                                | 24.8 ms: 1.12x faster                                                           |
| xml_etree_iterparse      | 115 ms                                                 | 106 ms: 1.08x faster                                                            |
| json_loads               | 31.2 us                                                | 28.8 us: 1.08x faster                                                           |
| meteor_contest           | 120 ms                                                 | 110 ms: 1.08x faster                                                            |
| xml_etree_parse          | 168 ms                                                 | 158 ms: 1.06x faster                                                            |
| json                     | 5.69 ms                                                | 5.39 ms: 1.06x faster                                                           |
| mdp                      | 2.85 sec                                               | 2.71 sec: 1.05x faster                                                          |
| sqlite_synth             | 3.02 us                                                | 2.97 us: 1.02x faster                                                           |
| regex_dna                | 227 ms                                                 | 223 ms: 1.02x faster                                                            |
| pickle_list              | 5.08 us                                                | 5.04 us: 1.01x faster                                                           |
| pidigits                 | 191 ms                                                 | 189 ms: 1.01x faster                                                            |
| asyncio_websockets       | 559 ms                                                 | 564 ms: 1.01x slower                                                            |
| async_generators         | 444 ms                                                 | 458 ms: 1.03x slower                                                            |
| unpickle_list            | 5.20 us                                                | 5.40 us: 1.04x slower                                                           |
| unpickle                 | 14.4 us                                                | 15.3 us: 1.06x slower                                                           |
| pickle                   | 10.7 us                                                | 11.7 us: 1.10x slower                                                           |
| gc_traversal             | 3.62 ms                                                | 4.00 ms: 1.10x slower                                                           |
| create_gc_cycles         | 1.62 ms                                                | 1.80 ms: 1.11x slower                                                           |
| telco                    | 7.27 ms                                                | 8.50 ms: 1.17x slower                                                           |
| coverage                 | 79.4 ms                                                | 94.2 ms: 1.19x slower                                                           |
| pickle_dict              | 29.6 us                                                | 35.3 us: 1.19x slower                                                           |
| python_startup_no_site   | 5.93 ms                                                | 7.13 ms: 1.20x slower                                                           |
| Geometric mean           | (ref)                                                  | 1.34x faster                                                                    |

Benchmark hidden because not significant (2): bench_mp_pool, regex_effbot
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240606-3.14.0a0-fb5ef8e/bm-20240606-linux-x86_64-faster%2dcpython-spill_stack_pointer_-3.14.0a0-fb5ef8e.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.11x