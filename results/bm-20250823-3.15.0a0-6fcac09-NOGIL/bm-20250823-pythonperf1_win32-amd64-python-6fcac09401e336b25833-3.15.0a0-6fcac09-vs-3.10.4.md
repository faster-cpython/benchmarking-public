# Results vs. 3.10.4

- fork: python
- ref: 6fcac09401e336b25833
- machine: windows-amd64
- commit hash: 6fcac09
- commit date: 2025-08-23
- overall geometric mean: 1.304x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 222 ms: 1.19x faster                                                             |
| docutils       | 1.95 sec                                                        | 2.77 sec: 1.42x slower                                                           |
| html5lib       | 52.1 ms                                                         | 41.1 ms: 1.27x faster                                                            |
| Geometric mean | (ref)                                                           | 1.02x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|-------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 328 ms: 2.81x faster                                                             |
| async_tree_io           | 940 ms                                                          | 349 ms: 2.70x faster                                                             |
| async_tree_none         | 394 ms                                                          | 170 ms: 2.32x faster                                                             |
| async_tree_memoization  | 467 ms                                                          | 209 ms: 2.23x faster                                                             |
| Geometric mean          | (ref)                                                           | 2.50x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 135 ms: 3.73x faster                                                             |
| float          | 69.6 ms                                                         | 45.5 ms: 1.53x faster                                                            |
| nbody          | 79.1 ms                                                         | 81.3 ms: 1.03x slower                                                            |
| Geometric mean | (ref)                                                           | 1.77x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 93.8 ms: 1.24x faster                                                            |
| regex_v8       | 15.8 ms                                                         | 12.8 ms: 1.23x faster                                                            |
| regex_dna      | 131 ms                                                          | 111 ms: 1.17x faster                                                             |
| regex_effbot   | 1.66 ms                                                         | 1.49 ms: 1.11x faster                                                            |
| Geometric mean | (ref)                                                           | 1.19x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 5.90 ms: 1.66x faster                                                            |
| json_loads           | 22.4 us                                                         | 15.7 us: 1.42x faster                                                            |
| xml_etree_parse      | 120 ms                                                          | 90.5 ms: 1.33x faster                                                            |
| unpickle_pure_python | 189 us                                                          | 156 us: 1.22x faster                                                             |
| xml_etree_iterparse  | 70.8 ms                                                         | 58.3 ms: 1.22x faster                                                            |
| pickle_pure_python   | 280 us                                                          | 233 us: 1.20x faster                                                             |
| pickle_list          | 3.22 us                                                         | 2.95 us: 1.09x faster                                                            |
| xml_etree_process    | 48.1 ms                                                         | 44.5 ms: 1.08x faster                                                            |
| pickle               | 7.83 us                                                         | 7.75 us: 1.01x faster                                                            |
| unpickle_list        | 2.98 us                                                         | 3.00 us: 1.01x slower                                                            |
| unpickle             | 9.82 us                                                         | 9.98 us: 1.02x slower                                                            |
| pickle_dict          | 18.2 us                                                         | 19.9 us: 1.09x slower                                                            |
| tomli_loads          | 1.91 sec                                                        | 2.60 sec: 1.36x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.11x faster                                                                     |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 19.0 ms: 1.05x slower                                                            |
| python_startup         | 22.9 ms                                                         | 25.5 ms: 1.11x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.08x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 36.0 ms                                                         | 27.1 ms: 1.33x faster                                                            |
| genshi_xml      | 46.6 ms                                                         | 38.7 ms: 1.20x faster                                                            |
| genshi_text     | 21.0 ms                                                         | 18.9 ms: 1.11x faster                                                            |
| mako            | 9.10 ms                                                         | 10.1 ms: 1.11x slower                                                            |
| Geometric mean  | (ref)                                                           | 1.13x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|--------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl          | 17.0 sec                                                        | 2.00 sec: 8.48x faster                                                           |
| pidigits                 | 502 ms                                                          | 135 ms: 3.73x faster                                                             |
| typing_runtime_protocols | 396 us                                                          | 128 us: 3.09x faster                                                             |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 328 ms: 2.81x faster                                                             |
| async_tree_io            | 940 ms                                                          | 349 ms: 2.70x faster                                                             |
| pathlib                  | 81.2 ms                                                         | 30.2 ms: 2.69x faster                                                            |
| async_tree_none          | 394 ms                                                          | 170 ms: 2.32x faster                                                             |
| async_tree_memoization   | 467 ms                                                          | 209 ms: 2.23x faster                                                             |
| pylint                   | 384 ms                                                          | 201 ms: 1.91x faster                                                             |
| asyncio_tcp              | 744 ms                                                          | 423 ms: 1.76x faster                                                             |
| sqlite_synth             | 2.29 us                                                         | 1.33 us: 1.73x faster                                                            |
| mdp                      | 1.83 sec                                                        | 1.07 sec: 1.70x faster                                                           |
| json_dumps               | 9.82 ms                                                         | 5.90 ms: 1.66x faster                                                            |
| deltablue                | 4.04 ms                                                         | 2.43 ms: 1.66x faster                                                            |
| chaos                    | 74.4 ms                                                         | 46.3 ms: 1.61x faster                                                            |
| go                       | 146 ms                                                          | 92.1 ms: 1.58x faster                                                            |
| logging_silent           | 97.9 ns                                                         | 61.9 ns: 1.58x faster                                                            |
| thrift                   | 902 us                                                          | 572 us: 1.58x faster                                                             |
| json                     | 4.76 ms                                                         | 3.07 ms: 1.55x faster                                                            |
| deepcopy                 | 310 us                                                          | 200 us: 1.55x faster                                                             |
| float                    | 69.6 ms                                                         | 45.5 ms: 1.53x faster                                                            |
| comprehensions           | 17.7 us                                                         | 11.9 us: 1.49x faster                                                            |
| crypto_pyaes             | 81.3 ms                                                         | 56.2 ms: 1.45x faster                                                            |
| pycparser                | 1.04 sec                                                        | 721 ms: 1.45x faster                                                             |
| dulwich_log              | 58.5 ms                                                         | 40.8 ms: 1.44x faster                                                            |
| raytrace                 | 303 ms                                                          | 211 ms: 1.43x faster                                                             |
| deepcopy_memo            | 29.6 us                                                         | 20.7 us: 1.43x faster                                                            |
| json_loads               | 22.4 us                                                         | 15.7 us: 1.42x faster                                                            |
| scimark_lu               | 89.8 ms                                                         | 65.2 ms: 1.38x faster                                                            |
| pyflate                  | 422 ms                                                          | 314 ms: 1.34x faster                                                             |
| hexiom                   | 6.13 ms                                                         | 4.59 ms: 1.34x faster                                                            |
| django_template          | 36.0 ms                                                         | 27.1 ms: 1.33x faster                                                            |
| xml_etree_parse          | 120 ms                                                          | 90.5 ms: 1.33x faster                                                            |
| scimark_sor              | 115 ms                                                          | 88.0 ms: 1.31x faster                                                            |
| sympy_sum                | 122 ms                                                          | 96.2 ms: 1.27x faster                                                            |
| generators               | 31.6 ms                                                         | 24.9 ms: 1.27x faster                                                            |
| html5lib                 | 52.1 ms                                                         | 41.1 ms: 1.27x faster                                                            |
| deepcopy_reduce          | 2.68 us                                                         | 2.12 us: 1.26x faster                                                            |
| regex_compile            | 117 ms                                                          | 93.8 ms: 1.24x faster                                                            |
| regex_v8                 | 15.8 ms                                                         | 12.8 ms: 1.23x faster                                                            |
| sympy_expand             | 391 ms                                                          | 318 ms: 1.23x faster                                                             |
| sympy_str                | 229 ms                                                          | 187 ms: 1.22x faster                                                             |
| unpickle_pure_python     | 189 us                                                          | 156 us: 1.22x faster                                                             |
| xml_etree_iterparse      | 70.8 ms                                                         | 58.3 ms: 1.22x faster                                                            |
| richards_super           | 49.9 ms                                                         | 41.1 ms: 1.21x faster                                                            |
| coroutines               | 17.9 ms                                                         | 14.8 ms: 1.21x faster                                                            |
| genshi_xml               | 46.6 ms                                                         | 38.7 ms: 1.20x faster                                                            |
| pickle_pure_python       | 280 us                                                          | 233 us: 1.20x faster                                                             |
| scimark_monte_carlo      | 61.9 ms                                                         | 51.6 ms: 1.20x faster                                                            |
| 2to3                     | 265 ms                                                          | 222 ms: 1.19x faster                                                             |
| sympy_integrate          | 16.6 ms                                                         | 14.0 ms: 1.19x faster                                                            |
| nqueens                  | 87.1 ms                                                         | 73.1 ms: 1.19x faster                                                            |
| pprint_safe_repr         | 658 ms                                                          | 558 ms: 1.18x faster                                                             |
| regex_dna                | 131 ms                                                          | 111 ms: 1.17x faster                                                             |
| richards                 | 40.3 ms                                                         | 35.9 ms: 1.12x faster                                                            |
| regex_effbot             | 1.66 ms                                                         | 1.49 ms: 1.11x faster                                                            |
| genshi_text              | 21.0 ms                                                         | 18.9 ms: 1.11x faster                                                            |
| logging_format           | 7.91 us                                                         | 7.16 us: 1.10x faster                                                            |
| logging_simple           | 7.29 us                                                         | 6.63 us: 1.10x faster                                                            |
| pickle_list              | 3.22 us                                                         | 2.95 us: 1.09x faster                                                            |
| gc_traversal             | 1.28 ms                                                         | 1.17 ms: 1.09x faster                                                            |
| spectral_norm            | 80.2 ms                                                         | 73.5 ms: 1.09x faster                                                            |
| xml_etree_process        | 48.1 ms                                                         | 44.5 ms: 1.08x faster                                                            |
| unpack_sequence          | 40.0 ns                                                         | 37.7 ns: 1.06x faster                                                            |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.09 ms: 1.05x faster                                                            |
| fannkuch                 | 317 ms                                                          | 304 ms: 1.04x faster                                                             |
| scimark_fft              | 216 ms                                                          | 210 ms: 1.03x faster                                                             |
| pickle                   | 7.83 us                                                         | 7.75 us: 1.01x faster                                                            |
| unpickle_list            | 2.98 us                                                         | 3.00 us: 1.01x slower                                                            |
| unpickle                 | 9.82 us                                                         | 9.98 us: 1.02x slower                                                            |
| nbody                    | 79.1 ms                                                         | 81.3 ms: 1.03x slower                                                            |
| async_generators         | 241 ms                                                          | 254 ms: 1.05x slower                                                             |
| python_startup_no_site   | 18.1 ms                                                         | 19.0 ms: 1.05x slower                                                            |
| meteor_contest           | 80.0 ms                                                         | 85.7 ms: 1.07x slower                                                            |
| pickle_dict              | 18.2 us                                                         | 19.9 us: 1.09x slower                                                            |
| mako                     | 9.10 ms                                                         | 10.1 ms: 1.11x slower                                                            |
| python_startup           | 22.9 ms                                                         | 25.5 ms: 1.11x slower                                                            |
| bench_mp_pool            | 66.4 ms                                                         | 77.8 ms: 1.17x slower                                                            |
| pprint_pformat           | 1.37 sec                                                        | 1.61 sec: 1.18x slower                                                           |
| tomli_loads              | 1.91 sec                                                        | 2.60 sec: 1.36x slower                                                           |
| docutils                 | 1.95 sec                                                        | 2.77 sec: 1.42x slower                                                           |
| create_gc_cycles         | 694 us                                                          | 994 us: 1.43x slower                                                             |
| coverage                 | 46.6 ms                                                         | 66.8 ms: 1.44x slower                                                            |
| Geometric mean           | (ref)                                                           | 1.30x faster                                                                     |

Benchmark hidden because not significant (3): bench_thread_pool, xml_etree_generate, telco
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250823-3.15.0a0-6fcac09-NOGIL/bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.304x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: unknown