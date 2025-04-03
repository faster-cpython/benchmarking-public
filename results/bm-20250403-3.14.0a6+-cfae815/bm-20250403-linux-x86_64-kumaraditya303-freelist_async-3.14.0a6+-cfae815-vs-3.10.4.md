# Results vs. 3.10.4

- fork: kumaraditya303
- ref: freelist_async
- machine: linux-x86_64
- commit hash: cfae815
- commit date: 2025-04-03
- overall geometric mean: 1.470x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.33x faster
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-linux-x86_64-kumaraditya303-freelist_async-3.14.0a6+-cfae815 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 247 ms: 1.41x faster                                                     |
| docutils       | 3.30 sec                                               | 2.59 sec: 1.27x faster                                                   |
| html5lib       | 88.9 ms                                                | 60.6 ms: 1.47x faster                                                    |
| Geometric mean | (ref)                                                  | 1.38x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-linux-x86_64-kumaraditya303-freelist_async-3.14.0a6+-cfae815 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 621 ms: 2.85x faster                                                     |
| async_tree_memoization  | 870 ms                                                 | 311 ms: 2.79x faster                                                     |
| async_tree_none         | 728 ms                                                 | 263 ms: 2.77x faster                                                     |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 485 ms: 2.09x faster                                                     |
| Geometric mean          | (ref)                                                  | 2.61x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-linux-x86_64-kumaraditya303-freelist_async-3.14.0a6+-cfae815 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 67.0 ms: 1.75x faster                                                    |
| nbody          | 154 ms                                                 | 90.1 ms: 1.70x faster                                                    |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                     |
| Geometric mean | (ref)                                                  | 1.45x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-linux-x86_64-kumaraditya303-freelist_async-3.14.0a6+-cfae815 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 123 ms: 1.53x faster                                                     |
| regex_v8       | 27.8 ms                                                | 23.1 ms: 1.20x faster                                                    |
| regex_effbot   | 3.63 ms                                                | 3.34 ms: 1.09x faster                                                    |
| regex_dna      | 227 ms                                                 | 219 ms: 1.04x faster                                                     |
| Geometric mean | (ref)                                                  | 1.20x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-linux-x86_64-kumaraditya303-freelist_async-3.14.0a6+-cfae815 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.90 sec: 1.65x faster                                                   |
| pickle_pure_python   | 484 us                                                 | 311 us: 1.56x faster                                                     |
| unpickle_pure_python | 331 us                                                 | 215 us: 1.54x faster                                                     |
| xml_etree_process    | 79.1 ms                                                | 58.5 ms: 1.35x faster                                                    |
| json_dumps           | 14.2 ms                                                | 11.5 ms: 1.23x faster                                                    |
| xml_etree_parse      | 168 ms                                                 | 140 ms: 1.20x faster                                                     |
| xml_etree_generate   | 99.4 ms                                                | 84.1 ms: 1.18x faster                                                    |
| xml_etree_iterparse  | 115 ms                                                 | 98.5 ms: 1.17x faster                                                    |
| json_loads           | 31.2 us                                                | 30.0 us: 1.04x faster                                                    |
| Geometric mean       | (ref)                                                  | 1.31x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-linux-x86_64-kumaraditya303-freelist_async-3.14.0a6+-cfae815 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.1 ms: 1.11x faster                                                    |
| python_startup_no_site | 5.93 ms                                                | 8.17 ms: 1.38x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-linux-x86_64-kumaraditya303-freelist_async-3.14.0a6+-cfae815 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 21.4 ms: 1.49x faster                                                    |
| django_template | 48.2 ms                                                | 32.4 ms: 1.49x faster                                                    |
| mako            | 16.3 ms                                                | 11.3 ms: 1.45x faster                                                    |
| genshi_xml      | 66.0 ms                                                | 49.5 ms: 1.33x faster                                                    |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-linux-x86_64-kumaraditya303-freelist_async-3.14.0a6+-cfae815 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 165 us: 3.29x faster                                                     |
| async_tree_io            | 1.77 sec                                               | 621 ms: 2.85x faster                                                     |
| async_tree_memoization   | 870 ms                                                 | 311 ms: 2.79x faster                                                     |
| generators               | 80.1 ms                                                | 28.7 ms: 2.79x faster                                                    |
| async_tree_none          | 728 ms                                                 | 263 ms: 2.77x faster                                                     |
| deltablue                | 7.91 ms                                                | 3.24 ms: 2.44x faster                                                    |
| mdp                      | 2.85 sec                                               | 1.22 sec: 2.33x faster                                                   |
| go                       | 240 ms                                                 | 108 ms: 2.22x faster                                                     |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 485 ms: 2.09x faster                                                     |
| logging_silent           | 190 ns                                                 | 92.2 ns: 2.06x faster                                                    |
| chaos                    | 115 ms                                                 | 56.2 ms: 2.05x faster                                                    |
| deepcopy_memo            | 58.5 us                                                | 28.9 us: 2.03x faster                                                    |
| raytrace                 | 507 ms                                                 | 254 ms: 1.99x faster                                                     |
| pylint                   | 551 ms                                                 | 277 ms: 1.99x faster                                                     |
| richards_super           | 94.7 ms                                                | 48.3 ms: 1.96x faster                                                    |
| deepcopy                 | 479 us                                                 | 252 us: 1.90x faster                                                     |
| scimark_sor              | 220 ms                                                 | 115 ms: 1.90x faster                                                     |
| richards                 | 79.3 ms                                                | 42.3 ms: 1.88x faster                                                    |
| scimark_monte_carlo      | 118 ms                                                 | 63.9 ms: 1.85x faster                                                    |
| crypto_pyaes             | 128 ms                                                 | 73.1 ms: 1.75x faster                                                    |
| float                    | 117 ms                                                 | 67.0 ms: 1.75x faster                                                    |
| comprehensions           | 28.8 us                                                | 16.6 us: 1.73x faster                                                    |
| nbody                    | 154 ms                                                 | 90.1 ms: 1.70x faster                                                    |
| hexiom                   | 10.4 ms                                                | 6.19 ms: 1.68x faster                                                    |
| tomli_loads              | 3.14 sec                                               | 1.90 sec: 1.65x faster                                                   |
| pyflate                  | 716 ms                                                 | 435 ms: 1.65x faster                                                     |
| spectral_norm            | 170 ms                                                 | 104 ms: 1.63x faster                                                     |
| pickle_pure_python       | 484 us                                                 | 311 us: 1.56x faster                                                     |
| deepcopy_reduce          | 4.17 us                                                | 2.69 us: 1.55x faster                                                    |
| unpickle_pure_python     | 331 us                                                 | 215 us: 1.54x faster                                                     |
| regex_compile            | 188 ms                                                 | 123 ms: 1.53x faster                                                     |
| scimark_lu               | 176 ms                                                 | 116 ms: 1.52x faster                                                     |
| logging_simple           | 8.30 us                                                | 5.50 us: 1.51x faster                                                    |
| logging_format           | 9.09 us                                                | 6.08 us: 1.49x faster                                                    |
| genshi_text              | 31.8 ms                                                | 21.4 ms: 1.49x faster                                                    |
| django_template          | 48.2 ms                                                | 32.4 ms: 1.49x faster                                                    |
| coroutines               | 35.1 ms                                                | 23.8 ms: 1.48x faster                                                    |
| html5lib                 | 88.9 ms                                                | 60.6 ms: 1.47x faster                                                    |
| pprint_pformat           | 2.10 sec                                               | 1.45 sec: 1.45x faster                                                   |
| mako                     | 16.3 ms                                                | 11.3 ms: 1.45x faster                                                    |
| dulwich_log              | 84.3 ms                                                | 59.0 ms: 1.43x faster                                                    |
| pprint_safe_repr         | 1.02 sec                                               | 713 ms: 1.43x faster                                                     |
| 2to3                     | 348 ms                                                 | 247 ms: 1.41x faster                                                     |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.70 ms: 1.38x faster                                                    |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.0 ms: 1.37x faster                                                    |
| scimark_fft              | 466 ms                                                 | 340 ms: 1.37x faster                                                     |
| pycparser                | 1.58 sec                                               | 1.16 sec: 1.36x faster                                                   |
| xml_etree_process        | 79.1 ms                                                | 58.5 ms: 1.35x faster                                                    |
| sympy_integrate          | 25.8 ms                                                | 19.1 ms: 1.35x faster                                                    |
| genshi_xml               | 66.0 ms                                                | 49.5 ms: 1.33x faster                                                    |
| sympy_sum                | 196 ms                                                 | 150 ms: 1.31x faster                                                     |
| nqueens                  | 106 ms                                                 | 80.7 ms: 1.31x faster                                                    |
| sqlalchemy_declarative   | 172 ms                                                 | 132 ms: 1.31x faster                                                     |
| sympy_str                | 346 ms                                                 | 267 ms: 1.29x faster                                                     |
| fannkuch                 | 532 ms                                                 | 412 ms: 1.29x faster                                                     |
| docutils                 | 3.30 sec                                               | 2.59 sec: 1.27x faster                                                   |
| sympy_expand             | 566 ms                                                 | 457 ms: 1.24x faster                                                     |
| json_dumps               | 14.2 ms                                                | 11.5 ms: 1.23x faster                                                    |
| pathlib                  | 20.5 ms                                                | 16.7 ms: 1.22x faster                                                    |
| regex_v8                 | 27.8 ms                                                | 23.1 ms: 1.20x faster                                                    |
| xml_etree_parse          | 168 ms                                                 | 140 ms: 1.20x faster                                                     |
| xml_etree_generate       | 99.4 ms                                                | 84.1 ms: 1.18x faster                                                    |
| xml_etree_iterparse      | 115 ms                                                 | 98.5 ms: 1.17x faster                                                    |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                     |
| bench_thread_pool        | 986 us                                                 | 875 us: 1.13x faster                                                     |
| async_generators         | 444 ms                                                 | 394 ms: 1.13x faster                                                     |
| python_startup           | 14.6 ms                                                | 13.1 ms: 1.11x faster                                                    |
| regex_effbot             | 3.63 ms                                                | 3.34 ms: 1.09x faster                                                    |
| sqlite_synth             | 3.02 us                                                | 2.78 us: 1.09x faster                                                    |
| json                     | 5.69 ms                                                | 5.29 ms: 1.08x faster                                                    |
| json_loads               | 31.2 us                                                | 30.0 us: 1.04x faster                                                    |
| regex_dna                | 227 ms                                                 | 219 ms: 1.04x faster                                                     |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                     |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                                     |
| telco                    | 7.27 ms                                                | 7.79 ms: 1.07x slower                                                    |
| coverage                 | 79.4 ms                                                | 85.5 ms: 1.08x slower                                                    |
| gc_traversal             | 3.62 ms                                                | 4.95 ms: 1.37x slower                                                    |
| python_startup_no_site   | 5.93 ms                                                | 8.17 ms: 1.38x slower                                                    |
| create_gc_cycles         | 1.62 ms                                                | 2.45 ms: 1.51x slower                                                    |
| bench_mp_pool            | 24.0 ms                                                | 82.1 ms: 3.42x slower                                                    |
| Geometric mean           | (ref)                                                  | 1.44x faster                                                             |
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250403-3.14.0a6+-cfae815/bm-20250403-linux-x86_64-kumaraditya303-freelist_async-3.14.0a6+-cfae815.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.470x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.37x
- 95% likely to have a speedup of 1.36x
- 99% likely to have a speedup of 1.33x

# Memory
- memory change: 1.27x