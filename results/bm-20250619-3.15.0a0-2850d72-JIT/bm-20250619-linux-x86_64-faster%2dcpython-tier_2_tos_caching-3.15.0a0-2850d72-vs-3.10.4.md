# Results vs. 3.10.4

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: linux-x86_64
- commit hash: 2850d72
- commit date: 2025-06-19
- overall geometric mean: 1.470x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.34x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250619-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 260 ms: 1.34x faster                                                          |
| docutils       | 3.30 sec                                               | 2.64 sec: 1.25x faster                                                        |
| html5lib       | 88.9 ms                                                | 61.5 ms: 1.44x faster                                                         |
| Geometric mean | (ref)                                                  | 1.34x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250619-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 607 ms: 2.91x faster                                                          |
| async_tree_none         | 728 ms                                                 | 265 ms: 2.75x faster                                                          |
| async_tree_memoization  | 870 ms                                                 | 317 ms: 2.74x faster                                                          |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 506 ms: 2.01x faster                                                          |
| Geometric mean          | (ref)                                                  | 2.58x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250619-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 82.8 ms: 1.85x faster                                                         |
| float          | 117 ms                                                 | 65.0 ms: 1.80x faster                                                         |
| pidigits       | 191 ms                                                 | 193 ms: 1.01x slower                                                          |
| Geometric mean | (ref)                                                  | 1.49x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250619-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 127 ms: 1.49x faster                                                          |
| regex_v8       | 27.8 ms                                                | 22.3 ms: 1.25x faster                                                         |
| regex_dna      | 227 ms                                                 | 186 ms: 1.22x faster                                                          |
| regex_effbot   | 3.63 ms                                                | 3.10 ms: 1.17x faster                                                         |
| Geometric mean | (ref)                                                  | 1.28x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250619-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.86 sec: 1.68x faster                                                        |
| unpickle_pure_python | 331 us                                                 | 205 us: 1.61x faster                                                          |
| pickle_pure_python   | 484 us                                                 | 324 us: 1.50x faster                                                          |
| xml_etree_process    | 79.1 ms                                                | 56.0 ms: 1.41x faster                                                         |
| json_dumps           | 14.2 ms                                                | 11.0 ms: 1.29x faster                                                         |
| xml_etree_generate   | 99.4 ms                                                | 81.1 ms: 1.23x faster                                                         |
| xml_etree_parse      | 168 ms                                                 | 139 ms: 1.21x faster                                                          |
| xml_etree_iterparse  | 115 ms                                                 | 98.5 ms: 1.17x faster                                                         |
| json_loads           | 31.2 us                                                | 27.9 us: 1.12x faster                                                         |
| Geometric mean       | (ref)                                                  | 1.34x faster                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250619-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.2 ms: 1.19x faster                                                         |
| python_startup_no_site | 5.93 ms                                                | 6.98 ms: 1.18x slower                                                         |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250619-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.8 ms: 1.51x faster                                                         |
| django_template | 48.2 ms                                                | 32.3 ms: 1.49x faster                                                         |
| genshi_text     | 31.8 ms                                                | 21.8 ms: 1.46x faster                                                         |
| genshi_xml      | 66.0 ms                                                | 51.0 ms: 1.30x faster                                                         |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                                  |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250619-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 171 us: 3.18x faster                                                          |
| async_tree_io            | 1.77 sec                                               | 607 ms: 2.91x faster                                                          |
| async_tree_none          | 728 ms                                                 | 265 ms: 2.75x faster                                                          |
| async_tree_memoization   | 870 ms                                                 | 317 ms: 2.74x faster                                                          |
| generators               | 80.1 ms                                                | 30.3 ms: 2.65x faster                                                         |
| deltablue                | 7.91 ms                                                | 3.14 ms: 2.52x faster                                                         |
| richards_super           | 94.7 ms                                                | 38.9 ms: 2.44x faster                                                         |
| richards                 | 79.3 ms                                                | 33.8 ms: 2.34x faster                                                         |
| mdp                      | 2.85 sec                                               | 1.24 sec: 2.30x faster                                                        |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 506 ms: 2.01x faster                                                          |
| deepcopy_memo            | 58.5 us                                                | 29.5 us: 1.98x faster                                                         |
| go                       | 240 ms                                                 | 121 ms: 1.98x faster                                                          |
| pylint                   | 551 ms                                                 | 283 ms: 1.95x faster                                                          |
| chaos                    | 115 ms                                                 | 61.5 ms: 1.88x faster                                                         |
| scimark_sor              | 220 ms                                                 | 118 ms: 1.87x faster                                                          |
| nbody                    | 154 ms                                                 | 82.8 ms: 1.85x faster                                                         |
| raytrace                 | 507 ms                                                 | 274 ms: 1.85x faster                                                          |
| deepcopy                 | 479 us                                                 | 262 us: 1.83x faster                                                          |
| float                    | 117 ms                                                 | 65.0 ms: 1.80x faster                                                         |
| spectral_norm            | 170 ms                                                 | 94.7 ms: 1.79x faster                                                         |
| scimark_monte_carlo      | 118 ms                                                 | 66.0 ms: 1.79x faster                                                         |
| pyflate                  | 716 ms                                                 | 420 ms: 1.71x faster                                                          |
| djangocms                | 38.4 us                                                | 22.7 us: 1.69x faster                                                         |
| tomli_loads              | 3.14 sec                                               | 1.86 sec: 1.68x faster                                                        |
| comprehensions           | 28.8 us                                                | 17.2 us: 1.68x faster                                                         |
| crypto_pyaes             | 128 ms                                                 | 76.8 ms: 1.66x faster                                                         |
| hexiom                   | 10.4 ms                                                | 6.41 ms: 1.62x faster                                                         |
| unpickle_pure_python     | 331 us                                                 | 205 us: 1.61x faster                                                          |
| deepcopy_reduce          | 4.17 us                                                | 2.69 us: 1.55x faster                                                         |
| mako                     | 16.3 ms                                                | 10.8 ms: 1.51x faster                                                         |
| pickle_pure_python       | 484 us                                                 | 324 us: 1.50x faster                                                          |
| scimark_lu               | 176 ms                                                 | 118 ms: 1.49x faster                                                          |
| django_template          | 48.2 ms                                                | 32.3 ms: 1.49x faster                                                         |
| regex_compile            | 188 ms                                                 | 127 ms: 1.49x faster                                                          |
| scimark_fft              | 466 ms                                                 | 318 ms: 1.46x faster                                                          |
| genshi_text              | 31.8 ms                                                | 21.8 ms: 1.46x faster                                                         |
| html5lib                 | 88.9 ms                                                | 61.5 ms: 1.44x faster                                                         |
| pycparser                | 1.58 sec                                               | 1.11 sec: 1.43x faster                                                        |
| dulwich_log              | 84.3 ms                                                | 59.5 ms: 1.42x faster                                                         |
| xml_etree_process        | 79.1 ms                                                | 56.0 ms: 1.41x faster                                                         |
| coroutines               | 35.1 ms                                                | 25.1 ms: 1.40x faster                                                         |
| thrift                   | 1.07 ms                                                | 781 us: 1.37x faster                                                          |
| logging_simple           | 8.30 us                                                | 6.19 us: 1.34x faster                                                         |
| 2to3                     | 348 ms                                                 | 260 ms: 1.34x faster                                                          |
| sympy_integrate          | 25.8 ms                                                | 19.3 ms: 1.33x faster                                                         |
| logging_format           | 9.09 us                                                | 6.85 us: 1.33x faster                                                         |
| fannkuch                 | 532 ms                                                 | 401 ms: 1.32x faster                                                          |
| sympy_sum                | 196 ms                                                 | 150 ms: 1.31x faster                                                          |
| genshi_xml               | 66.0 ms                                                | 51.0 ms: 1.30x faster                                                         |
| nqueens                  | 106 ms                                                 | 82.0 ms: 1.29x faster                                                         |
| json_dumps               | 14.2 ms                                                | 11.0 ms: 1.29x faster                                                         |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.04 ms: 1.28x faster                                                         |
| sympy_str                | 346 ms                                                 | 271 ms: 1.27x faster                                                          |
| docutils                 | 3.30 sec                                               | 2.64 sec: 1.25x faster                                                        |
| regex_v8                 | 27.8 ms                                                | 22.3 ms: 1.25x faster                                                         |
| xml_etree_generate       | 99.4 ms                                                | 81.1 ms: 1.23x faster                                                         |
| regex_dna                | 227 ms                                                 | 186 ms: 1.22x faster                                                          |
| xml_etree_parse          | 168 ms                                                 | 139 ms: 1.21x faster                                                          |
| sympy_expand             | 566 ms                                                 | 468 ms: 1.21x faster                                                          |
| pathlib                  | 20.5 ms                                                | 17.0 ms: 1.20x faster                                                         |
| pprint_pformat           | 2.10 sec                                               | 1.75 sec: 1.20x faster                                                        |
| python_startup           | 14.6 ms                                                | 12.2 ms: 1.19x faster                                                         |
| pprint_safe_repr         | 1.02 sec                                               | 855 ms: 1.19x faster                                                          |
| xml_etree_iterparse      | 115 ms                                                 | 98.5 ms: 1.17x faster                                                         |
| regex_effbot             | 3.63 ms                                                | 3.10 ms: 1.17x faster                                                         |
| json_loads               | 31.2 us                                                | 27.9 us: 1.12x faster                                                         |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.11x faster                                                          |
| json                     | 5.69 ms                                                | 5.15 ms: 1.10x faster                                                         |
| sqlite_synth             | 3.02 us                                                | 2.81 us: 1.08x faster                                                         |
| async_generators         | 444 ms                                                 | 428 ms: 1.04x faster                                                          |
| asyncio_websockets       | 559 ms                                                 | 553 ms: 1.01x faster                                                          |
| pidigits                 | 191 ms                                                 | 193 ms: 1.01x slower                                                          |
| telco                    | 7.27 ms                                                | 7.91 ms: 1.09x slower                                                         |
| coverage                 | 79.4 ms                                                | 87.4 ms: 1.10x slower                                                         |
| python_startup_no_site   | 5.93 ms                                                | 6.98 ms: 1.18x slower                                                         |
| gc_traversal             | 3.62 ms                                                | 5.07 ms: 1.40x slower                                                         |
| create_gc_cycles         | 1.62 ms                                                | 2.59 ms: 1.60x slower                                                         |
| logging_silent           | 190 ns                                                 | 477 ns: 2.51x slower                                                          |
| Geometric mean           | (ref)                                                  | 1.45x faster                                                                  |
Ignored benchmarks (23) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250619-3.15.0a0-2850d72-JIT/bm-20250619-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.470x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.36x
- 95% likely to have a speedup of 1.33x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.34x