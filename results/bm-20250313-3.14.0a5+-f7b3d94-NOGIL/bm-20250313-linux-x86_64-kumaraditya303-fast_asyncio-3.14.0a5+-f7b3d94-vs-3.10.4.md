# Results vs. 3.10.4

- fork: kumaraditya303
- ref: fast_asyncio
- machine: linux-x86_64
- commit hash: f7b3d94
- commit date: 2025-03-13
- overall geometric mean: 1.368x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.48x slower
- Memory change: 1.51x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250313-linux-x86_64-kumaraditya303-fast_asyncio-3.14.0a5+-f7b3d94 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 607 ms: 1.74x slower                                                   |
| docutils       | 3.30 sec                                               | 5.62 sec: 1.70x slower                                                 |
| html5lib       | 88.9 ms                                                | 138 ms: 1.55x slower                                                   |
| Geometric mean | (ref)                                                  | 1.66x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250313-linux-x86_64-kumaraditya303-fast_asyncio-3.14.0a5+-f7b3d94 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io          | 1.77 sec                                               | 1.14 sec: 1.55x faster                                                 |
| async_tree_none        | 728 ms                                                 | 547 ms: 1.33x faster                                                   |
| async_tree_memoization | 870 ms                                                 | 693 ms: 1.25x faster                                                   |
| Geometric mean         | (ref)                                                  | 1.27x faster                                                           |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250313-linux-x86_64-kumaraditya303-fast_asyncio-3.14.0a5+-f7b3d94 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 117 ms                                                 | 153 ms: 1.31x slower                                                   |
| nbody          | 154 ms                                                 | 277 ms: 1.80x slower                                                   |
| pidigits       | 191 ms                                                 | 379 ms: 1.98x slower                                                   |
| Geometric mean | (ref)                                                  | 1.67x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250313-linux-x86_64-kumaraditya303-fast_asyncio-3.14.0a5+-f7b3d94 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 297 ms: 1.58x slower                                                   |
| regex_v8       | 27.8 ms                                                | 45.1 ms: 1.63x slower                                                  |
| regex_effbot   | 3.63 ms                                                | 6.75 ms: 1.86x slower                                                  |
| regex_dna      | 227 ms                                                 | 432 ms: 1.91x slower                                                   |
| Geometric mean | (ref)                                                  | 1.74x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250313-linux-x86_64-kumaraditya303-fast_asyncio-3.14.0a5+-f7b3d94 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 698 us: 1.44x slower                                                   |
| tomli_loads          | 3.14 sec                                               | 4.64 sec: 1.48x slower                                                 |
| unpickle_pure_python | 331 us                                                 | 503 us: 1.52x slower                                                   |
| xml_etree_iterparse  | 115 ms                                                 | 185 ms: 1.60x slower                                                   |
| xml_etree_process    | 79.1 ms                                                | 138 ms: 1.74x slower                                                   |
| xml_etree_parse      | 168 ms                                                 | 298 ms: 1.77x slower                                                   |
| json_dumps           | 14.2 ms                                                | 25.6 ms: 1.81x slower                                                  |
| xml_etree_generate   | 99.4 ms                                                | 197 ms: 1.98x slower                                                   |
| json_loads           | 31.2 us                                                | 65.4 us: 2.10x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.70x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250313-linux-x86_64-kumaraditya303-fast_asyncio-3.14.0a5+-f7b3d94 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 32.6 ms: 2.24x slower                                                  |
| python_startup_no_site | 5.93 ms                                                | 30.9 ms: 5.21x slower                                                  |
| Geometric mean         | (ref)                                                  | 3.41x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250313-linux-x86_64-kumaraditya303-fast_asyncio-3.14.0a5+-f7b3d94 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 80.4 ms: 1.67x slower                                                  |
| genshi_text     | 31.8 ms                                                | 56.6 ms: 1.78x slower                                                  |
| genshi_xml      | 66.0 ms                                                | 123 ms: 1.86x slower                                                   |
| mako            | 16.3 ms                                                | 32.3 ms: 1.98x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.82x slower                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250313-linux-x86_64-kumaraditya303-fast_asyncio-3.14.0a5+-f7b3d94 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io            | 1.77 sec                                               | 1.14 sec: 1.55x faster                                                 |
| typing_runtime_protocols | 544 us                                                 | 408 us: 1.33x faster                                                   |
| async_tree_none          | 728 ms                                                 | 547 ms: 1.33x faster                                                   |
| generators               | 80.1 ms                                                | 60.3 ms: 1.33x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 693 ms: 1.25x faster                                                   |
| pylint                   | 551 ms                                                 | 619 ms: 1.12x slower                                                   |
| logging_silent           | 190 ns                                                 | 222 ns: 1.17x slower                                                   |
| go                       | 240 ms                                                 | 284 ms: 1.18x slower                                                   |
| chaos                    | 115 ms                                                 | 144 ms: 1.25x slower                                                   |
| gc_traversal             | 3.62 ms                                                | 4.55 ms: 1.25x slower                                                  |
| scimark_sor              | 220 ms                                                 | 278 ms: 1.27x slower                                                   |
| deepcopy                 | 479 us                                                 | 615 us: 1.28x slower                                                   |
| float                    | 117 ms                                                 | 153 ms: 1.31x slower                                                   |
| raytrace                 | 507 ms                                                 | 667 ms: 1.32x slower                                                   |
| spectral_norm            | 170 ms                                                 | 224 ms: 1.32x slower                                                   |
| coroutines               | 35.1 ms                                                | 46.2 ms: 1.32x slower                                                  |
| richards_super           | 94.7 ms                                                | 127 ms: 1.34x slower                                                   |
| richards                 | 79.3 ms                                                | 107 ms: 1.35x slower                                                   |
| deepcopy_memo            | 58.5 us                                                | 79.7 us: 1.36x slower                                                  |
| comprehensions           | 28.8 us                                                | 39.7 us: 1.38x slower                                                  |
| crypto_pyaes             | 128 ms                                                 | 179 ms: 1.40x slower                                                   |
| pycparser                | 1.58 sec                                               | 2.27 sec: 1.44x slower                                                 |
| pickle_pure_python       | 484 us                                                 | 698 us: 1.44x slower                                                   |
| pyflate                  | 716 ms                                                 | 1.05 sec: 1.47x slower                                                 |
| scimark_monte_carlo      | 118 ms                                                 | 174 ms: 1.47x slower                                                   |
| hexiom                   | 10.4 ms                                                | 15.3 ms: 1.48x slower                                                  |
| tomli_loads              | 3.14 sec                                               | 4.64 sec: 1.48x slower                                                 |
| dulwich_log              | 84.3 ms                                                | 126 ms: 1.49x slower                                                   |
| unpickle_pure_python     | 331 us                                                 | 503 us: 1.52x slower                                                   |
| html5lib                 | 88.9 ms                                                | 138 ms: 1.55x slower                                                   |
| logging_simple           | 8.30 us                                                | 13.1 us: 1.58x slower                                                  |
| deepcopy_reduce          | 4.17 us                                                | 6.58 us: 1.58x slower                                                  |
| regex_compile            | 188 ms                                                 | 297 ms: 1.58x slower                                                   |
| xml_etree_iterparse      | 115 ms                                                 | 185 ms: 1.60x slower                                                   |
| logging_format           | 9.09 us                                                | 14.7 us: 1.61x slower                                                  |
| regex_v8                 | 27.8 ms                                                | 45.1 ms: 1.63x slower                                                  |
| scimark_lu               | 176 ms                                                 | 288 ms: 1.63x slower                                                   |
| pprint_safe_repr         | 1.02 sec                                               | 1.69 sec: 1.66x slower                                                 |
| thrift                   | 1.07 ms                                                | 1.78 ms: 1.66x slower                                                  |
| pprint_pformat           | 2.10 sec                                               | 3.50 sec: 1.67x slower                                                 |
| django_template          | 48.2 ms                                                | 80.4 ms: 1.67x slower                                                  |
| docutils                 | 3.30 sec                                               | 5.62 sec: 1.70x slower                                                 |
| pathlib                  | 20.5 ms                                                | 34.9 ms: 1.70x slower                                                  |
| 2to3                     | 348 ms                                                 | 607 ms: 1.74x slower                                                   |
| xml_etree_process        | 79.1 ms                                                | 138 ms: 1.74x slower                                                   |
| sqlalchemy_imperative    | 23.3 ms                                                | 40.8 ms: 1.75x slower                                                  |
| xml_etree_parse          | 168 ms                                                 | 298 ms: 1.77x slower                                                   |
| genshi_text              | 31.8 ms                                                | 56.6 ms: 1.78x slower                                                  |
| sympy_sum                | 196 ms                                                 | 352 ms: 1.79x slower                                                   |
| nbody                    | 154 ms                                                 | 277 ms: 1.80x slower                                                   |
| json_dumps               | 14.2 ms                                                | 25.6 ms: 1.81x slower                                                  |
| sqlite_synth             | 3.02 us                                                | 5.49 us: 1.82x slower                                                  |
| sympy_integrate          | 25.8 ms                                                | 47.1 ms: 1.82x slower                                                  |
| scimark_fft              | 466 ms                                                 | 854 ms: 1.83x slower                                                   |
| sympy_str                | 346 ms                                                 | 637 ms: 1.84x slower                                                   |
| genshi_xml               | 66.0 ms                                                | 123 ms: 1.86x slower                                                   |
| nqueens                  | 106 ms                                                 | 196 ms: 1.86x slower                                                   |
| regex_effbot             | 3.63 ms                                                | 6.75 ms: 1.86x slower                                                  |
| sqlalchemy_declarative   | 172 ms                                                 | 320 ms: 1.86x slower                                                   |
| sympy_expand             | 566 ms                                                 | 1.07 sec: 1.89x slower                                                 |
| regex_dna                | 227 ms                                                 | 432 ms: 1.91x slower                                                   |
| mdp                      | 2.85 sec                                               | 5.49 sec: 1.93x slower                                                 |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 12.5 ms: 1.93x slower                                                  |
| async_generators         | 444 ms                                                 | 862 ms: 1.94x slower                                                   |
| fannkuch                 | 532 ms                                                 | 1.05 sec: 1.97x slower                                                 |
| mako                     | 16.3 ms                                                | 32.3 ms: 1.98x slower                                                  |
| xml_etree_generate       | 99.4 ms                                                | 197 ms: 1.98x slower                                                   |
| pidigits                 | 191 ms                                                 | 379 ms: 1.98x slower                                                   |
| asyncio_websockets       | 559 ms                                                 | 1.11 sec: 1.99x slower                                                 |
| json                     | 5.69 ms                                                | 11.4 ms: 2.00x slower                                                  |
| json_loads               | 31.2 us                                                | 65.4 us: 2.10x slower                                                  |
| create_gc_cycles         | 1.62 ms                                                | 3.47 ms: 2.14x slower                                                  |
| meteor_contest           | 120 ms                                                 | 267 ms: 2.23x slower                                                   |
| python_startup           | 14.6 ms                                                | 32.6 ms: 2.24x slower                                                  |
| telco                    | 7.27 ms                                                | 19.0 ms: 2.62x slower                                                  |
| coverage                 | 79.4 ms                                                | 218 ms: 2.74x slower                                                   |
| python_startup_no_site   | 5.93 ms                                                | 30.9 ms: 5.21x slower                                                  |
| bench_mp_pool            | 24.0 ms                                                | 142 ms: 5.91x slower                                                   |
| bench_thread_pool        | 986 us                                                 | 36.5 ms: 36.99x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.67x slower                                                           |

Benchmark hidden because not significant (2): deltablue, async_tree_cpu_io_mixed
Ignored benchmarks (20) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250313-3.14.0a5+-f7b3d94-NOGIL/bm-20250313-linux-x86_64-kumaraditya303-fast_asyncio-3.14.0a5+-f7b3d94.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.368x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.55x
- 95% likely to have a slowdown of 1.52x
- 99% likely to have a slowdown of 1.48x

# Memory
- memory change: 1.51x