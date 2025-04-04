# Results vs. 3.10.4

- fork: faster-cpython
- ref: tos_caching_1
- machine: linux-x86_64
- commit hash: 492df4e
- commit date: 2025-04-04
- overall geometric mean: 1.458x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.32x faster
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250404-linux-x86_64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 248 ms: 1.40x faster                                                      |
| docutils       | 3.30 sec                                               | 2.59 sec: 1.27x faster                                                    |
| html5lib       | 88.9 ms                                                | 62.1 ms: 1.43x faster                                                     |
| Geometric mean | (ref)                                                  | 1.37x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250404-linux-x86_64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 620 ms: 2.85x faster                                                      |
| async_tree_none         | 728 ms                                                 | 263 ms: 2.77x faster                                                      |
| async_tree_memoization  | 870 ms                                                 | 314 ms: 2.77x faster                                                      |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 481 ms: 2.11x faster                                                      |
| Geometric mean          | (ref)                                                  | 2.61x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250404-linux-x86_64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 67.4 ms: 1.74x faster                                                     |
| nbody          | 154 ms                                                 | 91.6 ms: 1.68x faster                                                     |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                  | 1.44x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250404-linux-x86_64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 126 ms: 1.49x faster                                                      |
| regex_v8       | 27.8 ms                                                | 23.3 ms: 1.19x faster                                                     |
| regex_effbot   | 3.63 ms                                                | 3.35 ms: 1.08x faster                                                     |
| regex_dna      | 227 ms                                                 | 216 ms: 1.05x faster                                                      |
| Geometric mean | (ref)                                                  | 1.19x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250404-linux-x86_64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.94 sec: 1.62x faster                                                    |
| pickle_pure_python   | 484 us                                                 | 316 us: 1.53x faster                                                      |
| unpickle_pure_python | 331 us                                                 | 221 us: 1.50x faster                                                      |
| xml_etree_process    | 79.1 ms                                                | 59.7 ms: 1.33x faster                                                     |
| json_dumps           | 14.2 ms                                                | 11.6 ms: 1.22x faster                                                     |
| xml_etree_parse      | 168 ms                                                 | 141 ms: 1.19x faster                                                      |
| xml_etree_generate   | 99.4 ms                                                | 84.9 ms: 1.17x faster                                                     |
| xml_etree_iterparse  | 115 ms                                                 | 99.0 ms: 1.17x faster                                                     |
| json_loads           | 31.2 us                                                | 29.7 us: 1.05x faster                                                     |
| Geometric mean       | (ref)                                                  | 1.30x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250404-linux-x86_64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.1 ms: 1.11x faster                                                     |
| python_startup_no_site | 5.93 ms                                                | 8.18 ms: 1.38x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250404-linux-x86_64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 32.1 ms: 1.50x faster                                                     |
| genshi_text     | 31.8 ms                                                | 21.2 ms: 1.50x faster                                                     |
| mako            | 16.3 ms                                                | 11.5 ms: 1.42x faster                                                     |
| genshi_xml      | 66.0 ms                                                | 49.6 ms: 1.33x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                              |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250404-linux-x86_64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 160 us: 3.41x faster                                                      |
| async_tree_io            | 1.77 sec                                               | 620 ms: 2.85x faster                                                      |
| async_tree_none          | 728 ms                                                 | 263 ms: 2.77x faster                                                      |
| async_tree_memoization   | 870 ms                                                 | 314 ms: 2.77x faster                                                      |
| generators               | 80.1 ms                                                | 30.5 ms: 2.63x faster                                                     |
| mdp                      | 2.85 sec                                               | 1.22 sec: 2.34x faster                                                    |
| deltablue                | 7.91 ms                                                | 3.43 ms: 2.31x faster                                                     |
| go                       | 240 ms                                                 | 113 ms: 2.12x faster                                                      |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 481 ms: 2.11x faster                                                      |
| chaos                    | 115 ms                                                 | 56.8 ms: 2.03x faster                                                     |
| pylint                   | 551 ms                                                 | 276 ms: 1.99x faster                                                      |
| deepcopy_memo            | 58.5 us                                                | 30.1 us: 1.94x faster                                                     |
| raytrace                 | 507 ms                                                 | 262 ms: 1.93x faster                                                      |
| logging_silent           | 190 ns                                                 | 99.0 ns: 1.92x faster                                                     |
| deepcopy                 | 479 us                                                 | 253 us: 1.90x faster                                                      |
| richards_super           | 94.7 ms                                                | 50.0 ms: 1.89x faster                                                     |
| scimark_sor              | 220 ms                                                 | 119 ms: 1.85x faster                                                      |
| scimark_monte_carlo      | 118 ms                                                 | 65.1 ms: 1.81x faster                                                     |
| richards                 | 79.3 ms                                                | 44.0 ms: 1.80x faster                                                     |
| crypto_pyaes             | 128 ms                                                 | 72.5 ms: 1.76x faster                                                     |
| float                    | 117 ms                                                 | 67.4 ms: 1.74x faster                                                     |
| comprehensions           | 28.8 us                                                | 16.8 us: 1.71x faster                                                     |
| nbody                    | 154 ms                                                 | 91.6 ms: 1.68x faster                                                     |
| hexiom                   | 10.4 ms                                                | 6.29 ms: 1.65x faster                                                     |
| pyflate                  | 716 ms                                                 | 437 ms: 1.64x faster                                                      |
| tomli_loads              | 3.14 sec                                               | 1.94 sec: 1.62x faster                                                    |
| spectral_norm            | 170 ms                                                 | 105 ms: 1.62x faster                                                      |
| deepcopy_reduce          | 4.17 us                                                | 2.66 us: 1.56x faster                                                     |
| pickle_pure_python       | 484 us                                                 | 316 us: 1.53x faster                                                      |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.51x faster                                                      |
| django_template          | 48.2 ms                                                | 32.1 ms: 1.50x faster                                                     |
| genshi_text              | 31.8 ms                                                | 21.2 ms: 1.50x faster                                                     |
| unpickle_pure_python     | 331 us                                                 | 221 us: 1.50x faster                                                      |
| regex_compile            | 188 ms                                                 | 126 ms: 1.49x faster                                                      |
| logging_simple           | 8.30 us                                                | 5.67 us: 1.47x faster                                                     |
| logging_format           | 9.09 us                                                | 6.21 us: 1.46x faster                                                     |
| coroutines               | 35.1 ms                                                | 24.2 ms: 1.45x faster                                                     |
| html5lib                 | 88.9 ms                                                | 62.1 ms: 1.43x faster                                                     |
| dulwich_log              | 84.3 ms                                                | 59.1 ms: 1.43x faster                                                     |
| mako                     | 16.3 ms                                                | 11.5 ms: 1.42x faster                                                     |
| pprint_pformat           | 2.10 sec                                               | 1.49 sec: 1.41x faster                                                    |
| pprint_safe_repr         | 1.02 sec                                               | 723 ms: 1.41x faster                                                      |
| 2to3                     | 348 ms                                                 | 248 ms: 1.40x faster                                                      |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.67 ms: 1.39x faster                                                     |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.9 ms: 1.38x faster                                                     |
| pycparser                | 1.58 sec                                               | 1.15 sec: 1.37x faster                                                    |
| scimark_fft              | 466 ms                                                 | 344 ms: 1.35x faster                                                      |
| sympy_integrate          | 25.8 ms                                                | 19.1 ms: 1.35x faster                                                     |
| genshi_xml               | 66.0 ms                                                | 49.6 ms: 1.33x faster                                                     |
| xml_etree_process        | 79.1 ms                                                | 59.7 ms: 1.33x faster                                                     |
| sympy_sum                | 196 ms                                                 | 149 ms: 1.32x faster                                                      |
| fannkuch                 | 532 ms                                                 | 405 ms: 1.31x faster                                                      |
| sqlalchemy_declarative   | 172 ms                                                 | 131 ms: 1.31x faster                                                      |
| sympy_str                | 346 ms                                                 | 267 ms: 1.30x faster                                                      |
| nqueens                  | 106 ms                                                 | 82.4 ms: 1.28x faster                                                     |
| docutils                 | 3.30 sec                                               | 2.59 sec: 1.27x faster                                                    |
| sympy_expand             | 566 ms                                                 | 459 ms: 1.23x faster                                                      |
| pathlib                  | 20.5 ms                                                | 16.7 ms: 1.22x faster                                                     |
| json_dumps               | 14.2 ms                                                | 11.6 ms: 1.22x faster                                                     |
| regex_v8                 | 27.8 ms                                                | 23.3 ms: 1.19x faster                                                     |
| xml_etree_parse          | 168 ms                                                 | 141 ms: 1.19x faster                                                      |
| xml_etree_generate       | 99.4 ms                                                | 84.9 ms: 1.17x faster                                                     |
| xml_etree_iterparse      | 115 ms                                                 | 99.0 ms: 1.17x faster                                                     |
| meteor_contest           | 120 ms                                                 | 105 ms: 1.14x faster                                                      |
| async_generators         | 444 ms                                                 | 395 ms: 1.12x faster                                                      |
| bench_thread_pool        | 986 us                                                 | 881 us: 1.12x faster                                                      |
| python_startup           | 14.6 ms                                                | 13.1 ms: 1.11x faster                                                     |
| regex_effbot             | 3.63 ms                                                | 3.35 ms: 1.08x faster                                                     |
| json                     | 5.69 ms                                                | 5.29 ms: 1.08x faster                                                     |
| sqlite_synth             | 3.02 us                                                | 2.83 us: 1.07x faster                                                     |
| json_loads               | 31.2 us                                                | 29.7 us: 1.05x faster                                                     |
| regex_dna                | 227 ms                                                 | 216 ms: 1.05x faster                                                      |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                      |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                      |
| coverage                 | 79.4 ms                                                | 84.6 ms: 1.06x slower                                                     |
| telco                    | 7.27 ms                                                | 7.75 ms: 1.07x slower                                                     |
| gc_traversal             | 3.62 ms                                                | 4.76 ms: 1.31x slower                                                     |
| python_startup_no_site   | 5.93 ms                                                | 8.18 ms: 1.38x slower                                                     |
| create_gc_cycles         | 1.62 ms                                                | 2.46 ms: 1.52x slower                                                     |
| bench_mp_pool            | 24.0 ms                                                | 81.9 ms: 3.41x slower                                                     |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                              |
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250404-3.14.0a6+-492df4e/bm-20250404-linux-x86_64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.458x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.37x
- 95% likely to have a speedup of 1.35x
- 99% likely to have a speedup of 1.32x

# Memory
- memory change: 1.27x