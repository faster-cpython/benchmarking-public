# Results vs. 3.10.4

- fork: kumaraditya303
- ref: per_thread_cur_task
- machine: linux-x86_64
- commit hash: ba92dfb
- commit date: 2025-02-10
- overall geometric mean: 1.265x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: 1.51x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 304 ms: 1.14x faster                                                          |
| docutils       | 3.30 sec                                               | 2.82 sec: 1.17x faster                                                        |
| html5lib       | 88.9 ms                                                | 69.9 ms: 1.27x faster                                                         |
| Geometric mean | (ref)                                                  | 1.19x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 590 ms: 3.00x faster                                                          |
| async_tree_none         | 728 ms                                                 | 281 ms: 2.59x faster                                                          |
| async_tree_memoization  | 870 ms                                                 | 360 ms: 2.42x faster                                                          |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 516 ms: 1.97x faster                                                          |
| Geometric mean          | (ref)                                                  | 2.47x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 76.9 ms: 1.52x faster                                                         |
| nbody          | 154 ms                                                 | 136 ms: 1.13x faster                                                          |
| pidigits       | 191 ms                                                 | 192 ms: 1.00x slower                                                          |
| Geometric mean | (ref)                                                  | 1.20x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 146 ms: 1.29x faster                                                          |
| regex_v8       | 27.8 ms                                                | 25.7 ms: 1.08x faster                                                         |
| regex_effbot   | 3.63 ms                                                | 3.46 ms: 1.05x faster                                                         |
| Geometric mean | (ref)                                                  | 1.10x faster                                                                  |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 2.31 sec: 1.36x faster                                                        |
| pickle_pure_python   | 484 us                                                 | 370 us: 1.31x faster                                                          |
| unpickle_pure_python | 331 us                                                 | 257 us: 1.29x faster                                                          |
| xml_etree_iterparse  | 115 ms                                                 | 95.2 ms: 1.21x faster                                                         |
| xml_etree_process    | 79.1 ms                                                | 67.3 ms: 1.18x faster                                                         |
| xml_etree_parse      | 168 ms                                                 | 149 ms: 1.13x faster                                                          |
| json_dumps           | 14.2 ms                                                | 12.8 ms: 1.11x faster                                                         |
| xml_etree_generate   | 99.4 ms                                                | 94.9 ms: 1.05x faster                                                         |
| json_loads           | 31.2 us                                                | 33.0 us: 1.06x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 15.0 ms: 1.03x slower                                                         |
| python_startup_no_site | 5.93 ms                                                | 9.31 ms: 1.57x slower                                                         |
| Geometric mean         | (ref)                                                  | 1.27x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 40.4 ms: 1.19x faster                                                         |
| genshi_text     | 31.8 ms                                                | 27.7 ms: 1.15x faster                                                         |
| genshi_xml      | 66.0 ms                                                | 60.2 ms: 1.10x faster                                                         |
| Geometric mean  | (ref)                                                  | 1.11x faster                                                                  |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_io            | 1.77 sec                                               | 590 ms: 3.00x faster                                                          |
| typing_runtime_protocols | 544 us                                                 | 203 us: 2.68x faster                                                          |
| async_tree_none          | 728 ms                                                 | 281 ms: 2.59x faster                                                          |
| generators               | 80.1 ms                                                | 31.6 ms: 2.53x faster                                                         |
| async_tree_memoization   | 870 ms                                                 | 360 ms: 2.42x faster                                                          |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 516 ms: 1.97x faster                                                          |
| gc_traversal             | 3.62 ms                                                | 1.98 ms: 1.83x faster                                                         |
| pylint                   | 551 ms                                                 | 311 ms: 1.77x faster                                                          |
| go                       | 240 ms                                                 | 141 ms: 1.70x faster                                                          |
| logging_silent           | 190 ns                                                 | 112 ns: 1.70x faster                                                          |
| deltablue                | 7.91 ms                                                | 4.72 ms: 1.68x faster                                                         |
| scimark_sor              | 220 ms                                                 | 138 ms: 1.59x faster                                                          |
| chaos                    | 115 ms                                                 | 73.1 ms: 1.58x faster                                                         |
| deepcopy                 | 479 us                                                 | 305 us: 1.57x faster                                                          |
| deepcopy_memo            | 58.5 us                                                | 38.2 us: 1.53x faster                                                         |
| float                    | 117 ms                                                 | 76.9 ms: 1.52x faster                                                         |
| richards_super           | 94.7 ms                                                | 63.1 ms: 1.50x faster                                                         |
| spectral_norm            | 170 ms                                                 | 114 ms: 1.49x faster                                                          |
| coroutines               | 35.1 ms                                                | 23.8 ms: 1.47x faster                                                         |
| richards                 | 79.3 ms                                                | 54.0 ms: 1.47x faster                                                         |
| comprehensions           | 28.8 us                                                | 19.6 us: 1.47x faster                                                         |
| crypto_pyaes             | 128 ms                                                 | 88.6 ms: 1.44x faster                                                         |
| raytrace                 | 507 ms                                                 | 351 ms: 1.44x faster                                                          |
| pyflate                  | 716 ms                                                 | 506 ms: 1.41x faster                                                          |
| sqlglot_parse            | 2.17 ms                                                | 1.54 ms: 1.40x faster                                                         |
| scimark_monte_carlo      | 118 ms                                                 | 85.7 ms: 1.38x faster                                                         |
| sqlglot_transpile        | 2.57 ms                                                | 1.88 ms: 1.37x faster                                                         |
| tomli_loads              | 3.14 sec                                               | 2.31 sec: 1.36x faster                                                        |
| hexiom                   | 10.4 ms                                                | 7.69 ms: 1.35x faster                                                         |
| pycparser                | 1.58 sec                                               | 1.20 sec: 1.31x faster                                                        |
| pickle_pure_python       | 484 us                                                 | 370 us: 1.31x faster                                                          |
| deepcopy_reduce          | 4.17 us                                                | 3.23 us: 1.29x faster                                                         |
| regex_compile            | 188 ms                                                 | 146 ms: 1.29x faster                                                          |
| unpickle_pure_python     | 331 us                                                 | 257 us: 1.29x faster                                                          |
| html5lib                 | 88.9 ms                                                | 69.9 ms: 1.27x faster                                                         |
| scimark_lu               | 176 ms                                                 | 141 ms: 1.25x faster                                                          |
| logging_simple           | 8.30 us                                                | 6.67 us: 1.24x faster                                                         |
| dulwich_log              | 84.3 ms                                                | 68.5 ms: 1.23x faster                                                         |
| pathlib                  | 20.5 ms                                                | 16.7 ms: 1.22x faster                                                         |
| sqlglot_normalize        | 143 ms                                                 | 117 ms: 1.22x faster                                                          |
| logging_format           | 9.09 us                                                | 7.46 us: 1.22x faster                                                         |
| xml_etree_iterparse      | 115 ms                                                 | 95.2 ms: 1.21x faster                                                         |
| pprint_pformat           | 2.10 sec                                               | 1.76 sec: 1.19x faster                                                        |
| django_template          | 48.2 ms                                                | 40.4 ms: 1.19x faster                                                         |
| pprint_safe_repr         | 1.02 sec                                               | 859 ms: 1.18x faster                                                          |
| xml_etree_process        | 79.1 ms                                                | 67.3 ms: 1.18x faster                                                         |
| docutils                 | 3.30 sec                                               | 2.82 sec: 1.17x faster                                                        |
| sqlglot_optimize         | 69.2 ms                                                | 59.8 ms: 1.16x faster                                                         |
| genshi_text              | 31.8 ms                                                | 27.7 ms: 1.15x faster                                                         |
| 2to3                     | 348 ms                                                 | 304 ms: 1.14x faster                                                          |
| thrift                   | 1.07 ms                                                | 947 us: 1.13x faster                                                          |
| nbody                    | 154 ms                                                 | 136 ms: 1.13x faster                                                          |
| scimark_fft              | 466 ms                                                 | 413 ms: 1.13x faster                                                          |
| xml_etree_parse          | 168 ms                                                 | 149 ms: 1.13x faster                                                          |
| sympy_sum                | 196 ms                                                 | 176 ms: 1.12x faster                                                          |
| sqlalchemy_imperative    | 23.3 ms                                                | 20.9 ms: 1.12x faster                                                         |
| sqlite_synth             | 3.02 us                                                | 2.72 us: 1.11x faster                                                         |
| json_dumps               | 14.2 ms                                                | 12.8 ms: 1.11x faster                                                         |
| sympy_integrate          | 25.8 ms                                                | 23.5 ms: 1.10x faster                                                         |
| genshi_xml               | 66.0 ms                                                | 60.2 ms: 1.10x faster                                                         |
| sympy_str                | 346 ms                                                 | 315 ms: 1.10x faster                                                          |
| regex_v8                 | 27.8 ms                                                | 25.7 ms: 1.08x faster                                                         |
| sqlalchemy_declarative   | 172 ms                                                 | 159 ms: 1.08x faster                                                          |
| nqueens                  | 106 ms                                                 | 98.8 ms: 1.07x faster                                                         |
| sympy_expand             | 566 ms                                                 | 529 ms: 1.07x faster                                                          |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 6.06 ms: 1.07x faster                                                         |
| regex_effbot             | 3.63 ms                                                | 3.46 ms: 1.05x faster                                                         |
| xml_etree_generate       | 99.4 ms                                                | 94.9 ms: 1.05x faster                                                         |
| fannkuch                 | 532 ms                                                 | 512 ms: 1.04x faster                                                          |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                                          |
| async_generators         | 444 ms                                                 | 438 ms: 1.01x faster                                                          |
| pidigits                 | 191 ms                                                 | 192 ms: 1.00x slower                                                          |
| python_startup           | 14.6 ms                                                | 15.0 ms: 1.03x slower                                                         |
| json_loads               | 31.2 us                                                | 33.0 us: 1.06x slower                                                         |
| create_gc_cycles         | 1.62 ms                                                | 1.74 ms: 1.08x slower                                                         |
| meteor_contest           | 120 ms                                                 | 132 ms: 1.10x slower                                                          |
| telco                    | 7.27 ms                                                | 9.38 ms: 1.29x slower                                                         |
| coverage                 | 79.4 ms                                                | 106 ms: 1.34x slower                                                          |
| python_startup_no_site   | 5.93 ms                                                | 9.31 ms: 1.57x slower                                                         |
| bench_thread_pool        | 986 us                                                 | 3.46 ms: 3.51x slower                                                         |
| bench_mp_pool            | 24.0 ms                                                | 88.6 ms: 3.69x slower                                                         |
| Geometric mean           | (ref)                                                  | 1.23x faster                                                                  |

Benchmark hidden because not significant (4): json, regex_dna, mako, mdp
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250210-3.14.0a4+-ba92dfb-NOGIL/bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.265x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.16x
- 95% likely to have a speedup of 1.15x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: 1.51x