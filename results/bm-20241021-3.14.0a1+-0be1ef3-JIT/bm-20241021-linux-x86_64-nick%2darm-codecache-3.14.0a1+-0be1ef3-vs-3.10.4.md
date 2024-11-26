# Results vs. 3.10.4

- fork: nick-arm
- ref: codecache
- machine: linux-x86_64
- commit hash: 0be1ef3
- commit date: 2024-10-21
- overall geometric mean: 1.403x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.35x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-linux-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 276 ms: 1.26x faster                                            |
| docutils       | 3.30 sec                                               | 2.91 sec: 1.13x faster                                          |
| html5lib       | 88.9 ms                                                | 67.1 ms: 1.32x faster                                           |
| tornado_http   | 136 ms                                                 | 94.8 ms: 1.44x faster                                           |
| Geometric mean | (ref)                                                  | 1.29x faster                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-linux-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 339 ms: 2.15x faster                                            |
| async_tree_memoization  | 870 ms                                                 | 418 ms: 2.08x faster                                            |
| async_tree_io           | 1.77 sec                                               | 858 ms: 2.06x faster                                            |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 572 ms: 1.78x faster                                            |
| Geometric mean          | (ref)                                                  | 2.01x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-linux-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 82.3 ms: 1.86x faster                                           |
| float          | 117 ms                                                 | 75.6 ms: 1.55x faster                                           |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                            |
| Geometric mean | (ref)                                                  | 1.44x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-linux-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 139 ms: 1.36x faster                                            |
| regex_v8       | 27.8 ms                                                | 24.7 ms: 1.13x faster                                           |
| regex_dna      | 227 ms                                                 | 214 ms: 1.06x faster                                            |
| regex_effbot   | 3.63 ms                                                | 3.72 ms: 1.02x slower                                           |
| Geometric mean | (ref)                                                  | 1.12x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-linux-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.90 sec: 1.65x faster                                          |
| pickle_pure_python   | 484 us                                                 | 311 us: 1.56x faster                                            |
| unpickle_pure_python | 331 us                                                 | 215 us: 1.54x faster                                            |
| xml_etree_process    | 79.1 ms                                                | 54.8 ms: 1.44x faster                                           |
| json_dumps           | 14.2 ms                                                | 10.8 ms: 1.31x faster                                           |
| xml_etree_generate   | 99.4 ms                                                | 78.2 ms: 1.27x faster                                           |
| json_loads           | 31.2 us                                                | 26.8 us: 1.16x faster                                           |
| xml_etree_iterparse  | 115 ms                                                 | 101 ms: 1.14x faster                                            |
| xml_etree_parse      | 168 ms                                                 | 148 ms: 1.13x faster                                            |
| Geometric mean       | (ref)                                                  | 1.34x faster                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-linux-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 11.8 ms: 1.23x faster                                           |
| python_startup_no_site | 5.93 ms                                                | 7.07 ms: 1.19x slower                                           |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-linux-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.2 ms: 1.60x faster                                           |
| django_template | 48.2 ms                                                | 35.8 ms: 1.35x faster                                           |
| genshi_text     | 31.8 ms                                                | 25.8 ms: 1.24x faster                                           |
| genshi_xml      | 66.0 ms                                                | 60.4 ms: 1.09x faster                                           |
| Geometric mean  | (ref)                                                  | 1.31x faster                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-linux-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 165 us: 3.30x faster                                            |
| deltablue                | 7.91 ms                                                | 3.27 ms: 2.42x faster                                           |
| generators               | 80.1 ms                                                | 35.5 ms: 2.26x faster                                           |
| async_tree_none          | 728 ms                                                 | 339 ms: 2.15x faster                                            |
| async_tree_memoization   | 870 ms                                                 | 418 ms: 2.08x faster                                            |
| async_tree_io            | 1.77 sec                                               | 858 ms: 2.06x faster                                            |
| deepcopy_memo            | 58.5 us                                                | 29.1 us: 2.01x faster                                           |
| richards_super           | 94.7 ms                                                | 47.6 ms: 1.99x faster                                           |
| logging_silent           | 190 ns                                                 | 97.1 ns: 1.95x faster                                           |
| chaos                    | 115 ms                                                 | 59.1 ms: 1.95x faster                                           |
| richards                 | 79.3 ms                                                | 40.8 ms: 1.94x faster                                           |
| nbody                    | 154 ms                                                 | 82.3 ms: 1.86x faster                                           |
| crypto_pyaes             | 128 ms                                                 | 68.6 ms: 1.86x faster                                           |
| raytrace                 | 507 ms                                                 | 273 ms: 1.86x faster                                            |
| scimark_sor              | 220 ms                                                 | 119 ms: 1.85x faster                                            |
| scimark_monte_carlo      | 118 ms                                                 | 64.3 ms: 1.84x faster                                           |
| deepcopy                 | 479 us                                                 | 266 us: 1.80x faster                                            |
| go                       | 240 ms                                                 | 133 ms: 1.80x faster                                            |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 572 ms: 1.78x faster                                            |
| comprehensions           | 28.8 us                                                | 17.0 us: 1.70x faster                                           |
| tomli_loads              | 3.14 sec                                               | 1.90 sec: 1.65x faster                                          |
| sqlglot_parse            | 2.17 ms                                                | 1.34 ms: 1.62x faster                                           |
| pyflate                  | 716 ms                                                 | 447 ms: 1.60x faster                                            |
| mako                     | 16.3 ms                                                | 10.2 ms: 1.60x faster                                           |
| scimark_lu               | 176 ms                                                 | 113 ms: 1.56x faster                                            |
| pickle_pure_python       | 484 us                                                 | 311 us: 1.56x faster                                            |
| float                    | 117 ms                                                 | 75.6 ms: 1.55x faster                                           |
| unpickle_pure_python     | 331 us                                                 | 215 us: 1.54x faster                                            |
| deepcopy_reduce          | 4.17 us                                                | 2.73 us: 1.52x faster                                           |
| sqlglot_transpile        | 2.57 ms                                                | 1.70 ms: 1.52x faster                                           |
| logging_simple           | 8.30 us                                                | 5.57 us: 1.49x faster                                           |
| logging_format           | 9.09 us                                                | 6.10 us: 1.49x faster                                           |
| coroutines               | 35.1 ms                                                | 23.7 ms: 1.48x faster                                           |
| hexiom                   | 10.4 ms                                                | 7.01 ms: 1.48x faster                                           |
| spectral_norm            | 170 ms                                                 | 115 ms: 1.48x faster                                            |
| scimark_fft              | 466 ms                                                 | 315 ms: 1.48x faster                                            |
| pylint                   | 551 ms                                                 | 374 ms: 1.48x faster                                            |
| pprint_safe_repr         | 1.02 sec                                               | 696 ms: 1.46x faster                                            |
| xml_etree_process        | 79.1 ms                                                | 54.8 ms: 1.44x faster                                           |
| tornado_http             | 136 ms                                                 | 94.8 ms: 1.44x faster                                           |
| pprint_pformat           | 2.10 sec                                               | 1.46 sec: 1.44x faster                                          |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.63 ms: 1.40x faster                                           |
| fannkuch                 | 532 ms                                                 | 381 ms: 1.40x faster                                            |
| pycparser                | 1.58 sec                                               | 1.14 sec: 1.39x faster                                          |
| thrift                   | 1.07 ms                                                | 779 us: 1.38x faster                                            |
| regex_compile            | 188 ms                                                 | 139 ms: 1.36x faster                                            |
| django_template          | 48.2 ms                                                | 35.8 ms: 1.35x faster                                           |
| html5lib                 | 88.9 ms                                                | 67.1 ms: 1.32x faster                                           |
| json_dumps               | 14.2 ms                                                | 10.8 ms: 1.31x faster                                           |
| pathlib                  | 20.5 ms                                                | 16.0 ms: 1.28x faster                                           |
| xml_etree_generate       | 99.4 ms                                                | 78.2 ms: 1.27x faster                                           |
| sqlglot_normalize        | 143 ms                                                 | 113 ms: 1.26x faster                                            |
| 2to3                     | 348 ms                                                 | 276 ms: 1.26x faster                                            |
| dulwich_log              | 84.3 ms                                                | 66.9 ms: 1.26x faster                                           |
| genshi_text              | 31.8 ms                                                | 25.8 ms: 1.24x faster                                           |
| python_startup           | 14.6 ms                                                | 11.8 ms: 1.23x faster                                           |
| nqueens                  | 106 ms                                                 | 87.6 ms: 1.21x faster                                           |
| sqlglot_optimize         | 69.2 ms                                                | 59.3 ms: 1.17x faster                                           |
| json_loads               | 31.2 us                                                | 26.8 us: 1.16x faster                                           |
| sympy_str                | 346 ms                                                 | 299 ms: 1.16x faster                                            |
| xml_etree_iterparse      | 115 ms                                                 | 101 ms: 1.14x faster                                            |
| json                     | 5.69 ms                                                | 5.00 ms: 1.14x faster                                           |
| sympy_expand             | 566 ms                                                 | 498 ms: 1.13x faster                                            |
| docutils                 | 3.30 sec                                               | 2.91 sec: 1.13x faster                                          |
| xml_etree_parse          | 168 ms                                                 | 148 ms: 1.13x faster                                            |
| regex_v8                 | 27.8 ms                                                | 24.7 ms: 1.13x faster                                           |
| sympy_sum                | 196 ms                                                 | 175 ms: 1.12x faster                                            |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                            |
| mdp                      | 2.85 sec                                               | 2.54 sec: 1.12x faster                                          |
| bench_thread_pool        | 986 us                                                 | 881 us: 1.12x faster                                            |
| sympy_integrate          | 25.8 ms                                                | 23.3 ms: 1.11x faster                                           |
| genshi_xml               | 66.0 ms                                                | 60.4 ms: 1.09x faster                                           |
| regex_dna                | 227 ms                                                 | 214 ms: 1.06x faster                                            |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                            |
| asyncio_websockets       | 559 ms                                                 | 554 ms: 1.01x faster                                            |
| regex_effbot             | 3.63 ms                                                | 3.72 ms: 1.02x slower                                           |
| async_generators         | 444 ms                                                 | 457 ms: 1.03x slower                                            |
| telco                    | 7.27 ms                                                | 7.58 ms: 1.04x slower                                           |
| coverage                 | 79.4 ms                                                | 84.4 ms: 1.06x slower                                           |
| python_startup_no_site   | 5.93 ms                                                | 7.07 ms: 1.19x slower                                           |
| gc_traversal             | 3.62 ms                                                | 4.37 ms: 1.21x slower                                           |
| create_gc_cycles         | 1.62 ms                                                | 2.66 ms: 1.64x slower                                           |
| bench_mp_pool            | 24.0 ms                                                | 83.8 ms: 3.49x slower                                           |
| Geometric mean           | (ref)                                                  | 1.38x faster                                                    |
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20241021-3.14.0a1+-0be1ef3-JIT/bm-20241021-linux-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx

- Geometric mean (including insignificant results): 1.403x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.35x