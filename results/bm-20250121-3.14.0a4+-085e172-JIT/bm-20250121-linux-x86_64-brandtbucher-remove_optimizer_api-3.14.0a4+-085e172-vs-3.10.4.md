# Results vs. 3.10.4

- fork: brandtbucher
- ref: remove_optimizer_api
- machine: linux-x86_64
- commit hash: 085e172
- commit date: 2025-01-21
- overall geometric mean: 1.429x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250121-linux-x86_64-brandtbucher-remove_optimizer_api-3.14.0a4+-085e172 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 262 ms: 1.33x faster                                                         |
| docutils       | 3.30 sec                                               | 2.70 sec: 1.22x faster                                                       |
| html5lib       | 88.9 ms                                                | 64.6 ms: 1.38x faster                                                        |
| Geometric mean | (ref)                                                  | 1.31x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250121-linux-x86_64-brandtbucher-remove_optimizer_api-3.14.0a4+-085e172 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 598 ms: 2.96x faster                                                         |
| async_tree_none         | 728 ms                                                 | 257 ms: 2.84x faster                                                         |
| async_tree_memoization  | 870 ms                                                 | 322 ms: 2.70x faster                                                         |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 485 ms: 2.10x faster                                                         |
| Geometric mean          | (ref)                                                  | 2.63x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250121-linux-x86_64-brandtbucher-remove_optimizer_api-3.14.0a4+-085e172 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 65.1 ms: 1.80x faster                                                        |
| nbody          | 154 ms                                                 | 86.7 ms: 1.77x faster                                                        |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                         |
| Geometric mean | (ref)                                                  | 1.48x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250121-linux-x86_64-brandtbucher-remove_optimizer_api-3.14.0a4+-085e172 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 130 ms: 1.45x faster                                                         |
| regex_v8       | 27.8 ms                                                | 23.6 ms: 1.18x faster                                                        |
| regex_effbot   | 3.63 ms                                                | 3.30 ms: 1.10x faster                                                        |
| regex_dna      | 227 ms                                                 | 212 ms: 1.07x faster                                                         |
| Geometric mean | (ref)                                                  | 1.19x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250121-linux-x86_64-brandtbucher-remove_optimizer_api-3.14.0a4+-085e172 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.85 sec: 1.70x faster                                                       |
| unpickle_pure_python | 331 us                                                 | 206 us: 1.60x faster                                                         |
| pickle_pure_python   | 484 us                                                 | 328 us: 1.48x faster                                                         |
| xml_etree_process    | 79.1 ms                                                | 59.6 ms: 1.33x faster                                                        |
| xml_etree_generate   | 99.4 ms                                                | 80.3 ms: 1.24x faster                                                        |
| xml_etree_iterparse  | 115 ms                                                 | 94.0 ms: 1.23x faster                                                        |
| xml_etree_parse      | 168 ms                                                 | 138 ms: 1.22x faster                                                         |
| json_dumps           | 14.2 ms                                                | 11.7 ms: 1.21x faster                                                        |
| json_loads           | 31.2 us                                                | 29.4 us: 1.06x faster                                                        |
| Geometric mean       | (ref)                                                  | 1.33x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250121-linux-x86_64-brandtbucher-remove_optimizer_api-3.14.0a4+-085e172 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.9 ms: 1.13x faster                                                        |
| python_startup_no_site | 5.93 ms                                                | 7.07 ms: 1.19x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250121-linux-x86_64-brandtbucher-remove_optimizer_api-3.14.0a4+-085e172 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.83 ms: 1.66x faster                                                        |
| django_template | 48.2 ms                                                | 33.5 ms: 1.44x faster                                                        |
| genshi_text     | 31.8 ms                                                | 24.2 ms: 1.31x faster                                                        |
| genshi_xml      | 66.0 ms                                                | 59.1 ms: 1.12x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.37x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250121-linux-x86_64-brandtbucher-remove_optimizer_api-3.14.0a4+-085e172 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 167 us: 3.26x faster                                                         |
| async_tree_io            | 1.77 sec                                               | 598 ms: 2.96x faster                                                         |
| async_tree_none          | 728 ms                                                 | 257 ms: 2.84x faster                                                         |
| async_tree_memoization   | 870 ms                                                 | 322 ms: 2.70x faster                                                         |
| deltablue                | 7.91 ms                                                | 3.19 ms: 2.48x faster                                                        |
| generators               | 80.1 ms                                                | 37.2 ms: 2.15x faster                                                        |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 485 ms: 2.10x faster                                                         |
| chaos                    | 115 ms                                                 | 59.0 ms: 1.96x faster                                                        |
| deepcopy_memo            | 58.5 us                                                | 30.0 us: 1.95x faster                                                        |
| pylint                   | 551 ms                                                 | 287 ms: 1.92x faster                                                         |
| richards_super           | 94.7 ms                                                | 49.3 ms: 1.92x faster                                                        |
| scimark_sor              | 220 ms                                                 | 115 ms: 1.91x faster                                                         |
| scimark_monte_carlo      | 118 ms                                                 | 62.2 ms: 1.90x faster                                                        |
| crypto_pyaes             | 128 ms                                                 | 68.4 ms: 1.87x faster                                                        |
| go                       | 240 ms                                                 | 133 ms: 1.80x faster                                                         |
| float                    | 117 ms                                                 | 65.1 ms: 1.80x faster                                                        |
| spectral_norm            | 170 ms                                                 | 95.1 ms: 1.79x faster                                                        |
| raytrace                 | 507 ms                                                 | 286 ms: 1.77x faster                                                         |
| nbody                    | 154 ms                                                 | 86.7 ms: 1.77x faster                                                        |
| deepcopy                 | 479 us                                                 | 271 us: 1.77x faster                                                         |
| logging_silent           | 190 ns                                                 | 111 ns: 1.71x faster                                                         |
| sqlglot_parse            | 2.17 ms                                                | 1.27 ms: 1.70x faster                                                        |
| tomli_loads              | 3.14 sec                                               | 1.85 sec: 1.70x faster                                                       |
| richards                 | 79.3 ms                                                | 47.1 ms: 1.68x faster                                                        |
| mako                     | 16.3 ms                                                | 9.83 ms: 1.66x faster                                                        |
| comprehensions           | 28.8 us                                                | 17.4 us: 1.65x faster                                                        |
| sqlglot_transpile        | 2.57 ms                                                | 1.58 ms: 1.62x faster                                                        |
| pyflate                  | 716 ms                                                 | 443 ms: 1.62x faster                                                         |
| unpickle_pure_python     | 331 us                                                 | 206 us: 1.60x faster                                                         |
| scimark_lu               | 176 ms                                                 | 113 ms: 1.55x faster                                                         |
| deepcopy_reduce          | 4.17 us                                                | 2.69 us: 1.55x faster                                                        |
| scimark_fft              | 466 ms                                                 | 313 ms: 1.49x faster                                                         |
| pickle_pure_python       | 484 us                                                 | 328 us: 1.48x faster                                                         |
| coroutines               | 35.1 ms                                                | 23.8 ms: 1.47x faster                                                        |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.42 ms: 1.46x faster                                                        |
| hexiom                   | 10.4 ms                                                | 7.11 ms: 1.46x faster                                                        |
| regex_compile            | 188 ms                                                 | 130 ms: 1.45x faster                                                         |
| django_template          | 48.2 ms                                                | 33.5 ms: 1.44x faster                                                        |
| pprint_safe_repr         | 1.02 sec                                               | 737 ms: 1.38x faster                                                         |
| html5lib                 | 88.9 ms                                                | 64.6 ms: 1.38x faster                                                        |
| thrift                   | 1.07 ms                                                | 783 us: 1.37x faster                                                         |
| pprint_pformat           | 2.10 sec                                               | 1.54 sec: 1.36x faster                                                       |
| pycparser                | 1.58 sec                                               | 1.16 sec: 1.36x faster                                                       |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.2 ms: 1.36x faster                                                        |
| logging_format           | 9.09 us                                                | 6.71 us: 1.36x faster                                                        |
| fannkuch                 | 532 ms                                                 | 393 ms: 1.35x faster                                                         |
| logging_simple           | 8.30 us                                                | 6.15 us: 1.35x faster                                                        |
| 2to3                     | 348 ms                                                 | 262 ms: 1.33x faster                                                         |
| xml_etree_process        | 79.1 ms                                                | 59.6 ms: 1.33x faster                                                        |
| genshi_text              | 31.8 ms                                                | 24.2 ms: 1.31x faster                                                        |
| sqlglot_normalize        | 143 ms                                                 | 109 ms: 1.31x faster                                                         |
| sqlalchemy_declarative   | 172 ms                                                 | 133 ms: 1.29x faster                                                         |
| sympy_sum                | 196 ms                                                 | 155 ms: 1.27x faster                                                         |
| sqlglot_optimize         | 69.2 ms                                                | 54.9 ms: 1.26x faster                                                        |
| pathlib                  | 20.5 ms                                                | 16.3 ms: 1.25x faster                                                        |
| sympy_integrate          | 25.8 ms                                                | 20.7 ms: 1.25x faster                                                        |
| dulwich_log              | 84.3 ms                                                | 67.9 ms: 1.24x faster                                                        |
| xml_etree_generate       | 99.4 ms                                                | 80.3 ms: 1.24x faster                                                        |
| sympy_str                | 346 ms                                                 | 281 ms: 1.23x faster                                                         |
| xml_etree_iterparse      | 115 ms                                                 | 94.0 ms: 1.23x faster                                                        |
| docutils                 | 3.30 sec                                               | 2.70 sec: 1.22x faster                                                       |
| xml_etree_parse          | 168 ms                                                 | 138 ms: 1.22x faster                                                         |
| json_dumps               | 14.2 ms                                                | 11.7 ms: 1.21x faster                                                        |
| sympy_expand             | 566 ms                                                 | 475 ms: 1.19x faster                                                         |
| regex_v8                 | 27.8 ms                                                | 23.6 ms: 1.18x faster                                                        |
| nqueens                  | 106 ms                                                 | 90.9 ms: 1.16x faster                                                        |
| python_startup           | 14.6 ms                                                | 12.9 ms: 1.13x faster                                                        |
| genshi_xml               | 66.0 ms                                                | 59.1 ms: 1.12x faster                                                        |
| mdp                      | 2.85 sec                                               | 2.56 sec: 1.11x faster                                                       |
| bench_thread_pool        | 986 us                                                 | 890 us: 1.11x faster                                                         |
| sqlite_synth             | 3.02 us                                                | 2.74 us: 1.10x faster                                                        |
| regex_effbot             | 3.63 ms                                                | 3.30 ms: 1.10x faster                                                        |
| meteor_contest           | 120 ms                                                 | 109 ms: 1.10x faster                                                         |
| json                     | 5.69 ms                                                | 5.32 ms: 1.07x faster                                                        |
| regex_dna                | 227 ms                                                 | 212 ms: 1.07x faster                                                         |
| async_generators         | 444 ms                                                 | 415 ms: 1.07x faster                                                         |
| json_loads               | 31.2 us                                                | 29.4 us: 1.06x faster                                                        |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                         |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                         |
| telco                    | 7.27 ms                                                | 7.58 ms: 1.04x slower                                                        |
| coverage                 | 79.4 ms                                                | 91.8 ms: 1.16x slower                                                        |
| python_startup_no_site   | 5.93 ms                                                | 7.07 ms: 1.19x slower                                                        |
| gc_traversal             | 3.62 ms                                                | 4.60 ms: 1.27x slower                                                        |
| create_gc_cycles         | 1.62 ms                                                | 2.45 ms: 1.51x slower                                                        |
| bench_mp_pool            | 24.0 ms                                                | 81.7 ms: 3.40x slower                                                        |
| Geometric mean           | (ref)                                                  | 1.40x faster                                                                 |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250121-3.14.0a4+-085e172-JIT/bm-20250121-linux-x86_64-brandtbucher-remove_optimizer_api-3.14.0a4+-085e172.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.429x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.28x

# Memory
- memory change: 1.28x