# Results vs. 3.10.4

- fork: brandtbucher
- ref: jit_up_10_12
- machine: linux-x86_64
- commit hash: 0f33ad5
- commit date: 2025-06-29
- overall geometric mean: 1.480x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.33x faster
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250629-linux-x86_64-brandtbucher-jit_up_10_12-3.15.0a0-0f33ad5 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 261 ms: 1.34x faster                                                |
| docutils       | 3.30 sec                                               | 2.64 sec: 1.25x faster                                              |
| html5lib       | 88.9 ms                                                | 61.8 ms: 1.44x faster                                               |
| Geometric mean | (ref)                                                  | 1.34x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250629-linux-x86_64-brandtbucher-jit_up_10_12-3.15.0a0-0f33ad5 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 603 ms: 2.93x faster                                                |
| async_tree_none         | 728 ms                                                 | 264 ms: 2.76x faster                                                |
| async_tree_memoization  | 870 ms                                                 | 317 ms: 2.74x faster                                                |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 498 ms: 2.04x faster                                                |
| Geometric mean          | (ref)                                                  | 2.59x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250629-linux-x86_64-brandtbucher-jit_up_10_12-3.15.0a0-0f33ad5 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 117 ms                                                 | 65.8 ms: 1.78x faster                                               |
| nbody          | 154 ms                                                 | 97.0 ms: 1.58x faster                                               |
| pidigits       | 191 ms                                                 | 188 ms: 1.01x faster                                                |
| Geometric mean | (ref)                                                  | 1.42x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250629-linux-x86_64-brandtbucher-jit_up_10_12-3.15.0a0-0f33ad5 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 127 ms: 1.48x faster                                                |
| regex_v8       | 27.8 ms                                                | 23.0 ms: 1.21x faster                                               |
| regex_effbot   | 3.63 ms                                                | 3.32 ms: 1.09x faster                                               |
| regex_dna      | 227 ms                                                 | 215 ms: 1.06x faster                                                |
| Geometric mean | (ref)                                                  | 1.20x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250629-linux-x86_64-brandtbucher-jit_up_10_12-3.15.0a0-0f33ad5 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 192 us: 1.72x faster                                                |
| tomli_loads          | 3.14 sec                                               | 1.83 sec: 1.71x faster                                              |
| pickle_pure_python   | 484 us                                                 | 322 us: 1.50x faster                                                |
| xml_etree_process    | 79.1 ms                                                | 55.4 ms: 1.43x faster                                               |
| json_dumps           | 14.2 ms                                                | 11.1 ms: 1.28x faster                                               |
| xml_etree_generate   | 99.4 ms                                                | 79.5 ms: 1.25x faster                                               |
| xml_etree_parse      | 168 ms                                                 | 140 ms: 1.20x faster                                                |
| xml_etree_iterparse  | 115 ms                                                 | 98.1 ms: 1.18x faster                                               |
| json_loads           | 31.2 us                                                | 28.0 us: 1.12x faster                                               |
| Geometric mean       | (ref)                                                  | 1.36x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250629-linux-x86_64-brandtbucher-jit_up_10_12-3.15.0a0-0f33ad5 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.2 ms: 1.20x faster                                               |
| python_startup_no_site | 5.93 ms                                                | 6.93 ms: 1.17x slower                                               |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250629-linux-x86_64-brandtbucher-jit_up_10_12-3.15.0a0-0f33ad5 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.5 ms: 1.55x faster                                               |
| genshi_text     | 31.8 ms                                                | 21.7 ms: 1.47x faster                                               |
| django_template | 48.2 ms                                                | 33.0 ms: 1.46x faster                                               |
| genshi_xml      | 66.0 ms                                                | 50.2 ms: 1.31x faster                                               |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250629-linux-x86_64-brandtbucher-jit_up_10_12-3.15.0a0-0f33ad5 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 168 us: 3.23x faster                                                |
| async_tree_io            | 1.77 sec                                               | 603 ms: 2.93x faster                                                |
| async_tree_none          | 728 ms                                                 | 264 ms: 2.76x faster                                                |
| async_tree_memoization   | 870 ms                                                 | 317 ms: 2.74x faster                                                |
| generators               | 80.1 ms                                                | 30.0 ms: 2.67x faster                                               |
| deltablue                | 7.91 ms                                                | 3.06 ms: 2.58x faster                                               |
| richards_super           | 94.7 ms                                                | 39.4 ms: 2.40x faster                                               |
| richards                 | 79.3 ms                                                | 34.3 ms: 2.31x faster                                               |
| mdp                      | 2.85 sec                                               | 1.24 sec: 2.30x faster                                              |
| go                       | 240 ms                                                 | 117 ms: 2.06x faster                                                |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 498 ms: 2.04x faster                                                |
| deepcopy_memo            | 58.5 us                                                | 29.8 us: 1.96x faster                                               |
| pylint                   | 551 ms                                                 | 284 ms: 1.94x faster                                                |
| chaos                    | 115 ms                                                 | 61.6 ms: 1.87x faster                                               |
| logging_silent           | 190 ns                                                 | 102 ns: 1.87x faster                                                |
| spectral_norm            | 170 ms                                                 | 92.0 ms: 1.85x faster                                               |
| scimark_sor              | 220 ms                                                 | 119 ms: 1.84x faster                                                |
| raytrace                 | 507 ms                                                 | 276 ms: 1.84x faster                                                |
| deepcopy                 | 479 us                                                 | 262 us: 1.83x faster                                                |
| scimark_monte_carlo      | 118 ms                                                 | 65.9 ms: 1.79x faster                                               |
| crypto_pyaes             | 128 ms                                                 | 71.6 ms: 1.79x faster                                               |
| float                    | 117 ms                                                 | 65.8 ms: 1.78x faster                                               |
| pyflate                  | 716 ms                                                 | 414 ms: 1.73x faster                                                |
| unpickle_pure_python     | 331 us                                                 | 192 us: 1.72x faster                                                |
| comprehensions           | 28.8 us                                                | 16.7 us: 1.72x faster                                               |
| tomli_loads              | 3.14 sec                                               | 1.83 sec: 1.71x faster                                              |
| djangocms                | 38.4 us                                                | 22.6 us: 1.70x faster                                               |
| hexiom                   | 10.4 ms                                                | 6.27 ms: 1.66x faster                                               |
| nbody                    | 154 ms                                                 | 97.0 ms: 1.58x faster                                               |
| mako                     | 16.3 ms                                                | 10.5 ms: 1.55x faster                                               |
| deepcopy_reduce          | 4.17 us                                                | 2.74 us: 1.52x faster                                               |
| pickle_pure_python       | 484 us                                                 | 322 us: 1.50x faster                                                |
| scimark_lu               | 176 ms                                                 | 119 ms: 1.48x faster                                                |
| regex_compile            | 188 ms                                                 | 127 ms: 1.48x faster                                                |
| scimark_fft              | 466 ms                                                 | 315 ms: 1.48x faster                                                |
| genshi_text              | 31.8 ms                                                | 21.7 ms: 1.47x faster                                               |
| logging_simple           | 8.30 us                                                | 5.67 us: 1.47x faster                                               |
| django_template          | 48.2 ms                                                | 33.0 ms: 1.46x faster                                               |
| html5lib                 | 88.9 ms                                                | 61.8 ms: 1.44x faster                                               |
| logging_format           | 9.09 us                                                | 6.36 us: 1.43x faster                                               |
| xml_etree_process        | 79.1 ms                                                | 55.4 ms: 1.43x faster                                               |
| coroutines               | 35.1 ms                                                | 24.6 ms: 1.42x faster                                               |
| dulwich_log              | 84.3 ms                                                | 59.6 ms: 1.41x faster                                               |
| thrift                   | 1.07 ms                                                | 766 us: 1.40x faster                                                |
| pprint_pformat           | 2.10 sec                                               | 1.52 sec: 1.39x faster                                              |
| pycparser                | 1.58 sec                                               | 1.15 sec: 1.37x faster                                              |
| pprint_safe_repr         | 1.02 sec                                               | 754 ms: 1.35x faster                                                |
| fannkuch                 | 532 ms                                                 | 395 ms: 1.35x faster                                                |
| 2to3                     | 348 ms                                                 | 261 ms: 1.34x faster                                                |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.89 ms: 1.32x faster                                               |
| sympy_integrate          | 25.8 ms                                                | 19.6 ms: 1.32x faster                                               |
| genshi_xml               | 66.0 ms                                                | 50.2 ms: 1.31x faster                                               |
| sympy_sum                | 196 ms                                                 | 151 ms: 1.30x faster                                                |
| nqueens                  | 106 ms                                                 | 82.9 ms: 1.28x faster                                               |
| json_dumps               | 14.2 ms                                                | 11.1 ms: 1.28x faster                                               |
| sympy_str                | 346 ms                                                 | 273 ms: 1.27x faster                                                |
| xml_etree_generate       | 99.4 ms                                                | 79.5 ms: 1.25x faster                                               |
| docutils                 | 3.30 sec                                               | 2.64 sec: 1.25x faster                                              |
| pathlib                  | 20.5 ms                                                | 16.9 ms: 1.21x faster                                               |
| regex_v8                 | 27.8 ms                                                | 23.0 ms: 1.21x faster                                               |
| sympy_expand             | 566 ms                                                 | 470 ms: 1.20x faster                                                |
| python_startup           | 14.6 ms                                                | 12.2 ms: 1.20x faster                                               |
| xml_etree_parse          | 168 ms                                                 | 140 ms: 1.20x faster                                                |
| xml_etree_iterparse      | 115 ms                                                 | 98.1 ms: 1.18x faster                                               |
| meteor_contest           | 120 ms                                                 | 105 ms: 1.14x faster                                                |
| json_loads               | 31.2 us                                                | 28.0 us: 1.12x faster                                               |
| json                     | 5.69 ms                                                | 5.19 ms: 1.10x faster                                               |
| regex_effbot             | 3.63 ms                                                | 3.32 ms: 1.09x faster                                               |
| sqlite_synth             | 3.02 us                                                | 2.79 us: 1.09x faster                                               |
| regex_dna                | 227 ms                                                 | 215 ms: 1.06x faster                                                |
| async_generators         | 444 ms                                                 | 433 ms: 1.02x faster                                                |
| pidigits                 | 191 ms                                                 | 188 ms: 1.01x faster                                                |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                |
| telco                    | 7.27 ms                                                | 7.58 ms: 1.04x slower                                               |
| coverage                 | 79.4 ms                                                | 87.6 ms: 1.10x slower                                               |
| python_startup_no_site   | 5.93 ms                                                | 6.93 ms: 1.17x slower                                               |
| gc_traversal             | 3.62 ms                                                | 4.93 ms: 1.36x slower                                               |
| create_gc_cycles         | 1.62 ms                                                | 2.58 ms: 1.59x slower                                               |
| Geometric mean           | (ref)                                                  | 1.48x faster                                                        |
Ignored benchmarks (23) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250629-3.15.0a0-0f33ad5-JIT/bm-20250629-linux-x86_64-brandtbucher-jit_up_10_12-3.15.0a0-0f33ad5.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.480x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.39x
- 95% likely to have a speedup of 1.36x
- 99% likely to have a speedup of 1.33x

# Memory
- memory change: 1.33x