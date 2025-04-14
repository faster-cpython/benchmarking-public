# Results vs. 3.10.4

- fork: kumaraditya303
- ref: per_thread_cur_task
- machine: linux-x86_64
- commit hash: ba92dfb
- commit date: 2025-02-10
- overall geometric mean: 1.448x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.31x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 257 ms: 1.35x faster                                                          |
| docutils       | 3.30 sec                                               | 2.66 sec: 1.24x faster                                                        |
| html5lib       | 88.9 ms                                                | 62.1 ms: 1.43x faster                                                         |
| Geometric mean | (ref)                                                  | 1.34x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 617 ms: 2.87x faster                                                          |
| async_tree_none         | 728 ms                                                 | 264 ms: 2.76x faster                                                          |
| async_tree_memoization  | 870 ms                                                 | 324 ms: 2.68x faster                                                          |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 497 ms: 2.04x faster                                                          |
| Geometric mean          | (ref)                                                  | 2.57x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 70.8 ms: 1.65x faster                                                         |
| nbody          | 154 ms                                                 | 94.5 ms: 1.62x faster                                                         |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                          |
| Geometric mean | (ref)                                                  | 1.40x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 125 ms: 1.51x faster                                                          |
| regex_v8       | 27.8 ms                                                | 24.1 ms: 1.15x faster                                                         |
| regex_effbot   | 3.63 ms                                                | 3.23 ms: 1.12x faster                                                         |
| regex_dna      | 227 ms                                                 | 212 ms: 1.07x faster                                                          |
| Geometric mean | (ref)                                                  | 1.20x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.84 sec: 1.70x faster                                                        |
| unpickle_pure_python | 331 us                                                 | 198 us: 1.67x faster                                                          |
| pickle_pure_python   | 484 us                                                 | 315 us: 1.54x faster                                                          |
| xml_etree_process    | 79.1 ms                                                | 55.1 ms: 1.44x faster                                                         |
| xml_etree_generate   | 99.4 ms                                                | 78.5 ms: 1.27x faster                                                         |
| xml_etree_parse      | 168 ms                                                 | 138 ms: 1.22x faster                                                          |
| xml_etree_iterparse  | 115 ms                                                 | 96.0 ms: 1.20x faster                                                         |
| json_dumps           | 14.2 ms                                                | 12.0 ms: 1.18x faster                                                         |
| json_loads           | 31.2 us                                                | 29.0 us: 1.08x faster                                                         |
| Geometric mean       | (ref)                                                  | 1.35x faster                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.9 ms: 1.13x faster                                                         |
| python_startup_no_site | 5.93 ms                                                | 7.08 ms: 1.19x slower                                                         |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.2 ms: 1.60x faster                                                         |
| django_template | 48.2 ms                                                | 32.2 ms: 1.49x faster                                                         |
| genshi_text     | 31.8 ms                                                | 21.8 ms: 1.46x faster                                                         |
| genshi_xml      | 66.0 ms                                                | 49.7 ms: 1.33x faster                                                         |
| Geometric mean  | (ref)                                                  | 1.47x faster                                                                  |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 162 us: 3.36x faster                                                          |
| async_tree_io            | 1.77 sec                                               | 617 ms: 2.87x faster                                                          |
| generators               | 80.1 ms                                                | 28.4 ms: 2.82x faster                                                         |
| async_tree_none          | 728 ms                                                 | 264 ms: 2.76x faster                                                          |
| async_tree_memoization   | 870 ms                                                 | 324 ms: 2.68x faster                                                          |
| deltablue                | 7.91 ms                                                | 3.38 ms: 2.34x faster                                                         |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 497 ms: 2.04x faster                                                          |
| chaos                    | 115 ms                                                 | 58.4 ms: 1.98x faster                                                         |
| pylint                   | 551 ms                                                 | 279 ms: 1.97x faster                                                          |
| deepcopy_memo            | 58.5 us                                                | 30.7 us: 1.91x faster                                                         |
| richards_super           | 94.7 ms                                                | 50.3 ms: 1.88x faster                                                         |
| deepcopy                 | 479 us                                                 | 257 us: 1.86x faster                                                          |
| go                       | 240 ms                                                 | 129 ms: 1.86x faster                                                          |
| scimark_sor              | 220 ms                                                 | 119 ms: 1.85x faster                                                          |
| raytrace                 | 507 ms                                                 | 276 ms: 1.84x faster                                                          |
| crypto_pyaes             | 128 ms                                                 | 70.0 ms: 1.83x faster                                                         |
| richards                 | 79.3 ms                                                | 44.1 ms: 1.80x faster                                                         |
| logging_silent           | 190 ns                                                 | 106 ns: 1.80x faster                                                          |
| scimark_monte_carlo      | 118 ms                                                 | 66.3 ms: 1.78x faster                                                         |
| spectral_norm            | 170 ms                                                 | 95.7 ms: 1.78x faster                                                         |
| tomli_loads              | 3.14 sec                                               | 1.84 sec: 1.70x faster                                                        |
| sqlglot_parse            | 2.17 ms                                                | 1.27 ms: 1.70x faster                                                         |
| comprehensions           | 28.8 us                                                | 17.2 us: 1.67x faster                                                         |
| unpickle_pure_python     | 331 us                                                 | 198 us: 1.67x faster                                                          |
| float                    | 117 ms                                                 | 70.8 ms: 1.65x faster                                                         |
| nbody                    | 154 ms                                                 | 94.5 ms: 1.62x faster                                                         |
| sqlglot_transpile        | 2.57 ms                                                | 1.59 ms: 1.62x faster                                                         |
| pyflate                  | 716 ms                                                 | 446 ms: 1.61x faster                                                          |
| mako                     | 16.3 ms                                                | 10.2 ms: 1.60x faster                                                         |
| deepcopy_reduce          | 4.17 us                                                | 2.66 us: 1.57x faster                                                         |
| coroutines               | 35.1 ms                                                | 22.6 ms: 1.55x faster                                                         |
| scimark_lu               | 176 ms                                                 | 114 ms: 1.54x faster                                                          |
| pickle_pure_python       | 484 us                                                 | 315 us: 1.54x faster                                                          |
| hexiom                   | 10.4 ms                                                | 6.86 ms: 1.52x faster                                                         |
| regex_compile            | 188 ms                                                 | 125 ms: 1.51x faster                                                          |
| logging_simple           | 8.30 us                                                | 5.51 us: 1.51x faster                                                         |
| django_template          | 48.2 ms                                                | 32.2 ms: 1.49x faster                                                         |
| logging_format           | 9.09 us                                                | 6.10 us: 1.49x faster                                                         |
| scimark_fft              | 466 ms                                                 | 313 ms: 1.49x faster                                                          |
| genshi_text              | 31.8 ms                                                | 21.8 ms: 1.46x faster                                                         |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.48 ms: 1.44x faster                                                         |
| xml_etree_process        | 79.1 ms                                                | 55.1 ms: 1.44x faster                                                         |
| html5lib                 | 88.9 ms                                                | 62.1 ms: 1.43x faster                                                         |
| pycparser                | 1.58 sec                                               | 1.11 sec: 1.42x faster                                                        |
| thrift                   | 1.07 ms                                                | 768 us: 1.40x faster                                                          |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.7 ms: 1.39x faster                                                         |
| pprint_pformat           | 2.10 sec                                               | 1.54 sec: 1.36x faster                                                        |
| pprint_safe_repr         | 1.02 sec                                               | 749 ms: 1.36x faster                                                          |
| sqlglot_normalize        | 143 ms                                                 | 106 ms: 1.35x faster                                                          |
| 2to3                     | 348 ms                                                 | 257 ms: 1.35x faster                                                          |
| fannkuch                 | 532 ms                                                 | 397 ms: 1.34x faster                                                          |
| genshi_xml               | 66.0 ms                                                | 49.7 ms: 1.33x faster                                                         |
| sqlalchemy_declarative   | 172 ms                                                 | 131 ms: 1.32x faster                                                          |
| sympy_sum                | 196 ms                                                 | 151 ms: 1.30x faster                                                          |
| sqlglot_optimize         | 69.2 ms                                                | 53.5 ms: 1.29x faster                                                         |
| sympy_integrate          | 25.8 ms                                                | 20.1 ms: 1.28x faster                                                         |
| dulwich_log              | 84.3 ms                                                | 66.0 ms: 1.28x faster                                                         |
| xml_etree_generate       | 99.4 ms                                                | 78.5 ms: 1.27x faster                                                         |
| sympy_str                | 346 ms                                                 | 275 ms: 1.26x faster                                                          |
| pathlib                  | 20.5 ms                                                | 16.5 ms: 1.24x faster                                                         |
| docutils                 | 3.30 sec                                               | 2.66 sec: 1.24x faster                                                        |
| xml_etree_parse          | 168 ms                                                 | 138 ms: 1.22x faster                                                          |
| sympy_expand             | 566 ms                                                 | 468 ms: 1.21x faster                                                          |
| xml_etree_iterparse      | 115 ms                                                 | 96.0 ms: 1.20x faster                                                         |
| nqueens                  | 106 ms                                                 | 88.2 ms: 1.20x faster                                                         |
| json_dumps               | 14.2 ms                                                | 12.0 ms: 1.18x faster                                                         |
| regex_v8                 | 27.8 ms                                                | 24.1 ms: 1.15x faster                                                         |
| python_startup           | 14.6 ms                                                | 12.9 ms: 1.13x faster                                                         |
| regex_effbot             | 3.63 ms                                                | 3.23 ms: 1.12x faster                                                         |
| mdp                      | 2.85 sec                                               | 2.55 sec: 1.12x faster                                                        |
| bench_thread_pool        | 986 us                                                 | 885 us: 1.11x faster                                                          |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.11x faster                                                          |
| sqlite_synth             | 3.02 us                                                | 2.74 us: 1.10x faster                                                         |
| json                     | 5.69 ms                                                | 5.22 ms: 1.09x faster                                                         |
| json_loads               | 31.2 us                                                | 29.0 us: 1.08x faster                                                         |
| regex_dna                | 227 ms                                                 | 212 ms: 1.07x faster                                                          |
| async_generators         | 444 ms                                                 | 416 ms: 1.07x faster                                                          |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                          |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                                          |
| telco                    | 7.27 ms                                                | 7.59 ms: 1.05x slower                                                         |
| coverage                 | 79.4 ms                                                | 89.5 ms: 1.13x slower                                                         |
| python_startup_no_site   | 5.93 ms                                                | 7.08 ms: 1.19x slower                                                         |
| gc_traversal             | 3.62 ms                                                | 4.72 ms: 1.30x slower                                                         |
| create_gc_cycles         | 1.62 ms                                                | 2.48 ms: 1.53x slower                                                         |
| bench_mp_pool            | 24.0 ms                                                | 81.6 ms: 3.40x slower                                                         |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                                  |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250210-3.14.0a4+-ba92dfb-JIT/bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.448x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.35x
- 95% likely to have a speedup of 1.34x
- 99% likely to have a speedup of 1.31x

# Memory
- memory change: 1.28x