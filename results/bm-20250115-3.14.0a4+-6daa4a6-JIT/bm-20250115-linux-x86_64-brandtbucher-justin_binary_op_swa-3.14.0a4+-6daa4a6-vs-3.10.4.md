# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_binary_op_swa
- machine: linux-x86_64
- commit hash: 6daa4a6
- commit date: 2025-01-15
- overall geometric mean: 1.426x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250115-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a4+-6daa4a6 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 260 ms: 1.34x faster                                                         |
| docutils       | 3.30 sec                                               | 2.69 sec: 1.22x faster                                                       |
| html5lib       | 88.9 ms                                                | 63.9 ms: 1.39x faster                                                        |
| Geometric mean | (ref)                                                  | 1.32x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250115-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a4+-6daa4a6 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 616 ms: 2.87x faster                                                         |
| async_tree_none         | 728 ms                                                 | 266 ms: 2.74x faster                                                         |
| async_tree_memoization  | 870 ms                                                 | 332 ms: 2.62x faster                                                         |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 500 ms: 2.03x faster                                                         |
| Geometric mean          | (ref)                                                  | 2.54x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250115-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a4+-6daa4a6 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 85.2 ms: 1.80x faster                                                        |
| float          | 117 ms                                                 | 69.1 ms: 1.69x faster                                                        |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                         |
| Geometric mean | (ref)                                                  | 1.46x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250115-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a4+-6daa4a6 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 130 ms: 1.46x faster                                                         |
| regex_effbot   | 3.63 ms                                                | 3.12 ms: 1.17x faster                                                        |
| regex_v8       | 27.8 ms                                                | 24.2 ms: 1.15x faster                                                        |
| regex_dna      | 227 ms                                                 | 203 ms: 1.11x faster                                                         |
| Geometric mean | (ref)                                                  | 1.21x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250115-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a4+-6daa4a6 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.83 sec: 1.71x faster                                                       |
| unpickle_pure_python | 331 us                                                 | 196 us: 1.68x faster                                                         |
| pickle_pure_python   | 484 us                                                 | 316 us: 1.53x faster                                                         |
| xml_etree_process    | 79.1 ms                                                | 54.8 ms: 1.44x faster                                                        |
| xml_etree_generate   | 99.4 ms                                                | 77.9 ms: 1.28x faster                                                        |
| xml_etree_parse      | 168 ms                                                 | 136 ms: 1.24x faster                                                         |
| json_dumps           | 14.2 ms                                                | 11.6 ms: 1.22x faster                                                        |
| xml_etree_iterparse  | 115 ms                                                 | 94.9 ms: 1.22x faster                                                        |
| json_loads           | 31.2 us                                                | 29.8 us: 1.05x faster                                                        |
| Geometric mean       | (ref)                                                  | 1.36x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250115-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a4+-6daa4a6 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.9 ms: 1.13x faster                                                        |
| python_startup_no_site | 5.93 ms                                                | 7.11 ms: 1.20x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250115-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a4+-6daa4a6 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.94 ms: 1.64x faster                                                        |
| django_template | 48.2 ms                                                | 34.1 ms: 1.41x faster                                                        |
| genshi_text     | 31.8 ms                                                | 23.6 ms: 1.35x faster                                                        |
| genshi_xml      | 66.0 ms                                                | 59.2 ms: 1.12x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.37x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250115-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a4+-6daa4a6 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 167 us: 3.25x faster                                                         |
| async_tree_io            | 1.77 sec                                               | 616 ms: 2.87x faster                                                         |
| async_tree_none          | 728 ms                                                 | 266 ms: 2.74x faster                                                         |
| async_tree_memoization   | 870 ms                                                 | 332 ms: 2.62x faster                                                         |
| deltablue                | 7.91 ms                                                | 3.24 ms: 2.44x faster                                                        |
| generators               | 80.1 ms                                                | 37.8 ms: 2.12x faster                                                        |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 500 ms: 2.03x faster                                                         |
| deepcopy_memo            | 58.5 us                                                | 30.3 us: 1.93x faster                                                        |
| pylint                   | 551 ms                                                 | 288 ms: 1.92x faster                                                         |
| scimark_sor              | 220 ms                                                 | 115 ms: 1.91x faster                                                         |
| richards_super           | 94.7 ms                                                | 49.9 ms: 1.90x faster                                                        |
| scimark_monte_carlo      | 118 ms                                                 | 63.0 ms: 1.88x faster                                                        |
| chaos                    | 115 ms                                                 | 63.1 ms: 1.83x faster                                                        |
| richards                 | 79.3 ms                                                | 43.7 ms: 1.81x faster                                                        |
| nbody                    | 154 ms                                                 | 85.2 ms: 1.80x faster                                                        |
| crypto_pyaes             | 128 ms                                                 | 71.6 ms: 1.79x faster                                                        |
| logging_silent           | 190 ns                                                 | 107 ns: 1.77x faster                                                         |
| go                       | 240 ms                                                 | 136 ms: 1.77x faster                                                         |
| deepcopy                 | 479 us                                                 | 272 us: 1.76x faster                                                         |
| raytrace                 | 507 ms                                                 | 291 ms: 1.74x faster                                                         |
| tomli_loads              | 3.14 sec                                               | 1.83 sec: 1.71x faster                                                       |
| sqlglot_parse            | 2.17 ms                                                | 1.27 ms: 1.71x faster                                                        |
| float                    | 117 ms                                                 | 69.1 ms: 1.69x faster                                                        |
| unpickle_pure_python     | 331 us                                                 | 196 us: 1.68x faster                                                         |
| comprehensions           | 28.8 us                                                | 17.2 us: 1.67x faster                                                        |
| pyflate                  | 716 ms                                                 | 435 ms: 1.65x faster                                                         |
| mako                     | 16.3 ms                                                | 9.94 ms: 1.64x faster                                                        |
| sqlglot_transpile        | 2.57 ms                                                | 1.58 ms: 1.63x faster                                                        |
| spectral_norm            | 170 ms                                                 | 106 ms: 1.60x faster                                                         |
| pickle_pure_python       | 484 us                                                 | 316 us: 1.53x faster                                                         |
| coroutines               | 35.1 ms                                                | 23.2 ms: 1.51x faster                                                        |
| deepcopy_reduce          | 4.17 us                                                | 2.78 us: 1.50x faster                                                        |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.50x faster                                                         |
| scimark_fft              | 466 ms                                                 | 319 ms: 1.46x faster                                                         |
| regex_compile            | 188 ms                                                 | 130 ms: 1.46x faster                                                         |
| hexiom                   | 10.4 ms                                                | 7.17 ms: 1.45x faster                                                        |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.47 ms: 1.45x faster                                                        |
| xml_etree_process        | 79.1 ms                                                | 54.8 ms: 1.44x faster                                                        |
| logging_simple           | 8.30 us                                                | 5.76 us: 1.44x faster                                                        |
| logging_format           | 9.09 us                                                | 6.33 us: 1.44x faster                                                        |
| django_template          | 48.2 ms                                                | 34.1 ms: 1.41x faster                                                        |
| pycparser                | 1.58 sec                                               | 1.13 sec: 1.40x faster                                                       |
| html5lib                 | 88.9 ms                                                | 63.9 ms: 1.39x faster                                                        |
| thrift                   | 1.07 ms                                                | 775 us: 1.38x faster                                                         |
| pprint_pformat           | 2.10 sec                                               | 1.53 sec: 1.37x faster                                                       |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.2 ms: 1.36x faster                                                        |
| pprint_safe_repr         | 1.02 sec                                               | 752 ms: 1.35x faster                                                         |
| genshi_text              | 31.8 ms                                                | 23.6 ms: 1.35x faster                                                        |
| fannkuch                 | 532 ms                                                 | 396 ms: 1.34x faster                                                         |
| 2to3                     | 348 ms                                                 | 260 ms: 1.34x faster                                                         |
| sqlalchemy_declarative   | 172 ms                                                 | 131 ms: 1.31x faster                                                         |
| sqlglot_normalize        | 143 ms                                                 | 109 ms: 1.31x faster                                                         |
| xml_etree_generate       | 99.4 ms                                                | 77.9 ms: 1.28x faster                                                        |
| sqlglot_optimize         | 69.2 ms                                                | 54.9 ms: 1.26x faster                                                        |
| pathlib                  | 20.5 ms                                                | 16.3 ms: 1.25x faster                                                        |
| sympy_sum                | 196 ms                                                 | 158 ms: 1.24x faster                                                         |
| sympy_integrate          | 25.8 ms                                                | 20.8 ms: 1.24x faster                                                        |
| xml_etree_parse          | 168 ms                                                 | 136 ms: 1.24x faster                                                         |
| dulwich_log              | 84.3 ms                                                | 68.3 ms: 1.24x faster                                                        |
| docutils                 | 3.30 sec                                               | 2.69 sec: 1.22x faster                                                       |
| sympy_str                | 346 ms                                                 | 283 ms: 1.22x faster                                                         |
| json_dumps               | 14.2 ms                                                | 11.6 ms: 1.22x faster                                                        |
| xml_etree_iterparse      | 115 ms                                                 | 94.9 ms: 1.22x faster                                                        |
| sympy_expand             | 566 ms                                                 | 478 ms: 1.18x faster                                                         |
| regex_effbot             | 3.63 ms                                                | 3.12 ms: 1.17x faster                                                        |
| nqueens                  | 106 ms                                                 | 91.6 ms: 1.15x faster                                                        |
| regex_v8                 | 27.8 ms                                                | 24.2 ms: 1.15x faster                                                        |
| python_startup           | 14.6 ms                                                | 12.9 ms: 1.13x faster                                                        |
| mdp                      | 2.85 sec                                               | 2.55 sec: 1.12x faster                                                       |
| genshi_xml               | 66.0 ms                                                | 59.2 ms: 1.12x faster                                                        |
| regex_dna                | 227 ms                                                 | 203 ms: 1.11x faster                                                         |
| sqlite_synth             | 3.02 us                                                | 2.74 us: 1.10x faster                                                        |
| bench_thread_pool        | 986 us                                                 | 897 us: 1.10x faster                                                         |
| meteor_contest           | 120 ms                                                 | 109 ms: 1.10x faster                                                         |
| async_generators         | 444 ms                                                 | 407 ms: 1.09x faster                                                         |
| json                     | 5.69 ms                                                | 5.28 ms: 1.08x faster                                                        |
| json_loads               | 31.2 us                                                | 29.8 us: 1.05x faster                                                        |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                         |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                         |
| telco                    | 7.27 ms                                                | 7.70 ms: 1.06x slower                                                        |
| coverage                 | 79.4 ms                                                | 90.0 ms: 1.13x slower                                                        |
| python_startup_no_site   | 5.93 ms                                                | 7.11 ms: 1.20x slower                                                        |
| gc_traversal             | 3.62 ms                                                | 5.04 ms: 1.39x slower                                                        |
| create_gc_cycles         | 1.62 ms                                                | 2.47 ms: 1.52x slower                                                        |
| bench_mp_pool            | 24.0 ms                                                | 81.6 ms: 3.40x slower                                                        |
| Geometric mean           | (ref)                                                  | 1.40x faster                                                                 |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250115-3.14.0a4+-6daa4a6-JIT/bm-20250115-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a4+-6daa4a6.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.426x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.28x

# Memory
- memory change: 1.28x