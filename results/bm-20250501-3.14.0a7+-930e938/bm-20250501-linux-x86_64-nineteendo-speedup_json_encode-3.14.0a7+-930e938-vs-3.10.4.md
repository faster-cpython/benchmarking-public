# Results vs. 3.10.4

- fork: nineteendo
- ref: speedup_json_encode
- machine: linux-x86_64
- commit hash: 930e938
- commit date: 2025-05-01
- overall geometric mean: 1.442x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.31x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250501-linux-x86_64-nineteendo-speedup_json_encode-3.14.0a7+-930e938 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 256 ms: 1.36x faster                                                      |
| docutils       | 3.30 sec                                               | 2.62 sec: 1.26x faster                                                    |
| html5lib       | 88.9 ms                                                | 61.4 ms: 1.45x faster                                                     |
| Geometric mean | (ref)                                                  | 1.35x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250501-linux-x86_64-nineteendo-speedup_json_encode-3.14.0a7+-930e938 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 597 ms: 2.96x faster                                                      |
| async_tree_memoization  | 870 ms                                                 | 313 ms: 2.78x faster                                                      |
| async_tree_none         | 728 ms                                                 | 262 ms: 2.77x faster                                                      |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 493 ms: 2.06x faster                                                      |
| Geometric mean          | (ref)                                                  | 2.62x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250501-linux-x86_64-nineteendo-speedup_json_encode-3.14.0a7+-930e938 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 70.0 ms: 1.67x faster                                                     |
| nbody          | 154 ms                                                 | 99.1 ms: 1.55x faster                                                     |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                  | 1.38x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250501-linux-x86_64-nineteendo-speedup_json_encode-3.14.0a7+-930e938 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 128 ms: 1.48x faster                                                      |
| regex_v8       | 27.8 ms                                                | 23.3 ms: 1.19x faster                                                     |
| regex_dna      | 227 ms                                                 | 205 ms: 1.10x faster                                                      |
| regex_effbot   | 3.63 ms                                                | 3.31 ms: 1.10x faster                                                     |
| Geometric mean | (ref)                                                  | 1.21x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250501-linux-x86_64-nineteendo-speedup_json_encode-3.14.0a7+-930e938 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 2.00 sec: 1.57x faster                                                    |
| unpickle_pure_python | 331 us                                                 | 219 us: 1.51x faster                                                      |
| pickle_pure_python   | 484 us                                                 | 321 us: 1.51x faster                                                      |
| json_dumps           | 14.2 ms                                                | 10.5 ms: 1.35x faster                                                     |
| xml_etree_process    | 79.1 ms                                                | 59.9 ms: 1.32x faster                                                     |
| xml_etree_parse      | 168 ms                                                 | 143 ms: 1.18x faster                                                      |
| xml_etree_generate   | 99.4 ms                                                | 85.4 ms: 1.16x faster                                                     |
| xml_etree_iterparse  | 115 ms                                                 | 99.2 ms: 1.16x faster                                                     |
| json_loads           | 31.2 us                                                | 30.4 us: 1.02x faster                                                     |
| Geometric mean       | (ref)                                                  | 1.30x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250501-linux-x86_64-nineteendo-speedup_json_encode-3.14.0a7+-930e938 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.2 ms: 1.11x faster                                                     |
| python_startup_no_site | 5.93 ms                                                | 6.93 ms: 1.17x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250501-linux-x86_64-nineteendo-speedup_json_encode-3.14.0a7+-930e938 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 21.2 ms: 1.50x faster                                                     |
| django_template | 48.2 ms                                                | 32.3 ms: 1.49x faster                                                     |
| mako            | 16.3 ms                                                | 11.6 ms: 1.40x faster                                                     |
| genshi_xml      | 66.0 ms                                                | 50.1 ms: 1.32x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                              |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250501-linux-x86_64-nineteendo-speedup_json_encode-3.14.0a7+-930e938 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 167 us: 3.26x faster                                                      |
| async_tree_io            | 1.77 sec                                               | 597 ms: 2.96x faster                                                      |
| async_tree_memoization   | 870 ms                                                 | 313 ms: 2.78x faster                                                      |
| async_tree_none          | 728 ms                                                 | 262 ms: 2.77x faster                                                      |
| generators               | 80.1 ms                                                | 30.5 ms: 2.62x faster                                                     |
| deltablue                | 7.91 ms                                                | 3.41 ms: 2.32x faster                                                     |
| mdp                      | 2.85 sec                                               | 1.24 sec: 2.30x faster                                                    |
| go                       | 240 ms                                                 | 114 ms: 2.11x faster                                                      |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 493 ms: 2.06x faster                                                      |
| deepcopy_memo            | 58.5 us                                                | 28.7 us: 2.04x faster                                                     |
| pylint                   | 551 ms                                                 | 281 ms: 1.96x faster                                                      |
| logging_silent           | 190 ns                                                 | 97.2 ns: 1.95x faster                                                     |
| chaos                    | 115 ms                                                 | 60.7 ms: 1.90x faster                                                     |
| richards_super           | 94.7 ms                                                | 49.9 ms: 1.90x faster                                                     |
| deepcopy                 | 479 us                                                 | 260 us: 1.85x faster                                                      |
| scimark_sor              | 220 ms                                                 | 120 ms: 1.83x faster                                                      |
| richards                 | 79.3 ms                                                | 43.4 ms: 1.83x faster                                                     |
| raytrace                 | 507 ms                                                 | 280 ms: 1.81x faster                                                      |
| scimark_monte_carlo      | 118 ms                                                 | 67.8 ms: 1.74x faster                                                     |
| crypto_pyaes             | 128 ms                                                 | 74.8 ms: 1.71x faster                                                     |
| comprehensions           | 28.8 us                                                | 17.0 us: 1.69x faster                                                     |
| float                    | 117 ms                                                 | 70.0 ms: 1.67x faster                                                     |
| hexiom                   | 10.4 ms                                                | 6.27 ms: 1.66x faster                                                     |
| spectral_norm            | 170 ms                                                 | 105 ms: 1.61x faster                                                      |
| pyflate                  | 716 ms                                                 | 453 ms: 1.58x faster                                                      |
| tomli_loads              | 3.14 sec                                               | 2.00 sec: 1.57x faster                                                    |
| nbody                    | 154 ms                                                 | 99.1 ms: 1.55x faster                                                     |
| scimark_lu               | 176 ms                                                 | 116 ms: 1.52x faster                                                      |
| unpickle_pure_python     | 331 us                                                 | 219 us: 1.51x faster                                                      |
| pickle_pure_python       | 484 us                                                 | 321 us: 1.51x faster                                                      |
| genshi_text              | 31.8 ms                                                | 21.2 ms: 1.50x faster                                                     |
| deepcopy_reduce          | 4.17 us                                                | 2.79 us: 1.50x faster                                                     |
| django_template          | 48.2 ms                                                | 32.3 ms: 1.49x faster                                                     |
| logging_simple           | 8.30 us                                                | 5.62 us: 1.48x faster                                                     |
| regex_compile            | 188 ms                                                 | 128 ms: 1.48x faster                                                      |
| logging_format           | 9.09 us                                                | 6.28 us: 1.45x faster                                                     |
| html5lib                 | 88.9 ms                                                | 61.4 ms: 1.45x faster                                                     |
| pprint_pformat           | 2.10 sec                                               | 1.49 sec: 1.41x faster                                                    |
| coroutines               | 35.1 ms                                                | 24.9 ms: 1.41x faster                                                     |
| mako                     | 16.3 ms                                                | 11.6 ms: 1.40x faster                                                     |
| pprint_safe_repr         | 1.02 sec                                               | 730 ms: 1.40x faster                                                      |
| dulwich_log              | 84.3 ms                                                | 60.6 ms: 1.39x faster                                                     |
| pycparser                | 1.58 sec                                               | 1.14 sec: 1.38x faster                                                    |
| 2to3                     | 348 ms                                                 | 256 ms: 1.36x faster                                                      |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.2 ms: 1.36x faster                                                     |
| json_dumps               | 14.2 ms                                                | 10.5 ms: 1.35x faster                                                     |
| sympy_integrate          | 25.8 ms                                                | 19.1 ms: 1.35x faster                                                     |
| xml_etree_process        | 79.1 ms                                                | 59.9 ms: 1.32x faster                                                     |
| sympy_sum                | 196 ms                                                 | 149 ms: 1.32x faster                                                      |
| genshi_xml               | 66.0 ms                                                | 50.1 ms: 1.32x faster                                                     |
| nqueens                  | 106 ms                                                 | 81.9 ms: 1.29x faster                                                     |
| sqlalchemy_declarative   | 172 ms                                                 | 133 ms: 1.29x faster                                                      |
| sympy_str                | 346 ms                                                 | 268 ms: 1.29x faster                                                      |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.12 ms: 1.26x faster                                                     |
| fannkuch                 | 532 ms                                                 | 421 ms: 1.26x faster                                                      |
| docutils                 | 3.30 sec                                               | 2.62 sec: 1.26x faster                                                    |
| scimark_fft              | 466 ms                                                 | 371 ms: 1.25x faster                                                      |
| sympy_expand             | 566 ms                                                 | 459 ms: 1.23x faster                                                      |
| regex_v8                 | 27.8 ms                                                | 23.3 ms: 1.19x faster                                                     |
| pathlib                  | 20.5 ms                                                | 17.3 ms: 1.18x faster                                                     |
| xml_etree_parse          | 168 ms                                                 | 143 ms: 1.18x faster                                                      |
| xml_etree_generate       | 99.4 ms                                                | 85.4 ms: 1.16x faster                                                     |
| xml_etree_iterparse      | 115 ms                                                 | 99.2 ms: 1.16x faster                                                     |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                      |
| python_startup           | 14.6 ms                                                | 13.2 ms: 1.11x faster                                                     |
| bench_thread_pool        | 986 us                                                 | 892 us: 1.11x faster                                                      |
| regex_dna                | 227 ms                                                 | 205 ms: 1.10x faster                                                      |
| regex_effbot             | 3.63 ms                                                | 3.31 ms: 1.10x faster                                                     |
| async_generators         | 444 ms                                                 | 411 ms: 1.08x faster                                                      |
| sqlite_synth             | 3.02 us                                                | 2.85 us: 1.06x faster                                                     |
| json                     | 5.69 ms                                                | 5.50 ms: 1.03x faster                                                     |
| json_loads               | 31.2 us                                                | 30.4 us: 1.02x faster                                                     |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                      |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                      |
| telco                    | 7.27 ms                                                | 8.01 ms: 1.10x slower                                                     |
| coverage                 | 79.4 ms                                                | 92.0 ms: 1.16x slower                                                     |
| python_startup_no_site   | 5.93 ms                                                | 6.93 ms: 1.17x slower                                                     |
| gc_traversal             | 3.62 ms                                                | 4.81 ms: 1.33x slower                                                     |
| create_gc_cycles         | 1.62 ms                                                | 2.47 ms: 1.53x slower                                                     |
| bench_mp_pool            | 24.0 ms                                                | 83.1 ms: 3.46x slower                                                     |
| Geometric mean           | (ref)                                                  | 1.41x faster                                                              |
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (23) of results/bm-20250501-3.14.0a7+-930e938/bm-20250501-linux-x86_64-nineteendo-speedup_json_encode-3.14.0a7+-930e938.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.442x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.35x
- 95% likely to have a speedup of 1.34x
- 99% likely to have a speedup of 1.31x

# Memory
- memory change: 1.28x