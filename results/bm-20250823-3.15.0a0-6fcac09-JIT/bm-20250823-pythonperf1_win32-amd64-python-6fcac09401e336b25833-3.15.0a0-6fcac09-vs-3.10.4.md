# Results vs. 3.10.4

- fork: python
- ref: 6fcac09401e336b25833
- machine: windows-amd64
- commit hash: 6fcac09
- commit date: 2025-08-23
- overall geometric mean: 1.505x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.41x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 214 ms: 1.24x faster                                                             |
| docutils       | 1.95 sec                                                        | 1.61 sec: 1.21x faster                                                           |
| html5lib       | 52.1 ms                                                         | 37.8 ms: 1.38x faster                                                            |
| Geometric mean | (ref)                                                           | 1.27x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|-------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 329 ms: 2.80x faster                                                             |
| async_tree_io           | 940 ms                                                          | 389 ms: 2.42x faster                                                             |
| async_tree_memoization  | 467 ms                                                          | 201 ms: 2.32x faster                                                             |
| async_tree_none         | 394 ms                                                          | 170 ms: 2.31x faster                                                             |
| Geometric mean          | (ref)                                                           | 2.46x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 145 ms: 3.47x faster                                                             |
| float          | 69.6 ms                                                         | 43.6 ms: 1.60x faster                                                            |
| nbody          | 79.1 ms                                                         | 53.0 ms: 1.49x faster                                                            |
| Geometric mean | (ref)                                                           | 2.02x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 78.1 ms: 1.49x faster                                                            |
| regex_v8       | 15.8 ms                                                         | 13.1 ms: 1.20x faster                                                            |
| regex_dna      | 131 ms                                                          | 116 ms: 1.13x faster                                                             |
| regex_effbot   | 1.66 ms                                                         | 1.57 ms: 1.06x faster                                                            |
| Geometric mean | (ref)                                                           | 1.21x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| unpickle_pure_python | 189 us                                                          | 104 us: 1.83x faster                                                             |
| json_dumps           | 9.82 ms                                                         | 5.38 ms: 1.82x faster                                                            |
| tomli_loads          | 1.91 sec                                                        | 1.09 sec: 1.75x faster                                                           |
| json_loads           | 22.4 us                                                         | 13.9 us: 1.61x faster                                                            |
| xml_etree_parse      | 120 ms                                                          | 85.5 ms: 1.40x faster                                                            |
| pickle_pure_python   | 280 us                                                          | 201 us: 1.39x faster                                                             |
| xml_etree_process    | 48.1 ms                                                         | 35.4 ms: 1.36x faster                                                            |
| xml_etree_generate   | 61.6 ms                                                         | 51.1 ms: 1.21x faster                                                            |
| xml_etree_iterparse  | 70.8 ms                                                         | 61.6 ms: 1.15x faster                                                            |
| unpickle             | 9.82 us                                                         | 8.61 us: 1.14x faster                                                            |
| unpickle_list        | 2.98 us                                                         | 2.69 us: 1.11x faster                                                            |
| pickle               | 7.83 us                                                         | 7.72 us: 1.01x faster                                                            |
| pickle_list          | 3.22 us                                                         | 3.33 us: 1.03x slower                                                            |
| pickle_dict          | 18.2 us                                                         | 19.5 us: 1.07x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.30x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 18.9 ms: 1.05x slower                                                            |
| python_startup         | 22.9 ms                                                         | 25.2 ms: 1.10x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.07x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 5.20 ms: 1.75x faster                                                            |
| django_template | 36.0 ms                                                         | 24.1 ms: 1.49x faster                                                            |
| genshi_xml      | 46.6 ms                                                         | 34.5 ms: 1.35x faster                                                            |
| genshi_text     | 21.0 ms                                                         | 15.6 ms: 1.35x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.48x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|--------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl          | 17.0 sec                                                        | 1.24 sec: 13.67x faster                                                          |
| typing_runtime_protocols | 396 us                                                          | 101 us: 3.91x faster                                                             |
| pidigits                 | 502 ms                                                          | 145 ms: 3.47x faster                                                             |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 329 ms: 2.80x faster                                                             |
| pathlib                  | 81.2 ms                                                         | 30.1 ms: 2.69x faster                                                            |
| async_tree_io            | 940 ms                                                          | 389 ms: 2.42x faster                                                             |
| async_tree_memoization   | 467 ms                                                          | 201 ms: 2.32x faster                                                             |
| mdp                      | 1.83 sec                                                        | 788 ms: 2.32x faster                                                             |
| async_tree_none          | 394 ms                                                          | 170 ms: 2.31x faster                                                             |
| asyncio_tcp              | 744 ms                                                          | 368 ms: 2.02x faster                                                             |
| pylint                   | 384 ms                                                          | 192 ms: 1.99x faster                                                             |
| go                       | 146 ms                                                          | 76.8 ms: 1.90x faster                                                            |
| deepcopy                 | 310 us                                                          | 170 us: 1.83x faster                                                             |
| unpickle_pure_python     | 189 us                                                          | 104 us: 1.83x faster                                                             |
| json_dumps               | 9.82 ms                                                         | 5.38 ms: 1.82x faster                                                            |
| crypto_pyaes             | 81.3 ms                                                         | 44.6 ms: 1.82x faster                                                            |
| deltablue                | 4.04 ms                                                         | 2.22 ms: 1.82x faster                                                            |
| chaos                    | 74.4 ms                                                         | 41.1 ms: 1.81x faster                                                            |
| logging_silent           | 97.9 ns                                                         | 54.4 ns: 1.80x faster                                                            |
| thrift                   | 902 us                                                          | 506 us: 1.78x faster                                                             |
| raytrace                 | 303 ms                                                          | 172 ms: 1.76x faster                                                             |
| tomli_loads              | 1.91 sec                                                        | 1.09 sec: 1.75x faster                                                           |
| mako                     | 9.10 ms                                                         | 5.20 ms: 1.75x faster                                                            |
| comprehensions           | 17.7 us                                                         | 10.3 us: 1.73x faster                                                            |
| richards_super           | 49.9 ms                                                         | 30.1 ms: 1.66x faster                                                            |
| generators               | 31.6 ms                                                         | 19.2 ms: 1.64x faster                                                            |
| pprint_pformat           | 1.37 sec                                                        | 851 ms: 1.61x faster                                                             |
| json_loads               | 22.4 us                                                         | 13.9 us: 1.61x faster                                                            |
| json                     | 4.76 ms                                                         | 2.98 ms: 1.60x faster                                                            |
| float                    | 69.6 ms                                                         | 43.6 ms: 1.60x faster                                                            |
| pprint_safe_repr         | 658 ms                                                          | 417 ms: 1.58x faster                                                             |
| pyflate                  | 422 ms                                                          | 268 ms: 1.57x faster                                                             |
| hexiom                   | 6.13 ms                                                         | 3.95 ms: 1.55x faster                                                            |
| scimark_monte_carlo      | 61.9 ms                                                         | 40.3 ms: 1.54x faster                                                            |
| pycparser                | 1.04 sec                                                        | 678 ms: 1.54x faster                                                             |
| sqlite_synth             | 2.29 us                                                         | 1.52 us: 1.51x faster                                                            |
| richards                 | 40.3 ms                                                         | 26.7 ms: 1.51x faster                                                            |
| scimark_lu               | 89.8 ms                                                         | 59.7 ms: 1.50x faster                                                            |
| dulwich_log              | 58.5 ms                                                         | 39.1 ms: 1.50x faster                                                            |
| fannkuch                 | 317 ms                                                          | 212 ms: 1.49x faster                                                             |
| regex_compile            | 117 ms                                                          | 78.1 ms: 1.49x faster                                                            |
| deepcopy_memo            | 29.6 us                                                         | 19.8 us: 1.49x faster                                                            |
| django_template          | 36.0 ms                                                         | 24.1 ms: 1.49x faster                                                            |
| scimark_sor              | 115 ms                                                          | 77.1 ms: 1.49x faster                                                            |
| nbody                    | 79.1 ms                                                         | 53.0 ms: 1.49x faster                                                            |
| nqueens                  | 87.1 ms                                                         | 59.7 ms: 1.46x faster                                                            |
| deepcopy_reduce          | 2.68 us                                                         | 1.85 us: 1.45x faster                                                            |
| scimark_fft              | 216 ms                                                          | 149 ms: 1.45x faster                                                             |
| sympy_sum                | 122 ms                                                          | 85.5 ms: 1.43x faster                                                            |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.27 ms: 1.43x faster                                                            |
| xml_etree_parse          | 120 ms                                                          | 85.5 ms: 1.40x faster                                                            |
| pickle_pure_python       | 280 us                                                          | 201 us: 1.39x faster                                                             |
| html5lib                 | 52.1 ms                                                         | 37.8 ms: 1.38x faster                                                            |
| sympy_str                | 229 ms                                                          | 167 ms: 1.37x faster                                                             |
| xml_etree_process        | 48.1 ms                                                         | 35.4 ms: 1.36x faster                                                            |
| sympy_expand             | 391 ms                                                          | 288 ms: 1.36x faster                                                             |
| sympy_integrate          | 16.6 ms                                                         | 12.3 ms: 1.35x faster                                                            |
| genshi_xml               | 46.6 ms                                                         | 34.5 ms: 1.35x faster                                                            |
| genshi_text              | 21.0 ms                                                         | 15.6 ms: 1.35x faster                                                            |
| bench_thread_pool        | 1.12 ms                                                         | 835 us: 1.34x faster                                                             |
| spectral_norm            | 80.2 ms                                                         | 61.5 ms: 1.30x faster                                                            |
| coroutines               | 17.9 ms                                                         | 14.0 ms: 1.28x faster                                                            |
| telco                    | 4.83 ms                                                         | 3.82 ms: 1.27x faster                                                            |
| 2to3                     | 265 ms                                                          | 214 ms: 1.24x faster                                                             |
| logging_format           | 7.91 us                                                         | 6.44 us: 1.23x faster                                                            |
| docutils                 | 1.95 sec                                                        | 1.61 sec: 1.21x faster                                                           |
| xml_etree_generate       | 61.6 ms                                                         | 51.1 ms: 1.21x faster                                                            |
| logging_simple           | 7.29 us                                                         | 6.05 us: 1.20x faster                                                            |
| regex_v8                 | 15.8 ms                                                         | 13.1 ms: 1.20x faster                                                            |
| unpack_sequence          | 40.0 ns                                                         | 34.4 ns: 1.16x faster                                                            |
| xml_etree_iterparse      | 70.8 ms                                                         | 61.6 ms: 1.15x faster                                                            |
| unpickle                 | 9.82 us                                                         | 8.61 us: 1.14x faster                                                            |
| meteor_contest           | 80.0 ms                                                         | 70.4 ms: 1.14x faster                                                            |
| regex_dna                | 131 ms                                                          | 116 ms: 1.13x faster                                                             |
| unpickle_list            | 2.98 us                                                         | 2.69 us: 1.11x faster                                                            |
| regex_effbot             | 1.66 ms                                                         | 1.57 ms: 1.06x faster                                                            |
| pickle                   | 7.83 us                                                         | 7.72 us: 1.01x faster                                                            |
| async_generators         | 241 ms                                                          | 245 ms: 1.02x slower                                                             |
| pickle_list              | 3.22 us                                                         | 3.33 us: 1.03x slower                                                            |
| python_startup_no_site   | 18.1 ms                                                         | 18.9 ms: 1.05x slower                                                            |
| pickle_dict              | 18.2 us                                                         | 19.5 us: 1.07x slower                                                            |
| coverage                 | 46.6 ms                                                         | 50.1 ms: 1.08x slower                                                            |
| python_startup           | 22.9 ms                                                         | 25.2 ms: 1.10x slower                                                            |
| bench_mp_pool            | 66.4 ms                                                         | 92.0 ms: 1.39x slower                                                            |
| gc_traversal             | 1.28 ms                                                         | 2.12 ms: 1.66x slower                                                            |
| create_gc_cycles         | 694 us                                                          | 1.26 ms: 1.81x slower                                                            |
| Geometric mean           | (ref)                                                           | 1.50x faster                                                                     |
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250823-3.15.0a0-6fcac09-JIT/bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.505x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.46x
- 95% likely to have a speedup of 1.44x
- 99% likely to have a speedup of 1.41x

# Memory
- memory change: unknown