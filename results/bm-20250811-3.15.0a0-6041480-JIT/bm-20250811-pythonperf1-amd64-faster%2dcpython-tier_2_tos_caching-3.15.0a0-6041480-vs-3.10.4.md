# Results vs. 3.10.4

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: windows-amd64
- commit hash: 6041480
- commit date: 2025-08-11
- overall geometric mean: 1.327x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250811-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6041480 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 222 ms: 1.11x faster                                                               |
| docutils       | 1.92 sec                                                    | 1.65 sec: 1.16x faster                                                             |
| html5lib       | 51.0 ms                                                     | 39.1 ms: 1.31x faster                                                              |
| Geometric mean | (ref)                                                       | 1.19x faster                                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250811-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6041480 |
|-------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 383 ms: 2.90x faster                                                               |
| async_tree_memoization  | 526 ms                                                      | 204 ms: 2.58x faster                                                               |
| async_tree_none         | 435 ms                                                      | 172 ms: 2.53x faster                                                               |
| async_tree_cpu_io_mixed | 638 ms                                                      | 335 ms: 1.91x faster                                                               |
| Geometric mean          | (ref)                                                       | 2.45x faster                                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250811-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6041480 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| nbody          | 71.3 ms                                                     | 45.2 ms: 1.58x faster                                                              |
| float          | 61.7 ms                                                     | 43.7 ms: 1.41x faster                                                              |
| pidigits       | 149 ms                                                      | 146 ms: 1.02x faster                                                               |
| Geometric mean | (ref)                                                       | 1.31x faster                                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250811-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6041480 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 78.0 ms: 1.36x faster                                                              |
| regex_dna      | 136 ms                                                      | 115 ms: 1.19x faster                                                               |
| regex_v8       | 15.4 ms                                                     | 13.3 ms: 1.16x faster                                                              |
| regex_effbot   | 1.66 ms                                                     | 1.54 ms: 1.07x faster                                                              |
| Geometric mean | (ref)                                                       | 1.19x faster                                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250811-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6041480 |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 108 us: 1.70x faster                                                               |
| json_dumps           | 9.16 ms                                                     | 5.60 ms: 1.63x faster                                                              |
| tomli_loads          | 1.67 sec                                                    | 1.11 sec: 1.50x faster                                                             |
| pickle_pure_python   | 270 us                                                      | 204 us: 1.32x faster                                                               |
| xml_etree_process    | 44.5 ms                                                     | 35.0 ms: 1.27x faster                                                              |
| xml_etree_parse      | 96.8 ms                                                     | 87.1 ms: 1.11x faster                                                              |
| xml_etree_generate   | 55.5 ms                                                     | 50.2 ms: 1.11x faster                                                              |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.1 ms: 1.03x faster                                                              |
| json_loads           | 14.0 us                                                     | 14.3 us: 1.02x slower                                                              |
| Geometric mean       | (ref)                                                       | 1.27x faster                                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250811-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6041480 |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 19.7 ms: 1.27x slower                                                              |
| python_startup         | 20.6 ms                                                     | 26.5 ms: 1.29x slower                                                              |
| Geometric mean         | (ref)                                                       | 1.28x slower                                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250811-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6041480 |
|-----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.47 ms: 1.65x faster                                                              |
| genshi_text     | 19.8 ms                                                     | 15.7 ms: 1.26x faster                                                              |
| genshi_xml      | 41.0 ms                                                     | 34.2 ms: 1.20x faster                                                              |
| django_template | 28.9 ms                                                     | 24.4 ms: 1.18x faster                                                              |
| Geometric mean  | (ref)                                                       | 1.31x faster                                                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250811-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6041480 |
|--------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 103 us: 3.26x faster                                                               |
| async_tree_io            | 1.11 sec                                                    | 383 ms: 2.90x faster                                                               |
| async_tree_memoization   | 526 ms                                                      | 204 ms: 2.58x faster                                                               |
| async_tree_none          | 435 ms                                                      | 172 ms: 2.53x faster                                                               |
| pathlib                  | 75.7 ms                                                     | 31.7 ms: 2.39x faster                                                              |
| mdp                      | 1.78 sec                                                    | 796 ms: 2.24x faster                                                               |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 335 ms: 1.91x faster                                                               |
| go                       | 139 ms                                                      | 75.7 ms: 1.84x faster                                                              |
| deltablue                | 4.19 ms                                                     | 2.29 ms: 1.83x faster                                                              |
| pylint                   | 350 ms                                                      | 200 ms: 1.75x faster                                                               |
| richards_super           | 52.2 ms                                                     | 30.1 ms: 1.73x faster                                                              |
| logging_silent           | 94.6 ns                                                     | 55.3 ns: 1.71x faster                                                              |
| unpickle_pure_python     | 183 us                                                      | 108 us: 1.70x faster                                                               |
| generators               | 32.4 ms                                                     | 19.4 ms: 1.67x faster                                                              |
| deepcopy_memo            | 28.8 us                                                     | 17.2 us: 1.67x faster                                                              |
| mako                     | 9.03 ms                                                     | 5.47 ms: 1.65x faster                                                              |
| json_dumps               | 9.16 ms                                                     | 5.60 ms: 1.63x faster                                                              |
| richards                 | 42.4 ms                                                     | 26.6 ms: 1.60x faster                                                              |
| nbody                    | 71.3 ms                                                     | 45.2 ms: 1.58x faster                                                              |
| comprehensions           | 16.5 us                                                     | 10.5 us: 1.57x faster                                                              |
| pyflate                  | 409 ms                                                      | 262 ms: 1.56x faster                                                               |
| raytrace                 | 273 ms                                                      | 177 ms: 1.55x faster                                                               |
| deepcopy                 | 255 us                                                      | 166 us: 1.54x faster                                                               |
| chaos                    | 61.7 ms                                                     | 40.5 ms: 1.52x faster                                                              |
| scimark_lu               | 85.8 ms                                                     | 56.9 ms: 1.51x faster                                                              |
| tomli_loads              | 1.67 sec                                                    | 1.11 sec: 1.50x faster                                                             |
| scimark_monte_carlo      | 57.3 ms                                                     | 39.8 ms: 1.44x faster                                                              |
| float                    | 61.7 ms                                                     | 43.7 ms: 1.41x faster                                                              |
| scimark_sor              | 106 ms                                                      | 75.4 ms: 1.41x faster                                                              |
| hexiom                   | 5.74 ms                                                     | 4.13 ms: 1.39x faster                                                              |
| crypto_pyaes             | 62.5 ms                                                     | 45.6 ms: 1.37x faster                                                              |
| regex_compile            | 106 ms                                                      | 78.0 ms: 1.36x faster                                                              |
| pprint_pformat           | 1.22 sec                                                    | 898 ms: 1.36x faster                                                               |
| pprint_safe_repr         | 592 ms                                                      | 437 ms: 1.35x faster                                                               |
| pycparser                | 930 ms                                                      | 688 ms: 1.35x faster                                                               |
| pickle_pure_python       | 270 us                                                      | 204 us: 1.32x faster                                                               |
| html5lib                 | 51.0 ms                                                     | 39.1 ms: 1.31x faster                                                              |
| scimark_fft              | 187 ms                                                      | 147 ms: 1.27x faster                                                               |
| xml_etree_process        | 44.5 ms                                                     | 35.0 ms: 1.27x faster                                                              |
| genshi_text              | 19.8 ms                                                     | 15.7 ms: 1.26x faster                                                              |
| sqlite_synth             | 1.91 us                                                     | 1.54 us: 1.24x faster                                                              |
| thrift                   | 617 us                                                      | 499 us: 1.24x faster                                                               |
| dulwich_log              | 50.5 ms                                                     | 41.3 ms: 1.22x faster                                                              |
| deepcopy_reduce          | 2.20 us                                                     | 1.81 us: 1.22x faster                                                              |
| sympy_sum                | 107 ms                                                      | 87.8 ms: 1.22x faster                                                              |
| fannkuch                 | 256 ms                                                      | 212 ms: 1.20x faster                                                               |
| sympy_integrate          | 15.3 ms                                                     | 12.7 ms: 1.20x faster                                                              |
| genshi_xml               | 41.0 ms                                                     | 34.2 ms: 1.20x faster                                                              |
| regex_dna                | 136 ms                                                      | 115 ms: 1.19x faster                                                               |
| django_template          | 28.9 ms                                                     | 24.4 ms: 1.18x faster                                                              |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.32 ms: 1.18x faster                                                              |
| spectral_norm            | 77.3 ms                                                     | 66.5 ms: 1.16x faster                                                              |
| regex_v8                 | 15.4 ms                                                     | 13.3 ms: 1.16x faster                                                              |
| docutils                 | 1.92 sec                                                    | 1.65 sec: 1.16x faster                                                             |
| sympy_str                | 194 ms                                                      | 171 ms: 1.14x faster                                                               |
| nqueens                  | 66.6 ms                                                     | 59.1 ms: 1.13x faster                                                              |
| xml_etree_parse          | 96.8 ms                                                     | 87.1 ms: 1.11x faster                                                              |
| 2to3                     | 246 ms                                                      | 222 ms: 1.11x faster                                                               |
| xml_etree_generate       | 55.5 ms                                                     | 50.2 ms: 1.11x faster                                                              |
| meteor_contest           | 75.9 ms                                                     | 70.2 ms: 1.08x faster                                                              |
| coroutines               | 16.0 ms                                                     | 14.8 ms: 1.08x faster                                                              |
| regex_effbot             | 1.66 ms                                                     | 1.54 ms: 1.07x faster                                                              |
| sympy_expand             | 314 ms                                                      | 297 ms: 1.06x faster                                                               |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.1 ms: 1.03x faster                                                              |
| json                     | 3.14 ms                                                     | 3.05 ms: 1.03x faster                                                              |
| logging_format           | 6.76 us                                                     | 6.60 us: 1.02x faster                                                              |
| logging_simple           | 6.22 us                                                     | 6.08 us: 1.02x faster                                                              |
| pidigits                 | 149 ms                                                      | 146 ms: 1.02x faster                                                               |
| json_loads               | 14.0 us                                                     | 14.3 us: 1.02x slower                                                              |
| telco                    | 3.94 ms                                                     | 4.25 ms: 1.08x slower                                                              |
| async_generators         | 222 ms                                                      | 246 ms: 1.11x slower                                                               |
| coverage                 | 39.0 ms                                                     | 49.5 ms: 1.27x slower                                                              |
| python_startup_no_site   | 15.5 ms                                                     | 19.7 ms: 1.27x slower                                                              |
| python_startup           | 20.6 ms                                                     | 26.5 ms: 1.29x slower                                                              |
| gc_traversal             | 1.41 ms                                                     | 2.13 ms: 1.51x slower                                                              |
| create_gc_cycles         | 800 us                                                      | 1.31 ms: 1.64x slower                                                              |
| Geometric mean           | (ref)                                                       | 1.33x faster                                                                       |
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250811-3.15.0a0-6041480-JIT/bm-20250811-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6041480.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.327x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: unknown