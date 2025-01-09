# Results vs. 3.10.4

- fork: kumaraditya303
- ref: fast_coro
- machine: linux-x86_64
- commit hash: e4984ea
- commit date: 2025-01-09
- overall geometric mean: 1.443x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.32x faster
- Memory change: 1.26x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250109-linux-x86_64-kumaraditya303-fast_coro-3.14.0a3+-e4984ea |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 254 ms: 1.37x faster                                                |
| docutils       | 3.30 sec                                               | 2.60 sec: 1.27x faster                                              |
| html5lib       | 88.9 ms                                                | 61.0 ms: 1.46x faster                                               |
| Geometric mean | (ref)                                                  | 1.36x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250109-linux-x86_64-kumaraditya303-fast_coro-3.14.0a3+-e4984ea |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 604 ms: 2.93x faster                                                |
| async_tree_none         | 728 ms                                                 | 261 ms: 2.79x faster                                                |
| async_tree_memoization  | 870 ms                                                 | 326 ms: 2.67x faster                                                |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 492 ms: 2.06x faster                                                |
| Geometric mean          | (ref)                                                  | 2.59x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250109-linux-x86_64-kumaraditya303-fast_coro-3.14.0a3+-e4984ea |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 94.0 ms: 1.63x faster                                               |
| float          | 117 ms                                                 | 72.6 ms: 1.61x faster                                               |
| pidigits       | 191 ms                                                 | 190 ms: 1.01x faster                                                |
| Geometric mean | (ref)                                                  | 1.38x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250109-linux-x86_64-kumaraditya303-fast_coro-3.14.0a3+-e4984ea |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 127 ms: 1.48x faster                                                |
| regex_v8       | 27.8 ms                                                | 25.5 ms: 1.09x faster                                               |
| regex_effbot   | 3.63 ms                                                | 3.34 ms: 1.09x faster                                               |
| regex_dna      | 227 ms                                                 | 211 ms: 1.07x faster                                                |
| Geometric mean | (ref)                                                  | 1.17x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250109-linux-x86_64-kumaraditya303-fast_coro-3.14.0a3+-e4984ea |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.99 sec: 1.58x faster                                              |
| unpickle_pure_python | 331 us                                                 | 216 us: 1.53x faster                                                |
| pickle_pure_python   | 484 us                                                 | 322 us: 1.51x faster                                                |
| xml_etree_process    | 79.1 ms                                                | 59.3 ms: 1.34x faster                                               |
| json_dumps           | 14.2 ms                                                | 11.6 ms: 1.23x faster                                               |
| xml_etree_parse      | 168 ms                                                 | 139 ms: 1.21x faster                                                |
| xml_etree_iterparse  | 115 ms                                                 | 96.5 ms: 1.20x faster                                               |
| json_loads           | 31.2 us                                                | 26.6 us: 1.17x faster                                               |
| xml_etree_generate   | 99.4 ms                                                | 85.0 ms: 1.17x faster                                               |
| Geometric mean       | (ref)                                                  | 1.32x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250109-linux-x86_64-kumaraditya303-fast_coro-3.14.0a3+-e4984ea |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.8 ms: 1.14x faster                                               |
| python_startup_no_site | 5.93 ms                                                | 7.06 ms: 1.19x slower                                               |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250109-linux-x86_64-kumaraditya303-fast_coro-3.14.0a3+-e4984ea |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 31.6 ms: 1.52x faster                                               |
| genshi_text     | 31.8 ms                                                | 22.5 ms: 1.41x faster                                               |
| mako            | 16.3 ms                                                | 11.6 ms: 1.40x faster                                               |
| genshi_xml      | 66.0 ms                                                | 49.7 ms: 1.33x faster                                               |
| Geometric mean  | (ref)                                                  | 1.42x faster                                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250109-linux-x86_64-kumaraditya303-fast_coro-3.14.0a3+-e4984ea |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 162 us: 3.35x faster                                                |
| generators               | 80.1 ms                                                | 27.1 ms: 2.95x faster                                               |
| async_tree_io            | 1.77 sec                                               | 604 ms: 2.93x faster                                                |
| async_tree_none          | 728 ms                                                 | 261 ms: 2.79x faster                                                |
| async_tree_memoization   | 870 ms                                                 | 326 ms: 2.67x faster                                                |
| deltablue                | 7.91 ms                                                | 3.25 ms: 2.43x faster                                               |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 492 ms: 2.06x faster                                                |
| go                       | 240 ms                                                 | 116 ms: 2.06x faster                                                |
| pylint                   | 551 ms                                                 | 276 ms: 2.00x faster                                                |
| deepcopy_memo            | 58.5 us                                                | 30.6 us: 1.91x faster                                               |
| chaos                    | 115 ms                                                 | 61.0 ms: 1.89x faster                                               |
| richards_super           | 94.7 ms                                                | 50.1 ms: 1.89x faster                                               |
| raytrace                 | 507 ms                                                 | 273 ms: 1.86x faster                                                |
| deepcopy                 | 479 us                                                 | 261 us: 1.84x faster                                                |
| scimark_sor              | 220 ms                                                 | 122 ms: 1.80x faster                                                |
| richards                 | 79.3 ms                                                | 44.3 ms: 1.79x faster                                               |
| logging_silent           | 190 ns                                                 | 106 ns: 1.79x faster                                                |
| crypto_pyaes             | 128 ms                                                 | 71.9 ms: 1.78x faster                                               |
| scimark_monte_carlo      | 118 ms                                                 | 67.6 ms: 1.75x faster                                               |
| comprehensions           | 28.8 us                                                | 16.7 us: 1.73x faster                                               |
| sqlglot_parse            | 2.17 ms                                                | 1.27 ms: 1.70x faster                                               |
| hexiom                   | 10.4 ms                                                | 6.22 ms: 1.67x faster                                               |
| nbody                    | 154 ms                                                 | 94.0 ms: 1.63x faster                                               |
| sqlglot_transpile        | 2.57 ms                                                | 1.58 ms: 1.63x faster                                               |
| float                    | 117 ms                                                 | 72.6 ms: 1.61x faster                                               |
| spectral_norm            | 170 ms                                                 | 106 ms: 1.60x faster                                                |
| tomli_loads              | 3.14 sec                                               | 1.99 sec: 1.58x faster                                              |
| pyflate                  | 716 ms                                                 | 455 ms: 1.57x faster                                                |
| deepcopy_reduce          | 4.17 us                                                | 2.71 us: 1.54x faster                                               |
| scimark_lu               | 176 ms                                                 | 115 ms: 1.53x faster                                                |
| unpickle_pure_python     | 331 us                                                 | 216 us: 1.53x faster                                                |
| django_template          | 48.2 ms                                                | 31.6 ms: 1.52x faster                                               |
| coroutines               | 35.1 ms                                                | 23.1 ms: 1.52x faster                                               |
| pickle_pure_python       | 484 us                                                 | 322 us: 1.51x faster                                                |
| regex_compile            | 188 ms                                                 | 127 ms: 1.48x faster                                                |
| logging_simple           | 8.30 us                                                | 5.62 us: 1.48x faster                                               |
| logging_format           | 9.09 us                                                | 6.20 us: 1.47x faster                                               |
| html5lib                 | 88.9 ms                                                | 61.0 ms: 1.46x faster                                               |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.5 ms: 1.41x faster                                               |
| genshi_text              | 31.8 ms                                                | 22.5 ms: 1.41x faster                                               |
| pprint_pformat           | 2.10 sec                                               | 1.49 sec: 1.41x faster                                              |
| mako                     | 16.3 ms                                                | 11.6 ms: 1.40x faster                                               |
| thrift                   | 1.07 ms                                                | 767 us: 1.40x faster                                                |
| pprint_safe_repr         | 1.02 sec                                               | 732 ms: 1.39x faster                                                |
| sqlglot_normalize        | 143 ms                                                 | 103 ms: 1.39x faster                                                |
| 2to3                     | 348 ms                                                 | 254 ms: 1.37x faster                                                |
| pycparser                | 1.58 sec                                               | 1.17 sec: 1.35x faster                                              |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.80 ms: 1.35x faster                                               |
| nqueens                  | 106 ms                                                 | 79.0 ms: 1.34x faster                                               |
| fannkuch                 | 532 ms                                                 | 397 ms: 1.34x faster                                                |
| xml_etree_process        | 79.1 ms                                                | 59.3 ms: 1.34x faster                                               |
| sqlalchemy_declarative   | 172 ms                                                 | 129 ms: 1.33x faster                                                |
| sympy_sum                | 196 ms                                                 | 148 ms: 1.33x faster                                                |
| genshi_xml               | 66.0 ms                                                | 49.7 ms: 1.33x faster                                               |
| sqlglot_optimize         | 69.2 ms                                                | 52.2 ms: 1.33x faster                                               |
| dulwich_log              | 84.3 ms                                                | 63.8 ms: 1.32x faster                                               |
| scimark_fft              | 466 ms                                                 | 354 ms: 1.32x faster                                                |
| sympy_integrate          | 25.8 ms                                                | 19.7 ms: 1.31x faster                                               |
| sympy_str                | 346 ms                                                 | 268 ms: 1.29x faster                                                |
| docutils                 | 3.30 sec                                               | 2.60 sec: 1.27x faster                                              |
| pathlib                  | 20.5 ms                                                | 16.3 ms: 1.26x faster                                               |
| sympy_expand             | 566 ms                                                 | 455 ms: 1.24x faster                                                |
| json_dumps               | 14.2 ms                                                | 11.6 ms: 1.23x faster                                               |
| xml_etree_parse          | 168 ms                                                 | 139 ms: 1.21x faster                                                |
| xml_etree_iterparse      | 115 ms                                                 | 96.5 ms: 1.20x faster                                               |
| json_loads               | 31.2 us                                                | 26.6 us: 1.17x faster                                               |
| xml_etree_generate       | 99.4 ms                                                | 85.0 ms: 1.17x faster                                               |
| json                     | 5.69 ms                                                | 4.95 ms: 1.15x faster                                               |
| bench_thread_pool        | 986 us                                                 | 863 us: 1.14x faster                                                |
| python_startup           | 14.6 ms                                                | 12.8 ms: 1.14x faster                                               |
| mdp                      | 2.85 sec                                               | 2.53 sec: 1.13x faster                                              |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                |
| regex_v8                 | 27.8 ms                                                | 25.5 ms: 1.09x faster                                               |
| regex_effbot             | 3.63 ms                                                | 3.34 ms: 1.09x faster                                               |
| regex_dna                | 227 ms                                                 | 211 ms: 1.07x faster                                                |
| sqlite_synth             | 3.02 us                                                | 2.84 us: 1.06x faster                                               |
| async_generators         | 444 ms                                                 | 424 ms: 1.05x faster                                                |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                                |
| pidigits                 | 191 ms                                                 | 190 ms: 1.01x faster                                                |
| coverage                 | 79.4 ms                                                | 84.4 ms: 1.06x slower                                               |
| telco                    | 7.27 ms                                                | 7.87 ms: 1.08x slower                                               |
| python_startup_no_site   | 5.93 ms                                                | 7.06 ms: 1.19x slower                                               |
| gc_traversal             | 3.62 ms                                                | 5.02 ms: 1.38x slower                                               |
| create_gc_cycles         | 1.62 ms                                                | 2.46 ms: 1.52x slower                                               |
| bench_mp_pool            | 24.0 ms                                                | 81.6 ms: 3.40x slower                                               |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                        |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250109-3.14.0a3+-e4984ea/bm-20250109-linux-x86_64-kumaraditya303-fast_coro-3.14.0a3+-e4984ea.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.443x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.33x
- 99% likely to have a speedup of 1.32x

# Memory
- memory change: 1.26x