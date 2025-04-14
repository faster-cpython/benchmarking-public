# Results vs. 3.10.4

- fork: faster-cpython
- ref: tos_caching_1
- machine: windows-amd64
- commit hash: 492df4e
- commit date: 2025-04-04
- overall geometric mean: 1.250x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250404-pythonperf1-amd64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 222 ms: 1.11x faster                                                           |
| docutils       | 1.92 sec                                                    | 1.64 sec: 1.17x faster                                                         |
| html5lib       | 51.0 ms                                                     | 38.2 ms: 1.34x faster                                                          |
| Geometric mean | (ref)                                                       | 1.20x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250404-pythonperf1-amd64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|-------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 420 ms: 2.64x faster                                                           |
| async_tree_memoization  | 526 ms                                                      | 213 ms: 2.47x faster                                                           |
| async_tree_none         | 435 ms                                                      | 187 ms: 2.33x faster                                                           |
| async_tree_cpu_io_mixed | 638 ms                                                      | 337 ms: 1.89x faster                                                           |
| Geometric mean          | (ref)                                                       | 2.31x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250404-pythonperf1-amd64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 46.9 ms: 1.32x faster                                                          |
| nbody          | 71.3 ms                                                     | 69.4 ms: 1.03x faster                                                          |
| pidigits       | 149 ms                                                      | 149 ms: 1.00x faster                                                           |
| Geometric mean | (ref)                                                       | 1.11x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250404-pythonperf1-amd64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 83.7 ms: 1.27x faster                                                          |
| regex_dna      | 136 ms                                                      | 114 ms: 1.19x faster                                                           |
| regex_effbot   | 1.66 ms                                                     | 1.40 ms: 1.18x faster                                                          |
| regex_v8       | 15.4 ms                                                     | 13.6 ms: 1.14x faster                                                          |
| Geometric mean | (ref)                                                       | 1.19x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250404-pythonperf1-amd64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.91 ms: 1.33x faster                                                          |
| unpickle_pure_python | 183 us                                                      | 148 us: 1.24x faster                                                           |
| pickle_pure_python   | 270 us                                                      | 221 us: 1.22x faster                                                           |
| tomli_loads          | 1.67 sec                                                    | 1.40 sec: 1.19x faster                                                         |
| xml_etree_parse      | 96.8 ms                                                     | 88.7 ms: 1.09x faster                                                          |
| xml_etree_process    | 44.5 ms                                                     | 41.8 ms: 1.06x faster                                                          |
| xml_etree_iterparse  | 65.0 ms                                                     | 68.1 ms: 1.05x slower                                                          |
| xml_etree_generate   | 55.5 ms                                                     | 59.3 ms: 1.07x slower                                                          |
| json_loads           | 14.0 us                                                     | 15.4 us: 1.10x slower                                                          |
| Geometric mean       | (ref)                                                       | 1.09x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250404-pythonperf1-amd64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 26.5 ms: 1.29x slower                                                          |
| python_startup_no_site | 15.5 ms                                                     | 20.4 ms: 1.32x slower                                                          |
| Geometric mean         | (ref)                                                       | 1.30x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250404-pythonperf1-amd64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 7.25 ms: 1.25x faster                                                          |
| genshi_text     | 19.8 ms                                                     | 16.2 ms: 1.22x faster                                                          |
| django_template | 28.9 ms                                                     | 24.4 ms: 1.19x faster                                                          |
| genshi_xml      | 41.0 ms                                                     | 35.2 ms: 1.16x faster                                                          |
| Geometric mean  | (ref)                                                       | 1.20x faster                                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250404-pythonperf1-amd64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|--------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 107 us: 3.15x faster                                                           |
| async_tree_io            | 1.11 sec                                                    | 420 ms: 2.64x faster                                                           |
| async_tree_memoization   | 526 ms                                                      | 213 ms: 2.47x faster                                                           |
| pathlib                  | 75.7 ms                                                     | 32.2 ms: 2.35x faster                                                          |
| async_tree_none          | 435 ms                                                      | 187 ms: 2.33x faster                                                           |
| mdp                      | 1.78 sec                                                    | 817 ms: 2.18x faster                                                           |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 337 ms: 1.89x faster                                                           |
| deltablue                | 4.19 ms                                                     | 2.26 ms: 1.85x faster                                                          |
| pylint                   | 350 ms                                                      | 200 ms: 1.75x faster                                                           |
| go                       | 139 ms                                                      | 80.0 ms: 1.74x faster                                                          |
| chaos                    | 61.7 ms                                                     | 38.8 ms: 1.59x faster                                                          |
| richards_super           | 52.2 ms                                                     | 33.2 ms: 1.57x faster                                                          |
| raytrace                 | 273 ms                                                      | 178 ms: 1.53x faster                                                           |
| deepcopy_memo            | 28.8 us                                                     | 19.2 us: 1.50x faster                                                          |
| logging_silent           | 94.6 ns                                                     | 64.0 ns: 1.48x faster                                                          |
| richards                 | 42.4 ms                                                     | 29.3 ms: 1.45x faster                                                          |
| deepcopy                 | 255 us                                                      | 177 us: 1.44x faster                                                           |
| generators               | 32.4 ms                                                     | 22.6 ms: 1.43x faster                                                          |
| comprehensions           | 16.5 us                                                     | 11.6 us: 1.42x faster                                                          |
| scimark_monte_carlo      | 57.3 ms                                                     | 40.5 ms: 1.42x faster                                                          |
| pyflate                  | 409 ms                                                      | 291 ms: 1.40x faster                                                           |
| scimark_lu               | 85.8 ms                                                     | 62.8 ms: 1.37x faster                                                          |
| hexiom                   | 5.74 ms                                                     | 4.25 ms: 1.35x faster                                                          |
| html5lib                 | 51.0 ms                                                     | 38.2 ms: 1.34x faster                                                          |
| scimark_sor              | 106 ms                                                      | 80.0 ms: 1.33x faster                                                          |
| crypto_pyaes             | 62.5 ms                                                     | 47.1 ms: 1.33x faster                                                          |
| json_dumps               | 9.16 ms                                                     | 6.91 ms: 1.33x faster                                                          |
| float                    | 61.7 ms                                                     | 46.9 ms: 1.32x faster                                                          |
| spectral_norm            | 77.3 ms                                                     | 59.1 ms: 1.31x faster                                                          |
| pycparser                | 930 ms                                                      | 720 ms: 1.29x faster                                                           |
| regex_compile            | 106 ms                                                      | 83.7 ms: 1.27x faster                                                          |
| mako                     | 9.03 ms                                                     | 7.25 ms: 1.25x faster                                                          |
| unpickle_pure_python     | 183 us                                                      | 148 us: 1.24x faster                                                           |
| genshi_text              | 19.8 ms                                                     | 16.2 ms: 1.22x faster                                                          |
| pickle_pure_python       | 270 us                                                      | 221 us: 1.22x faster                                                           |
| sqlite_synth             | 1.91 us                                                     | 1.58 us: 1.21x faster                                                          |
| sympy_integrate          | 15.3 ms                                                     | 12.7 ms: 1.20x faster                                                          |
| dulwich_log              | 50.5 ms                                                     | 42.0 ms: 1.20x faster                                                          |
| sympy_sum                | 107 ms                                                      | 89.5 ms: 1.20x faster                                                          |
| tomli_loads              | 1.67 sec                                                    | 1.40 sec: 1.19x faster                                                         |
| regex_dna                | 136 ms                                                      | 114 ms: 1.19x faster                                                           |
| django_template          | 28.9 ms                                                     | 24.4 ms: 1.19x faster                                                          |
| regex_effbot             | 1.66 ms                                                     | 1.40 ms: 1.18x faster                                                          |
| deepcopy_reduce          | 2.20 us                                                     | 1.89 us: 1.17x faster                                                          |
| docutils                 | 1.92 sec                                                    | 1.64 sec: 1.17x faster                                                         |
| genshi_xml               | 41.0 ms                                                     | 35.2 ms: 1.16x faster                                                          |
| pprint_pformat           | 1.22 sec                                                    | 1.06 sec: 1.15x faster                                                         |
| pprint_safe_repr         | 592 ms                                                      | 519 ms: 1.14x faster                                                           |
| regex_v8                 | 15.4 ms                                                     | 13.6 ms: 1.14x faster                                                          |
| sympy_str                | 194 ms                                                      | 173 ms: 1.12x faster                                                           |
| 2to3                     | 246 ms                                                      | 222 ms: 1.11x faster                                                           |
| bench_thread_pool        | 958 us                                                      | 870 us: 1.10x faster                                                           |
| xml_etree_parse          | 96.8 ms                                                     | 88.7 ms: 1.09x faster                                                          |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.50 ms: 1.09x faster                                                          |
| xml_etree_process        | 44.5 ms                                                     | 41.8 ms: 1.06x faster                                                          |
| nqueens                  | 66.6 ms                                                     | 62.8 ms: 1.06x faster                                                          |
| scimark_fft              | 187 ms                                                      | 178 ms: 1.05x faster                                                           |
| sympy_expand             | 314 ms                                                      | 299 ms: 1.05x faster                                                           |
| coroutines               | 16.0 ms                                                     | 15.3 ms: 1.05x faster                                                          |
| nbody                    | 71.3 ms                                                     | 69.4 ms: 1.03x faster                                                          |
| meteor_contest           | 75.9 ms                                                     | 74.0 ms: 1.03x faster                                                          |
| pidigits                 | 149 ms                                                      | 149 ms: 1.00x faster                                                           |
| fannkuch                 | 256 ms                                                      | 258 ms: 1.01x slower                                                           |
| logging_simple           | 6.22 us                                                     | 6.28 us: 1.01x slower                                                          |
| xml_etree_iterparse      | 65.0 ms                                                     | 68.1 ms: 1.05x slower                                                          |
| async_generators         | 222 ms                                                      | 233 ms: 1.05x slower                                                           |
| xml_etree_generate       | 55.5 ms                                                     | 59.3 ms: 1.07x slower                                                          |
| json_loads               | 14.0 us                                                     | 15.4 us: 1.10x slower                                                          |
| telco                    | 3.94 ms                                                     | 4.76 ms: 1.21x slower                                                          |
| coverage                 | 39.0 ms                                                     | 49.1 ms: 1.26x slower                                                          |
| python_startup           | 20.6 ms                                                     | 26.5 ms: 1.29x slower                                                          |
| python_startup_no_site   | 15.5 ms                                                     | 20.4 ms: 1.32x slower                                                          |
| bench_mp_pool            | 62.0 ms                                                     | 88.4 ms: 1.42x slower                                                          |
| gc_traversal             | 1.41 ms                                                     | 2.03 ms: 1.44x slower                                                          |
| create_gc_cycles         | 800 us                                                      | 1.22 ms: 1.53x slower                                                          |
| Geometric mean           | (ref)                                                       | 1.24x faster                                                                   |

Benchmark hidden because not significant (2): logging_format, json
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250404-3.14.0a6+-492df4e/bm-20250404-pythonperf1-amd64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.250x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.16x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.14x

# Memory
- memory change: unknown