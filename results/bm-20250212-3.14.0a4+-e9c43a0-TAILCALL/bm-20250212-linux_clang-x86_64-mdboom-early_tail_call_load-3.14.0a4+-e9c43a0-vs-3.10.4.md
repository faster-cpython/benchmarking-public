# Results vs. 3.10.4

- fork: mdboom
- ref: early_tail_call_load
- machine: linux-x86_64
- commit hash: e9c43a0
- commit date: 2025-02-12
- overall geometric mean: 1.510x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.38x faster
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250212-linux-x86_64-mdboom-early_tail_call_load-3.14.0a4+-e9c43a0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 244 ms: 1.43x faster                                                   |
| docutils       | 3.30 sec                                               | 2.51 sec: 1.31x faster                                                 |
| html5lib       | 88.9 ms                                                | 55.3 ms: 1.61x faster                                                  |
| Geometric mean | (ref)                                                  | 1.45x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250212-linux-x86_64-mdboom-early_tail_call_load-3.14.0a4+-e9c43a0 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 599 ms: 2.95x faster                                                   |
| async_tree_none         | 728 ms                                                 | 252 ms: 2.89x faster                                                   |
| async_tree_memoization  | 870 ms                                                 | 311 ms: 2.80x faster                                                   |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 487 ms: 2.09x faster                                                   |
| Geometric mean          | (ref)                                                  | 2.66x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250212-linux-x86_64-mdboom-early_tail_call_load-3.14.0a4+-e9c43a0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 80.5 ms: 1.91x faster                                                  |
| float          | 117 ms                                                 | 64.1 ms: 1.83x faster                                                  |
| pidigits       | 191 ms                                                 | 202 ms: 1.06x slower                                                   |
| Geometric mean | (ref)                                                  | 1.49x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250212-linux-x86_64-mdboom-early_tail_call_load-3.14.0a4+-e9c43a0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 119 ms: 1.58x faster                                                   |
| regex_effbot   | 3.63 ms                                                | 3.13 ms: 1.16x faster                                                  |
| regex_dna      | 227 ms                                                 | 198 ms: 1.15x faster                                                   |
| regex_v8       | 27.8 ms                                                | 24.9 ms: 1.11x faster                                                  |
| Geometric mean | (ref)                                                  | 1.24x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250212-linux-x86_64-mdboom-early_tail_call_load-3.14.0a4+-e9c43a0 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.86 sec: 1.69x faster                                                 |
| pickle_pure_python   | 484 us                                                 | 299 us: 1.62x faster                                                   |
| unpickle_pure_python | 331 us                                                 | 206 us: 1.61x faster                                                   |
| xml_etree_process    | 79.1 ms                                                | 56.9 ms: 1.39x faster                                                  |
| xml_etree_generate   | 99.4 ms                                                | 83.8 ms: 1.19x faster                                                  |
| xml_etree_iterparse  | 115 ms                                                 | 101 ms: 1.14x faster                                                   |
| json_dumps           | 14.2 ms                                                | 12.5 ms: 1.13x faster                                                  |
| xml_etree_parse      | 168 ms                                                 | 159 ms: 1.06x faster                                                   |
| json_loads           | 31.2 us                                                | 30.8 us: 1.01x faster                                                  |
| Geometric mean       | (ref)                                                  | 1.29x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250212-linux-x86_64-mdboom-early_tail_call_load-3.14.0a4+-e9c43a0 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.6 ms: 1.16x faster                                                  |
| python_startup_no_site | 5.93 ms                                                | 6.95 ms: 1.17x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250212-linux-x86_64-mdboom-early_tail_call_load-3.14.0a4+-e9c43a0 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 30.1 ms: 1.60x faster                                                  |
| genshi_text     | 31.8 ms                                                | 20.7 ms: 1.54x faster                                                  |
| mako            | 16.3 ms                                                | 11.3 ms: 1.45x faster                                                  |
| genshi_xml      | 66.0 ms                                                | 47.5 ms: 1.39x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.49x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250212-linux-x86_64-mdboom-early_tail_call_load-3.14.0a4+-e9c43a0 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 147 us: 3.70x faster                                                   |
| async_tree_io            | 1.77 sec                                               | 599 ms: 2.95x faster                                                   |
| generators               | 80.1 ms                                                | 27.7 ms: 2.89x faster                                                  |
| async_tree_none          | 728 ms                                                 | 252 ms: 2.89x faster                                                   |
| async_tree_memoization   | 870 ms                                                 | 311 ms: 2.80x faster                                                   |
| deltablue                | 7.91 ms                                                | 2.85 ms: 2.78x faster                                                  |
| logging_silent           | 190 ns                                                 | 82.3 ns: 2.31x faster                                                  |
| go                       | 240 ms                                                 | 107 ms: 2.24x faster                                                   |
| chaos                    | 115 ms                                                 | 52.7 ms: 2.19x faster                                                  |
| pylint                   | 551 ms                                                 | 262 ms: 2.10x faster                                                   |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 487 ms: 2.09x faster                                                   |
| scimark_sor              | 220 ms                                                 | 106 ms: 2.08x faster                                                   |
| deepcopy_memo            | 58.5 us                                                | 28.2 us: 2.07x faster                                                  |
| richards_super           | 94.7 ms                                                | 45.8 ms: 2.07x faster                                                  |
| raytrace                 | 507 ms                                                 | 249 ms: 2.04x faster                                                   |
| spectral_norm            | 170 ms                                                 | 84.1 ms: 2.02x faster                                                  |
| richards                 | 79.3 ms                                                | 39.3 ms: 2.02x faster                                                  |
| scimark_monte_carlo      | 118 ms                                                 | 58.7 ms: 2.01x faster                                                  |
| deepcopy                 | 479 us                                                 | 240 us: 1.99x faster                                                   |
| comprehensions           | 28.8 us                                                | 14.9 us: 1.93x faster                                                  |
| crypto_pyaes             | 128 ms                                                 | 66.5 ms: 1.92x faster                                                  |
| nbody                    | 154 ms                                                 | 80.5 ms: 1.91x faster                                                  |
| sqlglot_parse            | 2.17 ms                                                | 1.14 ms: 1.90x faster                                                  |
| float                    | 117 ms                                                 | 64.1 ms: 1.83x faster                                                  |
| hexiom                   | 10.4 ms                                                | 5.70 ms: 1.82x faster                                                  |
| pyflate                  | 716 ms                                                 | 394 ms: 1.82x faster                                                   |
| sqlglot_transpile        | 2.57 ms                                                | 1.44 ms: 1.79x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 1.86 sec: 1.69x faster                                                 |
| coroutines               | 35.1 ms                                                | 21.0 ms: 1.67x faster                                                  |
| scimark_fft              | 466 ms                                                 | 279 ms: 1.67x faster                                                   |
| scimark_lu               | 176 ms                                                 | 106 ms: 1.67x faster                                                   |
| deepcopy_reduce          | 4.17 us                                                | 2.52 us: 1.66x faster                                                  |
| pickle_pure_python       | 484 us                                                 | 299 us: 1.62x faster                                                   |
| html5lib                 | 88.9 ms                                                | 55.3 ms: 1.61x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 206 us: 1.61x faster                                                   |
| django_template          | 48.2 ms                                                | 30.1 ms: 1.60x faster                                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.07 ms: 1.59x faster                                                  |
| regex_compile            | 188 ms                                                 | 119 ms: 1.58x faster                                                   |
| logging_simple           | 8.30 us                                                | 5.28 us: 1.57x faster                                                  |
| logging_format           | 9.09 us                                                | 5.83 us: 1.56x faster                                                  |
| genshi_text              | 31.8 ms                                                | 20.7 ms: 1.54x faster                                                  |
| sqlalchemy_imperative    | 23.3 ms                                                | 15.2 ms: 1.53x faster                                                  |
| thrift                   | 1.07 ms                                                | 733 us: 1.46x faster                                                   |
| pprint_pformat           | 2.10 sec                                               | 1.45 sec: 1.45x faster                                                 |
| mako                     | 16.3 ms                                                | 11.3 ms: 1.45x faster                                                  |
| pycparser                | 1.58 sec                                               | 1.09 sec: 1.44x faster                                                 |
| 2to3                     | 348 ms                                                 | 244 ms: 1.43x faster                                                   |
| pprint_safe_repr         | 1.02 sec                                               | 713 ms: 1.43x faster                                                   |
| sqlalchemy_declarative   | 172 ms                                                 | 121 ms: 1.42x faster                                                   |
| pathlib                  | 20.5 ms                                                | 14.4 ms: 1.42x faster                                                  |
| sympy_sum                | 196 ms                                                 | 139 ms: 1.42x faster                                                   |
| nqueens                  | 106 ms                                                 | 74.8 ms: 1.41x faster                                                  |
| dulwich_log              | 84.3 ms                                                | 60.1 ms: 1.40x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 18.6 ms: 1.39x faster                                                  |
| xml_etree_process        | 79.1 ms                                                | 56.9 ms: 1.39x faster                                                  |
| genshi_xml               | 66.0 ms                                                | 47.5 ms: 1.39x faster                                                  |
| fannkuch                 | 532 ms                                                 | 384 ms: 1.38x faster                                                   |
| sympy_str                | 346 ms                                                 | 251 ms: 1.38x faster                                                   |
| sqlglot_optimize         | 69.2 ms                                                | 50.8 ms: 1.36x faster                                                  |
| sympy_expand             | 566 ms                                                 | 428 ms: 1.32x faster                                                   |
| docutils                 | 3.30 sec                                               | 2.51 sec: 1.31x faster                                                 |
| bench_thread_pool        | 986 us                                                 | 813 us: 1.21x faster                                                   |
| xml_etree_generate       | 99.4 ms                                                | 83.8 ms: 1.19x faster                                                  |
| async_generators         | 444 ms                                                 | 378 ms: 1.17x faster                                                   |
| regex_effbot             | 3.63 ms                                                | 3.13 ms: 1.16x faster                                                  |
| python_startup           | 14.6 ms                                                | 12.6 ms: 1.16x faster                                                  |
| regex_dna                | 227 ms                                                 | 198 ms: 1.15x faster                                                   |
| xml_etree_iterparse      | 115 ms                                                 | 101 ms: 1.14x faster                                                   |
| json_dumps               | 14.2 ms                                                | 12.5 ms: 1.13x faster                                                  |
| sqlite_synth             | 3.02 us                                                | 2.70 us: 1.12x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 24.9 ms: 1.11x faster                                                  |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.11x faster                                                   |
| mdp                      | 2.85 sec                                               | 2.61 sec: 1.09x faster                                                 |
| xml_etree_parse          | 168 ms                                                 | 159 ms: 1.06x faster                                                   |
| json                     | 5.69 ms                                                | 5.43 ms: 1.05x faster                                                  |
| json_loads               | 31.2 us                                                | 30.8 us: 1.01x faster                                                  |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                                   |
| telco                    | 7.27 ms                                                | 7.18 ms: 1.01x faster                                                  |
| coverage                 | 79.4 ms                                                | 80.6 ms: 1.01x slower                                                  |
| pidigits                 | 191 ms                                                 | 202 ms: 1.06x slower                                                   |
| python_startup_no_site   | 5.93 ms                                                | 6.95 ms: 1.17x slower                                                  |
| gc_traversal             | 3.62 ms                                                | 5.04 ms: 1.39x slower                                                  |
| create_gc_cycles         | 1.62 ms                                                | 2.54 ms: 1.57x slower                                                  |
| sqlglot_normalize        | 143 ms                                                 | 265 ms: 1.85x slower                                                   |
| bench_mp_pool            | 24.0 ms                                                | 79.0 ms: 3.29x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.49x faster                                                           |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250212-3.14.0a4+-e9c43a0-CLANG/bm-20250212-linux-x86_64-mdboom-early_tail_call_load-3.14.0a4+-e9c43a0.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.510x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.41x
- 95% likely to have a speedup of 1.40x
- 99% likely to have a speedup of 1.38x

# Memory
- memory change: 1.27x