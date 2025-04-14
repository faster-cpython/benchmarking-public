# Results vs. 3.10.4

- fork: diegorusso
- ref: remove_jumps_aarch64
- machine: linux-aarch64
- commit hash: 460d0d3
- commit date: 2025-03-10
- overall geometric mean: 1.334x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.32x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250310-arminc-aarch64-diegorusso-remove_jumps_aarch64-3.14.0a5+-460d0d3 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 300 ms: 1.27x faster                                                         |
| docutils       | 3.53 sec                                                              | 3.07 sec: 1.15x faster                                                       |
| html5lib       | 86.5 ms                                                               | 61.5 ms: 1.41x faster                                                        |
| Geometric mean | (ref)                                                                 | 1.27x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250310-arminc-aarch64-diegorusso-remove_jumps_aarch64-3.14.0a5+-460d0d3 |
|-------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 870 ms: 2.63x faster                                                         |
| async_tree_none         | 950 ms                                                                | 380 ms: 2.50x faster                                                         |
| async_tree_memoization  | 1.13 sec                                                              | 465 ms: 2.44x faster                                                         |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 652 ms: 1.95x faster                                                         |
| Geometric mean          | (ref)                                                                 | 2.36x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250310-arminc-aarch64-diegorusso-remove_jumps_aarch64-3.14.0a5+-460d0d3 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 82.7 ms: 1.63x faster                                                        |
| nbody          | 166 ms                                                                | 117 ms: 1.42x faster                                                         |
| Geometric mean | (ref)                                                                 | 1.32x faster                                                                 |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250310-arminc-aarch64-diegorusso-remove_jumps_aarch64-3.14.0a5+-460d0d3 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 122 ms: 1.45x faster                                                         |
| regex_v8       | 32.2 ms                                                               | 28.0 ms: 1.15x faster                                                        |
| regex_effbot   | 4.25 ms                                                               | 3.92 ms: 1.08x faster                                                        |
| regex_dna      | 257 ms                                                                | 249 ms: 1.03x faster                                                         |
| Geometric mean | (ref)                                                                 | 1.17x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250310-arminc-aarch64-diegorusso-remove_jumps_aarch64-3.14.0a5+-460d0d3 |
|----------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 3.36 sec                                                              | 2.31 sec: 1.46x faster                                                       |
| unpickle_pure_python | 366 us                                                                | 251 us: 1.46x faster                                                         |
| pickle_pure_python   | 529 us                                                                | 392 us: 1.35x faster                                                         |
| xml_etree_process    | 99.5 ms                                                               | 76.3 ms: 1.30x faster                                                        |
| xml_etree_parse      | 212 ms                                                                | 175 ms: 1.21x faster                                                         |
| json_dumps           | 16.7 ms                                                               | 14.2 ms: 1.17x faster                                                        |
| xml_etree_generate   | 123 ms                                                                | 108 ms: 1.14x faster                                                         |
| xml_etree_iterparse  | 156 ms                                                                | 142 ms: 1.10x faster                                                         |
| json_loads           | 30.9 us                                                               | 34.1 us: 1.10x slower                                                        |
| Geometric mean       | (ref)                                                                 | 1.22x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250310-arminc-aarch64-diegorusso-remove_jumps_aarch64-3.14.0a5+-460d0d3 |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 16.1 ms: 1.44x slower                                                        |
| python_startup_no_site | 6.89 ms                                                               | 10.1 ms: 1.47x slower                                                        |
| Geometric mean         | (ref)                                                                 | 1.46x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250310-arminc-aarch64-diegorusso-remove_jumps_aarch64-3.14.0a5+-460d0d3 |
|-----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 12.5 ms: 1.52x faster                                                        |
| django_template | 53.3 ms                                                               | 38.5 ms: 1.38x faster                                                        |
| genshi_text     | 35.2 ms                                                               | 26.5 ms: 1.33x faster                                                        |
| genshi_xml      | 69.8 ms                                                               | 60.0 ms: 1.16x faster                                                        |
| Geometric mean  | (ref)                                                                 | 1.34x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250310-arminc-aarch64-diegorusso-remove_jumps_aarch64-3.14.0a5+-460d0d3 |
|--------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 204 us: 3.25x faster                                                         |
| async_tree_io            | 2.28 sec                                                              | 870 ms: 2.63x faster                                                         |
| async_tree_none          | 950 ms                                                                | 380 ms: 2.50x faster                                                         |
| async_tree_memoization   | 1.13 sec                                                              | 465 ms: 2.44x faster                                                         |
| deltablue                | 8.94 ms                                                               | 3.81 ms: 2.35x faster                                                        |
| richards_super           | 107 ms                                                                | 51.7 ms: 2.08x faster                                                        |
| richards                 | 91.7 ms                                                               | 45.7 ms: 2.00x faster                                                        |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 652 ms: 1.95x faster                                                         |
| generators               | 68.1 ms                                                               | 35.7 ms: 1.90x faster                                                        |
| raytrace                 | 573 ms                                                                | 314 ms: 1.83x faster                                                         |
| chaos                    | 121 ms                                                                | 67.4 ms: 1.80x faster                                                        |
| logging_silent           | 222 ns                                                                | 132 ns: 1.69x faster                                                         |
| scimark_lu               | 227 ms                                                                | 138 ms: 1.65x faster                                                         |
| go                       | 264 ms                                                                | 161 ms: 1.64x faster                                                         |
| deepcopy_memo            | 61.7 us                                                               | 37.6 us: 1.64x faster                                                        |
| scimark_sor              | 246 ms                                                                | 150 ms: 1.64x faster                                                         |
| float                    | 135 ms                                                                | 82.7 ms: 1.63x faster                                                        |
| spectral_norm            | 186 ms                                                                | 117 ms: 1.59x faster                                                         |
| pylint                   | 485 ms                                                                | 313 ms: 1.55x faster                                                         |
| deepcopy                 | 511 us                                                                | 330 us: 1.55x faster                                                         |
| scimark_monte_carlo      | 128 ms                                                                | 83.2 ms: 1.54x faster                                                        |
| mako                     | 18.9 ms                                                               | 12.5 ms: 1.52x faster                                                        |
| pyflate                  | 795 ms                                                                | 540 ms: 1.47x faster                                                         |
| tomli_loads              | 3.36 sec                                                              | 2.31 sec: 1.46x faster                                                       |
| unpickle_pure_python     | 366 us                                                                | 251 us: 1.46x faster                                                         |
| regex_compile            | 177 ms                                                                | 122 ms: 1.45x faster                                                         |
| hexiom                   | 10.9 ms                                                               | 7.57 ms: 1.44x faster                                                        |
| crypto_pyaes             | 134 ms                                                                | 93.5 ms: 1.43x faster                                                        |
| logging_simple           | 9.78 us                                                               | 6.86 us: 1.43x faster                                                        |
| nbody                    | 166 ms                                                                | 117 ms: 1.42x faster                                                         |
| comprehensions           | 33.1 us                                                               | 23.4 us: 1.41x faster                                                        |
| html5lib                 | 86.5 ms                                                               | 61.5 ms: 1.41x faster                                                        |
| logging_format           | 10.6 us                                                               | 7.57 us: 1.40x faster                                                        |
| thrift                   | 1.26 ms                                                               | 906 us: 1.39x faster                                                         |
| django_template          | 53.3 ms                                                               | 38.5 ms: 1.38x faster                                                        |
| dulwich_log              | 73.5 ms                                                               | 53.8 ms: 1.37x faster                                                        |
| sqlalchemy_declarative   | 197 ms                                                                | 145 ms: 1.36x faster                                                         |
| pickle_pure_python       | 529 us                                                                | 392 us: 1.35x faster                                                         |
| deepcopy_reduce          | 4.60 us                                                               | 3.42 us: 1.35x faster                                                        |
| coroutines               | 37.2 ms                                                               | 27.8 ms: 1.34x faster                                                        |
| genshi_text              | 35.2 ms                                                               | 26.5 ms: 1.33x faster                                                        |
| sqlalchemy_imperative    | 20.5 ms                                                               | 15.5 ms: 1.32x faster                                                        |
| xml_etree_process        | 99.5 ms                                                               | 76.3 ms: 1.30x faster                                                        |
| scimark_fft              | 500 ms                                                                | 385 ms: 1.30x faster                                                         |
| pycparser                | 1.69 sec                                                              | 1.33 sec: 1.28x faster                                                       |
| 2to3                     | 381 ms                                                                | 300 ms: 1.27x faster                                                         |
| sympy_sum                | 184 ms                                                                | 147 ms: 1.25x faster                                                         |
| sympy_integrate          | 26.5 ms                                                               | 21.4 ms: 1.24x faster                                                        |
| sympy_str                | 329 ms                                                                | 268 ms: 1.23x faster                                                         |
| xml_etree_parse          | 212 ms                                                                | 175 ms: 1.21x faster                                                         |
| fannkuch                 | 546 ms                                                                | 457 ms: 1.19x faster                                                         |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.41 ms: 1.19x faster                                                        |
| bench_thread_pool        | 1.59 ms                                                               | 1.35 ms: 1.18x faster                                                        |
| json_dumps               | 16.7 ms                                                               | 14.2 ms: 1.17x faster                                                        |
| sympy_expand             | 543 ms                                                                | 466 ms: 1.16x faster                                                         |
| genshi_xml               | 69.8 ms                                                               | 60.0 ms: 1.16x faster                                                        |
| pathlib                  | 26.3 ms                                                               | 22.7 ms: 1.16x faster                                                        |
| docutils                 | 3.53 sec                                                              | 3.07 sec: 1.15x faster                                                       |
| regex_v8                 | 32.2 ms                                                               | 28.0 ms: 1.15x faster                                                        |
| nqueens                  | 117 ms                                                                | 102 ms: 1.15x faster                                                         |
| xml_etree_generate       | 123 ms                                                                | 108 ms: 1.14x faster                                                         |
| sqlite_synth             | 4.12 us                                                               | 3.63 us: 1.13x faster                                                        |
| mdp                      | 3.70 sec                                                              | 3.30 sec: 1.12x faster                                                       |
| xml_etree_iterparse      | 156 ms                                                                | 142 ms: 1.10x faster                                                         |
| regex_effbot             | 4.25 ms                                                               | 3.92 ms: 1.08x faster                                                        |
| meteor_contest           | 126 ms                                                                | 118 ms: 1.07x faster                                                         |
| pprint_safe_repr         | 1.15 sec                                                              | 1.11 sec: 1.03x faster                                                       |
| regex_dna                | 257 ms                                                                | 249 ms: 1.03x faster                                                         |
| pprint_pformat           | 2.36 sec                                                              | 2.31 sec: 1.02x faster                                                       |
| json                     | 5.88 ms                                                               | 5.80 ms: 1.01x faster                                                        |
| async_generators         | 452 ms                                                                | 458 ms: 1.01x slower                                                         |
| telco                    | 8.49 ms                                                               | 9.24 ms: 1.09x slower                                                        |
| json_loads               | 30.9 us                                                               | 34.1 us: 1.10x slower                                                        |
| coverage                 | 83.6 ms                                                               | 97.5 ms: 1.17x slower                                                        |
| python_startup           | 11.2 ms                                                               | 16.1 ms: 1.44x slower                                                        |
| python_startup_no_site   | 6.89 ms                                                               | 10.1 ms: 1.47x slower                                                        |
| gc_traversal             | 4.15 ms                                                               | 6.57 ms: 1.58x slower                                                        |
| create_gc_cycles         | 2.26 ms                                                               | 3.73 ms: 1.65x slower                                                        |
| bench_mp_pool            | 14.5 ms                                                               | 2.82 sec: 194.13x slower                                                     |
| Geometric mean           | (ref)                                                                 | 1.24x faster                                                                 |

Benchmark hidden because not significant (2): pidigits, asyncio_websockets
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250310-3.14.0a5+-460d0d3-JIT/bm-20250310-arminc-aarch64-diegorusso-remove_jumps_aarch64-3.14.0a5+-460d0d3.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.334x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.32x