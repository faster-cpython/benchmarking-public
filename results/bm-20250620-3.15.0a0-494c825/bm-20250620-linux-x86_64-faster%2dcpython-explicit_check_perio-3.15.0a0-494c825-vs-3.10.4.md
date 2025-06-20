# Results vs. 3.10.4

- fork: faster-cpython
- ref: explicit_check_perio
- machine: linux-x86_64
- commit hash: 494c825
- commit date: 2025-06-20
- overall geometric mean: 1.443x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.29x faster
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250620-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 257 ms: 1.36x faster                                                            |
| docutils       | 3.30 sec                                               | 2.61 sec: 1.26x faster                                                          |
| html5lib       | 88.9 ms                                                | 61.9 ms: 1.44x faster                                                           |
| Geometric mean | (ref)                                                  | 1.35x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250620-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 604 ms: 2.93x faster                                                            |
| async_tree_none         | 728 ms                                                 | 267 ms: 2.73x faster                                                            |
| async_tree_memoization  | 870 ms                                                 | 321 ms: 2.71x faster                                                            |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 502 ms: 2.02x faster                                                            |
| Geometric mean          | (ref)                                                  | 2.57x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250620-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 72.3 ms: 1.62x faster                                                           |
| nbody          | 154 ms                                                 | 99.1 ms: 1.55x faster                                                           |
| pidigits       | 191 ms                                                 | 189 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                  | 1.36x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250620-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 130 ms: 1.45x faster                                                            |
| regex_v8       | 27.8 ms                                                | 23.2 ms: 1.20x faster                                                           |
| regex_dna      | 227 ms                                                 | 199 ms: 1.14x faster                                                            |
| regex_effbot   | 3.63 ms                                                | 3.22 ms: 1.13x faster                                                           |
| Geometric mean | (ref)                                                  | 1.22x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250620-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 2.02 sec: 1.55x faster                                                          |
| unpickle_pure_python | 331 us                                                 | 222 us: 1.49x faster                                                            |
| pickle_pure_python   | 484 us                                                 | 327 us: 1.48x faster                                                            |
| xml_etree_process    | 79.1 ms                                                | 59.7 ms: 1.32x faster                                                           |
| json_dumps           | 14.2 ms                                                | 11.2 ms: 1.27x faster                                                           |
| xml_etree_parse      | 168 ms                                                 | 143 ms: 1.18x faster                                                            |
| xml_etree_generate   | 99.4 ms                                                | 84.8 ms: 1.17x faster                                                           |
| xml_etree_iterparse  | 115 ms                                                 | 98.8 ms: 1.17x faster                                                           |
| json_loads           | 31.2 us                                                | 28.3 us: 1.10x faster                                                           |
| Geometric mean       | (ref)                                                  | 1.29x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250620-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.2 ms: 1.20x faster                                                           |
| python_startup_no_site | 5.93 ms                                                | 6.94 ms: 1.17x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250620-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 21.6 ms: 1.47x faster                                                           |
| django_template | 48.2 ms                                                | 32.8 ms: 1.47x faster                                                           |
| mako            | 16.3 ms                                                | 11.6 ms: 1.41x faster                                                           |
| genshi_xml      | 66.0 ms                                                | 50.0 ms: 1.32x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.42x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250620-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 168 us: 3.25x faster                                                            |
| async_tree_io            | 1.77 sec                                               | 604 ms: 2.93x faster                                                            |
| async_tree_none          | 728 ms                                                 | 267 ms: 2.73x faster                                                            |
| generators               | 80.1 ms                                                | 29.4 ms: 2.72x faster                                                           |
| async_tree_memoization   | 870 ms                                                 | 321 ms: 2.71x faster                                                            |
| mdp                      | 2.85 sec                                               | 1.23 sec: 2.32x faster                                                          |
| deltablue                | 7.91 ms                                                | 3.50 ms: 2.26x faster                                                           |
| go                       | 240 ms                                                 | 111 ms: 2.17x faster                                                            |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 502 ms: 2.02x faster                                                            |
| pylint                   | 551 ms                                                 | 279 ms: 1.97x faster                                                            |
| deepcopy_memo            | 58.5 us                                                | 30.1 us: 1.94x faster                                                           |
| richards_super           | 94.7 ms                                                | 49.4 ms: 1.92x faster                                                           |
| chaos                    | 115 ms                                                 | 60.5 ms: 1.91x faster                                                           |
| scimark_sor              | 220 ms                                                 | 117 ms: 1.88x faster                                                            |
| deepcopy                 | 479 us                                                 | 257 us: 1.86x faster                                                            |
| raytrace                 | 507 ms                                                 | 272 ms: 1.86x faster                                                            |
| richards                 | 79.3 ms                                                | 43.2 ms: 1.83x faster                                                           |
| comprehensions           | 28.8 us                                                | 16.0 us: 1.80x faster                                                           |
| djangocms                | 38.4 us                                                | 21.6 us: 1.78x faster                                                           |
| scimark_monte_carlo      | 118 ms                                                 | 67.1 ms: 1.76x faster                                                           |
| pyflate                  | 716 ms                                                 | 427 ms: 1.68x faster                                                            |
| hexiom                   | 10.4 ms                                                | 6.22 ms: 1.67x faster                                                           |
| crypto_pyaes             | 128 ms                                                 | 76.8 ms: 1.66x faster                                                           |
| float                    | 117 ms                                                 | 72.3 ms: 1.62x faster                                                           |
| spectral_norm            | 170 ms                                                 | 107 ms: 1.59x faster                                                            |
| tomli_loads              | 3.14 sec                                               | 2.02 sec: 1.55x faster                                                          |
| nbody                    | 154 ms                                                 | 99.1 ms: 1.55x faster                                                           |
| deepcopy_reduce          | 4.17 us                                                | 2.72 us: 1.53x faster                                                           |
| scimark_lu               | 176 ms                                                 | 118 ms: 1.49x faster                                                            |
| unpickle_pure_python     | 331 us                                                 | 222 us: 1.49x faster                                                            |
| pickle_pure_python       | 484 us                                                 | 327 us: 1.48x faster                                                            |
| genshi_text              | 31.8 ms                                                | 21.6 ms: 1.47x faster                                                           |
| django_template          | 48.2 ms                                                | 32.8 ms: 1.47x faster                                                           |
| regex_compile            | 188 ms                                                 | 130 ms: 1.45x faster                                                            |
| html5lib                 | 88.9 ms                                                | 61.9 ms: 1.44x faster                                                           |
| coroutines               | 35.1 ms                                                | 24.7 ms: 1.42x faster                                                           |
| mako                     | 16.3 ms                                                | 11.6 ms: 1.41x faster                                                           |
| dulwich_log              | 84.3 ms                                                | 60.0 ms: 1.40x faster                                                           |
| pycparser                | 1.58 sec                                               | 1.14 sec: 1.38x faster                                                          |
| thrift                   | 1.07 ms                                                | 779 us: 1.38x faster                                                            |
| 2to3                     | 348 ms                                                 | 257 ms: 1.36x faster                                                            |
| sympy_integrate          | 25.8 ms                                                | 19.2 ms: 1.35x faster                                                           |
| xml_etree_process        | 79.1 ms                                                | 59.7 ms: 1.32x faster                                                           |
| genshi_xml               | 66.0 ms                                                | 50.0 ms: 1.32x faster                                                           |
| sympy_sum                | 196 ms                                                 | 149 ms: 1.32x faster                                                            |
| logging_simple           | 8.30 us                                                | 6.33 us: 1.31x faster                                                           |
| nqueens                  | 106 ms                                                 | 81.2 ms: 1.30x faster                                                           |
| sympy_str                | 346 ms                                                 | 268 ms: 1.29x faster                                                            |
| logging_format           | 9.09 us                                                | 7.11 us: 1.28x faster                                                           |
| fannkuch                 | 532 ms                                                 | 416 ms: 1.28x faster                                                            |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.09 ms: 1.27x faster                                                           |
| pprint_pformat           | 2.10 sec                                               | 1.66 sec: 1.27x faster                                                          |
| json_dumps               | 14.2 ms                                                | 11.2 ms: 1.27x faster                                                           |
| docutils                 | 3.30 sec                                               | 2.61 sec: 1.26x faster                                                          |
| pprint_safe_repr         | 1.02 sec                                               | 812 ms: 1.25x faster                                                            |
| scimark_fft              | 466 ms                                                 | 374 ms: 1.24x faster                                                            |
| sympy_expand             | 566 ms                                                 | 456 ms: 1.24x faster                                                            |
| regex_v8                 | 27.8 ms                                                | 23.2 ms: 1.20x faster                                                           |
| python_startup           | 14.6 ms                                                | 12.2 ms: 1.20x faster                                                           |
| pathlib                  | 20.5 ms                                                | 17.2 ms: 1.19x faster                                                           |
| xml_etree_parse          | 168 ms                                                 | 143 ms: 1.18x faster                                                            |
| xml_etree_generate       | 99.4 ms                                                | 84.8 ms: 1.17x faster                                                           |
| xml_etree_iterparse      | 115 ms                                                 | 98.8 ms: 1.17x faster                                                           |
| regex_dna                | 227 ms                                                 | 199 ms: 1.14x faster                                                            |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                            |
| regex_effbot             | 3.63 ms                                                | 3.22 ms: 1.13x faster                                                           |
| json_loads               | 31.2 us                                                | 28.3 us: 1.10x faster                                                           |
| json                     | 5.69 ms                                                | 5.28 ms: 1.08x faster                                                           |
| async_generators         | 444 ms                                                 | 412 ms: 1.08x faster                                                            |
| sqlite_synth             | 3.02 us                                                | 2.86 us: 1.06x faster                                                           |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                            |
| pidigits                 | 191 ms                                                 | 189 ms: 1.01x faster                                                            |
| coverage                 | 79.4 ms                                                | 87.1 ms: 1.10x slower                                                           |
| telco                    | 7.27 ms                                                | 7.99 ms: 1.10x slower                                                           |
| python_startup_no_site   | 5.93 ms                                                | 6.94 ms: 1.17x slower                                                           |
| gc_traversal             | 3.62 ms                                                | 5.17 ms: 1.43x slower                                                           |
| create_gc_cycles         | 1.62 ms                                                | 2.59 ms: 1.60x slower                                                           |
| logging_silent           | 190 ns                                                 | 480 ns: 2.53x slower                                                            |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                                    |
Ignored benchmarks (23) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250620-3.15.0a0-494c825/bm-20250620-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.443x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.29x

# Memory
- memory change: 1.31x