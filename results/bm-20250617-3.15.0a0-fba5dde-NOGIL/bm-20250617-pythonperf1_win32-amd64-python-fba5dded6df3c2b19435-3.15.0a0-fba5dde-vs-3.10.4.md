# Results vs. 3.10.4

- fork: python
- ref: fba5dded6df3c2b19435
- machine: windows-amd64
- commit hash: fba5dde
- commit date: 2025-06-17
- overall geometric mean: 1.231x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf1_win32-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 338 ms: 1.27x slower                                                             |
| docutils       | 1.95 sec                                                        | 4.22 sec: 2.17x slower                                                           |
| html5lib       | 52.1 ms                                                         | 63.4 ms: 1.22x slower                                                            |
| Geometric mean | (ref)                                                           | 1.50x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf1_win32-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 484 ms: 1.91x faster                                                             |
| async_tree_io           | 940 ms                                                          | 580 ms: 1.62x faster                                                             |
| async_tree_none         | 394 ms                                                          | 275 ms: 1.43x faster                                                             |
| async_tree_memoization  | 467 ms                                                          | 336 ms: 1.39x faster                                                             |
| Geometric mean          | (ref)                                                           | 1.57x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf1_win32-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 140 ms: 3.59x faster                                                             |
| float          | 69.6 ms                                                         | 97.7 ms: 1.40x slower                                                            |
| nbody          | 79.1 ms                                                         | 184 ms: 2.32x slower                                                             |
| Geometric mean | (ref)                                                           | 1.03x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf1_win32-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 113 ms: 1.15x faster                                                             |
| regex_v8       | 15.8 ms                                                         | 16.9 ms: 1.07x slower                                                            |
| regex_effbot   | 1.66 ms                                                         | 1.83 ms: 1.10x slower                                                            |
| regex_compile  | 117 ms                                                          | 161 ms: 1.38x slower                                                             |
| Geometric mean | (ref)                                                           | 1.09x slower                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf1_win32-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| xml_etree_parse      | 120 ms                                                          | 112 ms: 1.07x faster                                                             |
| json_dumps           | 9.82 ms                                                         | 9.52 ms: 1.03x faster                                                            |
| json_loads           | 22.4 us                                                         | 23.1 us: 1.03x slower                                                            |
| pickle_list          | 3.22 us                                                         | 3.81 us: 1.18x slower                                                            |
| unpickle_list        | 2.98 us                                                         | 3.55 us: 1.19x slower                                                            |
| pickle_dict          | 18.2 us                                                         | 22.0 us: 1.20x slower                                                            |
| unpickle             | 9.82 us                                                         | 12.0 us: 1.22x slower                                                            |
| pickle               | 7.83 us                                                         | 9.85 us: 1.26x slower                                                            |
| xml_etree_iterparse  | 70.8 ms                                                         | 92.3 ms: 1.30x slower                                                            |
| pickle_pure_python   | 280 us                                                          | 451 us: 1.61x slower                                                             |
| xml_etree_process    | 48.1 ms                                                         | 79.9 ms: 1.66x slower                                                            |
| xml_etree_generate   | 61.6 ms                                                         | 107 ms: 1.74x slower                                                             |
| unpickle_pure_python | 189 us                                                          | 356 us: 1.88x slower                                                             |
| tomli_loads          | 1.91 sec                                                        | 5.05 sec: 2.64x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.36x slower                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf1_win32-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 20.4 ms: 1.13x slower                                                            |
| python_startup         | 22.9 ms                                                         | 27.7 ms: 1.21x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.17x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf1_win32-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 36.0 ms                                                         | 45.9 ms: 1.27x slower                                                            |
| genshi_xml      | 46.6 ms                                                         | 66.2 ms: 1.42x slower                                                            |
| genshi_text     | 21.0 ms                                                         | 34.3 ms: 1.63x slower                                                            |
| mako            | 9.10 ms                                                         | 16.4 ms: 1.81x slower                                                            |
| Geometric mean  | (ref)                                                           | 1.52x slower                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf1_win32-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|--------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl          | 17.0 sec                                                        | 2.71 sec: 6.25x faster                                                           |
| pidigits                 | 502 ms                                                          | 140 ms: 3.59x faster                                                             |
| pathlib                  | 81.2 ms                                                         | 35.5 ms: 2.29x faster                                                            |
| typing_runtime_protocols | 396 us                                                          | 198 us: 2.00x faster                                                             |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 484 ms: 1.91x faster                                                             |
| async_tree_io            | 940 ms                                                          | 580 ms: 1.62x faster                                                             |
| async_tree_none          | 394 ms                                                          | 275 ms: 1.43x faster                                                             |
| async_tree_memoization   | 467 ms                                                          | 336 ms: 1.39x faster                                                             |
| pylint                   | 384 ms                                                          | 282 ms: 1.36x faster                                                             |
| sqlite_synth             | 2.29 us                                                         | 1.71 us: 1.34x faster                                                            |
| asyncio_tcp              | 744 ms                                                          | 608 ms: 1.22x faster                                                             |
| regex_dna                | 131 ms                                                          | 113 ms: 1.15x faster                                                             |
| json                     | 4.76 ms                                                         | 4.23 ms: 1.13x faster                                                            |
| xml_etree_parse          | 120 ms                                                          | 112 ms: 1.07x faster                                                             |
| thrift                   | 902 us                                                          | 852 us: 1.06x faster                                                             |
| dulwich_log              | 58.5 ms                                                         | 56.3 ms: 1.04x faster                                                            |
| json_dumps               | 9.82 ms                                                         | 9.52 ms: 1.03x faster                                                            |
| json_loads               | 22.4 us                                                         | 23.1 us: 1.03x slower                                                            |
| regex_v8                 | 15.8 ms                                                         | 16.9 ms: 1.07x slower                                                            |
| deepcopy                 | 310 us                                                          | 336 us: 1.08x slower                                                             |
| regex_effbot             | 1.66 ms                                                         | 1.83 ms: 1.10x slower                                                            |
| bench_thread_pool        | 1.12 ms                                                         | 1.23 ms: 1.10x slower                                                            |
| python_startup_no_site   | 18.1 ms                                                         | 20.4 ms: 1.13x slower                                                            |
| sympy_sum                | 122 ms                                                          | 144 ms: 1.18x slower                                                             |
| pickle_list              | 3.22 us                                                         | 3.81 us: 1.18x slower                                                            |
| unpickle_list            | 2.98 us                                                         | 3.55 us: 1.19x slower                                                            |
| pickle_dict              | 18.2 us                                                         | 22.0 us: 1.20x slower                                                            |
| python_startup           | 22.9 ms                                                         | 27.7 ms: 1.21x slower                                                            |
| mdp                      | 1.83 sec                                                        | 2.22 sec: 1.22x slower                                                           |
| html5lib                 | 52.1 ms                                                         | 63.4 ms: 1.22x slower                                                            |
| unpickle                 | 9.82 us                                                         | 12.0 us: 1.22x slower                                                            |
| sympy_integrate          | 16.6 ms                                                         | 20.8 ms: 1.25x slower                                                            |
| pickle                   | 7.83 us                                                         | 9.85 us: 1.26x slower                                                            |
| sympy_expand             | 391 ms                                                          | 496 ms: 1.27x slower                                                             |
| 2to3                     | 265 ms                                                          | 338 ms: 1.27x slower                                                             |
| django_template          | 36.0 ms                                                         | 45.9 ms: 1.27x slower                                                            |
| sympy_str                | 229 ms                                                          | 292 ms: 1.28x slower                                                             |
| chaos                    | 74.4 ms                                                         | 96.3 ms: 1.29x slower                                                            |
| deepcopy_reduce          | 2.68 us                                                         | 3.48 us: 1.30x slower                                                            |
| xml_etree_iterparse      | 70.8 ms                                                         | 92.3 ms: 1.30x slower                                                            |
| go                       | 146 ms                                                          | 191 ms: 1.31x slower                                                             |
| gc_traversal             | 1.28 ms                                                         | 1.72 ms: 1.34x slower                                                            |
| bench_mp_pool            | 66.4 ms                                                         | 89.4 ms: 1.35x slower                                                            |
| regex_compile            | 117 ms                                                          | 161 ms: 1.38x slower                                                             |
| raytrace                 | 303 ms                                                          | 419 ms: 1.38x slower                                                             |
| float                    | 69.6 ms                                                         | 97.7 ms: 1.40x slower                                                            |
| generators               | 31.6 ms                                                         | 44.8 ms: 1.42x slower                                                            |
| genshi_xml               | 46.6 ms                                                         | 66.2 ms: 1.42x slower                                                            |
| nqueens                  | 87.1 ms                                                         | 125 ms: 1.43x slower                                                             |
| comprehensions           | 17.7 us                                                         | 25.5 us: 1.44x slower                                                            |
| crypto_pyaes             | 81.3 ms                                                         | 117 ms: 1.44x slower                                                             |
| pyflate                  | 422 ms                                                          | 614 ms: 1.46x slower                                                             |
| deltablue                | 4.04 ms                                                         | 5.91 ms: 1.46x slower                                                            |
| meteor_contest           | 80.0 ms                                                         | 117 ms: 1.47x slower                                                             |
| logging_format           | 7.91 us                                                         | 11.7 us: 1.48x slower                                                            |
| deepcopy_memo            | 29.6 us                                                         | 43.7 us: 1.48x slower                                                            |
| logging_simple           | 7.29 us                                                         | 11.1 us: 1.52x slower                                                            |
| create_gc_cycles         | 694 us                                                          | 1.10 ms: 1.58x slower                                                            |
| richards_super           | 49.9 ms                                                         | 79.3 ms: 1.59x slower                                                            |
| pickle_pure_python       | 280 us                                                          | 451 us: 1.61x slower                                                             |
| genshi_text              | 21.0 ms                                                         | 34.3 ms: 1.63x slower                                                            |
| scimark_sor              | 115 ms                                                          | 189 ms: 1.64x slower                                                             |
| xml_etree_process        | 48.1 ms                                                         | 79.9 ms: 1.66x slower                                                            |
| telco                    | 4.83 ms                                                         | 8.06 ms: 1.67x slower                                                            |
| pycparser                | 1.04 sec                                                        | 1.74 sec: 1.67x slower                                                           |
| hexiom                   | 6.13 ms                                                         | 10.5 ms: 1.71x slower                                                            |
| async_generators         | 241 ms                                                          | 418 ms: 1.73x slower                                                             |
| richards                 | 40.3 ms                                                         | 70.2 ms: 1.74x slower                                                            |
| xml_etree_generate       | 61.6 ms                                                         | 107 ms: 1.74x slower                                                             |
| scimark_monte_carlo      | 61.9 ms                                                         | 108 ms: 1.74x slower                                                             |
| coverage                 | 46.6 ms                                                         | 84.1 ms: 1.81x slower                                                            |
| mako                     | 9.10 ms                                                         | 16.4 ms: 1.81x slower                                                            |
| fannkuch                 | 317 ms                                                          | 573 ms: 1.81x slower                                                             |
| scimark_lu               | 89.8 ms                                                         | 165 ms: 1.84x slower                                                             |
| unpickle_pure_python     | 189 us                                                          | 356 us: 1.88x slower                                                             |
| coroutines               | 17.9 ms                                                         | 34.0 ms: 1.90x slower                                                            |
| scimark_fft              | 216 ms                                                          | 425 ms: 1.97x slower                                                             |
| unpack_sequence          | 40.0 ns                                                         | 81.1 ns: 2.03x slower                                                            |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 6.61 ms: 2.04x slower                                                            |
| spectral_norm            | 80.2 ms                                                         | 165 ms: 2.05x slower                                                             |
| docutils                 | 1.95 sec                                                        | 4.22 sec: 2.17x slower                                                           |
| pprint_safe_repr         | 658 ms                                                          | 1.48 sec: 2.24x slower                                                           |
| nbody                    | 79.1 ms                                                         | 184 ms: 2.32x slower                                                             |
| tomli_loads              | 1.91 sec                                                        | 5.05 sec: 2.64x slower                                                           |
| pprint_pformat           | 1.37 sec                                                        | 4.25 sec: 3.11x slower                                                           |
| logging_silent           | 97.9 ns                                                         | 586 ns: 5.99x slower                                                             |
| Geometric mean           | (ref)                                                           | 1.29x slower                                                                     |
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250617-3.15.0a0-fba5dde-NOGIL/bm-20250617-pythonperf1_win32-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.231x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.33x
- 95% likely to have a slowdown of 1.31x
- 99% likely to have a slowdown of 1.27x

# Memory
- memory change: unknown