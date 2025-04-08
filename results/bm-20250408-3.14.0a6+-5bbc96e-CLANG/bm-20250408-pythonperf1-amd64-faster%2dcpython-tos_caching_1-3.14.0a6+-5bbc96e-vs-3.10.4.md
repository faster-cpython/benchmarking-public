# Results vs. 3.10.4

- fork: faster-cpython
- ref: tos_caching_1
- machine: windows-amd64
- commit hash: 5bbc96e
- commit date: 2025-04-08
- overall geometric mean: 1.526x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.36x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250408-pythonperf1-amd64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 198 ms: 1.24x faster                                                           |
| docutils       | 1.92 sec                                                    | 1.53 sec: 1.26x faster                                                         |
| html5lib       | 51.0 ms                                                     | 33.3 ms: 1.53x faster                                                          |
| Geometric mean | (ref)                                                       | 1.34x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250408-pythonperf1-amd64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|-------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 343 ms: 3.23x faster                                                           |
| async_tree_memoization  | 526 ms                                                      | 183 ms: 2.87x faster                                                           |
| async_tree_none         | 435 ms                                                      | 153 ms: 2.84x faster                                                           |
| async_tree_cpu_io_mixed | 638 ms                                                      | 311 ms: 2.05x faster                                                           |
| Geometric mean          | (ref)                                                       | 2.71x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250408-pythonperf1-amd64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 35.9 ms: 1.72x faster                                                          |
| nbody          | 71.3 ms                                                     | 52.8 ms: 1.35x faster                                                          |
| pidigits       | 149 ms                                                      | 144 ms: 1.03x faster                                                           |
| Geometric mean | (ref)                                                       | 1.34x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250408-pythonperf1-amd64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 67.5 ms: 1.57x faster                                                          |
| regex_v8       | 15.4 ms                                                     | 12.3 ms: 1.26x faster                                                          |
| regex_dna      | 136 ms                                                      | 116 ms: 1.18x faster                                                           |
| regex_effbot   | 1.66 ms                                                     | 1.47 ms: 1.13x faster                                                          |
| Geometric mean | (ref)                                                       | 1.27x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250408-pythonperf1-amd64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 104 us: 1.76x faster                                                           |
| tomli_loads          | 1.67 sec                                                    | 981 ms: 1.70x faster                                                           |
| json_dumps           | 9.16 ms                                                     | 5.58 ms: 1.64x faster                                                          |
| pickle_pure_python   | 270 us                                                      | 165 us: 1.63x faster                                                           |
| xml_etree_process    | 44.5 ms                                                     | 32.8 ms: 1.35x faster                                                          |
| xml_etree_generate   | 55.5 ms                                                     | 48.8 ms: 1.14x faster                                                          |
| xml_etree_parse      | 96.8 ms                                                     | 89.6 ms: 1.08x faster                                                          |
| xml_etree_iterparse  | 65.0 ms                                                     | 61.0 ms: 1.06x faster                                                          |
| Geometric mean       | (ref)                                                       | 1.34x faster                                                                   |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250408-pythonperf1-amd64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 26.8 ms: 1.30x slower                                                          |
| python_startup_no_site | 15.5 ms                                                     | 20.7 ms: 1.34x slower                                                          |
| Geometric mean         | (ref)                                                       | 1.32x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250408-pythonperf1-amd64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_text     | 19.8 ms                                                     | 11.1 ms: 1.79x faster                                                          |
| mako            | 9.03 ms                                                     | 5.76 ms: 1.57x faster                                                          |
| django_template | 28.9 ms                                                     | 18.8 ms: 1.54x faster                                                          |
| genshi_xml      | 41.0 ms                                                     | 27.1 ms: 1.52x faster                                                          |
| Geometric mean  | (ref)                                                       | 1.60x faster                                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250408-pythonperf1-amd64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|--------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 86.9 us: 3.87x faster                                                          |
| async_tree_io            | 1.11 sec                                                    | 343 ms: 3.23x faster                                                           |
| async_tree_memoization   | 526 ms                                                      | 183 ms: 2.87x faster                                                           |
| async_tree_none          | 435 ms                                                      | 153 ms: 2.84x faster                                                           |
| deltablue                | 4.19 ms                                                     | 1.48 ms: 2.83x faster                                                          |
| mdp                      | 1.78 sec                                                    | 671 ms: 2.65x faster                                                           |
| go                       | 139 ms                                                      | 54.8 ms: 2.53x faster                                                          |
| pathlib                  | 75.7 ms                                                     | 30.7 ms: 2.47x faster                                                          |
| generators               | 32.4 ms                                                     | 14.2 ms: 2.28x faster                                                          |
| scimark_sor              | 106 ms                                                      | 47.2 ms: 2.25x faster                                                          |
| logging_silent           | 94.6 ns                                                     | 42.4 ns: 2.23x faster                                                          |
| richards_super           | 52.2 ms                                                     | 23.5 ms: 2.22x faster                                                          |
| deepcopy_memo            | 28.8 us                                                     | 13.3 us: 2.17x faster                                                          |
| chaos                    | 61.7 ms                                                     | 29.5 ms: 2.09x faster                                                          |
| scimark_monte_carlo      | 57.3 ms                                                     | 27.5 ms: 2.08x faster                                                          |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 311 ms: 2.05x faster                                                           |
| raytrace                 | 273 ms                                                      | 134 ms: 2.04x faster                                                           |
| hexiom                   | 5.74 ms                                                     | 2.81 ms: 2.04x faster                                                          |
| richards                 | 42.4 ms                                                     | 20.8 ms: 2.04x faster                                                          |
| comprehensions           | 16.5 us                                                     | 8.19 us: 2.01x faster                                                          |
| pylint                   | 350 ms                                                      | 183 ms: 1.91x faster                                                           |
| deepcopy                 | 255 us                                                      | 135 us: 1.90x faster                                                           |
| scimark_lu               | 85.8 ms                                                     | 45.4 ms: 1.89x faster                                                          |
| pyflate                  | 409 ms                                                      | 224 ms: 1.83x faster                                                           |
| genshi_text              | 19.8 ms                                                     | 11.1 ms: 1.79x faster                                                          |
| unpickle_pure_python     | 183 us                                                      | 104 us: 1.76x faster                                                           |
| spectral_norm            | 77.3 ms                                                     | 44.9 ms: 1.72x faster                                                          |
| float                    | 61.7 ms                                                     | 35.9 ms: 1.72x faster                                                          |
| tomli_loads              | 1.67 sec                                                    | 981 ms: 1.70x faster                                                           |
| crypto_pyaes             | 62.5 ms                                                     | 37.8 ms: 1.66x faster                                                          |
| json_dumps               | 9.16 ms                                                     | 5.58 ms: 1.64x faster                                                          |
| pickle_pure_python       | 270 us                                                      | 165 us: 1.63x faster                                                           |
| regex_compile            | 106 ms                                                      | 67.5 ms: 1.57x faster                                                          |
| mako                     | 9.03 ms                                                     | 5.76 ms: 1.57x faster                                                          |
| deepcopy_reduce          | 2.20 us                                                     | 1.43 us: 1.55x faster                                                          |
| django_template          | 28.9 ms                                                     | 18.8 ms: 1.54x faster                                                          |
| html5lib                 | 51.0 ms                                                     | 33.3 ms: 1.53x faster                                                          |
| genshi_xml               | 41.0 ms                                                     | 27.1 ms: 1.52x faster                                                          |
| pycparser                | 930 ms                                                      | 622 ms: 1.50x faster                                                           |
| pprint_pformat           | 1.22 sec                                                    | 815 ms: 1.50x faster                                                           |
| pprint_safe_repr         | 592 ms                                                      | 399 ms: 1.48x faster                                                           |
| coroutines               | 16.0 ms                                                     | 10.9 ms: 1.47x faster                                                          |
| nqueens                  | 66.6 ms                                                     | 46.2 ms: 1.44x faster                                                          |
| sympy_integrate          | 15.3 ms                                                     | 11.2 ms: 1.37x faster                                                          |
| sympy_sum                | 107 ms                                                      | 78.2 ms: 1.37x faster                                                          |
| xml_etree_process        | 44.5 ms                                                     | 32.8 ms: 1.35x faster                                                          |
| scimark_fft              | 187 ms                                                      | 139 ms: 1.35x faster                                                           |
| nbody                    | 71.3 ms                                                     | 52.8 ms: 1.35x faster                                                          |
| sympy_str                | 194 ms                                                      | 149 ms: 1.31x faster                                                           |
| sqlite_synth             | 1.91 us                                                     | 1.48 us: 1.29x faster                                                          |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.13 ms: 1.28x faster                                                          |
| fannkuch                 | 256 ms                                                      | 200 ms: 1.28x faster                                                           |
| regex_v8                 | 15.4 ms                                                     | 12.3 ms: 1.26x faster                                                          |
| dulwich_log              | 50.5 ms                                                     | 40.1 ms: 1.26x faster                                                          |
| docutils                 | 1.92 sec                                                    | 1.53 sec: 1.26x faster                                                         |
| 2to3                     | 246 ms                                                      | 198 ms: 1.24x faster                                                           |
| async_generators         | 222 ms                                                      | 181 ms: 1.23x faster                                                           |
| sympy_expand             | 314 ms                                                      | 257 ms: 1.22x faster                                                           |
| logging_format           | 6.76 us                                                     | 5.70 us: 1.19x faster                                                          |
| regex_dna                | 136 ms                                                      | 116 ms: 1.18x faster                                                           |
| logging_simple           | 6.22 us                                                     | 5.29 us: 1.18x faster                                                          |
| bench_thread_pool        | 958 us                                                      | 834 us: 1.15x faster                                                           |
| meteor_contest           | 75.9 ms                                                     | 66.4 ms: 1.14x faster                                                          |
| xml_etree_generate       | 55.5 ms                                                     | 48.8 ms: 1.14x faster                                                          |
| regex_effbot             | 1.66 ms                                                     | 1.47 ms: 1.13x faster                                                          |
| json                     | 3.14 ms                                                     | 2.88 ms: 1.09x faster                                                          |
| xml_etree_parse          | 96.8 ms                                                     | 89.6 ms: 1.08x faster                                                          |
| xml_etree_iterparse      | 65.0 ms                                                     | 61.0 ms: 1.06x faster                                                          |
| pidigits                 | 149 ms                                                      | 144 ms: 1.03x faster                                                           |
| coverage                 | 39.0 ms                                                     | 39.5 ms: 1.01x slower                                                          |
| telco                    | 3.94 ms                                                     | 4.22 ms: 1.07x slower                                                          |
| python_startup           | 20.6 ms                                                     | 26.8 ms: 1.30x slower                                                          |
| python_startup_no_site   | 15.5 ms                                                     | 20.7 ms: 1.34x slower                                                          |
| bench_mp_pool            | 62.0 ms                                                     | 88.3 ms: 1.42x slower                                                          |
| create_gc_cycles         | 800 us                                                      | 1.35 ms: 1.69x slower                                                          |
| gc_traversal             | 1.41 ms                                                     | 2.77 ms: 1.97x slower                                                          |
| Geometric mean           | (ref)                                                       | 1.51x faster                                                                   |

Benchmark hidden because not significant (1): json_loads
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250408-3.14.0a6+-5bbc96e-CLANG/bm-20250408-pythonperf1-amd64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.526x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.44x
- 95% likely to have a speedup of 1.41x
- 99% likely to have a speedup of 1.36x

# Memory
- memory change: unknown