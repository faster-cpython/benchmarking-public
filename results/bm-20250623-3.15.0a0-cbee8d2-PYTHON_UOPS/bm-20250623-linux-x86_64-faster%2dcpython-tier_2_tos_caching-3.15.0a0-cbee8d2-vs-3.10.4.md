# Results vs. 3.10.4

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: linux-x86_64
- commit hash: cbee8d2
- commit date: 2025-06-23
- overall geometric mean: 1.266x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: 1.32x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250623-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-cbee8d2 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 292 ms: 1.19x faster                                                          |
| docutils       | 3.30 sec                                               | 2.82 sec: 1.17x faster                                                        |
| html5lib       | 88.9 ms                                                | 64.4 ms: 1.38x faster                                                         |
| Geometric mean | (ref)                                                  | 1.24x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250623-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-cbee8d2 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 643 ms: 2.75x faster                                                          |
| async_tree_memoization  | 870 ms                                                 | 341 ms: 2.55x faster                                                          |
| async_tree_none         | 728 ms                                                 | 289 ms: 2.52x faster                                                          |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 532 ms: 1.91x faster                                                          |
| Geometric mean          | (ref)                                                  | 2.41x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250623-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-cbee8d2 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 91.9 ms: 1.27x faster                                                         |
| pidigits       | 191 ms                                                 | 193 ms: 1.01x slower                                                          |
| nbody          | 154 ms                                                 | 176 ms: 1.14x slower                                                          |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250623-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-cbee8d2 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 143 ms: 1.32x faster                                                          |
| regex_v8       | 27.8 ms                                                | 22.4 ms: 1.24x faster                                                         |
| regex_dna      | 227 ms                                                 | 199 ms: 1.14x faster                                                          |
| regex_effbot   | 3.63 ms                                                | 3.22 ms: 1.13x faster                                                         |
| Geometric mean | (ref)                                                  | 1.20x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250623-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-cbee8d2 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| json_dumps           | 14.2 ms                                                | 10.9 ms: 1.29x faster                                                         |
| tomli_loads          | 3.14 sec                                               | 2.48 sec: 1.27x faster                                                        |
| pickle_pure_python   | 484 us                                                 | 398 us: 1.22x faster                                                          |
| xml_etree_parse      | 168 ms                                                 | 148 ms: 1.14x faster                                                          |
| json_loads           | 31.2 us                                                | 28.3 us: 1.10x faster                                                         |
| xml_etree_process    | 79.1 ms                                                | 72.1 ms: 1.10x faster                                                         |
| xml_etree_iterparse  | 115 ms                                                 | 106 ms: 1.09x faster                                                          |
| unpickle_pure_python | 331 us                                                 | 334 us: 1.01x slower                                                          |
| xml_etree_generate   | 99.4 ms                                                | 102 ms: 1.02x slower                                                          |
| Geometric mean       | (ref)                                                  | 1.13x faster                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250623-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-cbee8d2 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.2 ms: 1.20x faster                                                         |
| python_startup_no_site | 5.93 ms                                                | 6.94 ms: 1.17x slower                                                         |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250623-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-cbee8d2 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 21.6 ms: 1.47x faster                                                         |
| django_template | 48.2 ms                                                | 33.2 ms: 1.45x faster                                                         |
| genshi_xml      | 66.0 ms                                                | 54.0 ms: 1.22x faster                                                         |
| mako            | 16.3 ms                                                | 16.6 ms: 1.02x slower                                                         |
| Geometric mean  | (ref)                                                  | 1.27x faster                                                                  |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250623-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-cbee8d2 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_io            | 1.77 sec                                               | 643 ms: 2.75x faster                                                          |
| typing_runtime_protocols | 544 us                                                 | 200 us: 2.72x faster                                                          |
| generators               | 80.1 ms                                                | 30.5 ms: 2.62x faster                                                         |
| async_tree_memoization   | 870 ms                                                 | 341 ms: 2.55x faster                                                          |
| async_tree_none          | 728 ms                                                 | 289 ms: 2.52x faster                                                          |
| mdp                      | 2.85 sec                                               | 1.41 sec: 2.02x faster                                                        |
| deepcopy_memo            | 58.5 us                                                | 30.1 us: 1.94x faster                                                         |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 532 ms: 1.91x faster                                                          |
| pylint                   | 551 ms                                                 | 291 ms: 1.89x faster                                                          |
| scimark_sor              | 220 ms                                                 | 121 ms: 1.82x faster                                                          |
| deepcopy                 | 479 us                                                 | 267 us: 1.79x faster                                                          |
| chaos                    | 115 ms                                                 | 66.4 ms: 1.74x faster                                                         |
| djangocms                | 38.4 us                                                | 23.4 us: 1.64x faster                                                         |
| deltablue                | 7.91 ms                                                | 4.96 ms: 1.60x faster                                                         |
| richards_super           | 94.7 ms                                                | 59.6 ms: 1.59x faster                                                         |
| raytrace                 | 507 ms                                                 | 329 ms: 1.54x faster                                                          |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.50x faster                                                          |
| deepcopy_reduce          | 4.17 us                                                | 2.79 us: 1.49x faster                                                         |
| genshi_text              | 31.8 ms                                                | 21.6 ms: 1.47x faster                                                         |
| django_template          | 48.2 ms                                                | 33.2 ms: 1.45x faster                                                         |
| scimark_monte_carlo      | 118 ms                                                 | 82.9 ms: 1.43x faster                                                         |
| richards                 | 79.3 ms                                                | 56.0 ms: 1.42x faster                                                         |
| coroutines               | 35.1 ms                                                | 25.0 ms: 1.41x faster                                                         |
| thrift                   | 1.07 ms                                                | 774 us: 1.38x faster                                                          |
| html5lib                 | 88.9 ms                                                | 64.4 ms: 1.38x faster                                                         |
| dulwich_log              | 84.3 ms                                                | 62.0 ms: 1.36x faster                                                         |
| logging_simple           | 8.30 us                                                | 6.17 us: 1.35x faster                                                         |
| logging_format           | 9.09 us                                                | 6.89 us: 1.32x faster                                                         |
| regex_compile            | 188 ms                                                 | 143 ms: 1.32x faster                                                          |
| json_dumps               | 14.2 ms                                                | 10.9 ms: 1.29x faster                                                         |
| float                    | 117 ms                                                 | 91.9 ms: 1.27x faster                                                         |
| tomli_loads              | 3.14 sec                                               | 2.48 sec: 1.27x faster                                                        |
| sympy_integrate          | 25.8 ms                                                | 20.4 ms: 1.27x faster                                                         |
| pyflate                  | 716 ms                                                 | 573 ms: 1.25x faster                                                          |
| regex_v8                 | 27.8 ms                                                | 22.4 ms: 1.24x faster                                                         |
| sympy_sum                | 196 ms                                                 | 159 ms: 1.23x faster                                                          |
| genshi_xml               | 66.0 ms                                                | 54.0 ms: 1.22x faster                                                         |
| crypto_pyaes             | 128 ms                                                 | 105 ms: 1.22x faster                                                          |
| pickle_pure_python       | 484 us                                                 | 398 us: 1.22x faster                                                          |
| spectral_norm            | 170 ms                                                 | 141 ms: 1.21x faster                                                          |
| python_startup           | 14.6 ms                                                | 12.2 ms: 1.20x faster                                                         |
| 2to3                     | 348 ms                                                 | 292 ms: 1.19x faster                                                          |
| sympy_str                | 346 ms                                                 | 291 ms: 1.19x faster                                                          |
| pathlib                  | 20.5 ms                                                | 17.3 ms: 1.19x faster                                                         |
| docutils                 | 3.30 sec                                               | 2.82 sec: 1.17x faster                                                        |
| go                       | 240 ms                                                 | 207 ms: 1.16x faster                                                          |
| nqueens                  | 106 ms                                                 | 91.6 ms: 1.16x faster                                                         |
| regex_dna                | 227 ms                                                 | 199 ms: 1.14x faster                                                          |
| xml_etree_parse          | 168 ms                                                 | 148 ms: 1.14x faster                                                          |
| comprehensions           | 28.8 us                                                | 25.3 us: 1.13x faster                                                         |
| regex_effbot             | 3.63 ms                                                | 3.22 ms: 1.13x faster                                                         |
| sympy_expand             | 566 ms                                                 | 511 ms: 1.11x faster                                                          |
| json_loads               | 31.2 us                                                | 28.3 us: 1.10x faster                                                         |
| xml_etree_process        | 79.1 ms                                                | 72.1 ms: 1.10x faster                                                         |
| xml_etree_iterparse      | 115 ms                                                 | 106 ms: 1.09x faster                                                          |
| json                     | 5.69 ms                                                | 5.22 ms: 1.09x faster                                                         |
| pycparser                | 1.58 sec                                               | 1.45 sec: 1.09x faster                                                        |
| hexiom                   | 10.4 ms                                                | 9.66 ms: 1.08x faster                                                         |
| async_generators         | 444 ms                                                 | 434 ms: 1.02x faster                                                          |
| sqlite_synth             | 3.02 us                                                | 2.98 us: 1.01x faster                                                         |
| asyncio_websockets       | 559 ms                                                 | 553 ms: 1.01x faster                                                          |
| pidigits                 | 191 ms                                                 | 193 ms: 1.01x slower                                                          |
| unpickle_pure_python     | 331 us                                                 | 334 us: 1.01x slower                                                          |
| scimark_fft              | 466 ms                                                 | 472 ms: 1.01x slower                                                          |
| mako                     | 16.3 ms                                                | 16.6 ms: 1.02x slower                                                         |
| xml_etree_generate       | 99.4 ms                                                | 102 ms: 1.02x slower                                                          |
| fannkuch                 | 532 ms                                                 | 564 ms: 1.06x slower                                                          |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 6.97 ms: 1.08x slower                                                         |
| coverage                 | 79.4 ms                                                | 86.4 ms: 1.09x slower                                                         |
| pprint_safe_repr         | 1.02 sec                                               | 1.13 sec: 1.11x slower                                                        |
| pprint_pformat           | 2.10 sec                                               | 2.36 sec: 1.12x slower                                                        |
| meteor_contest           | 120 ms                                                 | 135 ms: 1.13x slower                                                          |
| nbody                    | 154 ms                                                 | 176 ms: 1.14x slower                                                          |
| python_startup_no_site   | 5.93 ms                                                | 6.94 ms: 1.17x slower                                                         |
| telco                    | 7.27 ms                                                | 9.25 ms: 1.27x slower                                                         |
| gc_traversal             | 3.62 ms                                                | 4.96 ms: 1.37x slower                                                         |
| create_gc_cycles         | 1.62 ms                                                | 2.60 ms: 1.60x slower                                                         |
| logging_silent           | 190 ns                                                 | 476 ns: 2.51x slower                                                          |
| Geometric mean           | (ref)                                                  | 1.25x faster                                                                  |
Ignored benchmarks (23) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250623-3.15.0a0-cbee8d2-PYTHON_UOPS/bm-20250623-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-cbee8d2.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.266x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.15x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: 1.32x