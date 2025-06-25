# Results vs. 3.10.4

- fork: python
- ref: fea5ccc55d8486300beb
- machine: linux-x86_64
- commit hash: fea5ccc
- commit date: 2025-06-24
- overall geometric mean: 1.470x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250624-linux-x86_64-python-fea5ccc55d8486300beb-3.15.0a0-fea5ccc |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 260 ms: 1.34x faster                                                  |
| docutils       | 3.30 sec                                               | 2.63 sec: 1.25x faster                                                |
| html5lib       | 88.9 ms                                                | 62.0 ms: 1.43x faster                                                 |
| Geometric mean | (ref)                                                  | 1.34x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250624-linux-x86_64-python-fea5ccc55d8486300beb-3.15.0a0-fea5ccc |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 603 ms: 2.93x faster                                                  |
| async_tree_none         | 728 ms                                                 | 261 ms: 2.79x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 314 ms: 2.77x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 502 ms: 2.03x faster                                                  |
| Geometric mean          | (ref)                                                  | 2.60x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250624-linux-x86_64-python-fea5ccc55d8486300beb-3.15.0a0-fea5ccc |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 117 ms                                                 | 66.2 ms: 1.77x faster                                                 |
| nbody          | 154 ms                                                 | 97.5 ms: 1.57x faster                                                 |
| pidigits       | 191 ms                                                 | 188 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.41x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250624-linux-x86_64-python-fea5ccc55d8486300beb-3.15.0a0-fea5ccc |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 128 ms: 1.47x faster                                                  |
| regex_v8       | 27.8 ms                                                | 22.1 ms: 1.26x faster                                                 |
| regex_effbot   | 3.63 ms                                                | 3.17 ms: 1.14x faster                                                 |
| regex_dna      | 227 ms                                                 | 200 ms: 1.13x faster                                                  |
| Geometric mean | (ref)                                                  | 1.24x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250624-linux-x86_64-python-fea5ccc55d8486300beb-3.15.0a0-fea5ccc |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.82 sec: 1.72x faster                                                |
| unpickle_pure_python | 331 us                                                 | 202 us: 1.64x faster                                                  |
| pickle_pure_python   | 484 us                                                 | 323 us: 1.50x faster                                                  |
| xml_etree_process    | 79.1 ms                                                | 56.2 ms: 1.41x faster                                                 |
| json_dumps           | 14.2 ms                                                | 11.1 ms: 1.28x faster                                                 |
| xml_etree_generate   | 99.4 ms                                                | 80.3 ms: 1.24x faster                                                 |
| xml_etree_parse      | 168 ms                                                 | 140 ms: 1.20x faster                                                  |
| xml_etree_iterparse  | 115 ms                                                 | 98.7 ms: 1.17x faster                                                 |
| json_loads           | 31.2 us                                                | 28.1 us: 1.11x faster                                                 |
| Geometric mean       | (ref)                                                  | 1.35x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250624-linux-x86_64-python-fea5ccc55d8486300beb-3.15.0a0-fea5ccc |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.2 ms: 1.20x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 6.95 ms: 1.17x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250624-linux-x86_64-python-fea5ccc55d8486300beb-3.15.0a0-fea5ccc |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.0 ms: 1.49x faster                                                 |
| django_template | 48.2 ms                                                | 32.6 ms: 1.48x faster                                                 |
| genshi_text     | 31.8 ms                                                | 21.7 ms: 1.46x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 51.4 ms: 1.29x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250624-linux-x86_64-python-fea5ccc55d8486300beb-3.15.0a0-fea5ccc |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 166 us: 3.28x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 603 ms: 2.93x faster                                                  |
| async_tree_none          | 728 ms                                                 | 261 ms: 2.79x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 314 ms: 2.77x faster                                                  |
| generators               | 80.1 ms                                                | 30.3 ms: 2.65x faster                                                 |
| deltablue                | 7.91 ms                                                | 3.10 ms: 2.55x faster                                                 |
| richards_super           | 94.7 ms                                                | 39.2 ms: 2.42x faster                                                 |
| richards                 | 79.3 ms                                                | 33.2 ms: 2.39x faster                                                 |
| mdp                      | 2.85 sec                                               | 1.24 sec: 2.29x faster                                                |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 502 ms: 2.03x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 29.3 us: 2.00x faster                                                 |
| go                       | 240 ms                                                 | 121 ms: 1.99x faster                                                  |
| pylint                   | 551 ms                                                 | 282 ms: 1.96x faster                                                  |
| chaos                    | 115 ms                                                 | 61.6 ms: 1.87x faster                                                 |
| scimark_sor              | 220 ms                                                 | 119 ms: 1.85x faster                                                  |
| deepcopy                 | 479 us                                                 | 260 us: 1.84x faster                                                  |
| raytrace                 | 507 ms                                                 | 275 ms: 1.84x faster                                                  |
| spectral_norm            | 170 ms                                                 | 94.8 ms: 1.79x faster                                                 |
| scimark_monte_carlo      | 118 ms                                                 | 66.0 ms: 1.79x faster                                                 |
| float                    | 117 ms                                                 | 66.2 ms: 1.77x faster                                                 |
| djangocms                | 38.4 us                                                | 21.8 us: 1.76x faster                                                 |
| tomli_loads              | 3.14 sec                                               | 1.82 sec: 1.72x faster                                                |
| pyflate                  | 716 ms                                                 | 420 ms: 1.71x faster                                                  |
| comprehensions           | 28.8 us                                                | 17.2 us: 1.67x faster                                                 |
| crypto_pyaes             | 128 ms                                                 | 76.8 ms: 1.66x faster                                                 |
| unpickle_pure_python     | 331 us                                                 | 202 us: 1.64x faster                                                  |
| hexiom                   | 10.4 ms                                                | 6.49 ms: 1.60x faster                                                 |
| nbody                    | 154 ms                                                 | 97.5 ms: 1.57x faster                                                 |
| deepcopy_reduce          | 4.17 us                                                | 2.78 us: 1.50x faster                                                 |
| pickle_pure_python       | 484 us                                                 | 323 us: 1.50x faster                                                  |
| scimark_lu               | 176 ms                                                 | 118 ms: 1.49x faster                                                  |
| mako                     | 16.3 ms                                                | 11.0 ms: 1.49x faster                                                 |
| scimark_fft              | 466 ms                                                 | 314 ms: 1.48x faster                                                  |
| django_template          | 48.2 ms                                                | 32.6 ms: 1.48x faster                                                 |
| regex_compile            | 188 ms                                                 | 128 ms: 1.47x faster                                                  |
| genshi_text              | 31.8 ms                                                | 21.7 ms: 1.46x faster                                                 |
| html5lib                 | 88.9 ms                                                | 62.0 ms: 1.43x faster                                                 |
| dulwich_log              | 84.3 ms                                                | 59.4 ms: 1.42x faster                                                 |
| coroutines               | 35.1 ms                                                | 24.9 ms: 1.41x faster                                                 |
| pycparser                | 1.58 sec                                               | 1.12 sec: 1.41x faster                                                |
| xml_etree_process        | 79.1 ms                                                | 56.2 ms: 1.41x faster                                                 |
| thrift                   | 1.07 ms                                                | 774 us: 1.39x faster                                                  |
| logging_simple           | 8.30 us                                                | 6.16 us: 1.35x faster                                                 |
| 2to3                     | 348 ms                                                 | 260 ms: 1.34x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 19.3 ms: 1.33x faster                                                 |
| logging_format           | 9.09 us                                                | 6.83 us: 1.33x faster                                                 |
| fannkuch                 | 532 ms                                                 | 403 ms: 1.32x faster                                                  |
| sympy_sum                | 196 ms                                                 | 150 ms: 1.31x faster                                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.03 ms: 1.29x faster                                                 |
| genshi_xml               | 66.0 ms                                                | 51.4 ms: 1.29x faster                                                 |
| json_dumps               | 14.2 ms                                                | 11.1 ms: 1.28x faster                                                 |
| sympy_str                | 346 ms                                                 | 272 ms: 1.27x faster                                                  |
| nqueens                  | 106 ms                                                 | 83.9 ms: 1.26x faster                                                 |
| regex_v8                 | 27.8 ms                                                | 22.1 ms: 1.26x faster                                                 |
| docutils                 | 3.30 sec                                               | 2.63 sec: 1.25x faster                                                |
| xml_etree_generate       | 99.4 ms                                                | 80.3 ms: 1.24x faster                                                 |
| pprint_safe_repr         | 1.02 sec                                               | 822 ms: 1.24x faster                                                  |
| pprint_pformat           | 2.10 sec                                               | 1.70 sec: 1.24x faster                                                |
| pathlib                  | 20.5 ms                                                | 17.0 ms: 1.20x faster                                                 |
| sympy_expand             | 566 ms                                                 | 470 ms: 1.20x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 140 ms: 1.20x faster                                                  |
| python_startup           | 14.6 ms                                                | 12.2 ms: 1.20x faster                                                 |
| xml_etree_iterparse      | 115 ms                                                 | 98.7 ms: 1.17x faster                                                 |
| regex_effbot             | 3.63 ms                                                | 3.17 ms: 1.14x faster                                                 |
| regex_dna                | 227 ms                                                 | 200 ms: 1.13x faster                                                  |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                  |
| json_loads               | 31.2 us                                                | 28.1 us: 1.11x faster                                                 |
| sqlite_synth             | 3.02 us                                                | 2.80 us: 1.08x faster                                                 |
| json                     | 5.69 ms                                                | 5.28 ms: 1.08x faster                                                 |
| async_generators         | 444 ms                                                 | 434 ms: 1.02x faster                                                  |
| pidigits                 | 191 ms                                                 | 188 ms: 1.01x faster                                                  |
| asyncio_websockets       | 559 ms                                                 | 553 ms: 1.01x faster                                                  |
| telco                    | 7.27 ms                                                | 7.73 ms: 1.06x slower                                                 |
| coverage                 | 79.4 ms                                                | 87.5 ms: 1.10x slower                                                 |
| python_startup_no_site   | 5.93 ms                                                | 6.95 ms: 1.17x slower                                                 |
| gc_traversal             | 3.62 ms                                                | 4.93 ms: 1.36x slower                                                 |
| create_gc_cycles         | 1.62 ms                                                | 2.59 ms: 1.60x slower                                                 |
| logging_silent           | 190 ns                                                 | 479 ns: 2.53x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.44x faster                                                          |
Ignored benchmarks (23) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250624-3.15.0a0-fea5ccc-JIT/bm-20250624-linux-x86_64-python-fea5ccc55d8486300beb-3.15.0a0-fea5ccc.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.470x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.35x
- 95% likely to have a speedup of 1.33x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.33x