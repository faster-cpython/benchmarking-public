# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_hot
- machine: linux-x86_64
- commit hash: d2c9ae9
- commit date: 2025-06-19
- overall geometric mean: 1.455x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x faster
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250619-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 260 ms: 1.34x faster                                              |
| docutils       | 3.30 sec                                               | 2.65 sec: 1.24x faster                                            |
| html5lib       | 88.9 ms                                                | 62.3 ms: 1.43x faster                                             |
| Geometric mean | (ref)                                                  | 1.33x faster                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250619-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 599 ms: 2.95x faster                                              |
| async_tree_none         | 728 ms                                                 | 262 ms: 2.77x faster                                              |
| async_tree_memoization  | 870 ms                                                 | 314 ms: 2.77x faster                                              |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 498 ms: 2.04x faster                                              |
| Geometric mean          | (ref)                                                  | 2.61x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250619-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 117 ms                                                 | 66.3 ms: 1.77x faster                                             |
| nbody          | 154 ms                                                 | 95.0 ms: 1.62x faster                                             |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                              |
| Geometric mean | (ref)                                                  | 1.43x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250619-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 128 ms: 1.48x faster                                              |
| regex_v8       | 27.8 ms                                                | 22.8 ms: 1.22x faster                                             |
| regex_effbot   | 3.63 ms                                                | 3.32 ms: 1.09x faster                                             |
| regex_dna      | 227 ms                                                 | 219 ms: 1.04x faster                                              |
| Geometric mean | (ref)                                                  | 1.19x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250619-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.92 sec: 1.64x faster                                            |
| unpickle_pure_python | 331 us                                                 | 205 us: 1.61x faster                                              |
| pickle_pure_python   | 484 us                                                 | 325 us: 1.49x faster                                              |
| xml_etree_process    | 79.1 ms                                                | 56.2 ms: 1.41x faster                                             |
| json_dumps           | 14.2 ms                                                | 11.0 ms: 1.28x faster                                             |
| xml_etree_generate   | 99.4 ms                                                | 80.8 ms: 1.23x faster                                             |
| xml_etree_parse      | 168 ms                                                 | 140 ms: 1.20x faster                                              |
| xml_etree_iterparse  | 115 ms                                                 | 98.3 ms: 1.17x faster                                             |
| json_loads           | 31.2 us                                                | 28.8 us: 1.08x faster                                             |
| Geometric mean       | (ref)                                                  | 1.33x faster                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250619-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.2 ms: 1.19x faster                                             |
| python_startup_no_site | 5.93 ms                                                | 6.96 ms: 1.17x slower                                             |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250619-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.8 ms: 1.51x faster                                             |
| genshi_text     | 31.8 ms                                                | 21.1 ms: 1.51x faster                                             |
| django_template | 48.2 ms                                                | 32.7 ms: 1.47x faster                                             |
| genshi_xml      | 66.0 ms                                                | 50.3 ms: 1.31x faster                                             |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250619-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 171 us: 3.18x faster                                              |
| async_tree_io            | 1.77 sec                                               | 599 ms: 2.95x faster                                              |
| async_tree_none          | 728 ms                                                 | 262 ms: 2.77x faster                                              |
| async_tree_memoization   | 870 ms                                                 | 314 ms: 2.77x faster                                              |
| generators               | 80.1 ms                                                | 30.5 ms: 2.62x faster                                             |
| deltablue                | 7.91 ms                                                | 3.22 ms: 2.46x faster                                             |
| richards_super           | 94.7 ms                                                | 39.3 ms: 2.41x faster                                             |
| richards                 | 79.3 ms                                                | 34.2 ms: 2.31x faster                                             |
| mdp                      | 2.85 sec                                               | 1.25 sec: 2.29x faster                                            |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 498 ms: 2.04x faster                                              |
| deepcopy_memo            | 58.5 us                                                | 29.8 us: 1.96x faster                                             |
| pylint                   | 551 ms                                                 | 283 ms: 1.95x faster                                              |
| go                       | 240 ms                                                 | 123 ms: 1.94x faster                                              |
| chaos                    | 115 ms                                                 | 62.4 ms: 1.85x faster                                             |
| deepcopy                 | 479 us                                                 | 260 us: 1.84x faster                                              |
| raytrace                 | 507 ms                                                 | 278 ms: 1.82x faster                                              |
| scimark_sor              | 220 ms                                                 | 121 ms: 1.82x faster                                              |
| float                    | 117 ms                                                 | 66.3 ms: 1.77x faster                                             |
| scimark_monte_carlo      | 118 ms                                                 | 67.0 ms: 1.76x faster                                             |
| djangocms                | 38.4 us                                                | 22.5 us: 1.71x faster                                             |
| crypto_pyaes             | 128 ms                                                 | 76.0 ms: 1.68x faster                                             |
| pyflate                  | 716 ms                                                 | 432 ms: 1.66x faster                                              |
| comprehensions           | 28.8 us                                                | 17.4 us: 1.65x faster                                             |
| tomli_loads              | 3.14 sec                                               | 1.92 sec: 1.64x faster                                            |
| nbody                    | 154 ms                                                 | 95.0 ms: 1.62x faster                                             |
| spectral_norm            | 170 ms                                                 | 105 ms: 1.62x faster                                              |
| unpickle_pure_python     | 331 us                                                 | 205 us: 1.61x faster                                              |
| hexiom                   | 10.4 ms                                                | 6.53 ms: 1.59x faster                                             |
| deepcopy_reduce          | 4.17 us                                                | 2.72 us: 1.53x faster                                             |
| mako                     | 16.3 ms                                                | 10.8 ms: 1.51x faster                                             |
| genshi_text              | 31.8 ms                                                | 21.1 ms: 1.51x faster                                             |
| pickle_pure_python       | 484 us                                                 | 325 us: 1.49x faster                                              |
| scimark_lu               | 176 ms                                                 | 119 ms: 1.49x faster                                              |
| regex_compile            | 188 ms                                                 | 128 ms: 1.48x faster                                              |
| django_template          | 48.2 ms                                                | 32.7 ms: 1.47x faster                                             |
| coroutines               | 35.1 ms                                                | 24.3 ms: 1.45x faster                                             |
| html5lib                 | 88.9 ms                                                | 62.3 ms: 1.43x faster                                             |
| dulwich_log              | 84.3 ms                                                | 59.6 ms: 1.41x faster                                             |
| pycparser                | 1.58 sec                                               | 1.12 sec: 1.41x faster                                            |
| xml_etree_process        | 79.1 ms                                                | 56.2 ms: 1.41x faster                                             |
| scimark_fft              | 466 ms                                                 | 336 ms: 1.39x faster                                              |
| thrift                   | 1.07 ms                                                | 780 us: 1.37x faster                                              |
| 2to3                     | 348 ms                                                 | 260 ms: 1.34x faster                                              |
| logging_simple           | 8.30 us                                                | 6.21 us: 1.34x faster                                             |
| sympy_integrate          | 25.8 ms                                                | 19.5 ms: 1.32x faster                                             |
| logging_format           | 9.09 us                                                | 6.89 us: 1.32x faster                                             |
| genshi_xml               | 66.0 ms                                                | 50.3 ms: 1.31x faster                                             |
| sympy_sum                | 196 ms                                                 | 151 ms: 1.30x faster                                              |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.04 ms: 1.28x faster                                             |
| json_dumps               | 14.2 ms                                                | 11.0 ms: 1.28x faster                                             |
| fannkuch                 | 532 ms                                                 | 416 ms: 1.28x faster                                              |
| sympy_str                | 346 ms                                                 | 273 ms: 1.27x faster                                              |
| nqueens                  | 106 ms                                                 | 84.0 ms: 1.26x faster                                             |
| docutils                 | 3.30 sec                                               | 2.65 sec: 1.24x faster                                            |
| xml_etree_generate       | 99.4 ms                                                | 80.8 ms: 1.23x faster                                             |
| regex_v8                 | 27.8 ms                                                | 22.8 ms: 1.22x faster                                             |
| pprint_pformat           | 2.10 sec                                               | 1.73 sec: 1.21x faster                                            |
| pprint_safe_repr         | 1.02 sec                                               | 839 ms: 1.21x faster                                              |
| pathlib                  | 20.5 ms                                                | 16.9 ms: 1.21x faster                                             |
| sympy_expand             | 566 ms                                                 | 469 ms: 1.21x faster                                              |
| xml_etree_parse          | 168 ms                                                 | 140 ms: 1.20x faster                                              |
| python_startup           | 14.6 ms                                                | 12.2 ms: 1.19x faster                                             |
| xml_etree_iterparse      | 115 ms                                                 | 98.3 ms: 1.17x faster                                             |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                              |
| regex_effbot             | 3.63 ms                                                | 3.32 ms: 1.09x faster                                             |
| json_loads               | 31.2 us                                                | 28.8 us: 1.08x faster                                             |
| sqlite_synth             | 3.02 us                                                | 2.79 us: 1.08x faster                                             |
| json                     | 5.69 ms                                                | 5.29 ms: 1.08x faster                                             |
| regex_dna                | 227 ms                                                 | 219 ms: 1.04x faster                                              |
| async_generators         | 444 ms                                                 | 433 ms: 1.02x faster                                              |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                              |
| asyncio_websockets       | 559 ms                                                 | 554 ms: 1.01x faster                                              |
| telco                    | 7.27 ms                                                | 7.80 ms: 1.07x slower                                             |
| coverage                 | 79.4 ms                                                | 88.1 ms: 1.11x slower                                             |
| python_startup_no_site   | 5.93 ms                                                | 6.96 ms: 1.17x slower                                             |
| gc_traversal             | 3.62 ms                                                | 4.93 ms: 1.36x slower                                             |
| create_gc_cycles         | 1.62 ms                                                | 2.59 ms: 1.60x slower                                             |
| logging_silent           | 190 ns                                                 | 474 ns: 2.50x slower                                              |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                      |
Ignored benchmarks (23) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250619-3.15.0a0-d2c9ae9-JIT/bm-20250619-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.455x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.35x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.28x

# Memory
- memory change: 1.33x