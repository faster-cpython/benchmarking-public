# Results vs. 3.10.4

- fork: python
- ref: d3d94e0ed715829d9bf9
- machine: windows-amd64
- commit hash: d3d94e0
- commit date: 2025-08-30
- overall geometric mean: 1.503x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.40x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 217 ms: 1.23x faster                                                             |
| docutils       | 1.95 sec                                                        | 1.61 sec: 1.21x faster                                                           |
| html5lib       | 52.1 ms                                                         | 38.0 ms: 1.37x faster                                                            |
| Geometric mean | (ref)                                                           | 1.27x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|-------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 330 ms: 2.80x faster                                                             |
| async_tree_io           | 940 ms                                                          | 386 ms: 2.44x faster                                                             |
| async_tree_none         | 394 ms                                                          | 169 ms: 2.32x faster                                                             |
| async_tree_memoization  | 467 ms                                                          | 206 ms: 2.27x faster                                                             |
| Geometric mean          | (ref)                                                           | 2.45x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 145 ms: 3.46x faster                                                             |
| float          | 69.6 ms                                                         | 44.4 ms: 1.57x faster                                                            |
| nbody          | 79.1 ms                                                         | 55.8 ms: 1.42x faster                                                            |
| Geometric mean | (ref)                                                           | 1.97x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 78.2 ms: 1.49x faster                                                            |
| regex_v8       | 15.8 ms                                                         | 13.8 ms: 1.15x faster                                                            |
| regex_dna      | 131 ms                                                          | 117 ms: 1.11x faster                                                             |
| regex_effbot   | 1.66 ms                                                         | 1.53 ms: 1.09x faster                                                            |
| Geometric mean | (ref)                                                           | 1.20x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 5.36 ms: 1.83x faster                                                            |
| unpickle_pure_python | 189 us                                                          | 107 us: 1.78x faster                                                             |
| tomli_loads          | 1.91 sec                                                        | 1.10 sec: 1.74x faster                                                           |
| json_loads           | 22.4 us                                                         | 14.0 us: 1.60x faster                                                            |
| xml_etree_parse      | 120 ms                                                          | 85.3 ms: 1.41x faster                                                            |
| pickle_pure_python   | 280 us                                                          | 201 us: 1.39x faster                                                             |
| xml_etree_process    | 48.1 ms                                                         | 34.9 ms: 1.38x faster                                                            |
| xml_etree_generate   | 61.6 ms                                                         | 49.1 ms: 1.26x faster                                                            |
| xml_etree_iterparse  | 70.8 ms                                                         | 61.1 ms: 1.16x faster                                                            |
| unpickle             | 9.82 us                                                         | 8.57 us: 1.15x faster                                                            |
| unpickle_list        | 2.98 us                                                         | 2.72 us: 1.10x faster                                                            |
| pickle               | 7.83 us                                                         | 7.42 us: 1.06x faster                                                            |
| pickle_list          | 3.22 us                                                         | 3.27 us: 1.02x slower                                                            |
| pickle_dict          | 18.2 us                                                         | 19.0 us: 1.04x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.31x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 19.2 ms: 1.06x slower                                                            |
| python_startup         | 22.9 ms                                                         | 25.5 ms: 1.11x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.09x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 5.34 ms: 1.71x faster                                                            |
| django_template | 36.0 ms                                                         | 24.0 ms: 1.50x faster                                                            |
| genshi_text     | 21.0 ms                                                         | 15.5 ms: 1.36x faster                                                            |
| genshi_xml      | 46.6 ms                                                         | 34.6 ms: 1.35x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.47x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|--------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl          | 17.0 sec                                                        | 1.35 sec: 12.55x faster                                                          |
| typing_runtime_protocols | 396 us                                                          | 102 us: 3.88x faster                                                             |
| pidigits                 | 502 ms                                                          | 145 ms: 3.46x faster                                                             |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 330 ms: 2.80x faster                                                             |
| pathlib                  | 81.2 ms                                                         | 29.5 ms: 2.76x faster                                                            |
| async_tree_io            | 940 ms                                                          | 386 ms: 2.44x faster                                                             |
| async_tree_none          | 394 ms                                                          | 169 ms: 2.32x faster                                                             |
| mdp                      | 1.83 sec                                                        | 791 ms: 2.31x faster                                                             |
| async_tree_memoization   | 467 ms                                                          | 206 ms: 2.27x faster                                                             |
| pylint                   | 384 ms                                                          | 194 ms: 1.98x faster                                                             |
| go                       | 146 ms                                                          | 77.5 ms: 1.88x faster                                                            |
| chaos                    | 74.4 ms                                                         | 40.0 ms: 1.86x faster                                                            |
| deltablue                | 4.04 ms                                                         | 2.20 ms: 1.84x faster                                                            |
| json_dumps               | 9.82 ms                                                         | 5.36 ms: 1.83x faster                                                            |
| logging_silent           | 97.9 ns                                                         | 53.6 ns: 1.83x faster                                                            |
| crypto_pyaes             | 81.3 ms                                                         | 44.6 ms: 1.82x faster                                                            |
| deepcopy                 | 310 us                                                          | 171 us: 1.81x faster                                                             |
| thrift                   | 902 us                                                          | 500 us: 1.80x faster                                                             |
| unpickle_pure_python     | 189 us                                                          | 107 us: 1.78x faster                                                             |
| tomli_loads              | 1.91 sec                                                        | 1.10 sec: 1.74x faster                                                           |
| raytrace                 | 303 ms                                                          | 174 ms: 1.74x faster                                                             |
| comprehensions           | 17.7 us                                                         | 10.4 us: 1.71x faster                                                            |
| mako                     | 9.10 ms                                                         | 5.34 ms: 1.71x faster                                                            |
| json                     | 4.76 ms                                                         | 2.88 ms: 1.66x faster                                                            |
| pyflate                  | 422 ms                                                          | 257 ms: 1.64x faster                                                             |
| generators               | 31.6 ms                                                         | 19.3 ms: 1.63x faster                                                            |
| richards_super           | 49.9 ms                                                         | 30.7 ms: 1.63x faster                                                            |
| json_loads               | 22.4 us                                                         | 14.0 us: 1.60x faster                                                            |
| asyncio_tcp              | 744 ms                                                          | 467 ms: 1.59x faster                                                             |
| fannkuch                 | 317 ms                                                          | 201 ms: 1.58x faster                                                             |
| pprint_pformat           | 1.37 sec                                                        | 868 ms: 1.58x faster                                                             |
| float                    | 69.6 ms                                                         | 44.4 ms: 1.57x faster                                                            |
| scimark_monte_carlo      | 61.9 ms                                                         | 40.1 ms: 1.54x faster                                                            |
| pprint_safe_repr         | 658 ms                                                          | 429 ms: 1.54x faster                                                             |
| pycparser                | 1.04 sec                                                        | 688 ms: 1.51x faster                                                             |
| dulwich_log              | 58.5 ms                                                         | 38.7 ms: 1.51x faster                                                            |
| scimark_lu               | 89.8 ms                                                         | 59.7 ms: 1.50x faster                                                            |
| django_template          | 36.0 ms                                                         | 24.0 ms: 1.50x faster                                                            |
| richards                 | 40.3 ms                                                         | 27.0 ms: 1.49x faster                                                            |
| regex_compile            | 117 ms                                                          | 78.2 ms: 1.49x faster                                                            |
| deepcopy_memo            | 29.6 us                                                         | 19.9 us: 1.48x faster                                                            |
| sqlite_synth             | 2.29 us                                                         | 1.55 us: 1.48x faster                                                            |
| nqueens                  | 87.1 ms                                                         | 58.9 ms: 1.48x faster                                                            |
| hexiom                   | 6.13 ms                                                         | 4.15 ms: 1.48x faster                                                            |
| scimark_sor              | 115 ms                                                          | 77.8 ms: 1.48x faster                                                            |
| scimark_fft              | 216 ms                                                          | 147 ms: 1.47x faster                                                             |
| deepcopy_reduce          | 2.68 us                                                         | 1.83 us: 1.47x faster                                                            |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.25 ms: 1.44x faster                                                            |
| sympy_sum                | 122 ms                                                          | 85.4 ms: 1.44x faster                                                            |
| nbody                    | 79.1 ms                                                         | 55.8 ms: 1.42x faster                                                            |
| xml_etree_parse          | 120 ms                                                          | 85.3 ms: 1.41x faster                                                            |
| pickle_pure_python       | 280 us                                                          | 201 us: 1.39x faster                                                             |
| xml_etree_process        | 48.1 ms                                                         | 34.9 ms: 1.38x faster                                                            |
| html5lib                 | 52.1 ms                                                         | 38.0 ms: 1.37x faster                                                            |
| sympy_str                | 229 ms                                                          | 168 ms: 1.37x faster                                                             |
| genshi_text              | 21.0 ms                                                         | 15.5 ms: 1.36x faster                                                            |
| sympy_expand             | 391 ms                                                          | 289 ms: 1.35x faster                                                             |
| genshi_xml               | 46.6 ms                                                         | 34.6 ms: 1.35x faster                                                            |
| sympy_integrate          | 16.6 ms                                                         | 12.4 ms: 1.34x faster                                                            |
| bench_thread_pool        | 1.12 ms                                                         | 843 us: 1.33x faster                                                             |
| spectral_norm            | 80.2 ms                                                         | 61.9 ms: 1.30x faster                                                            |
| telco                    | 4.83 ms                                                         | 3.75 ms: 1.29x faster                                                            |
| coroutines               | 17.9 ms                                                         | 14.2 ms: 1.26x faster                                                            |
| xml_etree_generate       | 61.6 ms                                                         | 49.1 ms: 1.26x faster                                                            |
| logging_format           | 7.91 us                                                         | 6.39 us: 1.24x faster                                                            |
| logging_simple           | 7.29 us                                                         | 5.92 us: 1.23x faster                                                            |
| 2to3                     | 265 ms                                                          | 217 ms: 1.23x faster                                                             |
| docutils                 | 1.95 sec                                                        | 1.61 sec: 1.21x faster                                                           |
| xml_etree_iterparse      | 70.8 ms                                                         | 61.1 ms: 1.16x faster                                                            |
| unpickle                 | 9.82 us                                                         | 8.57 us: 1.15x faster                                                            |
| regex_v8                 | 15.8 ms                                                         | 13.8 ms: 1.15x faster                                                            |
| meteor_contest           | 80.0 ms                                                         | 71.2 ms: 1.12x faster                                                            |
| regex_dna                | 131 ms                                                          | 117 ms: 1.11x faster                                                             |
| unpack_sequence          | 40.0 ns                                                         | 36.0 ns: 1.11x faster                                                            |
| unpickle_list            | 2.98 us                                                         | 2.72 us: 1.10x faster                                                            |
| regex_effbot             | 1.66 ms                                                         | 1.53 ms: 1.09x faster                                                            |
| pickle                   | 7.83 us                                                         | 7.42 us: 1.06x faster                                                            |
| pickle_list              | 3.22 us                                                         | 3.27 us: 1.02x slower                                                            |
| pickle_dict              | 18.2 us                                                         | 19.0 us: 1.04x slower                                                            |
| python_startup_no_site   | 18.1 ms                                                         | 19.2 ms: 1.06x slower                                                            |
| coverage                 | 46.6 ms                                                         | 49.4 ms: 1.06x slower                                                            |
| python_startup           | 22.9 ms                                                         | 25.5 ms: 1.11x slower                                                            |
| bench_mp_pool            | 66.4 ms                                                         | 92.6 ms: 1.40x slower                                                            |
| gc_traversal             | 1.28 ms                                                         | 2.11 ms: 1.65x slower                                                            |
| create_gc_cycles         | 694 us                                                          | 1.27 ms: 1.82x slower                                                            |
| Geometric mean           | (ref)                                                           | 1.49x faster                                                                     |

Benchmark hidden because not significant (1): async_generators
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250830-3.15.0a0-d3d94e0-JIT/bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.503x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.45x
- 95% likely to have a speedup of 1.44x
- 99% likely to have a speedup of 1.40x

# Memory
- memory change: unknown