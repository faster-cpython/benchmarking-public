# Results vs. 3.10.4

- fork: kumaraditya303
- ref: fast_asyncio
- machine: linux-x86_64
- commit hash: f7b3d94
- commit date: 2025-03-13
- overall geometric mean: 1.294x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x slower
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250313-linux-x86_64-kumaraditya303-fast_asyncio-3.14.0a5+-f7b3d94 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 522 ms: 1.50x slower                                                   |
| docutils       | 3.30 sec                                               | 5.25 sec: 1.59x slower                                                 |
| html5lib       | 88.9 ms                                                | 123 ms: 1.39x slower                                                   |
| Geometric mean | (ref)                                                  | 1.49x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250313-linux-x86_64-kumaraditya303-fast_asyncio-3.14.0a5+-f7b3d94 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 1.21 sec: 1.46x faster                                                 |
| async_tree_none         | 728 ms                                                 | 515 ms: 1.41x faster                                                   |
| async_tree_memoization  | 870 ms                                                 | 646 ms: 1.35x faster                                                   |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 1.00 sec: 1.01x faster                                                 |
| Geometric mean          | (ref)                                                  | 1.29x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250313-linux-x86_64-kumaraditya303-fast_asyncio-3.14.0a5+-f7b3d94 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 117 ms                                                 | 144 ms: 1.23x slower                                                   |
| nbody          | 154 ms                                                 | 203 ms: 1.32x slower                                                   |
| pidigits       | 191 ms                                                 | 372 ms: 1.95x slower                                                   |
| Geometric mean | (ref)                                                  | 1.47x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250313-linux-x86_64-kumaraditya303-fast_asyncio-3.14.0a5+-f7b3d94 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 256 ms: 1.36x slower                                                   |
| regex_v8       | 27.8 ms                                                | 46.5 ms: 1.68x slower                                                  |
| regex_effbot   | 3.63 ms                                                | 6.83 ms: 1.88x slower                                                  |
| regex_dna      | 227 ms                                                 | 427 ms: 1.88x slower                                                   |
| Geometric mean | (ref)                                                  | 1.68x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250313-linux-x86_64-kumaraditya303-fast_asyncio-3.14.0a5+-f7b3d94 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 3.88 sec: 1.23x slower                                                 |
| pickle_pure_python   | 484 us                                                 | 640 us: 1.32x slower                                                   |
| unpickle_pure_python | 331 us                                                 | 444 us: 1.34x slower                                                   |
| xml_etree_process    | 79.1 ms                                                | 119 ms: 1.50x slower                                                   |
| json_dumps           | 14.2 ms                                                | 22.8 ms: 1.61x slower                                                  |
| xml_etree_iterparse  | 115 ms                                                 | 189 ms: 1.64x slower                                                   |
| xml_etree_parse      | 168 ms                                                 | 287 ms: 1.71x slower                                                   |
| xml_etree_generate   | 99.4 ms                                                | 171 ms: 1.72x slower                                                   |
| json_loads           | 31.2 us                                                | 59.5 us: 1.91x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.54x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250313-linux-x86_64-kumaraditya303-fast_asyncio-3.14.0a5+-f7b3d94 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 31.0 ms: 2.13x slower                                                  |
| python_startup_no_site | 5.93 ms                                                | 31.4 ms: 5.29x slower                                                  |
| Geometric mean         | (ref)                                                  | 3.36x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250313-linux-x86_64-kumaraditya303-fast_asyncio-3.14.0a5+-f7b3d94 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 64.3 ms: 1.34x slower                                                  |
| genshi_text     | 31.8 ms                                                | 43.8 ms: 1.38x slower                                                  |
| mako            | 16.3 ms                                                | 22.5 ms: 1.38x slower                                                  |
| genshi_xml      | 66.0 ms                                                | 98.4 ms: 1.49x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.39x slower                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250313-linux-x86_64-kumaraditya303-fast_asyncio-3.14.0a5+-f7b3d94 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 323 us: 1.69x faster                                                   |
| async_tree_io            | 1.77 sec                                               | 1.21 sec: 1.46x faster                                                 |
| async_tree_none          | 728 ms                                                 | 515 ms: 1.41x faster                                                   |
| generators               | 80.1 ms                                                | 57.6 ms: 1.39x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 646 ms: 1.35x faster                                                   |
| deltablue                | 7.91 ms                                                | 6.40 ms: 1.24x faster                                                  |
| go                       | 240 ms                                                 | 235 ms: 1.02x faster                                                   |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 1.00 sec: 1.01x faster                                                 |
| deepcopy_memo            | 58.5 us                                                | 59.8 us: 1.02x slower                                                  |
| logging_silent           | 190 ns                                                 | 201 ns: 1.06x slower                                                   |
| chaos                    | 115 ms                                                 | 123 ms: 1.06x slower                                                   |
| richards_super           | 94.7 ms                                                | 101 ms: 1.07x slower                                                   |
| raytrace                 | 507 ms                                                 | 542 ms: 1.07x slower                                                   |
| scimark_sor              | 220 ms                                                 | 241 ms: 1.10x slower                                                   |
| deepcopy                 | 479 us                                                 | 529 us: 1.10x slower                                                   |
| richards                 | 79.3 ms                                                | 89.1 ms: 1.12x slower                                                  |
| comprehensions           | 28.8 us                                                | 33.4 us: 1.16x slower                                                  |
| scimark_monte_carlo      | 118 ms                                                 | 139 ms: 1.18x slower                                                   |
| spectral_norm            | 170 ms                                                 | 202 ms: 1.19x slower                                                   |
| hexiom                   | 10.4 ms                                                | 12.5 ms: 1.20x slower                                                  |
| crypto_pyaes             | 128 ms                                                 | 154 ms: 1.21x slower                                                   |
| float                    | 117 ms                                                 | 144 ms: 1.23x slower                                                   |
| tomli_loads              | 3.14 sec                                               | 3.88 sec: 1.23x slower                                                 |
| pyflate                  | 716 ms                                                 | 916 ms: 1.28x slower                                                   |
| deepcopy_reduce          | 4.17 us                                                | 5.40 us: 1.30x slower                                                  |
| logging_simple           | 8.30 us                                                | 10.9 us: 1.31x slower                                                  |
| logging_format           | 9.09 us                                                | 12.0 us: 1.32x slower                                                  |
| nbody                    | 154 ms                                                 | 203 ms: 1.32x slower                                                   |
| pickle_pure_python       | 484 us                                                 | 640 us: 1.32x slower                                                   |
| django_template          | 48.2 ms                                                | 64.3 ms: 1.34x slower                                                  |
| scimark_lu               | 176 ms                                                 | 236 ms: 1.34x slower                                                   |
| unpickle_pure_python     | 331 us                                                 | 444 us: 1.34x slower                                                   |
| regex_compile            | 188 ms                                                 | 256 ms: 1.36x slower                                                   |
| coroutines               | 35.1 ms                                                | 47.8 ms: 1.36x slower                                                  |
| genshi_text              | 31.8 ms                                                | 43.8 ms: 1.38x slower                                                  |
| mako                     | 16.3 ms                                                | 22.5 ms: 1.38x slower                                                  |
| html5lib                 | 88.9 ms                                                | 123 ms: 1.39x slower                                                   |
| dulwich_log              | 84.3 ms                                                | 118 ms: 1.40x slower                                                   |
| sqlalchemy_imperative    | 23.3 ms                                                | 33.0 ms: 1.41x slower                                                  |
| pprint_pformat           | 2.10 sec                                               | 2.99 sec: 1.42x slower                                                 |
| pprint_safe_repr         | 1.02 sec                                               | 1.47 sec: 1.45x slower                                                 |
| thrift                   | 1.07 ms                                                | 1.56 ms: 1.46x slower                                                  |
| genshi_xml               | 66.0 ms                                                | 98.4 ms: 1.49x slower                                                  |
| pycparser                | 1.58 sec                                               | 2.35 sec: 1.49x slower                                                 |
| 2to3                     | 348 ms                                                 | 522 ms: 1.50x slower                                                   |
| xml_etree_process        | 79.1 ms                                                | 119 ms: 1.50x slower                                                   |
| sympy_sum                | 196 ms                                                 | 297 ms: 1.51x slower                                                   |
| sqlalchemy_declarative   | 172 ms                                                 | 262 ms: 1.52x slower                                                   |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 9.84 ms: 1.52x slower                                                  |
| scimark_fft              | 466 ms                                                 | 717 ms: 1.54x slower                                                   |
| sympy_integrate          | 25.8 ms                                                | 39.9 ms: 1.54x slower                                                  |
| sympy_str                | 346 ms                                                 | 535 ms: 1.55x slower                                                   |
| nqueens                  | 106 ms                                                 | 166 ms: 1.57x slower                                                   |
| docutils                 | 3.30 sec                                               | 5.25 sec: 1.59x slower                                                 |
| sympy_expand             | 566 ms                                                 | 905 ms: 1.60x slower                                                   |
| json_dumps               | 14.2 ms                                                | 22.8 ms: 1.61x slower                                                  |
| fannkuch                 | 532 ms                                                 | 860 ms: 1.62x slower                                                   |
| xml_etree_iterparse      | 115 ms                                                 | 189 ms: 1.64x slower                                                   |
| pathlib                  | 20.5 ms                                                | 33.6 ms: 1.64x slower                                                  |
| regex_v8                 | 27.8 ms                                                | 46.5 ms: 1.68x slower                                                  |
| xml_etree_parse          | 168 ms                                                 | 287 ms: 1.71x slower                                                   |
| xml_etree_generate       | 99.4 ms                                                | 171 ms: 1.72x slower                                                   |
| mdp                      | 2.85 sec                                               | 4.98 sec: 1.75x slower                                                 |
| async_generators         | 444 ms                                                 | 787 ms: 1.77x slower                                                   |
| meteor_contest           | 120 ms                                                 | 213 ms: 1.78x slower                                                   |
| sqlite_synth             | 3.02 us                                                | 5.58 us: 1.85x slower                                                  |
| json                     | 5.69 ms                                                | 10.6 ms: 1.86x slower                                                  |
| regex_effbot             | 3.63 ms                                                | 6.83 ms: 1.88x slower                                                  |
| regex_dna                | 227 ms                                                 | 427 ms: 1.88x slower                                                   |
| json_loads               | 31.2 us                                                | 59.5 us: 1.91x slower                                                  |
| asyncio_websockets       | 559 ms                                                 | 1.09 sec: 1.94x slower                                                 |
| pidigits                 | 191 ms                                                 | 372 ms: 1.95x slower                                                   |
| python_startup           | 14.6 ms                                                | 31.0 ms: 2.13x slower                                                  |
| telco                    | 7.27 ms                                                | 16.0 ms: 2.20x slower                                                  |
| coverage                 | 79.4 ms                                                | 183 ms: 2.30x slower                                                   |
| gc_traversal             | 3.62 ms                                                | 10.4 ms: 2.86x slower                                                  |
| create_gc_cycles         | 1.62 ms                                                | 5.07 ms: 3.13x slower                                                  |
| python_startup_no_site   | 5.93 ms                                                | 31.4 ms: 5.29x slower                                                  |
| bench_mp_pool            | 24.0 ms                                                | 130 ms: 5.41x slower                                                   |
| bench_thread_pool        | 986 us                                                 | 29.8 ms: 30.26x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.49x slower                                                           |

Benchmark hidden because not significant (1): pylint
Ignored benchmarks (20) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250313-3.14.0a5+-f7b3d94/bm-20250313-linux-x86_64-kumaraditya303-fast_asyncio-3.14.0a5+-f7b3d94.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.294x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.37x
- 95% likely to have a slowdown of 1.35x
- 99% likely to have a slowdown of 1.30x

# Memory
- memory change: 1.27x