# Results vs. 3.10.4

- fork: eendebakpt
- ref: list_freelist_plus
- machine: linux-x86_64
- commit hash: 77f3e29
- commit date: 2025-04-08
- overall geometric mean: 1.474x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.35x faster
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250408-linux-x86_64-eendebakpt-list_freelist_plus-3.14.0a7+-77f3e29 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 252 ms: 1.38x faster                                                     |
| docutils       | 3.30 sec                                               | 2.59 sec: 1.27x faster                                                   |
| html5lib       | 88.9 ms                                                | 62.0 ms: 1.43x faster                                                    |
| Geometric mean | (ref)                                                  | 1.36x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250408-linux-x86_64-eendebakpt-list_freelist_plus-3.14.0a7+-77f3e29 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 608 ms: 2.91x faster                                                     |
| async_tree_none         | 728 ms                                                 | 255 ms: 2.85x faster                                                     |
| async_tree_memoization  | 870 ms                                                 | 310 ms: 2.81x faster                                                     |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 481 ms: 2.11x faster                                                     |
| Geometric mean          | (ref)                                                  | 2.65x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250408-linux-x86_64-eendebakpt-list_freelist_plus-3.14.0a7+-77f3e29 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 68.3 ms: 1.71x faster                                                    |
| nbody          | 154 ms                                                 | 95.5 ms: 1.61x faster                                                    |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                     |
| Geometric mean | (ref)                                                  | 1.41x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250408-linux-x86_64-eendebakpt-list_freelist_plus-3.14.0a7+-77f3e29 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 125 ms: 1.51x faster                                                     |
| regex_v8       | 27.8 ms                                                | 22.8 ms: 1.22x faster                                                    |
| regex_effbot   | 3.63 ms                                                | 3.10 ms: 1.17x faster                                                    |
| regex_dna      | 227 ms                                                 | 204 ms: 1.11x faster                                                     |
| Geometric mean | (ref)                                                  | 1.24x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250408-linux-x86_64-eendebakpt-list_freelist_plus-3.14.0a7+-77f3e29 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.94 sec: 1.62x faster                                                   |
| pickle_pure_python   | 484 us                                                 | 312 us: 1.55x faster                                                     |
| unpickle_pure_python | 331 us                                                 | 217 us: 1.53x faster                                                     |
| xml_etree_process    | 79.1 ms                                                | 59.9 ms: 1.32x faster                                                    |
| json_dumps           | 14.2 ms                                                | 11.6 ms: 1.22x faster                                                    |
| xml_etree_parse      | 168 ms                                                 | 143 ms: 1.17x faster                                                     |
| xml_etree_generate   | 99.4 ms                                                | 85.1 ms: 1.17x faster                                                    |
| xml_etree_iterparse  | 115 ms                                                 | 99.3 ms: 1.16x faster                                                    |
| json_loads           | 31.2 us                                                | 29.2 us: 1.07x faster                                                    |
| Geometric mean       | (ref)                                                  | 1.30x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250408-linux-x86_64-eendebakpt-list_freelist_plus-3.14.0a7+-77f3e29 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.2 ms: 1.10x faster                                                    |
| python_startup_no_site | 5.93 ms                                                | 8.21 ms: 1.38x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250408-linux-x86_64-eendebakpt-list_freelist_plus-3.14.0a7+-77f3e29 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 31.4 ms: 1.53x faster                                                    |
| genshi_text     | 31.8 ms                                                | 20.9 ms: 1.53x faster                                                    |
| mako            | 16.3 ms                                                | 11.2 ms: 1.46x faster                                                    |
| genshi_xml      | 66.0 ms                                                | 49.0 ms: 1.35x faster                                                    |
| Geometric mean  | (ref)                                                  | 1.46x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250408-linux-x86_64-eendebakpt-list_freelist_plus-3.14.0a7+-77f3e29 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 166 us: 3.29x faster                                                     |
| async_tree_io            | 1.77 sec                                               | 608 ms: 2.91x faster                                                     |
| async_tree_none          | 728 ms                                                 | 255 ms: 2.85x faster                                                     |
| async_tree_memoization   | 870 ms                                                 | 310 ms: 2.81x faster                                                     |
| generators               | 80.1 ms                                                | 29.5 ms: 2.72x faster                                                    |
| deltablue                | 7.91 ms                                                | 3.36 ms: 2.35x faster                                                    |
| mdp                      | 2.85 sec                                               | 1.21 sec: 2.35x faster                                                   |
| go                       | 240 ms                                                 | 112 ms: 2.15x faster                                                     |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 481 ms: 2.11x faster                                                     |
| chaos                    | 115 ms                                                 | 54.6 ms: 2.11x faster                                                    |
| deepcopy_memo            | 58.5 us                                                | 28.8 us: 2.03x faster                                                    |
| pylint                   | 551 ms                                                 | 277 ms: 1.99x faster                                                     |
| raytrace                 | 507 ms                                                 | 257 ms: 1.97x faster                                                     |
| logging_silent           | 190 ns                                                 | 98.2 ns: 1.93x faster                                                    |
| richards_super           | 94.7 ms                                                | 49.4 ms: 1.92x faster                                                    |
| deepcopy                 | 479 us                                                 | 251 us: 1.91x faster                                                     |
| scimark_sor              | 220 ms                                                 | 119 ms: 1.85x faster                                                     |
| richards                 | 79.3 ms                                                | 43.1 ms: 1.84x faster                                                    |
| crypto_pyaes             | 128 ms                                                 | 69.9 ms: 1.83x faster                                                    |
| scimark_monte_carlo      | 118 ms                                                 | 65.3 ms: 1.81x faster                                                    |
| hexiom                   | 10.4 ms                                                | 5.99 ms: 1.74x faster                                                    |
| float                    | 117 ms                                                 | 68.3 ms: 1.71x faster                                                    |
| comprehensions           | 28.8 us                                                | 16.8 us: 1.71x faster                                                    |
| spectral_norm            | 170 ms                                                 | 100.0 ms: 1.70x faster                                                   |
| tomli_loads              | 3.14 sec                                               | 1.94 sec: 1.62x faster                                                   |
| nbody                    | 154 ms                                                 | 95.5 ms: 1.61x faster                                                    |
| pyflate                  | 716 ms                                                 | 446 ms: 1.61x faster                                                     |
| deepcopy_reduce          | 4.17 us                                                | 2.60 us: 1.61x faster                                                    |
| pickle_pure_python       | 484 us                                                 | 312 us: 1.55x faster                                                     |
| django_template          | 48.2 ms                                                | 31.4 ms: 1.53x faster                                                    |
| unpickle_pure_python     | 331 us                                                 | 217 us: 1.53x faster                                                     |
| scimark_lu               | 176 ms                                                 | 115 ms: 1.53x faster                                                     |
| genshi_text              | 31.8 ms                                                | 20.9 ms: 1.53x faster                                                    |
| regex_compile            | 188 ms                                                 | 125 ms: 1.51x faster                                                     |
| logging_format           | 9.09 us                                                | 6.04 us: 1.50x faster                                                    |
| coroutines               | 35.1 ms                                                | 23.3 ms: 1.50x faster                                                    |
| logging_simple           | 8.30 us                                                | 5.55 us: 1.50x faster                                                    |
| mako                     | 16.3 ms                                                | 11.2 ms: 1.46x faster                                                    |
| html5lib                 | 88.9 ms                                                | 62.0 ms: 1.43x faster                                                    |
| pycparser                | 1.58 sec                                               | 1.10 sec: 1.43x faster                                                   |
| dulwich_log              | 84.3 ms                                                | 59.3 ms: 1.42x faster                                                    |
| pprint_pformat           | 2.10 sec                                               | 1.49 sec: 1.41x faster                                                   |
| pprint_safe_repr         | 1.02 sec                                               | 725 ms: 1.40x faster                                                     |
| fannkuch                 | 532 ms                                                 | 381 ms: 1.40x faster                                                     |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.9 ms: 1.38x faster                                                    |
| 2to3                     | 348 ms                                                 | 252 ms: 1.38x faster                                                     |
| nqueens                  | 106 ms                                                 | 77.7 ms: 1.36x faster                                                    |
| scimark_fft              | 466 ms                                                 | 344 ms: 1.35x faster                                                     |
| genshi_xml               | 66.0 ms                                                | 49.0 ms: 1.35x faster                                                    |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.80 ms: 1.35x faster                                                    |
| sympy_integrate          | 25.8 ms                                                | 19.2 ms: 1.35x faster                                                    |
| sympy_sum                | 196 ms                                                 | 148 ms: 1.32x faster                                                     |
| xml_etree_process        | 79.1 ms                                                | 59.9 ms: 1.32x faster                                                    |
| sqlalchemy_declarative   | 172 ms                                                 | 132 ms: 1.30x faster                                                     |
| sympy_str                | 346 ms                                                 | 268 ms: 1.29x faster                                                     |
| docutils                 | 3.30 sec                                               | 2.59 sec: 1.27x faster                                                   |
| sympy_expand             | 566 ms                                                 | 455 ms: 1.24x faster                                                     |
| pathlib                  | 20.5 ms                                                | 16.6 ms: 1.23x faster                                                    |
| json_dumps               | 14.2 ms                                                | 11.6 ms: 1.22x faster                                                    |
| regex_v8                 | 27.8 ms                                                | 22.8 ms: 1.22x faster                                                    |
| xml_etree_parse          | 168 ms                                                 | 143 ms: 1.17x faster                                                     |
| regex_effbot             | 3.63 ms                                                | 3.10 ms: 1.17x faster                                                    |
| xml_etree_generate       | 99.4 ms                                                | 85.1 ms: 1.17x faster                                                    |
| xml_etree_iterparse      | 115 ms                                                 | 99.3 ms: 1.16x faster                                                    |
| async_generators         | 444 ms                                                 | 388 ms: 1.14x faster                                                     |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                     |
| bench_thread_pool        | 986 us                                                 | 878 us: 1.12x faster                                                     |
| regex_dna                | 227 ms                                                 | 204 ms: 1.11x faster                                                     |
| python_startup           | 14.6 ms                                                | 13.2 ms: 1.10x faster                                                    |
| json                     | 5.69 ms                                                | 5.21 ms: 1.09x faster                                                    |
| sqlite_synth             | 3.02 us                                                | 2.79 us: 1.09x faster                                                    |
| json_loads               | 31.2 us                                                | 29.2 us: 1.07x faster                                                    |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                     |
| asyncio_websockets       | 559 ms                                                 | 553 ms: 1.01x faster                                                     |
| telco                    | 7.27 ms                                                | 7.70 ms: 1.06x slower                                                    |
| coverage                 | 79.4 ms                                                | 86.3 ms: 1.09x slower                                                    |
| gc_traversal             | 3.62 ms                                                | 4.64 ms: 1.28x slower                                                    |
| python_startup_no_site   | 5.93 ms                                                | 8.21 ms: 1.38x slower                                                    |
| create_gc_cycles         | 1.62 ms                                                | 2.45 ms: 1.51x slower                                                    |
| bench_mp_pool            | 24.0 ms                                                | 82.2 ms: 3.42x slower                                                    |
| Geometric mean           | (ref)                                                  | 1.45x faster                                                             |
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250408-3.14.0a7+-77f3e29/bm-20250408-linux-x86_64-eendebakpt-list_freelist_plus-3.14.0a7+-77f3e29.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.474x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.39x
- 95% likely to have a speedup of 1.38x
- 99% likely to have a speedup of 1.35x

# Memory
- memory change: 1.27x