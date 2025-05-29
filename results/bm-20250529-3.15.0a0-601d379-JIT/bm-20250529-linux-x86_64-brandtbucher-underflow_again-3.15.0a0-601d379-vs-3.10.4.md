# Results vs. 3.10.4

- fork: brandtbucher
- ref: underflow_again
- machine: linux-x86_64
- commit hash: 601d379
- commit date: 2025-05-29
- overall geometric mean: 1.923x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.32x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250529-linux-x86_64-brandtbucher-underflow_again-3.15.0a0-601d379 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 261 ms: 1.33x faster                                                   |
| docutils       | 3.30 sec                                               | 2.70 sec: 1.22x faster                                                 |
| html5lib       | 88.9 ms                                                | 62.2 ms: 1.43x faster                                                  |
| Geometric mean | (ref)                                                  | 1.33x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250529-linux-x86_64-brandtbucher-underflow_again-3.15.0a0-601d379 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 600 ms: 2.95x faster                                                   |
| async_tree_none         | 728 ms                                                 | 261 ms: 2.79x faster                                                   |
| async_tree_memoization  | 870 ms                                                 | 314 ms: 2.77x faster                                                   |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 498 ms: 2.04x faster                                                   |
| Geometric mean          | (ref)                                                  | 2.61x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250529-linux-x86_64-brandtbucher-underflow_again-3.15.0a0-601d379 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 117 ms                                                 | 64.3 ms: 1.82x faster                                                  |
| nbody          | 154 ms                                                 | 89.7 ms: 1.71x faster                                                  |
| pidigits       | 191 ms                                                 | 195 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                  | 1.45x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250529-linux-x86_64-brandtbucher-underflow_again-3.15.0a0-601d379 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_v8       | 27.8 ms                                                | 24.2 ms: 1.15x faster                                                  |
| regex_dna      | 227 ms                                                 | 208 ms: 1.09x faster                                                   |
| regex_effbot   | 3.63 ms                                                | 3.37 ms: 1.08x faster                                                  |
| Geometric mean | (ref)                                                  | 1.10x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250529-linux-x86_64-brandtbucher-underflow_again-3.15.0a0-601d379 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.89 sec: 1.66x faster                                                 |
| unpickle_pure_python | 331 us                                                 | 202 us: 1.64x faster                                                   |
| pickle_pure_python   | 484 us                                                 | 320 us: 1.51x faster                                                   |
| xml_etree_process    | 79.1 ms                                                | 55.6 ms: 1.42x faster                                                  |
| json_dumps           | 14.2 ms                                                | 11.1 ms: 1.27x faster                                                  |
| xml_etree_generate   | 99.4 ms                                                | 79.9 ms: 1.24x faster                                                  |
| xml_etree_parse      | 168 ms                                                 | 141 ms: 1.19x faster                                                   |
| xml_etree_iterparse  | 115 ms                                                 | 98.4 ms: 1.17x faster                                                  |
| json_loads           | 31.2 us                                                | 30.7 us: 1.02x faster                                                  |
| Geometric mean       | (ref)                                                  | 1.33x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250529-linux-x86_64-brandtbucher-underflow_again-3.15.0a0-601d379 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.2 ms: 1.20x faster                                                  |
| python_startup_no_site | 5.93 ms                                                | 6.96 ms: 1.17x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250529-linux-x86_64-brandtbucher-underflow_again-3.15.0a0-601d379 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.6 ms: 1.53x faster                                                  |
| django_template | 48.2 ms                                                | 32.4 ms: 1.49x faster                                                  |
| genshi_text     | 31.8 ms                                                | 21.7 ms: 1.47x faster                                                  |
| genshi_xml      | 66.0 ms                                                | 50.2 ms: 1.32x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250529-linux-x86_64-brandtbucher-underflow_again-3.15.0a0-601d379 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pprint_pformat           | 2.10 sec                                               | 1.47 us: 1428998.38x faster                                            |
| pprint_safe_repr         | 1.02 sec                                               | 857 ns: 1188047.57x faster                                             |
| typing_runtime_protocols | 544 us                                                 | 171 us: 3.19x faster                                                   |
| async_tree_io            | 1.77 sec                                               | 600 ms: 2.95x faster                                                   |
| async_tree_none          | 728 ms                                                 | 261 ms: 2.79x faster                                                   |
| async_tree_memoization   | 870 ms                                                 | 314 ms: 2.77x faster                                                   |
| generators               | 80.1 ms                                                | 30.3 ms: 2.64x faster                                                  |
| deltablue                | 7.91 ms                                                | 3.08 ms: 2.57x faster                                                  |
| richards_super           | 94.7 ms                                                | 38.2 ms: 2.48x faster                                                  |
| richards                 | 79.3 ms                                                | 33.7 ms: 2.35x faster                                                  |
| mdp                      | 2.85 sec                                               | 1.25 sec: 2.28x faster                                                 |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 498 ms: 2.04x faster                                                   |
| pylint                   | 551 ms                                                 | 283 ms: 1.95x faster                                                   |
| deepcopy_memo            | 58.5 us                                                | 30.1 us: 1.94x faster                                                  |
| deepcopy                 | 479 us                                                 | 257 us: 1.86x faster                                                   |
| scimark_sor              | 220 ms                                                 | 120 ms: 1.84x faster                                                   |
| raytrace                 | 507 ms                                                 | 278 ms: 1.82x faster                                                   |
| float                    | 117 ms                                                 | 64.3 ms: 1.82x faster                                                  |
| chaos                    | 115 ms                                                 | 63.9 ms: 1.81x faster                                                  |
| nbody                    | 154 ms                                                 | 89.7 ms: 1.71x faster                                                  |
| go                       | 240 ms                                                 | 141 ms: 1.71x faster                                                   |
| spectral_norm            | 170 ms                                                 | 99.8 ms: 1.70x faster                                                  |
| comprehensions           | 28.8 us                                                | 17.0 us: 1.69x faster                                                  |
| crypto_pyaes             | 128 ms                                                 | 75.5 ms: 1.69x faster                                                  |
| scimark_monte_carlo      | 118 ms                                                 | 70.3 ms: 1.68x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 1.89 sec: 1.66x faster                                                 |
| unpickle_pure_python     | 331 us                                                 | 202 us: 1.64x faster                                                   |
| pyflate                  | 716 ms                                                 | 441 ms: 1.62x faster                                                   |
| hexiom                   | 10.4 ms                                                | 6.42 ms: 1.62x faster                                                  |
| mako                     | 16.3 ms                                                | 10.6 ms: 1.53x faster                                                  |
| deepcopy_reduce          | 4.17 us                                                | 2.73 us: 1.53x faster                                                  |
| pickle_pure_python       | 484 us                                                 | 320 us: 1.51x faster                                                   |
| django_template          | 48.2 ms                                                | 32.4 ms: 1.49x faster                                                  |
| genshi_text              | 31.8 ms                                                | 21.7 ms: 1.47x faster                                                  |
| scimark_lu               | 176 ms                                                 | 120 ms: 1.47x faster                                                   |
| html5lib                 | 88.9 ms                                                | 62.2 ms: 1.43x faster                                                  |
| xml_etree_process        | 79.1 ms                                                | 55.6 ms: 1.42x faster                                                  |
| scimark_fft              | 466 ms                                                 | 328 ms: 1.42x faster                                                   |
| dulwich_log              | 84.3 ms                                                | 61.6 ms: 1.37x faster                                                  |
| coroutines               | 35.1 ms                                                | 25.9 ms: 1.36x faster                                                  |
| pycparser                | 1.58 sec                                               | 1.17 sec: 1.35x faster                                                 |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.82 ms: 1.34x faster                                                  |
| logging_simple           | 8.30 us                                                | 6.19 us: 1.34x faster                                                  |
| 2to3                     | 348 ms                                                 | 261 ms: 1.33x faster                                                   |
| sympy_integrate          | 25.8 ms                                                | 19.5 ms: 1.32x faster                                                  |
| logging_format           | 9.09 us                                                | 6.88 us: 1.32x faster                                                  |
| genshi_xml               | 66.0 ms                                                | 50.2 ms: 1.32x faster                                                  |
| fannkuch                 | 532 ms                                                 | 407 ms: 1.31x faster                                                   |
| sympy_sum                | 196 ms                                                 | 152 ms: 1.29x faster                                                   |
| json_dumps               | 14.2 ms                                                | 11.1 ms: 1.27x faster                                                  |
| sympy_str                | 346 ms                                                 | 273 ms: 1.26x faster                                                   |
| nqueens                  | 106 ms                                                 | 84.3 ms: 1.26x faster                                                  |
| xml_etree_generate       | 99.4 ms                                                | 79.9 ms: 1.24x faster                                                  |
| docutils                 | 3.30 sec                                               | 2.70 sec: 1.22x faster                                                 |
| sympy_expand             | 566 ms                                                 | 466 ms: 1.21x faster                                                   |
| python_startup           | 14.6 ms                                                | 12.2 ms: 1.20x faster                                                  |
| pathlib                  | 20.5 ms                                                | 17.2 ms: 1.19x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 141 ms: 1.19x faster                                                   |
| xml_etree_iterparse      | 115 ms                                                 | 98.4 ms: 1.17x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 24.2 ms: 1.15x faster                                                  |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                   |
| bench_thread_pool        | 986 us                                                 | 897 us: 1.10x faster                                                   |
| regex_dna                | 227 ms                                                 | 208 ms: 1.09x faster                                                   |
| sqlite_synth             | 3.02 us                                                | 2.79 us: 1.08x faster                                                  |
| regex_effbot             | 3.63 ms                                                | 3.37 ms: 1.08x faster                                                  |
| json                     | 5.69 ms                                                | 5.40 ms: 1.05x faster                                                  |
| async_generators         | 444 ms                                                 | 429 ms: 1.03x faster                                                   |
| json_loads               | 31.2 us                                                | 30.7 us: 1.02x faster                                                  |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                   |
| pidigits                 | 191 ms                                                 | 195 ms: 1.02x slower                                                   |
| telco                    | 7.27 ms                                                | 7.93 ms: 1.09x slower                                                  |
| python_startup_no_site   | 5.93 ms                                                | 6.96 ms: 1.17x slower                                                  |
| gc_traversal             | 3.62 ms                                                | 5.02 ms: 1.39x slower                                                  |
| create_gc_cycles         | 1.62 ms                                                | 2.59 ms: 1.60x slower                                                  |
| logging_silent           | 190 ns                                                 | 476 ns: 2.51x slower                                                   |
| bench_mp_pool            | 24.0 ms                                                | 93.5 ms: 3.89x slower                                                  |
| coverage                 | 79.4 ms                                                | 432 ms: 5.44x slower                                                   |
| thrift                   | 1.07 ms                                                | 148 ms: 138.52x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.82x faster                                                           |
Ignored benchmarks (23) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, regex_compile, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250529-3.15.0a0-601d379-JIT/bm-20250529-linux-x86_64-brandtbucher-underflow_again-3.15.0a0-601d379.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.923x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.32x