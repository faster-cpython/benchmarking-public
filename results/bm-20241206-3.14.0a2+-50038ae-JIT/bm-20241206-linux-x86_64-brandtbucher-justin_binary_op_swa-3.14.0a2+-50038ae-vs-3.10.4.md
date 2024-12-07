# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_binary_op_swa
- machine: linux-x86_64
- commit hash: 50038ae
- commit date: 2024-12-06
- overall geometric mean: 1.421x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241206-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-50038ae |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 259 ms: 1.35x faster                                                         |
| docutils       | 3.30 sec                                               | 2.68 sec: 1.23x faster                                                       |
| html5lib       | 88.9 ms                                                | 65.6 ms: 1.35x faster                                                        |
| Geometric mean | (ref)                                                  | 1.31x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241206-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-50038ae |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 620 ms: 2.85x faster                                                         |
| async_tree_none         | 728 ms                                                 | 272 ms: 2.68x faster                                                         |
| async_tree_memoization  | 870 ms                                                 | 343 ms: 2.53x faster                                                         |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 507 ms: 2.00x faster                                                         |
| Geometric mean          | (ref)                                                  | 2.50x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241206-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-50038ae |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 94.2 ms: 1.63x faster                                                        |
| float          | 117 ms                                                 | 76.8 ms: 1.52x faster                                                        |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                         |
| Geometric mean | (ref)                                                  | 1.36x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241206-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-50038ae |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 130 ms: 1.45x faster                                                         |
| regex_v8       | 27.8 ms                                                | 25.2 ms: 1.10x faster                                                        |
| regex_effbot   | 3.63 ms                                                | 3.47 ms: 1.05x faster                                                        |
| regex_dna      | 227 ms                                                 | 217 ms: 1.05x faster                                                         |
| Geometric mean | (ref)                                                  | 1.15x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241206-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-50038ae |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 197 us: 1.68x faster                                                         |
| tomli_loads          | 3.14 sec                                               | 1.96 sec: 1.60x faster                                                       |
| pickle_pure_python   | 484 us                                                 | 322 us: 1.50x faster                                                         |
| xml_etree_process    | 79.1 ms                                                | 54.9 ms: 1.44x faster                                                        |
| json_dumps           | 14.2 ms                                                | 11.1 ms: 1.27x faster                                                        |
| xml_etree_generate   | 99.4 ms                                                | 80.5 ms: 1.24x faster                                                        |
| xml_etree_iterparse  | 115 ms                                                 | 94.7 ms: 1.22x faster                                                        |
| xml_etree_parse      | 168 ms                                                 | 138 ms: 1.22x faster                                                         |
| json_loads           | 31.2 us                                                | 26.1 us: 1.20x faster                                                        |
| Geometric mean       | (ref)                                                  | 1.36x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241206-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-50038ae |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.7 ms: 1.15x faster                                                        |
| python_startup_no_site | 5.93 ms                                                | 7.03 ms: 1.19x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241206-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-50038ae |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.1 ms: 1.62x faster                                                        |
| django_template | 48.2 ms                                                | 33.9 ms: 1.42x faster                                                        |
| genshi_text     | 31.8 ms                                                | 24.4 ms: 1.31x faster                                                        |
| genshi_xml      | 66.0 ms                                                | 56.5 ms: 1.17x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.37x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241206-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-50038ae |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 170 us: 3.21x faster                                                         |
| async_tree_io            | 1.77 sec                                               | 620 ms: 2.85x faster                                                         |
| async_tree_none          | 728 ms                                                 | 272 ms: 2.68x faster                                                         |
| async_tree_memoization   | 870 ms                                                 | 343 ms: 2.53x faster                                                         |
| deltablue                | 7.91 ms                                                | 3.19 ms: 2.48x faster                                                        |
| generators               | 80.1 ms                                                | 36.4 ms: 2.20x faster                                                        |
| richards_super           | 94.7 ms                                                | 44.1 ms: 2.15x faster                                                        |
| richards                 | 79.3 ms                                                | 38.0 ms: 2.09x faster                                                        |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 507 ms: 2.00x faster                                                         |
| deepcopy_memo            | 58.5 us                                                | 29.2 us: 2.00x faster                                                        |
| pylint                   | 551 ms                                                 | 287 ms: 1.92x faster                                                         |
| logging_silent           | 190 ns                                                 | 101 ns: 1.89x faster                                                         |
| chaos                    | 115 ms                                                 | 63.4 ms: 1.82x faster                                                        |
| scimark_sor              | 220 ms                                                 | 121 ms: 1.81x faster                                                         |
| crypto_pyaes             | 128 ms                                                 | 70.8 ms: 1.80x faster                                                        |
| scimark_monte_carlo      | 118 ms                                                 | 65.9 ms: 1.79x faster                                                        |
| deepcopy                 | 479 us                                                 | 269 us: 1.78x faster                                                         |
| go                       | 240 ms                                                 | 135 ms: 1.78x faster                                                         |
| djangocms                | 38.4 us                                                | 22.0 us: 1.74x faster                                                        |
| raytrace                 | 507 ms                                                 | 298 ms: 1.70x faster                                                         |
| unpickle_pure_python     | 331 us                                                 | 197 us: 1.68x faster                                                         |
| comprehensions           | 28.8 us                                                | 17.3 us: 1.66x faster                                                        |
| sqlglot_parse            | 2.17 ms                                                | 1.33 ms: 1.63x faster                                                        |
| nbody                    | 154 ms                                                 | 94.2 ms: 1.63x faster                                                        |
| mako                     | 16.3 ms                                                | 10.1 ms: 1.62x faster                                                        |
| tomli_loads              | 3.14 sec                                               | 1.96 sec: 1.60x faster                                                       |
| sqlglot_transpile        | 2.57 ms                                                | 1.64 ms: 1.57x faster                                                        |
| pyflate                  | 716 ms                                                 | 461 ms: 1.55x faster                                                         |
| scimark_lu               | 176 ms                                                 | 114 ms: 1.55x faster                                                         |
| deepcopy_reduce          | 4.17 us                                                | 2.72 us: 1.53x faster                                                        |
| float                    | 117 ms                                                 | 76.8 ms: 1.52x faster                                                        |
| pickle_pure_python       | 484 us                                                 | 322 us: 1.50x faster                                                         |
| coroutines               | 35.1 ms                                                | 23.9 ms: 1.47x faster                                                        |
| hexiom                   | 10.4 ms                                                | 7.13 ms: 1.46x faster                                                        |
| regex_compile            | 188 ms                                                 | 130 ms: 1.45x faster                                                         |
| xml_etree_process        | 79.1 ms                                                | 54.9 ms: 1.44x faster                                                        |
| pprint_safe_repr         | 1.02 sec                                               | 713 ms: 1.43x faster                                                         |
| pprint_pformat           | 2.10 sec                                               | 1.47 sec: 1.43x faster                                                       |
| django_template          | 48.2 ms                                                | 33.9 ms: 1.42x faster                                                        |
| logging_format           | 9.09 us                                                | 6.41 us: 1.42x faster                                                        |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.6 ms: 1.40x faster                                                        |
| logging_simple           | 8.30 us                                                | 5.92 us: 1.40x faster                                                        |
| spectral_norm            | 170 ms                                                 | 121 ms: 1.40x faster                                                         |
| thrift                   | 1.07 ms                                                | 779 us: 1.38x faster                                                         |
| pycparser                | 1.58 sec                                               | 1.15 sec: 1.37x faster                                                       |
| scimark_fft              | 466 ms                                                 | 341 ms: 1.36x faster                                                         |
| html5lib                 | 88.9 ms                                                | 65.6 ms: 1.35x faster                                                        |
| 2to3                     | 348 ms                                                 | 259 ms: 1.35x faster                                                         |
| fannkuch                 | 532 ms                                                 | 396 ms: 1.34x faster                                                         |
| sqlalchemy_declarative   | 172 ms                                                 | 129 ms: 1.33x faster                                                         |
| genshi_text              | 31.8 ms                                                | 24.4 ms: 1.31x faster                                                        |
| sqlglot_normalize        | 143 ms                                                 | 110 ms: 1.30x faster                                                         |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.07 ms: 1.27x faster                                                        |
| json_dumps               | 14.2 ms                                                | 11.1 ms: 1.27x faster                                                        |
| sympy_sum                | 196 ms                                                 | 156 ms: 1.26x faster                                                         |
| sqlglot_optimize         | 69.2 ms                                                | 55.4 ms: 1.25x faster                                                        |
| sympy_integrate          | 25.8 ms                                                | 20.7 ms: 1.25x faster                                                        |
| pathlib                  | 20.5 ms                                                | 16.4 ms: 1.25x faster                                                        |
| dulwich_log              | 84.3 ms                                                | 68.2 ms: 1.24x faster                                                        |
| xml_etree_generate       | 99.4 ms                                                | 80.5 ms: 1.24x faster                                                        |
| docutils                 | 3.30 sec                                               | 2.68 sec: 1.23x faster                                                       |
| sympy_str                | 346 ms                                                 | 283 ms: 1.22x faster                                                         |
| xml_etree_iterparse      | 115 ms                                                 | 94.7 ms: 1.22x faster                                                        |
| xml_etree_parse          | 168 ms                                                 | 138 ms: 1.22x faster                                                         |
| json_loads               | 31.2 us                                                | 26.1 us: 1.20x faster                                                        |
| sympy_expand             | 566 ms                                                 | 474 ms: 1.19x faster                                                         |
| genshi_xml               | 66.0 ms                                                | 56.5 ms: 1.17x faster                                                        |
| json                     | 5.69 ms                                                | 4.89 ms: 1.16x faster                                                        |
| nqueens                  | 106 ms                                                 | 91.4 ms: 1.16x faster                                                        |
| python_startup           | 14.6 ms                                                | 12.7 ms: 1.15x faster                                                        |
| bench_thread_pool        | 986 us                                                 | 875 us: 1.13x faster                                                         |
| mdp                      | 2.85 sec                                               | 2.57 sec: 1.11x faster                                                       |
| regex_v8                 | 27.8 ms                                                | 25.2 ms: 1.10x faster                                                        |
| meteor_contest           | 120 ms                                                 | 109 ms: 1.09x faster                                                         |
| sqlite_synth             | 3.02 us                                                | 2.82 us: 1.07x faster                                                        |
| regex_effbot             | 3.63 ms                                                | 3.47 ms: 1.05x faster                                                        |
| regex_dna                | 227 ms                                                 | 217 ms: 1.05x faster                                                         |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                         |
| asyncio_websockets       | 559 ms                                                 | 553 ms: 1.01x faster                                                         |
| async_generators         | 444 ms                                                 | 451 ms: 1.02x slower                                                         |
| telco                    | 7.27 ms                                                | 7.64 ms: 1.05x slower                                                        |
| coverage                 | 79.4 ms                                                | 86.3 ms: 1.09x slower                                                        |
| python_startup_no_site   | 5.93 ms                                                | 7.03 ms: 1.19x slower                                                        |
| gc_traversal             | 3.62 ms                                                | 4.80 ms: 1.32x slower                                                        |
| create_gc_cycles         | 1.62 ms                                                | 2.46 ms: 1.52x slower                                                        |
| bench_mp_pool            | 24.0 ms                                                | 80.9 ms: 3.37x slower                                                        |
| Geometric mean           | (ref)                                                  | 1.40x faster                                                                 |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20241206-3.14.0a2+-50038ae-JIT/bm-20241206-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-50038ae.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.421x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.28x

# Memory
- memory change: 1.28x