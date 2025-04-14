# Results vs. 3.10.4

- fork: kumaraditya303
- ref: per_thread_cur_task
- machine: linux-x86_64
- commit hash: ba92dfb
- commit date: 2025-02-10
- overall geometric mean: 1.459x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.33x faster
- Memory change: 1.26x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 252 ms: 1.38x faster                                                          |
| docutils       | 3.30 sec                                               | 2.58 sec: 1.28x faster                                                        |
| html5lib       | 88.9 ms                                                | 61.4 ms: 1.45x faster                                                         |
| Geometric mean | (ref)                                                  | 1.37x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 605 ms: 2.92x faster                                                          |
| async_tree_none         | 728 ms                                                 | 259 ms: 2.82x faster                                                          |
| async_tree_memoization  | 870 ms                                                 | 318 ms: 2.73x faster                                                          |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 490 ms: 2.07x faster                                                          |
| Geometric mean          | (ref)                                                  | 2.61x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 69.0 ms: 1.70x faster                                                         |
| nbody          | 154 ms                                                 | 94.3 ms: 1.63x faster                                                         |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                          |
| Geometric mean | (ref)                                                  | 1.41x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 126 ms: 1.50x faster                                                          |
| regex_v8       | 27.8 ms                                                | 24.3 ms: 1.14x faster                                                         |
| regex_effbot   | 3.63 ms                                                | 3.24 ms: 1.12x faster                                                         |
| regex_dna      | 227 ms                                                 | 216 ms: 1.05x faster                                                          |
| Geometric mean | (ref)                                                  | 1.19x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.98 sec: 1.59x faster                                                        |
| unpickle_pure_python | 331 us                                                 | 218 us: 1.51x faster                                                          |
| pickle_pure_python   | 484 us                                                 | 320 us: 1.51x faster                                                          |
| xml_etree_process    | 79.1 ms                                                | 58.6 ms: 1.35x faster                                                         |
| json_dumps           | 14.2 ms                                                | 11.5 ms: 1.23x faster                                                         |
| xml_etree_parse      | 168 ms                                                 | 139 ms: 1.21x faster                                                          |
| xml_etree_iterparse  | 115 ms                                                 | 96.5 ms: 1.20x faster                                                         |
| xml_etree_generate   | 99.4 ms                                                | 83.6 ms: 1.19x faster                                                         |
| json_loads           | 31.2 us                                                | 28.7 us: 1.09x faster                                                         |
| Geometric mean       | (ref)                                                  | 1.31x faster                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                         |
| python_startup_no_site | 5.93 ms                                                | 7.02 ms: 1.18x slower                                                         |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.6 ms: 1.54x faster                                                         |
| django_template | 48.2 ms                                                | 32.1 ms: 1.50x faster                                                         |
| genshi_text     | 31.8 ms                                                | 21.3 ms: 1.49x faster                                                         |
| genshi_xml      | 66.0 ms                                                | 47.8 ms: 1.38x faster                                                         |
| Geometric mean  | (ref)                                                  | 1.48x faster                                                                  |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 159 us: 3.42x faster                                                          |
| async_tree_io            | 1.77 sec                                               | 605 ms: 2.92x faster                                                          |
| generators               | 80.1 ms                                                | 27.5 ms: 2.91x faster                                                         |
| async_tree_none          | 728 ms                                                 | 259 ms: 2.82x faster                                                          |
| async_tree_memoization   | 870 ms                                                 | 318 ms: 2.73x faster                                                          |
| deltablue                | 7.91 ms                                                | 3.15 ms: 2.51x faster                                                         |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 490 ms: 2.07x faster                                                          |
| go                       | 240 ms                                                 | 116 ms: 2.07x faster                                                          |
| pylint                   | 551 ms                                                 | 271 ms: 2.03x faster                                                          |
| chaos                    | 115 ms                                                 | 58.6 ms: 1.97x faster                                                         |
| deepcopy_memo            | 58.5 us                                                | 30.9 us: 1.89x faster                                                         |
| richards_super           | 94.7 ms                                                | 50.2 ms: 1.89x faster                                                         |
| raytrace                 | 507 ms                                                 | 274 ms: 1.85x faster                                                          |
| deepcopy                 | 479 us                                                 | 262 us: 1.83x faster                                                          |
| crypto_pyaes             | 128 ms                                                 | 70.1 ms: 1.82x faster                                                         |
| richards                 | 79.3 ms                                                | 44.0 ms: 1.80x faster                                                         |
| scimark_sor              | 220 ms                                                 | 122 ms: 1.80x faster                                                          |
| logging_silent           | 190 ns                                                 | 105 ns: 1.80x faster                                                          |
| comprehensions           | 28.8 us                                                | 16.2 us: 1.78x faster                                                         |
| spectral_norm            | 170 ms                                                 | 97.1 ms: 1.75x faster                                                         |
| sqlglot_parse            | 2.17 ms                                                | 1.24 ms: 1.75x faster                                                         |
| scimark_monte_carlo      | 118 ms                                                 | 67.7 ms: 1.75x faster                                                         |
| float                    | 117 ms                                                 | 69.0 ms: 1.70x faster                                                         |
| hexiom                   | 10.4 ms                                                | 6.24 ms: 1.66x faster                                                         |
| sqlglot_transpile        | 2.57 ms                                                | 1.55 ms: 1.66x faster                                                         |
| nbody                    | 154 ms                                                 | 94.3 ms: 1.63x faster                                                         |
| pyflate                  | 716 ms                                                 | 443 ms: 1.62x faster                                                          |
| tomli_loads              | 3.14 sec                                               | 1.98 sec: 1.59x faster                                                        |
| deepcopy_reduce          | 4.17 us                                                | 2.71 us: 1.54x faster                                                         |
| mako                     | 16.3 ms                                                | 10.6 ms: 1.54x faster                                                         |
| logging_simple           | 8.30 us                                                | 5.42 us: 1.53x faster                                                         |
| coroutines               | 35.1 ms                                                | 23.0 ms: 1.53x faster                                                         |
| logging_format           | 9.09 us                                                | 5.99 us: 1.52x faster                                                         |
| unpickle_pure_python     | 331 us                                                 | 218 us: 1.51x faster                                                          |
| pickle_pure_python       | 484 us                                                 | 320 us: 1.51x faster                                                          |
| django_template          | 48.2 ms                                                | 32.1 ms: 1.50x faster                                                         |
| regex_compile            | 188 ms                                                 | 126 ms: 1.50x faster                                                          |
| scimark_lu               | 176 ms                                                 | 118 ms: 1.50x faster                                                          |
| genshi_text              | 31.8 ms                                                | 21.3 ms: 1.49x faster                                                         |
| html5lib                 | 88.9 ms                                                | 61.4 ms: 1.45x faster                                                         |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.3 ms: 1.43x faster                                                         |
| pprint_pformat           | 2.10 sec                                               | 1.48 sec: 1.42x faster                                                        |
| pprint_safe_repr         | 1.02 sec                                               | 724 ms: 1.41x faster                                                          |
| pycparser                | 1.58 sec                                               | 1.13 sec: 1.40x faster                                                        |
| 2to3                     | 348 ms                                                 | 252 ms: 1.38x faster                                                          |
| genshi_xml               | 66.0 ms                                                | 47.8 ms: 1.38x faster                                                         |
| sqlglot_normalize        | 143 ms                                                 | 103 ms: 1.38x faster                                                          |
| thrift                   | 1.07 ms                                                | 779 us: 1.38x faster                                                          |
| scimark_fft              | 466 ms                                                 | 341 ms: 1.37x faster                                                          |
| sqlalchemy_declarative   | 172 ms                                                 | 127 ms: 1.36x faster                                                          |
| xml_etree_process        | 79.1 ms                                                | 58.6 ms: 1.35x faster                                                         |
| sympy_sum                | 196 ms                                                 | 146 ms: 1.35x faster                                                          |
| sqlglot_optimize         | 69.2 ms                                                | 51.7 ms: 1.34x faster                                                         |
| nqueens                  | 106 ms                                                 | 79.4 ms: 1.33x faster                                                         |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.87 ms: 1.33x faster                                                         |
| sympy_integrate          | 25.8 ms                                                | 19.6 ms: 1.32x faster                                                         |
| dulwich_log              | 84.3 ms                                                | 64.2 ms: 1.31x faster                                                         |
| sympy_str                | 346 ms                                                 | 264 ms: 1.31x faster                                                          |
| fannkuch                 | 532 ms                                                 | 407 ms: 1.31x faster                                                          |
| docutils                 | 3.30 sec                                               | 2.58 sec: 1.28x faster                                                        |
| sympy_expand             | 566 ms                                                 | 449 ms: 1.26x faster                                                          |
| pathlib                  | 20.5 ms                                                | 16.3 ms: 1.26x faster                                                         |
| json_dumps               | 14.2 ms                                                | 11.5 ms: 1.23x faster                                                         |
| xml_etree_parse          | 168 ms                                                 | 139 ms: 1.21x faster                                                          |
| xml_etree_iterparse      | 115 ms                                                 | 96.5 ms: 1.20x faster                                                         |
| xml_etree_generate       | 99.4 ms                                                | 83.6 ms: 1.19x faster                                                         |
| async_generators         | 444 ms                                                 | 377 ms: 1.18x faster                                                          |
| meteor_contest           | 120 ms                                                 | 104 ms: 1.15x faster                                                          |
| mdp                      | 2.85 sec                                               | 2.48 sec: 1.15x faster                                                        |
| bench_thread_pool        | 986 us                                                 | 860 us: 1.15x faster                                                          |
| regex_v8                 | 27.8 ms                                                | 24.3 ms: 1.14x faster                                                         |
| python_startup           | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                         |
| regex_effbot             | 3.63 ms                                                | 3.24 ms: 1.12x faster                                                         |
| json                     | 5.69 ms                                                | 5.14 ms: 1.11x faster                                                         |
| json_loads               | 31.2 us                                                | 28.7 us: 1.09x faster                                                         |
| sqlite_synth             | 3.02 us                                                | 2.78 us: 1.09x faster                                                         |
| regex_dna                | 227 ms                                                 | 216 ms: 1.05x faster                                                          |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                          |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                          |
| telco                    | 7.27 ms                                                | 7.76 ms: 1.07x slower                                                         |
| coverage                 | 79.4 ms                                                | 91.6 ms: 1.15x slower                                                         |
| python_startup_no_site   | 5.93 ms                                                | 7.02 ms: 1.18x slower                                                         |
| gc_traversal             | 3.62 ms                                                | 4.78 ms: 1.32x slower                                                         |
| create_gc_cycles         | 1.62 ms                                                | 2.46 ms: 1.52x slower                                                         |
| bench_mp_pool            | 24.0 ms                                                | 80.9 ms: 3.37x slower                                                         |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                                  |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250210-3.14.0a4+-ba92dfb/bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.459x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.36x
- 95% likely to have a speedup of 1.36x
- 99% likely to have a speedup of 1.33x

# Memory
- memory change: 1.26x