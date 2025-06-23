# Results vs. 3.10.4

- fork: faster-cpython
- ref: explicit_check_perio
- machine: linux-x86_64
- commit hash: c84beef
- commit date: 2025-06-23
- overall geometric mean: 1.449x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.29x faster
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250623-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 255 ms: 1.37x faster                                                            |
| docutils       | 3.30 sec                                               | 2.59 sec: 1.27x faster                                                          |
| html5lib       | 88.9 ms                                                | 62.5 ms: 1.42x faster                                                           |
| Geometric mean | (ref)                                                  | 1.35x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250623-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 601 ms: 2.94x faster                                                            |
| async_tree_none         | 728 ms                                                 | 264 ms: 2.75x faster                                                            |
| async_tree_memoization  | 870 ms                                                 | 316 ms: 2.75x faster                                                            |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 508 ms: 2.00x faster                                                            |
| Geometric mean          | (ref)                                                  | 2.59x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250623-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 72.5 ms: 1.61x faster                                                           |
| nbody          | 154 ms                                                 | 95.5 ms: 1.61x faster                                                           |
| pidigits       | 191 ms                                                 | 193 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                  | 1.37x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250623-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 127 ms: 1.48x faster                                                            |
| regex_v8       | 27.8 ms                                                | 23.5 ms: 1.18x faster                                                           |
| regex_effbot   | 3.63 ms                                                | 3.33 ms: 1.09x faster                                                           |
| regex_dna      | 227 ms                                                 | 210 ms: 1.08x faster                                                            |
| Geometric mean | (ref)                                                  | 1.20x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250623-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 2.00 sec: 1.57x faster                                                          |
| pickle_pure_python   | 484 us                                                 | 321 us: 1.51x faster                                                            |
| unpickle_pure_python | 331 us                                                 | 222 us: 1.49x faster                                                            |
| xml_etree_process    | 79.1 ms                                                | 60.0 ms: 1.32x faster                                                           |
| json_dumps           | 14.2 ms                                                | 11.2 ms: 1.27x faster                                                           |
| xml_etree_parse      | 168 ms                                                 | 144 ms: 1.17x faster                                                            |
| xml_etree_generate   | 99.4 ms                                                | 85.6 ms: 1.16x faster                                                           |
| xml_etree_iterparse  | 115 ms                                                 | 99.6 ms: 1.16x faster                                                           |
| json_loads           | 31.2 us                                                | 28.3 us: 1.10x faster                                                           |
| Geometric mean       | (ref)                                                  | 1.30x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250623-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.2 ms: 1.19x faster                                                           |
| python_startup_no_site | 5.93 ms                                                | 6.95 ms: 1.17x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250623-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 21.2 ms: 1.50x faster                                                           |
| django_template | 48.2 ms                                                | 32.4 ms: 1.48x faster                                                           |
| mako            | 16.3 ms                                                | 11.5 ms: 1.42x faster                                                           |
| genshi_xml      | 66.0 ms                                                | 49.7 ms: 1.33x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250623-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 167 us: 3.25x faster                                                            |
| async_tree_io            | 1.77 sec                                               | 601 ms: 2.94x faster                                                            |
| async_tree_none          | 728 ms                                                 | 264 ms: 2.75x faster                                                            |
| async_tree_memoization   | 870 ms                                                 | 316 ms: 2.75x faster                                                            |
| generators               | 80.1 ms                                                | 29.7 ms: 2.70x faster                                                           |
| mdp                      | 2.85 sec                                               | 1.23 sec: 2.32x faster                                                          |
| deltablue                | 7.91 ms                                                | 3.45 ms: 2.29x faster                                                           |
| go                       | 240 ms                                                 | 111 ms: 2.17x faster                                                            |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 508 ms: 2.00x faster                                                            |
| pylint                   | 551 ms                                                 | 280 ms: 1.97x faster                                                            |
| richards_super           | 94.7 ms                                                | 48.8 ms: 1.94x faster                                                           |
| deepcopy_memo            | 58.5 us                                                | 30.3 us: 1.93x faster                                                           |
| chaos                    | 115 ms                                                 | 60.2 ms: 1.92x faster                                                           |
| scimark_sor              | 220 ms                                                 | 115 ms: 1.91x faster                                                            |
| raytrace                 | 507 ms                                                 | 268 ms: 1.89x faster                                                            |
| deepcopy                 | 479 us                                                 | 261 us: 1.84x faster                                                            |
| richards                 | 79.3 ms                                                | 43.2 ms: 1.84x faster                                                           |
| scimark_monte_carlo      | 118 ms                                                 | 65.7 ms: 1.80x faster                                                           |
| comprehensions           | 28.8 us                                                | 16.1 us: 1.79x faster                                                           |
| djangocms                | 38.4 us                                                | 22.2 us: 1.73x faster                                                           |
| hexiom                   | 10.4 ms                                                | 6.11 ms: 1.70x faster                                                           |
| crypto_pyaes             | 128 ms                                                 | 75.7 ms: 1.69x faster                                                           |
| pyflate                  | 716 ms                                                 | 425 ms: 1.68x faster                                                            |
| spectral_norm            | 170 ms                                                 | 101 ms: 1.68x faster                                                            |
| float                    | 117 ms                                                 | 72.5 ms: 1.61x faster                                                           |
| nbody                    | 154 ms                                                 | 95.5 ms: 1.61x faster                                                           |
| tomli_loads              | 3.14 sec                                               | 2.00 sec: 1.57x faster                                                          |
| deepcopy_reduce          | 4.17 us                                                | 2.70 us: 1.54x faster                                                           |
| pickle_pure_python       | 484 us                                                 | 321 us: 1.51x faster                                                            |
| genshi_text              | 31.8 ms                                                | 21.2 ms: 1.50x faster                                                           |
| scimark_lu               | 176 ms                                                 | 118 ms: 1.50x faster                                                            |
| unpickle_pure_python     | 331 us                                                 | 222 us: 1.49x faster                                                            |
| django_template          | 48.2 ms                                                | 32.4 ms: 1.48x faster                                                           |
| regex_compile            | 188 ms                                                 | 127 ms: 1.48x faster                                                            |
| coroutines               | 35.1 ms                                                | 24.4 ms: 1.44x faster                                                           |
| dulwich_log              | 84.3 ms                                                | 59.0 ms: 1.43x faster                                                           |
| html5lib                 | 88.9 ms                                                | 62.5 ms: 1.42x faster                                                           |
| mako                     | 16.3 ms                                                | 11.5 ms: 1.42x faster                                                           |
| pycparser                | 1.58 sec                                               | 1.14 sec: 1.39x faster                                                          |
| thrift                   | 1.07 ms                                                | 777 us: 1.38x faster                                                            |
| 2to3                     | 348 ms                                                 | 255 ms: 1.37x faster                                                            |
| sympy_integrate          | 25.8 ms                                                | 19.0 ms: 1.36x faster                                                           |
| logging_simple           | 8.30 us                                                | 6.19 us: 1.34x faster                                                           |
| genshi_xml               | 66.0 ms                                                | 49.7 ms: 1.33x faster                                                           |
| sympy_sum                | 196 ms                                                 | 149 ms: 1.32x faster                                                            |
| xml_etree_process        | 79.1 ms                                                | 60.0 ms: 1.32x faster                                                           |
| logging_format           | 9.09 us                                                | 6.90 us: 1.32x faster                                                           |
| nqueens                  | 106 ms                                                 | 81.2 ms: 1.30x faster                                                           |
| fannkuch                 | 532 ms                                                 | 408 ms: 1.30x faster                                                            |
| sympy_str                | 346 ms                                                 | 268 ms: 1.29x faster                                                            |
| scimark_fft              | 466 ms                                                 | 361 ms: 1.29x faster                                                            |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.04 ms: 1.28x faster                                                           |
| pprint_pformat           | 2.10 sec                                               | 1.65 sec: 1.28x faster                                                          |
| docutils                 | 3.30 sec                                               | 2.59 sec: 1.27x faster                                                          |
| json_dumps               | 14.2 ms                                                | 11.2 ms: 1.27x faster                                                           |
| pprint_safe_repr         | 1.02 sec                                               | 807 ms: 1.26x faster                                                            |
| sympy_expand             | 566 ms                                                 | 453 ms: 1.25x faster                                                            |
| python_startup           | 14.6 ms                                                | 12.2 ms: 1.19x faster                                                           |
| regex_v8                 | 27.8 ms                                                | 23.5 ms: 1.18x faster                                                           |
| pathlib                  | 20.5 ms                                                | 17.4 ms: 1.17x faster                                                           |
| xml_etree_parse          | 168 ms                                                 | 144 ms: 1.17x faster                                                            |
| xml_etree_generate       | 99.4 ms                                                | 85.6 ms: 1.16x faster                                                           |
| xml_etree_iterparse      | 115 ms                                                 | 99.6 ms: 1.16x faster                                                           |
| meteor_contest           | 120 ms                                                 | 105 ms: 1.14x faster                                                            |
| json_loads               | 31.2 us                                                | 28.3 us: 1.10x faster                                                           |
| regex_effbot             | 3.63 ms                                                | 3.33 ms: 1.09x faster                                                           |
| async_generators         | 444 ms                                                 | 410 ms: 1.08x faster                                                            |
| json                     | 5.69 ms                                                | 5.27 ms: 1.08x faster                                                           |
| regex_dna                | 227 ms                                                 | 210 ms: 1.08x faster                                                            |
| sqlite_synth             | 3.02 us                                                | 2.88 us: 1.05x faster                                                           |
| asyncio_websockets       | 559 ms                                                 | 554 ms: 1.01x faster                                                            |
| pidigits                 | 191 ms                                                 | 193 ms: 1.01x slower                                                            |
| telco                    | 7.27 ms                                                | 7.90 ms: 1.09x slower                                                           |
| coverage                 | 79.4 ms                                                | 87.3 ms: 1.10x slower                                                           |
| python_startup_no_site   | 5.93 ms                                                | 6.95 ms: 1.17x slower                                                           |
| gc_traversal             | 3.62 ms                                                | 5.02 ms: 1.39x slower                                                           |
| create_gc_cycles         | 1.62 ms                                                | 2.59 ms: 1.60x slower                                                           |
| logging_silent           | 190 ns                                                 | 471 ns: 2.48x slower                                                            |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                                    |
Ignored benchmarks (23) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250623-3.15.0a0-c84beef/bm-20250623-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.449x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.29x

# Memory
- memory change: 1.31x