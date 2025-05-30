# Results vs. 3.10.4

- fork: faster-cpython
- ref: current_executor
- machine: linux-x86_64
- commit hash: a30e444
- commit date: 2025-05-03
- overall geometric mean: 1.452x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.32x faster
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250503-linux-x86_64-faster%2dcpython-current_executor-3.14.0a7+-a30e444 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 258 ms: 1.35x faster                                                         |
| docutils       | 3.30 sec                                               | 2.68 sec: 1.23x faster                                                       |
| html5lib       | 88.9 ms                                                | 60.9 ms: 1.46x faster                                                        |
| Geometric mean | (ref)                                                  | 1.34x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250503-linux-x86_64-faster%2dcpython-current_executor-3.14.0a7+-a30e444 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 595 ms: 2.97x faster                                                         |
| async_tree_none         | 728 ms                                                 | 261 ms: 2.79x faster                                                         |
| async_tree_memoization  | 870 ms                                                 | 312 ms: 2.79x faster                                                         |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 492 ms: 2.06x faster                                                         |
| Geometric mean          | (ref)                                                  | 2.63x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250503-linux-x86_64-faster%2dcpython-current_executor-3.14.0a7+-a30e444 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 64.7 ms: 1.81x faster                                                        |
| nbody          | 154 ms                                                 | 93.9 ms: 1.63x faster                                                        |
| pidigits       | 191 ms                                                 | 186 ms: 1.02x faster                                                         |
| Geometric mean | (ref)                                                  | 1.45x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250503-linux-x86_64-faster%2dcpython-current_executor-3.14.0a7+-a30e444 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 128 ms: 1.48x faster                                                         |
| regex_v8       | 27.8 ms                                                | 23.3 ms: 1.19x faster                                                        |
| regex_dna      | 227 ms                                                 | 210 ms: 1.08x faster                                                         |
| regex_effbot   | 3.63 ms                                                | 3.39 ms: 1.07x faster                                                        |
| Geometric mean | (ref)                                                  | 1.19x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250503-linux-x86_64-faster%2dcpython-current_executor-3.14.0a7+-a30e444 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.88 sec: 1.67x faster                                                       |
| unpickle_pure_python | 331 us                                                 | 209 us: 1.58x faster                                                         |
| pickle_pure_python   | 484 us                                                 | 323 us: 1.50x faster                                                         |
| xml_etree_process    | 79.1 ms                                                | 56.6 ms: 1.40x faster                                                        |
| xml_etree_generate   | 99.4 ms                                                | 80.6 ms: 1.23x faster                                                        |
| xml_etree_parse      | 168 ms                                                 | 140 ms: 1.20x faster                                                         |
| json_dumps           | 14.2 ms                                                | 12.0 ms: 1.18x faster                                                        |
| xml_etree_iterparse  | 115 ms                                                 | 98.7 ms: 1.17x faster                                                        |
| json_loads           | 31.2 us                                                | 30.1 us: 1.04x faster                                                        |
| Geometric mean       | (ref)                                                  | 1.31x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250503-linux-x86_64-faster%2dcpython-current_executor-3.14.0a7+-a30e444 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.2 ms: 1.10x faster                                                        |
| python_startup_no_site | 5.93 ms                                                | 6.97 ms: 1.17x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250503-linux-x86_64-faster%2dcpython-current_executor-3.14.0a7+-a30e444 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 20.8 ms: 1.53x faster                                                        |
| django_template | 48.2 ms                                                | 32.4 ms: 1.48x faster                                                        |
| mako            | 16.3 ms                                                | 11.3 ms: 1.45x faster                                                        |
| genshi_xml      | 66.0 ms                                                | 49.1 ms: 1.35x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250503-linux-x86_64-faster%2dcpython-current_executor-3.14.0a7+-a30e444 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 173 us: 3.14x faster                                                         |
| async_tree_io            | 1.77 sec                                               | 595 ms: 2.97x faster                                                         |
| async_tree_none          | 728 ms                                                 | 261 ms: 2.79x faster                                                         |
| async_tree_memoization   | 870 ms                                                 | 312 ms: 2.79x faster                                                         |
| generators               | 80.1 ms                                                | 30.0 ms: 2.67x faster                                                        |
| deltablue                | 7.91 ms                                                | 3.08 ms: 2.57x faster                                                        |
| richards_super           | 94.7 ms                                                | 40.6 ms: 2.33x faster                                                        |
| mdp                      | 2.85 sec                                               | 1.23 sec: 2.32x faster                                                       |
| richards                 | 79.3 ms                                                | 35.4 ms: 2.24x faster                                                        |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 492 ms: 2.06x faster                                                         |
| deepcopy_memo            | 58.5 us                                                | 29.5 us: 1.98x faster                                                        |
| logging_silent           | 190 ns                                                 | 96.8 ns: 1.96x faster                                                        |
| pylint                   | 551 ms                                                 | 284 ms: 1.94x faster                                                         |
| go                       | 240 ms                                                 | 125 ms: 1.92x faster                                                         |
| chaos                    | 115 ms                                                 | 60.6 ms: 1.90x faster                                                        |
| deepcopy                 | 479 us                                                 | 254 us: 1.88x faster                                                         |
| raytrace                 | 507 ms                                                 | 276 ms: 1.84x faster                                                         |
| float                    | 117 ms                                                 | 64.7 ms: 1.81x faster                                                        |
| scimark_sor              | 220 ms                                                 | 121 ms: 1.81x faster                                                         |
| scimark_monte_carlo      | 118 ms                                                 | 68.8 ms: 1.72x faster                                                        |
| crypto_pyaes             | 128 ms                                                 | 76.2 ms: 1.68x faster                                                        |
| tomli_loads              | 3.14 sec                                               | 1.88 sec: 1.67x faster                                                       |
| spectral_norm            | 170 ms                                                 | 103 ms: 1.65x faster                                                         |
| nbody                    | 154 ms                                                 | 93.9 ms: 1.63x faster                                                        |
| pyflate                  | 716 ms                                                 | 444 ms: 1.61x faster                                                         |
| unpickle_pure_python     | 331 us                                                 | 209 us: 1.58x faster                                                         |
| comprehensions           | 28.8 us                                                | 18.3 us: 1.57x faster                                                        |
| deepcopy_reduce          | 4.17 us                                                | 2.67 us: 1.56x faster                                                        |
| hexiom                   | 10.4 ms                                                | 6.74 ms: 1.54x faster                                                        |
| genshi_text              | 31.8 ms                                                | 20.8 ms: 1.53x faster                                                        |
| pickle_pure_python       | 484 us                                                 | 323 us: 1.50x faster                                                         |
| django_template          | 48.2 ms                                                | 32.4 ms: 1.48x faster                                                        |
| regex_compile            | 188 ms                                                 | 128 ms: 1.48x faster                                                         |
| scimark_lu               | 176 ms                                                 | 120 ms: 1.46x faster                                                         |
| html5lib                 | 88.9 ms                                                | 60.9 ms: 1.46x faster                                                        |
| mako                     | 16.3 ms                                                | 11.3 ms: 1.45x faster                                                        |
| logging_simple           | 8.30 us                                                | 5.76 us: 1.44x faster                                                        |
| logging_format           | 9.09 us                                                | 6.35 us: 1.43x faster                                                        |
| scimark_fft              | 466 ms                                                 | 328 ms: 1.42x faster                                                         |
| xml_etree_process        | 79.1 ms                                                | 56.6 ms: 1.40x faster                                                        |
| dulwich_log              | 84.3 ms                                                | 60.9 ms: 1.38x faster                                                        |
| pprint_pformat           | 2.10 sec                                               | 1.52 sec: 1.38x faster                                                       |
| coroutines               | 35.1 ms                                                | 25.5 ms: 1.38x faster                                                        |
| pycparser                | 1.58 sec                                               | 1.15 sec: 1.37x faster                                                       |
| pprint_safe_repr         | 1.02 sec                                               | 747 ms: 1.36x faster                                                         |
| 2to3                     | 348 ms                                                 | 258 ms: 1.35x faster                                                         |
| genshi_xml               | 66.0 ms                                                | 49.1 ms: 1.35x faster                                                        |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.4 ms: 1.34x faster                                                        |
| sympy_integrate          | 25.8 ms                                                | 19.3 ms: 1.33x faster                                                        |
| sympy_sum                | 196 ms                                                 | 148 ms: 1.32x faster                                                         |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.92 ms: 1.32x faster                                                        |
| fannkuch                 | 532 ms                                                 | 407 ms: 1.31x faster                                                         |
| nqueens                  | 106 ms                                                 | 81.7 ms: 1.30x faster                                                        |
| sqlalchemy_declarative   | 172 ms                                                 | 135 ms: 1.28x faster                                                         |
| sympy_str                | 346 ms                                                 | 271 ms: 1.28x faster                                                         |
| xml_etree_generate       | 99.4 ms                                                | 80.6 ms: 1.23x faster                                                        |
| docutils                 | 3.30 sec                                               | 2.68 sec: 1.23x faster                                                       |
| pathlib                  | 20.5 ms                                                | 17.0 ms: 1.21x faster                                                        |
| xml_etree_parse          | 168 ms                                                 | 140 ms: 1.20x faster                                                         |
| sympy_expand             | 566 ms                                                 | 473 ms: 1.19x faster                                                         |
| regex_v8                 | 27.8 ms                                                | 23.3 ms: 1.19x faster                                                        |
| json_dumps               | 14.2 ms                                                | 12.0 ms: 1.18x faster                                                        |
| xml_etree_iterparse      | 115 ms                                                 | 98.7 ms: 1.17x faster                                                        |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                                         |
| bench_thread_pool        | 986 us                                                 | 894 us: 1.10x faster                                                         |
| python_startup           | 14.6 ms                                                | 13.2 ms: 1.10x faster                                                        |
| sqlite_synth             | 3.02 us                                                | 2.76 us: 1.09x faster                                                        |
| regex_dna                | 227 ms                                                 | 210 ms: 1.08x faster                                                         |
| regex_effbot             | 3.63 ms                                                | 3.39 ms: 1.07x faster                                                        |
| json                     | 5.69 ms                                                | 5.36 ms: 1.06x faster                                                        |
| async_generators         | 444 ms                                                 | 423 ms: 1.05x faster                                                         |
| json_loads               | 31.2 us                                                | 30.1 us: 1.04x faster                                                        |
| pidigits                 | 191 ms                                                 | 186 ms: 1.02x faster                                                         |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                         |
| telco                    | 7.27 ms                                                | 7.87 ms: 1.08x slower                                                        |
| python_startup_no_site   | 5.93 ms                                                | 6.97 ms: 1.17x slower                                                        |
| coverage                 | 79.4 ms                                                | 93.4 ms: 1.18x slower                                                        |
| gc_traversal             | 3.62 ms                                                | 5.08 ms: 1.40x slower                                                        |
| create_gc_cycles         | 1.62 ms                                                | 2.50 ms: 1.54x slower                                                        |
| bench_mp_pool            | 24.0 ms                                                | 82.9 ms: 3.45x slower                                                        |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                                 |
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (23) of results/bm-20250503-3.14.0a7+-a30e444-JIT/bm-20250503-linux-x86_64-faster%2dcpython-current_executor-3.14.0a7+-a30e444.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.452x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.36x
- 95% likely to have a speedup of 1.34x
- 99% likely to have a speedup of 1.32x

# Memory
- memory change: 1.31x