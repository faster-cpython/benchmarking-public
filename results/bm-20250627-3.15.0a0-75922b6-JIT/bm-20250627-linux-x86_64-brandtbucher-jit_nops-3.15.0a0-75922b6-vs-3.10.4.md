# Results vs. 3.10.4

- fork: brandtbucher
- ref: jit_nops
- machine: linux-x86_64
- commit hash: 75922b6
- commit date: 2025-06-27
- overall geometric mean: 1.484x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.34x faster
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250627-linux-x86_64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 259 ms: 1.34x faster                                            |
| docutils       | 3.30 sec                                               | 2.63 sec: 1.25x faster                                          |
| html5lib       | 88.9 ms                                                | 61.4 ms: 1.45x faster                                           |
| Geometric mean | (ref)                                                  | 1.35x faster                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250627-linux-x86_64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 600 ms: 2.95x faster                                            |
| async_tree_none         | 728 ms                                                 | 263 ms: 2.77x faster                                            |
| async_tree_memoization  | 870 ms                                                 | 314 ms: 2.77x faster                                            |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 499 ms: 2.04x faster                                            |
| Geometric mean          | (ref)                                                  | 2.60x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250627-linux-x86_64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 117 ms                                                 | 65.7 ms: 1.78x faster                                           |
| nbody          | 154 ms                                                 | 98.8 ms: 1.55x faster                                           |
| pidigits       | 191 ms                                                 | 188 ms: 1.01x faster                                            |
| Geometric mean | (ref)                                                  | 1.41x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250627-linux-x86_64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 127 ms: 1.49x faster                                            |
| regex_v8       | 27.8 ms                                                | 23.7 ms: 1.17x faster                                           |
| regex_effbot   | 3.63 ms                                                | 3.25 ms: 1.12x faster                                           |
| regex_dna      | 227 ms                                                 | 213 ms: 1.06x faster                                            |
| Geometric mean | (ref)                                                  | 1.20x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250627-linux-x86_64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.82 sec: 1.72x faster                                          |
| unpickle_pure_python | 331 us                                                 | 193 us: 1.71x faster                                            |
| pickle_pure_python   | 484 us                                                 | 320 us: 1.51x faster                                            |
| xml_etree_process    | 79.1 ms                                                | 55.3 ms: 1.43x faster                                           |
| json_dumps           | 14.2 ms                                                | 11.0 ms: 1.29x faster                                           |
| xml_etree_generate   | 99.4 ms                                                | 79.8 ms: 1.25x faster                                           |
| xml_etree_parse      | 168 ms                                                 | 142 ms: 1.19x faster                                            |
| xml_etree_iterparse  | 115 ms                                                 | 98.3 ms: 1.17x faster                                           |
| json_loads           | 31.2 us                                                | 28.2 us: 1.11x faster                                           |
| Geometric mean       | (ref)                                                  | 1.36x faster                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250627-linux-x86_64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.2 ms: 1.19x faster                                           |
| python_startup_no_site | 5.93 ms                                                | 6.98 ms: 1.18x slower                                           |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250627-linux-x86_64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.6 ms: 1.54x faster                                           |
| django_template | 48.2 ms                                                | 32.1 ms: 1.50x faster                                           |
| genshi_text     | 31.8 ms                                                | 21.6 ms: 1.47x faster                                           |
| genshi_xml      | 66.0 ms                                                | 50.7 ms: 1.30x faster                                           |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250627-linux-x86_64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 169 us: 3.22x faster                                            |
| async_tree_io            | 1.77 sec                                               | 600 ms: 2.95x faster                                            |
| async_tree_none          | 728 ms                                                 | 263 ms: 2.77x faster                                            |
| async_tree_memoization   | 870 ms                                                 | 314 ms: 2.77x faster                                            |
| generators               | 80.1 ms                                                | 30.3 ms: 2.64x faster                                           |
| deltablue                | 7.91 ms                                                | 3.04 ms: 2.60x faster                                           |
| richards_super           | 94.7 ms                                                | 37.8 ms: 2.50x faster                                           |
| richards                 | 79.3 ms                                                | 32.2 ms: 2.46x faster                                           |
| mdp                      | 2.85 sec                                               | 1.24 sec: 2.30x faster                                          |
| go                       | 240 ms                                                 | 115 ms: 2.08x faster                                            |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 499 ms: 2.04x faster                                            |
| deepcopy_memo            | 58.5 us                                                | 29.4 us: 1.99x faster                                           |
| pylint                   | 551 ms                                                 | 283 ms: 1.95x faster                                            |
| chaos                    | 115 ms                                                 | 61.3 ms: 1.88x faster                                           |
| deepcopy                 | 479 us                                                 | 257 us: 1.86x faster                                            |
| logging_silent           | 190 ns                                                 | 102 ns: 1.86x faster                                            |
| raytrace                 | 507 ms                                                 | 273 ms: 1.86x faster                                            |
| spectral_norm            | 170 ms                                                 | 91.9 ms: 1.85x faster                                           |
| scimark_sor              | 220 ms                                                 | 119 ms: 1.84x faster                                            |
| scimark_monte_carlo      | 118 ms                                                 | 65.9 ms: 1.79x faster                                           |
| float                    | 117 ms                                                 | 65.7 ms: 1.78x faster                                           |
| comprehensions           | 28.8 us                                                | 16.4 us: 1.75x faster                                           |
| djangocms                | 38.4 us                                                | 21.9 us: 1.75x faster                                           |
| pyflate                  | 716 ms                                                 | 410 ms: 1.75x faster                                            |
| tomli_loads              | 3.14 sec                                               | 1.82 sec: 1.72x faster                                          |
| crypto_pyaes             | 128 ms                                                 | 74.5 ms: 1.71x faster                                           |
| unpickle_pure_python     | 331 us                                                 | 193 us: 1.71x faster                                            |
| hexiom                   | 10.4 ms                                                | 6.19 ms: 1.68x faster                                           |
| nbody                    | 154 ms                                                 | 98.8 ms: 1.55x faster                                           |
| deepcopy_reduce          | 4.17 us                                                | 2.70 us: 1.54x faster                                           |
| mako                     | 16.3 ms                                                | 10.6 ms: 1.54x faster                                           |
| pickle_pure_python       | 484 us                                                 | 320 us: 1.51x faster                                            |
| django_template          | 48.2 ms                                                | 32.1 ms: 1.50x faster                                           |
| regex_compile            | 188 ms                                                 | 127 ms: 1.49x faster                                            |
| scimark_lu               | 176 ms                                                 | 118 ms: 1.49x faster                                            |
| scimark_fft              | 466 ms                                                 | 313 ms: 1.49x faster                                            |
| genshi_text              | 31.8 ms                                                | 21.6 ms: 1.47x faster                                           |
| logging_simple           | 8.30 us                                                | 5.73 us: 1.45x faster                                           |
| html5lib                 | 88.9 ms                                                | 61.4 ms: 1.45x faster                                           |
| xml_etree_process        | 79.1 ms                                                | 55.3 ms: 1.43x faster                                           |
| pycparser                | 1.58 sec                                               | 1.11 sec: 1.42x faster                                          |
| dulwich_log              | 84.3 ms                                                | 59.3 ms: 1.42x faster                                           |
| pprint_pformat           | 2.10 sec                                               | 1.48 sec: 1.42x faster                                          |
| pprint_safe_repr         | 1.02 sec                                               | 718 ms: 1.42x faster                                            |
| logging_format           | 9.09 us                                                | 6.43 us: 1.41x faster                                           |
| coroutines               | 35.1 ms                                                | 25.0 ms: 1.40x faster                                           |
| thrift                   | 1.07 ms                                                | 779 us: 1.38x faster                                            |
| 2to3                     | 348 ms                                                 | 259 ms: 1.34x faster                                            |
| fannkuch                 | 532 ms                                                 | 397 ms: 1.34x faster                                            |
| sympy_integrate          | 25.8 ms                                                | 19.3 ms: 1.34x faster                                           |
| sympy_sum                | 196 ms                                                 | 148 ms: 1.33x faster                                            |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.92 ms: 1.31x faster                                           |
| genshi_xml               | 66.0 ms                                                | 50.7 ms: 1.30x faster                                           |
| json_dumps               | 14.2 ms                                                | 11.0 ms: 1.29x faster                                           |
| nqueens                  | 106 ms                                                 | 82.0 ms: 1.29x faster                                           |
| sympy_str                | 346 ms                                                 | 272 ms: 1.27x faster                                            |
| docutils                 | 3.30 sec                                               | 2.63 sec: 1.25x faster                                          |
| xml_etree_generate       | 99.4 ms                                                | 79.8 ms: 1.25x faster                                           |
| sympy_expand             | 566 ms                                                 | 469 ms: 1.21x faster                                            |
| python_startup           | 14.6 ms                                                | 12.2 ms: 1.19x faster                                           |
| pathlib                  | 20.5 ms                                                | 17.2 ms: 1.19x faster                                           |
| xml_etree_parse          | 168 ms                                                 | 142 ms: 1.19x faster                                            |
| xml_etree_iterparse      | 115 ms                                                 | 98.3 ms: 1.17x faster                                           |
| regex_v8                 | 27.8 ms                                                | 23.7 ms: 1.17x faster                                           |
| meteor_contest           | 120 ms                                                 | 105 ms: 1.14x faster                                            |
| regex_effbot             | 3.63 ms                                                | 3.25 ms: 1.12x faster                                           |
| json_loads               | 31.2 us                                                | 28.2 us: 1.11x faster                                           |
| json                     | 5.69 ms                                                | 5.24 ms: 1.09x faster                                           |
| sqlite_synth             | 3.02 us                                                | 2.79 us: 1.09x faster                                           |
| regex_dna                | 227 ms                                                 | 213 ms: 1.06x faster                                            |
| async_generators         | 444 ms                                                 | 427 ms: 1.04x faster                                            |
| pidigits                 | 191 ms                                                 | 188 ms: 1.01x faster                                            |
| asyncio_websockets       | 559 ms                                                 | 553 ms: 1.01x faster                                            |
| telco                    | 7.27 ms                                                | 7.70 ms: 1.06x slower                                           |
| coverage                 | 79.4 ms                                                | 87.2 ms: 1.10x slower                                           |
| python_startup_no_site   | 5.93 ms                                                | 6.98 ms: 1.18x slower                                           |
| gc_traversal             | 3.62 ms                                                | 5.02 ms: 1.38x slower                                           |
| create_gc_cycles         | 1.62 ms                                                | 2.61 ms: 1.61x slower                                           |
| Geometric mean           | (ref)                                                  | 1.49x faster                                                    |
Ignored benchmarks (23) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250627-3.15.0a0-75922b6-JIT/bm-20250627-linux-x86_64-brandtbucher-jit_nops-3.15.0a0-75922b6.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.484x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.39x
- 95% likely to have a speedup of 1.38x
- 99% likely to have a speedup of 1.34x

# Memory
- memory change: 1.33x