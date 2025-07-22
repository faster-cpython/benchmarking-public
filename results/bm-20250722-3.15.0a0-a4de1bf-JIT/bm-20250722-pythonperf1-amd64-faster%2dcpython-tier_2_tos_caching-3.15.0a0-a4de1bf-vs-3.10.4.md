# Results vs. 3.10.4

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: windows-amd64
- commit hash: a4de1bf
- commit date: 2025-07-22
- overall geometric mean: 1.324x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250722-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 221 ms: 1.11x faster                                                               |
| docutils       | 1.92 sec                                                    | 1.65 sec: 1.16x faster                                                             |
| html5lib       | 51.0 ms                                                     | 38.5 ms: 1.33x faster                                                              |
| Geometric mean | (ref)                                                       | 1.20x faster                                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250722-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|-------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 397 ms: 2.79x faster                                                               |
| async_tree_none         | 435 ms                                                      | 167 ms: 2.60x faster                                                               |
| async_tree_memoization  | 526 ms                                                      | 203 ms: 2.59x faster                                                               |
| async_tree_cpu_io_mixed | 638 ms                                                      | 331 ms: 1.93x faster                                                               |
| Geometric mean          | (ref)                                                       | 2.45x faster                                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250722-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| nbody          | 71.3 ms                                                     | 47.8 ms: 1.49x faster                                                              |
| float          | 61.7 ms                                                     | 44.0 ms: 1.40x faster                                                              |
| pidigits       | 149 ms                                                      | 145 ms: 1.03x faster                                                               |
| Geometric mean | (ref)                                                       | 1.29x faster                                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250722-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 78.7 ms: 1.35x faster                                                              |
| regex_dna      | 136 ms                                                      | 121 ms: 1.13x faster                                                               |
| regex_v8       | 15.4 ms                                                     | 14.0 ms: 1.10x faster                                                              |
| regex_effbot   | 1.66 ms                                                     | 1.61 ms: 1.03x faster                                                              |
| Geometric mean | (ref)                                                       | 1.15x faster                                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250722-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 106 us: 1.73x faster                                                               |
| tomli_loads          | 1.67 sec                                                    | 1.08 sec: 1.55x faster                                                             |
| json_dumps           | 9.16 ms                                                     | 6.26 ms: 1.46x faster                                                              |
| pickle_pure_python   | 270 us                                                      | 202 us: 1.33x faster                                                               |
| xml_etree_process    | 44.5 ms                                                     | 35.2 ms: 1.26x faster                                                              |
| xml_etree_generate   | 55.5 ms                                                     | 51.0 ms: 1.09x faster                                                              |
| xml_etree_parse      | 96.8 ms                                                     | 89.5 ms: 1.08x faster                                                              |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.4 ms: 1.03x faster                                                              |
| json_loads           | 14.0 us                                                     | 14.2 us: 1.01x slower                                                              |
| Geometric mean       | (ref)                                                       | 1.26x faster                                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250722-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 19.2 ms: 1.24x slower                                                              |
| python_startup         | 20.6 ms                                                     | 25.7 ms: 1.25x slower                                                              |
| Geometric mean         | (ref)                                                       | 1.24x slower                                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250722-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|-----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.58 ms: 1.62x faster                                                              |
| genshi_text     | 19.8 ms                                                     | 15.5 ms: 1.28x faster                                                              |
| genshi_xml      | 41.0 ms                                                     | 34.2 ms: 1.20x faster                                                              |
| django_template | 28.9 ms                                                     | 24.2 ms: 1.19x faster                                                              |
| Geometric mean  | (ref)                                                       | 1.31x faster                                                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250722-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|--------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 104 us: 3.22x faster                                                               |
| async_tree_io            | 1.11 sec                                                    | 397 ms: 2.79x faster                                                               |
| async_tree_none          | 435 ms                                                      | 167 ms: 2.60x faster                                                               |
| async_tree_memoization   | 526 ms                                                      | 203 ms: 2.59x faster                                                               |
| pathlib                  | 75.7 ms                                                     | 30.3 ms: 2.50x faster                                                              |
| mdp                      | 1.78 sec                                                    | 804 ms: 2.21x faster                                                               |
| deltablue                | 4.19 ms                                                     | 2.16 ms: 1.94x faster                                                              |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 331 ms: 1.93x faster                                                               |
| go                       | 139 ms                                                      | 75.2 ms: 1.85x faster                                                              |
| pylint                   | 350 ms                                                      | 197 ms: 1.77x faster                                                               |
| logging_silent           | 94.6 ns                                                     | 54.6 ns: 1.73x faster                                                              |
| unpickle_pure_python     | 183 us                                                      | 106 us: 1.73x faster                                                               |
| richards_super           | 52.2 ms                                                     | 30.4 ms: 1.72x faster                                                              |
| generators               | 32.4 ms                                                     | 19.3 ms: 1.68x faster                                                              |
| deepcopy_memo            | 28.8 us                                                     | 17.3 us: 1.67x faster                                                              |
| mako                     | 9.03 ms                                                     | 5.58 ms: 1.62x faster                                                              |
| pyflate                  | 409 ms                                                      | 256 ms: 1.60x faster                                                               |
| comprehensions           | 16.5 us                                                     | 10.4 us: 1.59x faster                                                              |
| richards                 | 42.4 ms                                                     | 26.9 ms: 1.58x faster                                                              |
| tomli_loads              | 1.67 sec                                                    | 1.08 sec: 1.55x faster                                                             |
| deepcopy                 | 255 us                                                      | 168 us: 1.52x faster                                                               |
| raytrace                 | 273 ms                                                      | 180 ms: 1.52x faster                                                               |
| chaos                    | 61.7 ms                                                     | 40.8 ms: 1.51x faster                                                              |
| nbody                    | 71.3 ms                                                     | 47.8 ms: 1.49x faster                                                              |
| json_dumps               | 9.16 ms                                                     | 6.26 ms: 1.46x faster                                                              |
| scimark_sor              | 106 ms                                                      | 74.6 ms: 1.42x faster                                                              |
| hexiom                   | 5.74 ms                                                     | 4.04 ms: 1.42x faster                                                              |
| scimark_lu               | 85.8 ms                                                     | 61.0 ms: 1.41x faster                                                              |
| float                    | 61.7 ms                                                     | 44.0 ms: 1.40x faster                                                              |
| pprint_pformat           | 1.22 sec                                                    | 887 ms: 1.37x faster                                                               |
| crypto_pyaes             | 62.5 ms                                                     | 45.7 ms: 1.37x faster                                                              |
| pprint_safe_repr         | 592 ms                                                      | 435 ms: 1.36x faster                                                               |
| scimark_monte_carlo      | 57.3 ms                                                     | 42.4 ms: 1.35x faster                                                              |
| regex_compile            | 106 ms                                                      | 78.7 ms: 1.35x faster                                                              |
| pycparser                | 930 ms                                                      | 693 ms: 1.34x faster                                                               |
| pickle_pure_python       | 270 us                                                      | 202 us: 1.33x faster                                                               |
| html5lib                 | 51.0 ms                                                     | 38.5 ms: 1.33x faster                                                              |
| genshi_text              | 19.8 ms                                                     | 15.5 ms: 1.28x faster                                                              |
| scimark_fft              | 187 ms                                                      | 148 ms: 1.27x faster                                                               |
| xml_etree_process        | 44.5 ms                                                     | 35.2 ms: 1.26x faster                                                              |
| dulwich_log              | 50.5 ms                                                     | 40.3 ms: 1.25x faster                                                              |
| sqlite_synth             | 1.91 us                                                     | 1.55 us: 1.23x faster                                                              |
| thrift                   | 617 us                                                      | 502 us: 1.23x faster                                                               |
| sympy_sum                | 107 ms                                                      | 87.1 ms: 1.23x faster                                                              |
| deepcopy_reduce          | 2.20 us                                                     | 1.81 us: 1.21x faster                                                              |
| sympy_integrate          | 15.3 ms                                                     | 12.6 ms: 1.21x faster                                                              |
| spectral_norm            | 77.3 ms                                                     | 63.9 ms: 1.21x faster                                                              |
| genshi_xml               | 41.0 ms                                                     | 34.2 ms: 1.20x faster                                                              |
| django_template          | 28.9 ms                                                     | 24.2 ms: 1.19x faster                                                              |
| fannkuch                 | 256 ms                                                      | 218 ms: 1.17x faster                                                               |
| docutils                 | 1.92 sec                                                    | 1.65 sec: 1.16x faster                                                             |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.35 ms: 1.16x faster                                                              |
| sympy_str                | 194 ms                                                      | 170 ms: 1.14x faster                                                               |
| regex_dna                | 136 ms                                                      | 121 ms: 1.13x faster                                                               |
| 2to3                     | 246 ms                                                      | 221 ms: 1.11x faster                                                               |
| nqueens                  | 66.6 ms                                                     | 59.9 ms: 1.11x faster                                                              |
| coroutines               | 16.0 ms                                                     | 14.4 ms: 1.11x faster                                                              |
| regex_v8                 | 15.4 ms                                                     | 14.0 ms: 1.10x faster                                                              |
| xml_etree_generate       | 55.5 ms                                                     | 51.0 ms: 1.09x faster                                                              |
| xml_etree_parse          | 96.8 ms                                                     | 89.5 ms: 1.08x faster                                                              |
| sympy_expand             | 314 ms                                                      | 292 ms: 1.08x faster                                                               |
| meteor_contest           | 75.9 ms                                                     | 71.9 ms: 1.06x faster                                                              |
| json                     | 3.14 ms                                                     | 3.00 ms: 1.04x faster                                                              |
| logging_format           | 6.76 us                                                     | 6.57 us: 1.03x faster                                                              |
| regex_effbot             | 1.66 ms                                                     | 1.61 ms: 1.03x faster                                                              |
| pidigits                 | 149 ms                                                      | 145 ms: 1.03x faster                                                               |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.4 ms: 1.03x faster                                                              |
| logging_simple           | 6.22 us                                                     | 6.14 us: 1.01x faster                                                              |
| json_loads               | 14.0 us                                                     | 14.2 us: 1.01x slower                                                              |
| telco                    | 3.94 ms                                                     | 4.29 ms: 1.09x slower                                                              |
| async_generators         | 222 ms                                                      | 250 ms: 1.13x slower                                                               |
| python_startup_no_site   | 15.5 ms                                                     | 19.2 ms: 1.24x slower                                                              |
| python_startup           | 20.6 ms                                                     | 25.7 ms: 1.25x slower                                                              |
| coverage                 | 39.0 ms                                                     | 52.2 ms: 1.34x slower                                                              |
| gc_traversal             | 1.41 ms                                                     | 2.08 ms: 1.47x slower                                                              |
| create_gc_cycles         | 800 us                                                      | 1.32 ms: 1.65x slower                                                              |
| Geometric mean           | (ref)                                                       | 1.32x faster                                                                       |
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250722-3.15.0a0-a4de1bf-JIT/bm-20250722-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.324x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: unknown