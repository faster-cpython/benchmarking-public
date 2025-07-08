# Results vs. 3.10.4

- fork: faster-cpython
- ref: fast_side_exits
- machine: windows-amd64
- commit hash: 73832b2
- commit date: 2025-07-08
- overall geometric mean: 1.317x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250708-pythonperf1-amd64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 218 ms: 1.13x faster                                                            |
| docutils       | 1.92 sec                                                    | 1.64 sec: 1.17x faster                                                          |
| html5lib       | 51.0 ms                                                     | 38.0 ms: 1.34x faster                                                           |
| Geometric mean | (ref)                                                       | 1.21x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250708-pythonperf1-amd64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2 |
|-------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 396 ms: 2.80x faster                                                            |
| async_tree_none         | 435 ms                                                      | 168 ms: 2.59x faster                                                            |
| async_tree_memoization  | 526 ms                                                      | 205 ms: 2.56x faster                                                            |
| async_tree_cpu_io_mixed | 638 ms                                                      | 328 ms: 1.95x faster                                                            |
| Geometric mean          | (ref)                                                       | 2.45x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250708-pythonperf1-amd64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 43.7 ms: 1.41x faster                                                           |
| nbody          | 71.3 ms                                                     | 53.5 ms: 1.33x faster                                                           |
| pidigits       | 149 ms                                                      | 146 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                       | 1.24x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250708-pythonperf1-amd64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 79.1 ms: 1.34x faster                                                           |
| regex_dna      | 136 ms                                                      | 118 ms: 1.15x faster                                                            |
| regex_v8       | 15.4 ms                                                     | 13.4 ms: 1.15x faster                                                           |
| regex_effbot   | 1.66 ms                                                     | 1.54 ms: 1.07x faster                                                           |
| Geometric mean | (ref)                                                       | 1.18x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250708-pythonperf1-amd64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2 |
|----------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 108 us: 1.70x faster                                                            |
| tomli_loads          | 1.67 sec                                                    | 1.13 sec: 1.49x faster                                                          |
| json_dumps           | 9.16 ms                                                     | 6.26 ms: 1.46x faster                                                           |
| pickle_pure_python   | 270 us                                                      | 205 us: 1.31x faster                                                            |
| xml_etree_process    | 44.5 ms                                                     | 34.9 ms: 1.27x faster                                                           |
| xml_etree_parse      | 96.8 ms                                                     | 88.1 ms: 1.10x faster                                                           |
| xml_etree_generate   | 55.5 ms                                                     | 50.9 ms: 1.09x faster                                                           |
| xml_etree_iterparse  | 65.0 ms                                                     | 64.2 ms: 1.01x faster                                                           |
| json_loads           | 14.0 us                                                     | 14.5 us: 1.04x slower                                                           |
| Geometric mean       | (ref)                                                       | 1.25x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250708-pythonperf1-amd64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2 |
|------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 19.4 ms: 1.25x slower                                                           |
| python_startup         | 20.6 ms                                                     | 25.8 ms: 1.25x slower                                                           |
| Geometric mean         | (ref)                                                       | 1.25x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250708-pythonperf1-amd64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2 |
|-----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.36 ms: 1.68x faster                                                           |
| genshi_text     | 19.8 ms                                                     | 15.3 ms: 1.29x faster                                                           |
| genshi_xml      | 41.0 ms                                                     | 34.2 ms: 1.20x faster                                                           |
| django_template | 28.9 ms                                                     | 24.1 ms: 1.20x faster                                                           |
| Geometric mean  | (ref)                                                       | 1.33x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250708-pythonperf1-amd64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2 |
|--------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 102 us: 3.29x faster                                                            |
| async_tree_io            | 1.11 sec                                                    | 396 ms: 2.80x faster                                                            |
| async_tree_none          | 435 ms                                                      | 168 ms: 2.59x faster                                                            |
| async_tree_memoization   | 526 ms                                                      | 205 ms: 2.56x faster                                                            |
| pathlib                  | 75.7 ms                                                     | 32.0 ms: 2.36x faster                                                           |
| mdp                      | 1.78 sec                                                    | 804 ms: 2.21x faster                                                            |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 328 ms: 1.95x faster                                                            |
| deltablue                | 4.19 ms                                                     | 2.20 ms: 1.90x faster                                                           |
| go                       | 139 ms                                                      | 77.5 ms: 1.79x faster                                                           |
| pylint                   | 350 ms                                                      | 199 ms: 1.76x faster                                                            |
| logging_silent           | 94.6 ns                                                     | 54.0 ns: 1.75x faster                                                           |
| richards_super           | 52.2 ms                                                     | 30.2 ms: 1.73x faster                                                           |
| unpickle_pure_python     | 183 us                                                      | 108 us: 1.70x faster                                                            |
| mako                     | 9.03 ms                                                     | 5.36 ms: 1.68x faster                                                           |
| generators               | 32.4 ms                                                     | 19.4 ms: 1.67x faster                                                           |
| pyflate                  | 409 ms                                                      | 253 ms: 1.62x faster                                                            |
| richards                 | 42.4 ms                                                     | 26.3 ms: 1.61x faster                                                           |
| comprehensions           | 16.5 us                                                     | 10.4 us: 1.58x faster                                                           |
| deepcopy_memo            | 28.8 us                                                     | 18.5 us: 1.56x faster                                                           |
| raytrace                 | 273 ms                                                      | 177 ms: 1.54x faster                                                            |
| chaos                    | 61.7 ms                                                     | 40.1 ms: 1.54x faster                                                           |
| deepcopy                 | 255 us                                                      | 171 us: 1.50x faster                                                            |
| scimark_lu               | 85.8 ms                                                     | 57.7 ms: 1.49x faster                                                           |
| tomli_loads              | 1.67 sec                                                    | 1.13 sec: 1.49x faster                                                          |
| json_dumps               | 9.16 ms                                                     | 6.26 ms: 1.46x faster                                                           |
| float                    | 61.7 ms                                                     | 43.7 ms: 1.41x faster                                                           |
| hexiom                   | 5.74 ms                                                     | 4.09 ms: 1.41x faster                                                           |
| scimark_monte_carlo      | 57.3 ms                                                     | 41.1 ms: 1.40x faster                                                           |
| crypto_pyaes             | 62.5 ms                                                     | 45.6 ms: 1.37x faster                                                           |
| scimark_sor              | 106 ms                                                      | 78.1 ms: 1.36x faster                                                           |
| html5lib                 | 51.0 ms                                                     | 38.0 ms: 1.34x faster                                                           |
| regex_compile            | 106 ms                                                      | 79.1 ms: 1.34x faster                                                           |
| pycparser                | 930 ms                                                      | 695 ms: 1.34x faster                                                            |
| nbody                    | 71.3 ms                                                     | 53.5 ms: 1.33x faster                                                           |
| pprint_pformat           | 1.22 sec                                                    | 920 ms: 1.33x faster                                                            |
| pickle_pure_python       | 270 us                                                      | 205 us: 1.31x faster                                                            |
| genshi_text              | 19.8 ms                                                     | 15.3 ms: 1.29x faster                                                           |
| xml_etree_process        | 44.5 ms                                                     | 34.9 ms: 1.27x faster                                                           |
| pprint_safe_repr         | 592 ms                                                      | 467 ms: 1.27x faster                                                            |
| thrift                   | 617 us                                                      | 488 us: 1.26x faster                                                            |
| sqlite_synth             | 1.91 us                                                     | 1.55 us: 1.23x faster                                                           |
| dulwich_log              | 50.5 ms                                                     | 41.0 ms: 1.23x faster                                                           |
| sympy_sum                | 107 ms                                                      | 87.4 ms: 1.22x faster                                                           |
| deepcopy_reduce          | 2.20 us                                                     | 1.83 us: 1.21x faster                                                           |
| scimark_fft              | 187 ms                                                      | 156 ms: 1.20x faster                                                            |
| genshi_xml               | 41.0 ms                                                     | 34.2 ms: 1.20x faster                                                           |
| sympy_integrate          | 15.3 ms                                                     | 12.8 ms: 1.20x faster                                                           |
| django_template          | 28.9 ms                                                     | 24.1 ms: 1.20x faster                                                           |
| spectral_norm            | 77.3 ms                                                     | 65.7 ms: 1.18x faster                                                           |
| docutils                 | 1.92 sec                                                    | 1.64 sec: 1.17x faster                                                          |
| regex_dna                | 136 ms                                                      | 118 ms: 1.15x faster                                                            |
| regex_v8                 | 15.4 ms                                                     | 13.4 ms: 1.15x faster                                                           |
| sympy_str                | 194 ms                                                      | 170 ms: 1.15x faster                                                            |
| 2to3                     | 246 ms                                                      | 218 ms: 1.13x faster                                                            |
| nqueens                  | 66.6 ms                                                     | 59.7 ms: 1.12x faster                                                           |
| coroutines               | 16.0 ms                                                     | 14.4 ms: 1.11x faster                                                           |
| xml_etree_parse          | 96.8 ms                                                     | 88.1 ms: 1.10x faster                                                           |
| xml_etree_generate       | 55.5 ms                                                     | 50.9 ms: 1.09x faster                                                           |
| fannkuch                 | 256 ms                                                      | 235 ms: 1.09x faster                                                            |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.53 ms: 1.08x faster                                                           |
| regex_effbot             | 1.66 ms                                                     | 1.54 ms: 1.07x faster                                                           |
| sympy_expand             | 314 ms                                                      | 293 ms: 1.07x faster                                                            |
| meteor_contest           | 75.9 ms                                                     | 72.4 ms: 1.05x faster                                                           |
| json                     | 3.14 ms                                                     | 3.05 ms: 1.03x faster                                                           |
| logging_format           | 6.76 us                                                     | 6.61 us: 1.02x faster                                                           |
| pidigits                 | 149 ms                                                      | 146 ms: 1.02x faster                                                            |
| xml_etree_iterparse      | 65.0 ms                                                     | 64.2 ms: 1.01x faster                                                           |
| logging_simple           | 6.22 us                                                     | 6.15 us: 1.01x faster                                                           |
| json_loads               | 14.0 us                                                     | 14.5 us: 1.04x slower                                                           |
| telco                    | 3.94 ms                                                     | 4.29 ms: 1.09x slower                                                           |
| async_generators         | 222 ms                                                      | 244 ms: 1.10x slower                                                            |
| python_startup_no_site   | 15.5 ms                                                     | 19.4 ms: 1.25x slower                                                           |
| python_startup           | 20.6 ms                                                     | 25.8 ms: 1.25x slower                                                           |
| coverage                 | 39.0 ms                                                     | 49.2 ms: 1.26x slower                                                           |
| gc_traversal             | 1.41 ms                                                     | 2.17 ms: 1.54x slower                                                           |
| create_gc_cycles         | 800 us                                                      | 1.32 ms: 1.65x slower                                                           |
| Geometric mean           | (ref)                                                       | 1.32x faster                                                                    |
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250708-3.15.0a0-73832b2-JIT/bm-20250708-pythonperf1-amd64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.317x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: unknown