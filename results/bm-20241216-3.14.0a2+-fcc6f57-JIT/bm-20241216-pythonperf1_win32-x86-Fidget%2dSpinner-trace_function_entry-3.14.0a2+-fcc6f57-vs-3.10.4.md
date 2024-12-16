# Results vs. 3.10.4

- fork: Fidget-Spinner
- ref: trace_function_entry
- machine: windows-x86
- commit hash: fcc6f57
- commit date: 2024-12-16
- overall geometric mean: 1.104x faster
- HPT reliability: 99.91%
- HPT 99th percentile: 1.01x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241216-pythonperf1_win32-x86-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 259 ms: 1.02x faster                                                                      |
| docutils       | 1.95 sec                                                        | 1.91 sec: 1.02x faster                                                                    |
| html5lib       | 52.1 ms                                                         | 45.8 ms: 1.14x faster                                                                     |
| Geometric mean | (ref)                                                           | 1.06x faster                                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241216-pythonperf1_win32-x86-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|-------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------------------:|
| async_tree_io           | 940 ms                                                          | 466 ms: 2.02x faster                                                                      |
| async_tree_cpu_io_mixed | 922 ms                                                          | 472 ms: 1.95x faster                                                                      |
| async_tree_none         | 394 ms                                                          | 216 ms: 1.82x faster                                                                      |
| async_tree_memoization  | 467 ms                                                          | 273 ms: 1.71x faster                                                                      |
| Geometric mean          | (ref)                                                           | 1.87x faster                                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241216-pythonperf1_win32-x86-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 200 ms: 2.51x faster                                                                      |
| float          | 69.6 ms                                                         | 56.9 ms: 1.22x faster                                                                     |
| nbody          | 79.1 ms                                                         | 98.2 ms: 1.24x slower                                                                     |
| Geometric mean | (ref)                                                           | 1.35x faster                                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241216-pythonperf1_win32-x86-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 114 ms: 1.15x faster                                                                      |
| regex_compile  | 117 ms                                                          | 110 ms: 1.06x faster                                                                      |
| regex_effbot   | 1.66 ms                                                         | 1.58 ms: 1.05x faster                                                                     |
| regex_v8       | 15.8 ms                                                         | 15.5 ms: 1.01x faster                                                                     |
| Geometric mean | (ref)                                                           | 1.07x faster                                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241216-pythonperf1_win32-x86-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------------------:|
| xml_etree_parse      | 120 ms                                                          | 107 ms: 1.12x faster                                                                      |
| json_dumps           | 9.82 ms                                                         | 9.00 ms: 1.09x faster                                                                     |
| json_loads           | 22.4 us                                                         | 20.7 us: 1.08x faster                                                                     |
| tomli_loads          | 1.91 sec                                                        | 1.79 sec: 1.07x faster                                                                    |
| xml_etree_iterparse  | 70.8 ms                                                         | 66.4 ms: 1.07x faster                                                                     |
| pickle_pure_python   | 280 us                                                          | 303 us: 1.08x slower                                                                      |
| unpickle_pure_python | 189 us                                                          | 206 us: 1.09x slower                                                                      |
| xml_etree_process    | 48.1 ms                                                         | 53.5 ms: 1.11x slower                                                                     |
| xml_etree_generate   | 61.6 ms                                                         | 71.9 ms: 1.17x slower                                                                     |
| Geometric mean       | (ref)                                                           | 1.00x slower                                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241216-pythonperf1_win32-x86-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 19.6 ms: 1.08x slower                                                                     |
| python_startup         | 22.9 ms                                                         | 26.1 ms: 1.14x slower                                                                     |
| Geometric mean         | (ref)                                                           | 1.11x slower                                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241216-pythonperf1_win32-x86-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|-----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 7.49 ms: 1.22x faster                                                                     |
| django_template | 36.0 ms                                                         | 33.9 ms: 1.06x faster                                                                     |
| genshi_xml      | 46.6 ms                                                         | 51.5 ms: 1.11x slower                                                                     |
| genshi_text     | 21.0 ms                                                         | 24.7 ms: 1.18x slower                                                                     |
| Geometric mean  | (ref)                                                           | 1.00x slower                                                                              |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241216-pythonperf1_win32-x86-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|--------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------------------:|
| pidigits                 | 502 ms                                                          | 200 ms: 2.51x faster                                                                      |
| typing_runtime_protocols | 396 us                                                          | 167 us: 2.38x faster                                                                      |
| sqlglot_normalize        | 230 ms                                                          | 105 ms: 2.20x faster                                                                      |
| async_tree_io            | 940 ms                                                          | 466 ms: 2.02x faster                                                                      |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 472 ms: 1.95x faster                                                                      |
| async_tree_none          | 394 ms                                                          | 216 ms: 1.82x faster                                                                      |
| async_tree_memoization   | 467 ms                                                          | 273 ms: 1.71x faster                                                                      |
| pylint                   | 384 ms                                                          | 229 ms: 1.68x faster                                                                      |
| deltablue                | 4.04 ms                                                         | 2.69 ms: 1.50x faster                                                                     |
| deepcopy_memo            | 29.6 us                                                         | 21.0 us: 1.41x faster                                                                     |
| go                       | 146 ms                                                          | 104 ms: 1.40x faster                                                                      |
| deepcopy                 | 310 us                                                          | 230 us: 1.35x faster                                                                      |
| logging_silent           | 97.9 ns                                                         | 75.6 ns: 1.30x faster                                                                     |
| scimark_lu               | 89.8 ms                                                         | 70.1 ms: 1.28x faster                                                                     |
| raytrace                 | 303 ms                                                          | 242 ms: 1.25x faster                                                                      |
| dulwich_log              | 58.5 ms                                                         | 47.0 ms: 1.24x faster                                                                     |
| float                    | 69.6 ms                                                         | 56.9 ms: 1.22x faster                                                                     |
| mako                     | 9.10 ms                                                         | 7.49 ms: 1.22x faster                                                                     |
| pyflate                  | 422 ms                                                          | 350 ms: 1.21x faster                                                                      |
| generators               | 31.6 ms                                                         | 26.3 ms: 1.20x faster                                                                     |
| chaos                    | 74.4 ms                                                         | 62.6 ms: 1.19x faster                                                                     |
| sqlite_synth             | 2.29 us                                                         | 1.93 us: 1.19x faster                                                                     |
| crypto_pyaes             | 81.3 ms                                                         | 68.9 ms: 1.18x faster                                                                     |
| scimark_sor              | 115 ms                                                          | 97.8 ms: 1.18x faster                                                                     |
| thrift                   | 902 us                                                          | 776 us: 1.16x faster                                                                      |
| regex_dna                | 131 ms                                                          | 114 ms: 1.15x faster                                                                      |
| hexiom                   | 6.13 ms                                                         | 5.36 ms: 1.15x faster                                                                     |
| richards_super           | 49.9 ms                                                         | 43.6 ms: 1.14x faster                                                                     |
| pycparser                | 1.04 sec                                                        | 912 ms: 1.14x faster                                                                      |
| html5lib                 | 52.1 ms                                                         | 45.8 ms: 1.14x faster                                                                     |
| sqlglot_parse            | 1.33 ms                                                         | 1.17 ms: 1.13x faster                                                                     |
| xml_etree_parse          | 120 ms                                                          | 107 ms: 1.12x faster                                                                      |
| json                     | 4.76 ms                                                         | 4.26 ms: 1.12x faster                                                                     |
| spectral_norm            | 80.2 ms                                                         | 71.9 ms: 1.12x faster                                                                     |
| sympy_sum                | 122 ms                                                          | 110 ms: 1.11x faster                                                                      |
| deepcopy_reduce          | 2.68 us                                                         | 2.44 us: 1.10x faster                                                                     |
| bench_thread_pool        | 1.12 ms                                                         | 1.02 ms: 1.10x faster                                                                     |
| sqlglot_transpile        | 1.58 ms                                                         | 1.45 ms: 1.09x faster                                                                     |
| json_dumps               | 9.82 ms                                                         | 9.00 ms: 1.09x faster                                                                     |
| json_loads               | 22.4 us                                                         | 20.7 us: 1.08x faster                                                                     |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.02 ms: 1.07x faster                                                                     |
| tomli_loads              | 1.91 sec                                                        | 1.79 sec: 1.07x faster                                                                    |
| xml_etree_iterparse      | 70.8 ms                                                         | 66.4 ms: 1.07x faster                                                                     |
| comprehensions           | 17.7 us                                                         | 16.7 us: 1.06x faster                                                                     |
| django_template          | 36.0 ms                                                         | 33.9 ms: 1.06x faster                                                                     |
| regex_compile            | 117 ms                                                          | 110 ms: 1.06x faster                                                                      |
| regex_effbot             | 1.66 ms                                                         | 1.58 ms: 1.05x faster                                                                     |
| mdp                      | 1.83 sec                                                        | 1.75 sec: 1.04x faster                                                                    |
| coroutines               | 17.9 ms                                                         | 17.3 ms: 1.04x faster                                                                     |
| sympy_str                | 229 ms                                                          | 223 ms: 1.03x faster                                                                      |
| 2to3                     | 265 ms                                                          | 259 ms: 1.02x faster                                                                      |
| docutils                 | 1.95 sec                                                        | 1.91 sec: 1.02x faster                                                                    |
| scimark_monte_carlo      | 61.9 ms                                                         | 60.8 ms: 1.02x faster                                                                     |
| richards                 | 40.3 ms                                                         | 39.6 ms: 1.02x faster                                                                     |
| regex_v8                 | 15.8 ms                                                         | 15.5 ms: 1.01x faster                                                                     |
| sympy_expand             | 391 ms                                                          | 388 ms: 1.01x faster                                                                      |
| nqueens                  | 87.1 ms                                                         | 86.5 ms: 1.01x faster                                                                     |
| sympy_integrate          | 16.6 ms                                                         | 16.5 ms: 1.01x faster                                                                     |
| pathlib                  | 81.2 ms                                                         | 84.2 ms: 1.04x slower                                                                     |
| pickle_pure_python       | 280 us                                                          | 303 us: 1.08x slower                                                                      |
| python_startup_no_site   | 18.1 ms                                                         | 19.6 ms: 1.08x slower                                                                     |
| unpickle_pure_python     | 189 us                                                          | 206 us: 1.09x slower                                                                      |
| fannkuch                 | 317 ms                                                          | 346 ms: 1.09x slower                                                                      |
| meteor_contest           | 80.0 ms                                                         | 87.5 ms: 1.09x slower                                                                     |
| genshi_xml               | 46.6 ms                                                         | 51.5 ms: 1.11x slower                                                                     |
| coverage                 | 46.6 ms                                                         | 51.6 ms: 1.11x slower                                                                     |
| pprint_pformat           | 1.37 sec                                                        | 1.52 sec: 1.11x slower                                                                    |
| xml_etree_process        | 48.1 ms                                                         | 53.5 ms: 1.11x slower                                                                     |
| logging_format           | 7.91 us                                                         | 8.83 us: 1.12x slower                                                                     |
| pprint_safe_repr         | 658 ms                                                          | 736 ms: 1.12x slower                                                                      |
| logging_simple           | 7.29 us                                                         | 8.22 us: 1.13x slower                                                                     |
| scimark_fft              | 216 ms                                                          | 245 ms: 1.13x slower                                                                      |
| python_startup           | 22.9 ms                                                         | 26.1 ms: 1.14x slower                                                                     |
| sqlglot_optimize         | 44.7 ms                                                         | 51.2 ms: 1.14x slower                                                                     |
| xml_etree_generate       | 61.6 ms                                                         | 71.9 ms: 1.17x slower                                                                     |
| genshi_text              | 21.0 ms                                                         | 24.7 ms: 1.18x slower                                                                     |
| mypy2                    | 590 ms                                                          | 716 ms: 1.21x slower                                                                      |
| async_generators         | 241 ms                                                          | 294 ms: 1.22x slower                                                                      |
| nbody                    | 79.1 ms                                                         | 98.2 ms: 1.24x slower                                                                     |
| bench_mp_pool            | 66.4 ms                                                         | 87.1 ms: 1.31x slower                                                                     |
| gc_traversal             | 1.28 ms                                                         | 1.80 ms: 1.41x slower                                                                     |
| telco                    | 4.83 ms                                                         | 7.12 ms: 1.47x slower                                                                     |
| create_gc_cycles         | 694 us                                                          | 1.05 ms: 1.51x slower                                                                     |
| Geometric mean           | (ref)                                                           | 1.10x faster                                                                              |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20241216-3.14.0a2+-fcc6f57-JIT/bm-20241216-pythonperf1_win32-x86-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.104x faster

# HPT report

- Reliability score: 99.91% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: unknown