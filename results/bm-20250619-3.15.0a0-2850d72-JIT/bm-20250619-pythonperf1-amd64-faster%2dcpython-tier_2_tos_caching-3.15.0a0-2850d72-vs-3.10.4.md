# Results vs. 3.10.4

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: windows-amd64
- commit hash: 2850d72
- commit date: 2025-06-19
- overall geometric mean: 1.305x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250619-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 221 ms: 1.11x faster                                                               |
| docutils       | 1.92 sec                                                    | 1.67 sec: 1.15x faster                                                             |
| html5lib       | 51.0 ms                                                     | 38.6 ms: 1.32x faster                                                              |
| Geometric mean | (ref)                                                       | 1.19x faster                                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250619-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|-------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 399 ms: 2.78x faster                                                               |
| async_tree_none         | 435 ms                                                      | 169 ms: 2.58x faster                                                               |
| async_tree_memoization  | 526 ms                                                      | 206 ms: 2.56x faster                                                               |
| async_tree_cpu_io_mixed | 638 ms                                                      | 328 ms: 1.94x faster                                                               |
| Geometric mean          | (ref)                                                       | 2.44x faster                                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250619-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| nbody          | 71.3 ms                                                     | 44.8 ms: 1.59x faster                                                              |
| float          | 61.7 ms                                                     | 44.2 ms: 1.39x faster                                                              |
| pidigits       | 149 ms                                                      | 146 ms: 1.02x faster                                                               |
| Geometric mean | (ref)                                                       | 1.31x faster                                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250619-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 78.6 ms: 1.35x faster                                                              |
| regex_dna      | 136 ms                                                      | 118 ms: 1.15x faster                                                               |
| regex_v8       | 15.4 ms                                                     | 14.3 ms: 1.08x faster                                                              |
| regex_effbot   | 1.66 ms                                                     | 1.59 ms: 1.04x faster                                                              |
| Geometric mean | (ref)                                                       | 1.15x faster                                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250619-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 113 us: 1.62x faster                                                               |
| json_dumps           | 9.16 ms                                                     | 6.21 ms: 1.47x faster                                                              |
| tomli_loads          | 1.67 sec                                                    | 1.15 sec: 1.45x faster                                                             |
| pickle_pure_python   | 270 us                                                      | 204 us: 1.32x faster                                                               |
| xml_etree_process    | 44.5 ms                                                     | 35.9 ms: 1.24x faster                                                              |
| xml_etree_parse      | 96.8 ms                                                     | 87.8 ms: 1.10x faster                                                              |
| xml_etree_generate   | 55.5 ms                                                     | 51.4 ms: 1.08x faster                                                              |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.1 ms: 1.03x faster                                                              |
| Geometric mean       | (ref)                                                       | 1.24x faster                                                                       |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250619-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 19.3 ms: 1.24x slower                                                              |
| python_startup         | 20.6 ms                                                     | 25.6 ms: 1.24x slower                                                              |
| Geometric mean         | (ref)                                                       | 1.24x slower                                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250619-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|-----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.61 ms: 1.61x faster                                                              |
| genshi_text     | 19.8 ms                                                     | 15.5 ms: 1.27x faster                                                              |
| django_template | 28.9 ms                                                     | 23.5 ms: 1.23x faster                                                              |
| genshi_xml      | 41.0 ms                                                     | 35.2 ms: 1.17x faster                                                              |
| Geometric mean  | (ref)                                                       | 1.31x faster                                                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250619-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|--------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 105 us: 3.19x faster                                                               |
| async_tree_io            | 1.11 sec                                                    | 399 ms: 2.78x faster                                                               |
| async_tree_none          | 435 ms                                                      | 169 ms: 2.58x faster                                                               |
| async_tree_memoization   | 526 ms                                                      | 206 ms: 2.56x faster                                                               |
| pathlib                  | 75.7 ms                                                     | 31.8 ms: 2.38x faster                                                              |
| mdp                      | 1.78 sec                                                    | 810 ms: 2.20x faster                                                               |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 328 ms: 1.94x faster                                                               |
| deltablue                | 4.19 ms                                                     | 2.17 ms: 1.93x faster                                                              |
| go                       | 139 ms                                                      | 77.0 ms: 1.80x faster                                                              |
| pylint                   | 350 ms                                                      | 199 ms: 1.76x faster                                                               |
| richards_super           | 52.2 ms                                                     | 30.8 ms: 1.70x faster                                                              |
| generators               | 32.4 ms                                                     | 19.5 ms: 1.66x faster                                                              |
| unpickle_pure_python     | 183 us                                                      | 113 us: 1.62x faster                                                               |
| mako                     | 9.03 ms                                                     | 5.61 ms: 1.61x faster                                                              |
| nbody                    | 71.3 ms                                                     | 44.8 ms: 1.59x faster                                                              |
| deepcopy_memo            | 28.8 us                                                     | 18.3 us: 1.58x faster                                                              |
| pyflate                  | 409 ms                                                      | 261 ms: 1.57x faster                                                               |
| richards                 | 42.4 ms                                                     | 27.2 ms: 1.56x faster                                                              |
| raytrace                 | 273 ms                                                      | 176 ms: 1.56x faster                                                               |
| chaos                    | 61.7 ms                                                     | 40.8 ms: 1.51x faster                                                              |
| deepcopy                 | 255 us                                                      | 170 us: 1.51x faster                                                               |
| comprehensions           | 16.5 us                                                     | 11.0 us: 1.50x faster                                                              |
| json_dumps               | 9.16 ms                                                     | 6.21 ms: 1.47x faster                                                              |
| tomli_loads              | 1.67 sec                                                    | 1.15 sec: 1.45x faster                                                             |
| scimark_lu               | 85.8 ms                                                     | 59.7 ms: 1.44x faster                                                              |
| float                    | 61.7 ms                                                     | 44.2 ms: 1.39x faster                                                              |
| scimark_sor              | 106 ms                                                      | 76.7 ms: 1.38x faster                                                              |
| hexiom                   | 5.74 ms                                                     | 4.17 ms: 1.38x faster                                                              |
| regex_compile            | 106 ms                                                      | 78.6 ms: 1.35x faster                                                              |
| scimark_monte_carlo      | 57.3 ms                                                     | 42.5 ms: 1.35x faster                                                              |
| crypto_pyaes             | 62.5 ms                                                     | 46.5 ms: 1.35x faster                                                              |
| pycparser                | 930 ms                                                      | 703 ms: 1.32x faster                                                               |
| html5lib                 | 51.0 ms                                                     | 38.6 ms: 1.32x faster                                                              |
| pickle_pure_python       | 270 us                                                      | 204 us: 1.32x faster                                                               |
| genshi_text              | 19.8 ms                                                     | 15.5 ms: 1.27x faster                                                              |
| thrift                   | 617 us                                                      | 488 us: 1.26x faster                                                               |
| xml_etree_process        | 44.5 ms                                                     | 35.9 ms: 1.24x faster                                                              |
| dulwich_log              | 50.5 ms                                                     | 41.0 ms: 1.23x faster                                                              |
| sqlite_synth             | 1.91 us                                                     | 1.55 us: 1.23x faster                                                              |
| django_template          | 28.9 ms                                                     | 23.5 ms: 1.23x faster                                                              |
| scimark_fft              | 187 ms                                                      | 154 ms: 1.22x faster                                                               |
| sympy_sum                | 107 ms                                                      | 87.8 ms: 1.22x faster                                                              |
| deepcopy_reduce          | 2.20 us                                                     | 1.81 us: 1.22x faster                                                              |
| sympy_integrate          | 15.3 ms                                                     | 12.8 ms: 1.19x faster                                                              |
| spectral_norm            | 77.3 ms                                                     | 65.2 ms: 1.19x faster                                                              |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.31 ms: 1.18x faster                                                              |
| genshi_xml               | 41.0 ms                                                     | 35.2 ms: 1.17x faster                                                              |
| regex_dna                | 136 ms                                                      | 118 ms: 1.15x faster                                                               |
| docutils                 | 1.92 sec                                                    | 1.67 sec: 1.15x faster                                                             |
| pprint_pformat           | 1.22 sec                                                    | 1.06 sec: 1.15x faster                                                             |
| pprint_safe_repr         | 592 ms                                                      | 516 ms: 1.15x faster                                                               |
| sympy_str                | 194 ms                                                      | 171 ms: 1.14x faster                                                               |
| 2to3                     | 246 ms                                                      | 221 ms: 1.11x faster                                                               |
| nqueens                  | 66.6 ms                                                     | 60.0 ms: 1.11x faster                                                              |
| coroutines               | 16.0 ms                                                     | 14.5 ms: 1.10x faster                                                              |
| xml_etree_parse          | 96.8 ms                                                     | 87.8 ms: 1.10x faster                                                              |
| regex_v8                 | 15.4 ms                                                     | 14.3 ms: 1.08x faster                                                              |
| xml_etree_generate       | 55.5 ms                                                     | 51.4 ms: 1.08x faster                                                              |
| sympy_expand             | 314 ms                                                      | 294 ms: 1.07x faster                                                               |
| json                     | 3.14 ms                                                     | 2.96 ms: 1.06x faster                                                              |
| fannkuch                 | 256 ms                                                      | 244 ms: 1.05x faster                                                               |
| regex_effbot             | 1.66 ms                                                     | 1.59 ms: 1.04x faster                                                              |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.1 ms: 1.03x faster                                                              |
| pidigits                 | 149 ms                                                      | 146 ms: 1.02x faster                                                               |
| logging_format           | 6.76 us                                                     | 6.81 us: 1.01x slower                                                              |
| logging_simple           | 6.22 us                                                     | 6.32 us: 1.02x slower                                                              |
| telco                    | 3.94 ms                                                     | 4.22 ms: 1.07x slower                                                              |
| async_generators         | 222 ms                                                      | 246 ms: 1.11x slower                                                               |
| python_startup_no_site   | 15.5 ms                                                     | 19.3 ms: 1.24x slower                                                              |
| python_startup           | 20.6 ms                                                     | 25.6 ms: 1.24x slower                                                              |
| coverage                 | 39.0 ms                                                     | 50.6 ms: 1.30x slower                                                              |
| gc_traversal             | 1.41 ms                                                     | 2.14 ms: 1.52x slower                                                              |
| create_gc_cycles         | 800 us                                                      | 1.34 ms: 1.67x slower                                                              |
| logging_silent           | 94.6 ns                                                     | 311 ns: 3.28x slower                                                               |
| Geometric mean           | (ref)                                                       | 1.28x faster                                                                       |

Benchmark hidden because not significant (2): json_loads, meteor_contest
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250619-3.15.0a0-2850d72-JIT/bm-20250619-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.305x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.21x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.16x

# Memory
- memory change: unknown