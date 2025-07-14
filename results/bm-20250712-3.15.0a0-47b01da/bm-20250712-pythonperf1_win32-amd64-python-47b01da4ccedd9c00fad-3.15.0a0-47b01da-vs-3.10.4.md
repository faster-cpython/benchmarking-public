# Results vs. 3.10.4

- fork: python
- ref: 47b01da4ccedd9c00fad
- machine: windows-amd64
- commit hash: 47b01da
- commit date: 2025-07-12
- overall geometric mean: 1.455x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.35x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 221 ms: 1.20x faster                                                             |
| docutils       | 1.95 sec                                                        | 1.61 sec: 1.21x faster                                                           |
| html5lib       | 52.1 ms                                                         | 38.1 ms: 1.37x faster                                                            |
| Geometric mean | (ref)                                                           | 1.26x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|-------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 332 ms: 2.78x faster                                                             |
| async_tree_io           | 940 ms                                                          | 391 ms: 2.41x faster                                                             |
| async_tree_none         | 394 ms                                                          | 170 ms: 2.32x faster                                                             |
| async_tree_memoization  | 467 ms                                                          | 204 ms: 2.29x faster                                                             |
| Geometric mean          | (ref)                                                           | 2.44x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 145 ms: 3.47x faster                                                             |
| float          | 69.6 ms                                                         | 43.5 ms: 1.60x faster                                                            |
| nbody          | 79.1 ms                                                         | 65.6 ms: 1.21x faster                                                            |
| Geometric mean | (ref)                                                           | 1.88x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 79.0 ms: 1.48x faster                                                            |
| regex_v8       | 15.8 ms                                                         | 13.2 ms: 1.20x faster                                                            |
| regex_dna      | 131 ms                                                          | 116 ms: 1.13x faster                                                             |
| regex_effbot   | 1.66 ms                                                         | 1.49 ms: 1.12x faster                                                            |
| Geometric mean | (ref)                                                           | 1.22x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 6.13 ms: 1.60x faster                                                            |
| json_loads           | 22.4 us                                                         | 14.2 us: 1.58x faster                                                            |
| unpickle_pure_python | 189 us                                                          | 132 us: 1.43x faster                                                             |
| tomli_loads          | 1.91 sec                                                        | 1.35 sec: 1.41x faster                                                           |
| xml_etree_parse      | 120 ms                                                          | 86.6 ms: 1.39x faster                                                            |
| pickle_pure_python   | 280 us                                                          | 208 us: 1.35x faster                                                             |
| xml_etree_process    | 48.1 ms                                                         | 38.8 ms: 1.24x faster                                                            |
| unpickle             | 9.82 us                                                         | 8.48 us: 1.16x faster                                                            |
| xml_etree_generate   | 61.6 ms                                                         | 55.2 ms: 1.12x faster                                                            |
| xml_etree_iterparse  | 70.8 ms                                                         | 63.6 ms: 1.11x faster                                                            |
| unpickle_list        | 2.98 us                                                         | 2.77 us: 1.08x faster                                                            |
| pickle               | 7.83 us                                                         | 7.99 us: 1.02x slower                                                            |
| pickle_list          | 3.22 us                                                         | 3.29 us: 1.02x slower                                                            |
| pickle_dict          | 18.2 us                                                         | 19.8 us: 1.08x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.22x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 19.4 ms: 1.07x slower                                                            |
| python_startup         | 22.9 ms                                                         | 26.1 ms: 1.14x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.11x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 36.0 ms                                                         | 25.1 ms: 1.44x faster                                                            |
| mako            | 9.10 ms                                                         | 6.52 ms: 1.40x faster                                                            |
| genshi_xml      | 46.6 ms                                                         | 34.4 ms: 1.36x faster                                                            |
| genshi_text     | 21.0 ms                                                         | 15.6 ms: 1.34x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.38x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|--------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl          | 17.0 sec                                                        | 1.30 sec: 13.10x faster                                                          |
| typing_runtime_protocols | 396 us                                                          | 102 us: 3.87x faster                                                             |
| pidigits                 | 502 ms                                                          | 145 ms: 3.47x faster                                                             |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 332 ms: 2.78x faster                                                             |
| pathlib                  | 81.2 ms                                                         | 30.0 ms: 2.71x faster                                                            |
| async_tree_io            | 940 ms                                                          | 391 ms: 2.41x faster                                                             |
| async_tree_none          | 394 ms                                                          | 170 ms: 2.32x faster                                                             |
| async_tree_memoization   | 467 ms                                                          | 204 ms: 2.29x faster                                                             |
| mdp                      | 1.83 sec                                                        | 807 ms: 2.26x faster                                                             |
| pylint                   | 384 ms                                                          | 196 ms: 1.96x faster                                                             |
| go                       | 146 ms                                                          | 74.8 ms: 1.95x faster                                                            |
| deltablue                | 4.04 ms                                                         | 2.16 ms: 1.87x faster                                                            |
| asyncio_tcp              | 744 ms                                                          | 399 ms: 1.87x faster                                                             |
| deepcopy                 | 310 us                                                          | 167 us: 1.86x faster                                                             |
| chaos                    | 74.4 ms                                                         | 40.2 ms: 1.85x faster                                                            |
| thrift                   | 902 us                                                          | 495 us: 1.82x faster                                                             |
| logging_silent           | 97.9 ns                                                         | 55.2 ns: 1.77x faster                                                            |
| deepcopy_memo            | 29.6 us                                                         | 17.2 us: 1.72x faster                                                            |
| crypto_pyaes             | 81.3 ms                                                         | 47.6 ms: 1.71x faster                                                            |
| raytrace                 | 303 ms                                                          | 181 ms: 1.67x faster                                                             |
| comprehensions           | 17.7 us                                                         | 10.7 us: 1.66x faster                                                            |
| richards_super           | 49.9 ms                                                         | 30.3 ms: 1.65x faster                                                            |
| generators               | 31.6 ms                                                         | 19.3 ms: 1.64x faster                                                            |
| json                     | 4.76 ms                                                         | 2.97 ms: 1.61x faster                                                            |
| json_dumps               | 9.82 ms                                                         | 6.13 ms: 1.60x faster                                                            |
| float                    | 69.6 ms                                                         | 43.5 ms: 1.60x faster                                                            |
| scimark_monte_carlo      | 61.9 ms                                                         | 39.2 ms: 1.58x faster                                                            |
| json_loads               | 22.4 us                                                         | 14.2 us: 1.58x faster                                                            |
| scimark_sor              | 115 ms                                                          | 73.3 ms: 1.57x faster                                                            |
| scimark_lu               | 89.8 ms                                                         | 57.2 ms: 1.57x faster                                                            |
| hexiom                   | 6.13 ms                                                         | 4.04 ms: 1.52x faster                                                            |
| richards                 | 40.3 ms                                                         | 26.6 ms: 1.51x faster                                                            |
| pycparser                | 1.04 sec                                                        | 698 ms: 1.49x faster                                                             |
| regex_compile            | 117 ms                                                          | 79.0 ms: 1.48x faster                                                            |
| deepcopy_reduce          | 2.68 us                                                         | 1.82 us: 1.47x faster                                                            |
| pyflate                  | 422 ms                                                          | 287 ms: 1.47x faster                                                             |
| sqlite_synth             | 2.29 us                                                         | 1.57 us: 1.46x faster                                                            |
| django_template          | 36.0 ms                                                         | 25.1 ms: 1.44x faster                                                            |
| dulwich_log              | 58.5 ms                                                         | 40.7 ms: 1.44x faster                                                            |
| unpickle_pure_python     | 189 us                                                          | 132 us: 1.43x faster                                                             |
| nqueens                  | 87.1 ms                                                         | 61.4 ms: 1.42x faster                                                            |
| tomli_loads              | 1.91 sec                                                        | 1.35 sec: 1.41x faster                                                           |
| sympy_sum                | 122 ms                                                          | 87.3 ms: 1.40x faster                                                            |
| pprint_pformat           | 1.37 sec                                                        | 977 ms: 1.40x faster                                                             |
| mako                     | 9.10 ms                                                         | 6.52 ms: 1.40x faster                                                            |
| xml_etree_parse          | 120 ms                                                          | 86.6 ms: 1.39x faster                                                            |
| html5lib                 | 52.1 ms                                                         | 38.1 ms: 1.37x faster                                                            |
| pprint_safe_repr         | 658 ms                                                          | 485 ms: 1.36x faster                                                             |
| genshi_xml               | 46.6 ms                                                         | 34.4 ms: 1.36x faster                                                            |
| sympy_expand             | 391 ms                                                          | 289 ms: 1.35x faster                                                             |
| pickle_pure_python       | 280 us                                                          | 208 us: 1.35x faster                                                             |
| sympy_str                | 229 ms                                                          | 170 ms: 1.35x faster                                                             |
| genshi_text              | 21.0 ms                                                         | 15.6 ms: 1.34x faster                                                            |
| sympy_integrate          | 16.6 ms                                                         | 12.4 ms: 1.34x faster                                                            |
| bench_thread_pool        | 1.12 ms                                                         | 847 us: 1.32x faster                                                             |
| spectral_norm            | 80.2 ms                                                         | 61.2 ms: 1.31x faster                                                            |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.52 ms: 1.29x faster                                                            |
| coroutines               | 17.9 ms                                                         | 14.4 ms: 1.24x faster                                                            |
| xml_etree_process        | 48.1 ms                                                         | 38.8 ms: 1.24x faster                                                            |
| fannkuch                 | 317 ms                                                          | 257 ms: 1.24x faster                                                             |
| scimark_fft              | 216 ms                                                          | 176 ms: 1.23x faster                                                             |
| docutils                 | 1.95 sec                                                        | 1.61 sec: 1.21x faster                                                           |
| nbody                    | 79.1 ms                                                         | 65.6 ms: 1.21x faster                                                            |
| 2to3                     | 265 ms                                                          | 221 ms: 1.20x faster                                                             |
| logging_format           | 7.91 us                                                         | 6.60 us: 1.20x faster                                                            |
| regex_v8                 | 15.8 ms                                                         | 13.2 ms: 1.20x faster                                                            |
| logging_simple           | 7.29 us                                                         | 6.16 us: 1.18x faster                                                            |
| unpickle                 | 9.82 us                                                         | 8.48 us: 1.16x faster                                                            |
| regex_dna                | 131 ms                                                          | 116 ms: 1.13x faster                                                             |
| meteor_contest           | 80.0 ms                                                         | 71.4 ms: 1.12x faster                                                            |
| xml_etree_generate       | 61.6 ms                                                         | 55.2 ms: 1.12x faster                                                            |
| regex_effbot             | 1.66 ms                                                         | 1.49 ms: 1.12x faster                                                            |
| xml_etree_iterparse      | 70.8 ms                                                         | 63.6 ms: 1.11x faster                                                            |
| unpickle_list            | 2.98 us                                                         | 2.77 us: 1.08x faster                                                            |
| telco                    | 4.83 ms                                                         | 4.51 ms: 1.07x faster                                                            |
| unpack_sequence          | 40.0 ns                                                         | 37.5 ns: 1.07x faster                                                            |
| async_generators         | 241 ms                                                          | 229 ms: 1.05x faster                                                             |
| pickle                   | 7.83 us                                                         | 7.99 us: 1.02x slower                                                            |
| pickle_list              | 3.22 us                                                         | 3.29 us: 1.02x slower                                                            |
| coverage                 | 46.6 ms                                                         | 49.6 ms: 1.07x slower                                                            |
| python_startup_no_site   | 18.1 ms                                                         | 19.4 ms: 1.07x slower                                                            |
| pickle_dict              | 18.2 us                                                         | 19.8 us: 1.08x slower                                                            |
| python_startup           | 22.9 ms                                                         | 26.1 ms: 1.14x slower                                                            |
| bench_mp_pool            | 66.4 ms                                                         | 94.2 ms: 1.42x slower                                                            |
| gc_traversal             | 1.28 ms                                                         | 2.17 ms: 1.69x slower                                                            |
| create_gc_cycles         | 694 us                                                          | 1.34 ms: 1.94x slower                                                            |
| Geometric mean           | (ref)                                                           | 1.45x faster                                                                     |
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250712-3.15.0a0-47b01da/bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.455x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.38x
- 95% likely to have a speedup of 1.36x
- 99% likely to have a speedup of 1.35x

# Memory
- memory change: unknown