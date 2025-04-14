# Results vs. 3.10.4

- fork: Fidget-Spinner
- ref: trace_function_entry
- machine: windows-amd64
- commit hash: 553888a
- commit date: 2025-03-07
- overall geometric mean: 1.254x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250307-pythonperf1-amd64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 225 ms: 1.09x faster                                                                  |
| html5lib       | 51.0 ms                                                     | 40.6 ms: 1.26x faster                                                                 |
| Geometric mean | (ref)                                                       | 1.17x faster                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250307-pythonperf1-amd64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|-------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 418 ms: 2.65x faster                                                                  |
| async_tree_memoization  | 526 ms                                                      | 216 ms: 2.44x faster                                                                  |
| async_tree_none         | 435 ms                                                      | 185 ms: 2.35x faster                                                                  |
| async_tree_cpu_io_mixed | 638 ms                                                      | 343 ms: 1.86x faster                                                                  |
| Geometric mean          | (ref)                                                       | 2.31x faster                                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250307-pythonperf1-amd64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 41.4 ms: 1.49x faster                                                                 |
| nbody          | 71.3 ms                                                     | 62.2 ms: 1.15x faster                                                                 |
| pidigits       | 149 ms                                                      | 153 ms: 1.02x slower                                                                  |
| Geometric mean | (ref)                                                       | 1.19x faster                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250307-pythonperf1-amd64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 85.5 ms: 1.24x faster                                                                 |
| regex_dna      | 136 ms                                                      | 118 ms: 1.15x faster                                                                  |
| regex_effbot   | 1.66 ms                                                     | 1.46 ms: 1.14x faster                                                                 |
| Geometric mean | (ref)                                                       | 1.13x faster                                                                          |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250307-pythonperf1-amd64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|----------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 117 us: 1.57x faster                                                                  |
| tomli_loads          | 1.67 sec                                                    | 1.25 sec: 1.34x faster                                                                |
| json_dumps           | 9.16 ms                                                     | 6.87 ms: 1.33x faster                                                                 |
| pickle_pure_python   | 270 us                                                      | 218 us: 1.24x faster                                                                  |
| xml_etree_process    | 44.5 ms                                                     | 36.0 ms: 1.23x faster                                                                 |
| xml_etree_generate   | 55.5 ms                                                     | 50.9 ms: 1.09x faster                                                                 |
| xml_etree_parse      | 96.8 ms                                                     | 90.9 ms: 1.07x faster                                                                 |
| xml_etree_iterparse  | 65.0 ms                                                     | 62.9 ms: 1.03x faster                                                                 |
| json_loads           | 14.0 us                                                     | 14.9 us: 1.06x slower                                                                 |
| Geometric mean       | (ref)                                                       | 1.19x faster                                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250307-pythonperf1-amd64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 26.1 ms: 1.26x slower                                                                 |
| python_startup_no_site | 15.5 ms                                                     | 20.7 ms: 1.33x slower                                                                 |
| Geometric mean         | (ref)                                                       | 1.30x slower                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250307-pythonperf1-amd64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|-----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.46 ms: 1.66x faster                                                                 |
| genshi_text     | 19.8 ms                                                     | 17.0 ms: 1.17x faster                                                                 |
| django_template | 28.9 ms                                                     | 25.9 ms: 1.12x faster                                                                 |
| genshi_xml      | 41.0 ms                                                     | 38.3 ms: 1.07x faster                                                                 |
| Geometric mean  | (ref)                                                       | 1.23x faster                                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250307-pythonperf1-amd64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|--------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 106 us: 3.17x faster                                                                  |
| async_tree_io            | 1.11 sec                                                    | 418 ms: 2.65x faster                                                                  |
| async_tree_memoization   | 526 ms                                                      | 216 ms: 2.44x faster                                                                  |
| pathlib                  | 75.7 ms                                                     | 31.9 ms: 2.37x faster                                                                 |
| async_tree_none          | 435 ms                                                      | 185 ms: 2.35x faster                                                                  |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 343 ms: 1.86x faster                                                                  |
| deltablue                | 4.19 ms                                                     | 2.28 ms: 1.84x faster                                                                 |
| pylint                   | 350 ms                                                      | 203 ms: 1.72x faster                                                                  |
| mako                     | 9.03 ms                                                     | 5.46 ms: 1.66x faster                                                                 |
| go                       | 139 ms                                                      | 86.9 ms: 1.60x faster                                                                 |
| unpickle_pure_python     | 183 us                                                      | 117 us: 1.57x faster                                                                  |
| generators               | 32.4 ms                                                     | 20.7 ms: 1.56x faster                                                                 |
| richards_super           | 52.2 ms                                                     | 33.4 ms: 1.56x faster                                                                 |
| pyflate                  | 409 ms                                                      | 273 ms: 1.50x faster                                                                  |
| float                    | 61.7 ms                                                     | 41.4 ms: 1.49x faster                                                                 |
| logging_silent           | 94.6 ns                                                     | 63.8 ns: 1.48x faster                                                                 |
| comprehensions           | 16.5 us                                                     | 11.3 us: 1.46x faster                                                                 |
| chaos                    | 61.7 ms                                                     | 42.4 ms: 1.46x faster                                                                 |
| richards                 | 42.4 ms                                                     | 29.7 ms: 1.43x faster                                                                 |
| deepcopy_memo            | 28.8 us                                                     | 20.3 us: 1.42x faster                                                                 |
| sqlglot_parse            | 1.22 ms                                                     | 865 us: 1.40x faster                                                                  |
| raytrace                 | 273 ms                                                      | 195 ms: 1.40x faster                                                                  |
| deepcopy                 | 255 us                                                      | 187 us: 1.36x faster                                                                  |
| sqlglot_transpile        | 1.48 ms                                                     | 1.09 ms: 1.35x faster                                                                 |
| tomli_loads              | 1.67 sec                                                    | 1.25 sec: 1.34x faster                                                                |
| json_dumps               | 9.16 ms                                                     | 6.87 ms: 1.33x faster                                                                 |
| scimark_lu               | 85.8 ms                                                     | 64.7 ms: 1.33x faster                                                                 |
| crypto_pyaes             | 62.5 ms                                                     | 48.1 ms: 1.30x faster                                                                 |
| hexiom                   | 5.74 ms                                                     | 4.43 ms: 1.30x faster                                                                 |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.16 ms: 1.26x faster                                                                 |
| pycparser                | 930 ms                                                      | 739 ms: 1.26x faster                                                                  |
| html5lib                 | 51.0 ms                                                     | 40.6 ms: 1.26x faster                                                                 |
| sqlite_synth             | 1.91 us                                                     | 1.54 us: 1.24x faster                                                                 |
| regex_compile            | 106 ms                                                      | 85.5 ms: 1.24x faster                                                                 |
| pickle_pure_python       | 270 us                                                      | 218 us: 1.24x faster                                                                  |
| xml_etree_process        | 44.5 ms                                                     | 36.0 ms: 1.23x faster                                                                 |
| scimark_monte_carlo      | 57.3 ms                                                     | 46.5 ms: 1.23x faster                                                                 |
| scimark_fft              | 187 ms                                                      | 152 ms: 1.23x faster                                                                  |
| scimark_sor              | 106 ms                                                      | 88.2 ms: 1.20x faster                                                                 |
| thrift                   | 617 us                                                      | 516 us: 1.20x faster                                                                  |
| sympy_sum                | 107 ms                                                      | 90.5 ms: 1.18x faster                                                                 |
| dulwich_log              | 50.5 ms                                                     | 43.1 ms: 1.17x faster                                                                 |
| genshi_text              | 19.8 ms                                                     | 17.0 ms: 1.17x faster                                                                 |
| spectral_norm            | 77.3 ms                                                     | 66.6 ms: 1.16x faster                                                                 |
| coroutines               | 16.0 ms                                                     | 13.8 ms: 1.16x faster                                                                 |
| regex_dna                | 136 ms                                                      | 118 ms: 1.15x faster                                                                  |
| mdp                      | 1.78 sec                                                    | 1.55 sec: 1.15x faster                                                                |
| nbody                    | 71.3 ms                                                     | 62.2 ms: 1.15x faster                                                                 |
| regex_effbot             | 1.66 ms                                                     | 1.46 ms: 1.14x faster                                                                 |
| sympy_integrate          | 15.3 ms                                                     | 13.5 ms: 1.14x faster                                                                 |
| deepcopy_reduce          | 2.20 us                                                     | 1.95 us: 1.13x faster                                                                 |
| django_template          | 28.9 ms                                                     | 25.9 ms: 1.12x faster                                                                 |
| bench_thread_pool        | 958 us                                                      | 857 us: 1.12x faster                                                                  |
| sympy_str                | 194 ms                                                      | 178 ms: 1.09x faster                                                                  |
| xml_etree_generate       | 55.5 ms                                                     | 50.9 ms: 1.09x faster                                                                 |
| 2to3                     | 246 ms                                                      | 225 ms: 1.09x faster                                                                  |
| nqueens                  | 66.6 ms                                                     | 61.2 ms: 1.09x faster                                                                 |
| genshi_xml               | 41.0 ms                                                     | 38.3 ms: 1.07x faster                                                                 |
| xml_etree_parse          | 96.8 ms                                                     | 90.9 ms: 1.07x faster                                                                 |
| json                     | 3.14 ms                                                     | 2.97 ms: 1.06x faster                                                                 |
| fannkuch                 | 256 ms                                                      | 244 ms: 1.05x faster                                                                  |
| xml_etree_iterparse      | 65.0 ms                                                     | 62.9 ms: 1.03x faster                                                                 |
| sympy_expand             | 314 ms                                                      | 306 ms: 1.03x faster                                                                  |
| meteor_contest           | 75.9 ms                                                     | 74.2 ms: 1.02x faster                                                                 |
| pidigits                 | 149 ms                                                      | 153 ms: 1.02x slower                                                                  |
| logging_format           | 6.76 us                                                     | 7.00 us: 1.04x slower                                                                 |
| logging_simple           | 6.22 us                                                     | 6.58 us: 1.06x slower                                                                 |
| json_loads               | 14.0 us                                                     | 14.9 us: 1.06x slower                                                                 |
| telco                    | 3.94 ms                                                     | 4.40 ms: 1.12x slower                                                                 |
| coverage                 | 39.0 ms                                                     | 49.1 ms: 1.26x slower                                                                 |
| python_startup           | 20.6 ms                                                     | 26.1 ms: 1.26x slower                                                                 |
| python_startup_no_site   | 15.5 ms                                                     | 20.7 ms: 1.33x slower                                                                 |
| bench_mp_pool            | 62.0 ms                                                     | 87.5 ms: 1.41x slower                                                                 |
| gc_traversal             | 1.41 ms                                                     | 2.07 ms: 1.47x slower                                                                 |
| create_gc_cycles         | 800 us                                                      | 1.25 ms: 1.56x slower                                                                 |
| Geometric mean           | (ref)                                                       | 1.24x faster                                                                          |

Benchmark hidden because not significant (2): async_generators, regex_v8
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, docutils, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, pprint_pformat, pprint_safe_repr, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250307-3.14.0a5+-553888a-JIT/bm-20250307-pythonperf1-amd64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.254x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.14x

# Memory
- memory change: unknown