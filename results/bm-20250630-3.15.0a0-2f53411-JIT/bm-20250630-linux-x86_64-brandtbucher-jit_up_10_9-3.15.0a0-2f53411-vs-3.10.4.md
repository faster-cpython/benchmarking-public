# Results vs. 3.10.4

- fork: brandtbucher
- ref: jit_up_10_9
- machine: linux-x86_64
- commit hash: 2f53411
- commit date: 2025-06-30
- overall geometric mean: 1.479x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.33x faster
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250630-linux-x86_64-brandtbucher-jit_up_10_9-3.15.0a0-2f53411 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 261 ms: 1.34x faster                                               |
| docutils       | 3.30 sec                                               | 2.65 sec: 1.24x faster                                             |
| html5lib       | 88.9 ms                                                | 62.3 ms: 1.43x faster                                              |
| Geometric mean | (ref)                                                  | 1.33x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250630-linux-x86_64-brandtbucher-jit_up_10_9-3.15.0a0-2f53411 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 603 ms: 2.93x faster                                               |
| async_tree_none         | 728 ms                                                 | 261 ms: 2.79x faster                                               |
| async_tree_memoization  | 870 ms                                                 | 315 ms: 2.76x faster                                               |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 504 ms: 2.01x faster                                               |
| Geometric mean          | (ref)                                                  | 2.60x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250630-linux-x86_64-brandtbucher-jit_up_10_9-3.15.0a0-2f53411 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 117 ms                                                 | 66.3 ms: 1.77x faster                                              |
| nbody          | 154 ms                                                 | 94.3 ms: 1.63x faster                                              |
| pidigits       | 191 ms                                                 | 193 ms: 1.01x slower                                               |
| Geometric mean | (ref)                                                  | 1.42x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250630-linux-x86_64-brandtbucher-jit_up_10_9-3.15.0a0-2f53411 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 127 ms: 1.48x faster                                               |
| regex_v8       | 27.8 ms                                                | 22.0 ms: 1.26x faster                                              |
| regex_dna      | 227 ms                                                 | 203 ms: 1.12x faster                                               |
| regex_effbot   | 3.63 ms                                                | 3.27 ms: 1.11x faster                                              |
| Geometric mean | (ref)                                                  | 1.23x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250630-linux-x86_64-brandtbucher-jit_up_10_9-3.15.0a0-2f53411 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 190 us: 1.74x faster                                               |
| tomli_loads          | 3.14 sec                                               | 1.82 sec: 1.72x faster                                             |
| pickle_pure_python   | 484 us                                                 | 321 us: 1.51x faster                                               |
| xml_etree_process    | 79.1 ms                                                | 55.2 ms: 1.43x faster                                              |
| json_dumps           | 14.2 ms                                                | 11.1 ms: 1.28x faster                                              |
| xml_etree_generate   | 99.4 ms                                                | 80.3 ms: 1.24x faster                                              |
| xml_etree_parse      | 168 ms                                                 | 141 ms: 1.19x faster                                               |
| xml_etree_iterparse  | 115 ms                                                 | 98.7 ms: 1.17x faster                                              |
| json_loads           | 31.2 us                                                | 28.8 us: 1.09x faster                                              |
| Geometric mean       | (ref)                                                  | 1.36x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250630-linux-x86_64-brandtbucher-jit_up_10_9-3.15.0a0-2f53411 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.2 ms: 1.20x faster                                              |
| python_startup_no_site | 5.93 ms                                                | 6.93 ms: 1.17x slower                                              |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250630-linux-x86_64-brandtbucher-jit_up_10_9-3.15.0a0-2f53411 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.4 ms: 1.56x faster                                              |
| genshi_text     | 31.8 ms                                                | 21.6 ms: 1.48x faster                                              |
| django_template | 48.2 ms                                                | 32.8 ms: 1.47x faster                                              |
| genshi_xml      | 66.0 ms                                                | 50.8 ms: 1.30x faster                                              |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250630-linux-x86_64-brandtbucher-jit_up_10_9-3.15.0a0-2f53411 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 168 us: 3.23x faster                                               |
| async_tree_io            | 1.77 sec                                               | 603 ms: 2.93x faster                                               |
| async_tree_none          | 728 ms                                                 | 261 ms: 2.79x faster                                               |
| async_tree_memoization   | 870 ms                                                 | 315 ms: 2.76x faster                                               |
| generators               | 80.1 ms                                                | 30.8 ms: 2.60x faster                                              |
| deltablue                | 7.91 ms                                                | 3.07 ms: 2.58x faster                                              |
| mdp                      | 2.85 sec                                               | 1.23 sec: 2.31x faster                                             |
| richards_super           | 94.7 ms                                                | 43.5 ms: 2.18x faster                                              |
| go                       | 240 ms                                                 | 115 ms: 2.09x faster                                               |
| richards                 | 79.3 ms                                                | 38.7 ms: 2.05x faster                                              |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 504 ms: 2.01x faster                                               |
| deepcopy_memo            | 58.5 us                                                | 29.7 us: 1.97x faster                                              |
| pylint                   | 551 ms                                                 | 285 ms: 1.94x faster                                               |
| spectral_norm            | 170 ms                                                 | 89.9 ms: 1.89x faster                                              |
| logging_silent           | 190 ns                                                 | 101 ns: 1.89x faster                                               |
| chaos                    | 115 ms                                                 | 61.2 ms: 1.89x faster                                              |
| raytrace                 | 507 ms                                                 | 273 ms: 1.85x faster                                               |
| scimark_sor              | 220 ms                                                 | 119 ms: 1.85x faster                                               |
| deepcopy                 | 479 us                                                 | 260 us: 1.84x faster                                               |
| crypto_pyaes             | 128 ms                                                 | 71.6 ms: 1.78x faster                                              |
| scimark_monte_carlo      | 118 ms                                                 | 66.7 ms: 1.77x faster                                              |
| float                    | 117 ms                                                 | 66.3 ms: 1.77x faster                                              |
| unpickle_pure_python     | 331 us                                                 | 190 us: 1.74x faster                                               |
| pyflate                  | 716 ms                                                 | 415 ms: 1.73x faster                                               |
| tomli_loads              | 3.14 sec                                               | 1.82 sec: 1.72x faster                                             |
| comprehensions           | 28.8 us                                                | 16.7 us: 1.72x faster                                              |
| hexiom                   | 10.4 ms                                                | 6.23 ms: 1.67x faster                                              |
| djangocms                | 38.4 us                                                | 23.1 us: 1.66x faster                                              |
| nbody                    | 154 ms                                                 | 94.3 ms: 1.63x faster                                              |
| mako                     | 16.3 ms                                                | 10.4 ms: 1.56x faster                                              |
| deepcopy_reduce          | 4.17 us                                                | 2.74 us: 1.52x faster                                              |
| pickle_pure_python       | 484 us                                                 | 321 us: 1.51x faster                                               |
| scimark_fft              | 466 ms                                                 | 312 ms: 1.49x faster                                               |
| logging_simple           | 8.30 us                                                | 5.58 us: 1.49x faster                                              |
| scimark_lu               | 176 ms                                                 | 119 ms: 1.49x faster                                               |
| regex_compile            | 188 ms                                                 | 127 ms: 1.48x faster                                               |
| genshi_text              | 31.8 ms                                                | 21.6 ms: 1.48x faster                                              |
| django_template          | 48.2 ms                                                | 32.8 ms: 1.47x faster                                              |
| pprint_pformat           | 2.10 sec                                               | 1.45 sec: 1.45x faster                                             |
| logging_format           | 9.09 us                                                | 6.32 us: 1.44x faster                                              |
| pprint_safe_repr         | 1.02 sec                                               | 710 ms: 1.43x faster                                               |
| xml_etree_process        | 79.1 ms                                                | 55.2 ms: 1.43x faster                                              |
| html5lib                 | 88.9 ms                                                | 62.3 ms: 1.43x faster                                              |
| pycparser                | 1.58 sec                                               | 1.12 sec: 1.41x faster                                             |
| dulwich_log              | 84.3 ms                                                | 59.8 ms: 1.41x faster                                              |
| coroutines               | 35.1 ms                                                | 24.9 ms: 1.41x faster                                              |
| thrift                   | 1.07 ms                                                | 783 us: 1.37x faster                                               |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.74 ms: 1.36x faster                                              |
| 2to3                     | 348 ms                                                 | 261 ms: 1.34x faster                                               |
| fannkuch                 | 532 ms                                                 | 402 ms: 1.32x faster                                               |
| sympy_integrate          | 25.8 ms                                                | 19.6 ms: 1.32x faster                                              |
| genshi_xml               | 66.0 ms                                                | 50.8 ms: 1.30x faster                                              |
| sympy_sum                | 196 ms                                                 | 152 ms: 1.29x faster                                               |
| json_dumps               | 14.2 ms                                                | 11.1 ms: 1.28x faster                                              |
| sympy_str                | 346 ms                                                 | 273 ms: 1.27x faster                                               |
| regex_v8                 | 27.8 ms                                                | 22.0 ms: 1.26x faster                                              |
| nqueens                  | 106 ms                                                 | 84.1 ms: 1.26x faster                                              |
| docutils                 | 3.30 sec                                               | 2.65 sec: 1.24x faster                                             |
| xml_etree_generate       | 99.4 ms                                                | 80.3 ms: 1.24x faster                                              |
| pathlib                  | 20.5 ms                                                | 16.8 ms: 1.21x faster                                              |
| sympy_expand             | 566 ms                                                 | 468 ms: 1.21x faster                                               |
| python_startup           | 14.6 ms                                                | 12.2 ms: 1.20x faster                                              |
| xml_etree_parse          | 168 ms                                                 | 141 ms: 1.19x faster                                               |
| xml_etree_iterparse      | 115 ms                                                 | 98.7 ms: 1.17x faster                                              |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                               |
| regex_dna                | 227 ms                                                 | 203 ms: 1.12x faster                                               |
| regex_effbot             | 3.63 ms                                                | 3.27 ms: 1.11x faster                                              |
| json_loads               | 31.2 us                                                | 28.8 us: 1.09x faster                                              |
| sqlite_synth             | 3.02 us                                                | 2.82 us: 1.07x faster                                              |
| json                     | 5.69 ms                                                | 5.31 ms: 1.07x faster                                              |
| async_generators         | 444 ms                                                 | 432 ms: 1.03x faster                                               |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                               |
| pidigits                 | 191 ms                                                 | 193 ms: 1.01x slower                                               |
| telco                    | 7.27 ms                                                | 7.78 ms: 1.07x slower                                              |
| coverage                 | 79.4 ms                                                | 88.3 ms: 1.11x slower                                              |
| python_startup_no_site   | 5.93 ms                                                | 6.93 ms: 1.17x slower                                              |
| gc_traversal             | 3.62 ms                                                | 4.76 ms: 1.31x slower                                              |
| create_gc_cycles         | 1.62 ms                                                | 2.57 ms: 1.58x slower                                              |
| Geometric mean           | (ref)                                                  | 1.48x faster                                                       |
Ignored benchmarks (23) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250630-3.15.0a0-2f53411-JIT/bm-20250630-linux-x86_64-brandtbucher-jit_up_10_9-3.15.0a0-2f53411.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.479x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.39x
- 95% likely to have a speedup of 1.37x
- 99% likely to have a speedup of 1.33x

# Memory
- memory change: 1.33x