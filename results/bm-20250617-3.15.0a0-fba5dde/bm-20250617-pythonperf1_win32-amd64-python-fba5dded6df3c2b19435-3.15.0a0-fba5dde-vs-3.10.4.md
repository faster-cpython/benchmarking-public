# Results vs. 3.10.4

- fork: python
- ref: fba5dded6df3c2b19435
- machine: windows-amd64
- commit hash: fba5dde
- commit date: 2025-06-17
- overall geometric mean: 1.023x slower
- HPT reliability: 97.48%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf1_win32-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 291 ms: 1.10x slower                                                             |
| docutils       | 1.95 sec                                                        | 2.08 sec: 1.07x slower                                                           |
| Geometric mean | (ref)                                                           | 1.05x slower                                                                     |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf1_win32-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 442 ms: 2.09x faster                                                             |
| async_tree_io           | 940 ms                                                          | 548 ms: 1.72x faster                                                             |
| async_tree_none         | 394 ms                                                          | 243 ms: 1.62x faster                                                             |
| async_tree_memoization  | 467 ms                                                          | 295 ms: 1.58x faster                                                             |
| Geometric mean          | (ref)                                                           | 1.74x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf1_win32-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 147 ms: 3.42x faster                                                             |
| float          | 69.6 ms                                                         | 75.5 ms: 1.08x slower                                                            |
| nbody          | 79.1 ms                                                         | 99.3 ms: 1.25x slower                                                            |
| Geometric mean | (ref)                                                           | 1.36x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf1_win32-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 117 ms: 1.12x faster                                                             |
| regex_effbot   | 1.66 ms                                                         | 1.72 ms: 1.04x slower                                                            |
| regex_compile  | 117 ms                                                          | 122 ms: 1.04x slower                                                             |
| regex_v8       | 15.8 ms                                                         | 17.1 ms: 1.08x slower                                                            |
| Geometric mean | (ref)                                                           | 1.01x slower                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf1_win32-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 8.53 ms: 1.15x faster                                                            |
| xml_etree_parse      | 120 ms                                                          | 109 ms: 1.11x faster                                                             |
| json_loads           | 22.4 us                                                         | 20.8 us: 1.08x faster                                                            |
| unpickle_list        | 2.98 us                                                         | 3.06 us: 1.03x slower                                                            |
| tomli_loads          | 1.91 sec                                                        | 2.02 sec: 1.06x slower                                                           |
| unpickle             | 9.82 us                                                         | 11.5 us: 1.17x slower                                                            |
| pickle_list          | 3.22 us                                                         | 3.79 us: 1.18x slower                                                            |
| pickle               | 7.83 us                                                         | 9.57 us: 1.22x slower                                                            |
| pickle_dict          | 18.2 us                                                         | 22.7 us: 1.24x slower                                                            |
| pickle_pure_python   | 280 us                                                          | 358 us: 1.28x slower                                                             |
| xml_etree_iterparse  | 70.8 ms                                                         | 92.2 ms: 1.30x slower                                                            |
| xml_etree_process    | 48.1 ms                                                         | 64.0 ms: 1.33x slower                                                            |
| xml_etree_generate   | 61.6 ms                                                         | 89.1 ms: 1.44x slower                                                            |
| unpickle_pure_python | 189 us                                                          | 275 us: 1.45x slower                                                             |
| Geometric mean       | (ref)                                                           | 1.16x slower                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf1_win32-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 20.2 ms: 1.12x slower                                                            |
| python_startup         | 22.9 ms                                                         | 27.4 ms: 1.19x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.16x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf1_win32-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 36.0 ms                                                         | 36.3 ms: 1.01x slower                                                            |
| genshi_xml      | 46.6 ms                                                         | 48.3 ms: 1.04x slower                                                            |
| genshi_text     | 21.0 ms                                                         | 23.3 ms: 1.11x slower                                                            |
| mako            | 9.10 ms                                                         | 12.4 ms: 1.36x slower                                                            |
| Geometric mean  | (ref)                                                           | 1.12x slower                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf1_win32-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|--------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl          | 17.0 sec                                                        | 1.48 sec: 11.47x faster                                                          |
| pidigits                 | 502 ms                                                          | 147 ms: 3.42x faster                                                             |
| typing_runtime_protocols | 396 us                                                          | 154 us: 2.57x faster                                                             |
| pathlib                  | 81.2 ms                                                         | 34.2 ms: 2.38x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 442 ms: 2.09x faster                                                             |
| async_tree_io            | 940 ms                                                          | 548 ms: 1.72x faster                                                             |
| async_tree_none          | 394 ms                                                          | 243 ms: 1.62x faster                                                             |
| mdp                      | 1.83 sec                                                        | 1.15 sec: 1.59x faster                                                           |
| async_tree_memoization   | 467 ms                                                          | 295 ms: 1.58x faster                                                             |
| pylint                   | 384 ms                                                          | 246 ms: 1.56x faster                                                             |
| asyncio_tcp              | 744 ms                                                          | 560 ms: 1.33x faster                                                             |
| thrift                   | 902 us                                                          | 688 us: 1.31x faster                                                             |
| sqlite_synth             | 2.29 us                                                         | 1.86 us: 1.23x faster                                                            |
| deepcopy                 | 310 us                                                          | 262 us: 1.18x faster                                                             |
| json                     | 4.76 ms                                                         | 4.05 ms: 1.18x faster                                                            |
| chaos                    | 74.4 ms                                                         | 63.9 ms: 1.16x faster                                                            |
| json_dumps               | 9.82 ms                                                         | 8.53 ms: 1.15x faster                                                            |
| dulwich_log              | 58.5 ms                                                         | 50.9 ms: 1.15x faster                                                            |
| bench_thread_pool        | 1.12 ms                                                         | 993 us: 1.13x faster                                                             |
| regex_dna                | 131 ms                                                          | 117 ms: 1.12x faster                                                             |
| go                       | 146 ms                                                          | 132 ms: 1.11x faster                                                             |
| xml_etree_parse          | 120 ms                                                          | 109 ms: 1.11x faster                                                             |
| json_loads               | 22.4 us                                                         | 20.8 us: 1.08x faster                                                            |
| pycparser                | 1.04 sec                                                        | 975 ms: 1.07x faster                                                             |
| sympy_sum                | 122 ms                                                          | 115 ms: 1.07x faster                                                             |
| crypto_pyaes             | 81.3 ms                                                         | 79.5 ms: 1.02x faster                                                            |
| sympy_integrate          | 16.6 ms                                                         | 16.4 ms: 1.01x faster                                                            |
| raytrace                 | 303 ms                                                          | 301 ms: 1.01x faster                                                             |
| django_template          | 36.0 ms                                                         | 36.3 ms: 1.01x slower                                                            |
| sympy_str                | 229 ms                                                          | 232 ms: 1.01x slower                                                             |
| sympy_expand             | 391 ms                                                          | 395 ms: 1.01x slower                                                             |
| unpickle_list            | 2.98 us                                                         | 3.06 us: 1.03x slower                                                            |
| genshi_xml               | 46.6 ms                                                         | 48.3 ms: 1.04x slower                                                            |
| regex_effbot             | 1.66 ms                                                         | 1.72 ms: 1.04x slower                                                            |
| regex_compile            | 117 ms                                                          | 122 ms: 1.04x slower                                                             |
| nqueens                  | 87.1 ms                                                         | 91.5 ms: 1.05x slower                                                            |
| tomli_loads              | 1.91 sec                                                        | 2.02 sec: 1.06x slower                                                           |
| deltablue                | 4.04 ms                                                         | 4.29 ms: 1.06x slower                                                            |
| docutils                 | 1.95 sec                                                        | 2.08 sec: 1.07x slower                                                           |
| pyflate                  | 422 ms                                                          | 451 ms: 1.07x slower                                                             |
| regex_v8                 | 15.8 ms                                                         | 17.1 ms: 1.08x slower                                                            |
| float                    | 69.6 ms                                                         | 75.5 ms: 1.08x slower                                                            |
| comprehensions           | 17.7 us                                                         | 19.3 us: 1.09x slower                                                            |
| 2to3                     | 265 ms                                                          | 291 ms: 1.10x slower                                                             |
| genshi_text              | 21.0 ms                                                         | 23.3 ms: 1.11x slower                                                            |
| scimark_sor              | 115 ms                                                          | 129 ms: 1.12x slower                                                             |
| deepcopy_memo            | 29.6 us                                                         | 33.1 us: 1.12x slower                                                            |
| python_startup_no_site   | 18.1 ms                                                         | 20.2 ms: 1.12x slower                                                            |
| richards_super           | 49.9 ms                                                         | 57.3 ms: 1.15x slower                                                            |
| meteor_contest           | 80.0 ms                                                         | 92.2 ms: 1.15x slower                                                            |
| generators               | 31.6 ms                                                         | 36.5 ms: 1.16x slower                                                            |
| scimark_monte_carlo      | 61.9 ms                                                         | 71.7 ms: 1.16x slower                                                            |
| unpickle                 | 9.82 us                                                         | 11.5 us: 1.17x slower                                                            |
| pickle_list              | 3.22 us                                                         | 3.79 us: 1.18x slower                                                            |
| python_startup           | 22.9 ms                                                         | 27.4 ms: 1.19x slower                                                            |
| hexiom                   | 6.13 ms                                                         | 7.40 ms: 1.21x slower                                                            |
| pickle                   | 7.83 us                                                         | 9.57 us: 1.22x slower                                                            |
| scimark_fft              | 216 ms                                                          | 266 ms: 1.23x slower                                                             |
| logging_format           | 7.91 us                                                         | 9.72 us: 1.23x slower                                                            |
| pickle_dict              | 18.2 us                                                         | 22.7 us: 1.24x slower                                                            |
| nbody                    | 79.1 ms                                                         | 99.3 ms: 1.25x slower                                                            |
| richards                 | 40.3 ms                                                         | 50.6 ms: 1.26x slower                                                            |
| logging_simple           | 7.29 us                                                         | 9.21 us: 1.26x slower                                                            |
| pprint_pformat           | 1.37 sec                                                        | 1.74 sec: 1.28x slower                                                           |
| pickle_pure_python       | 280 us                                                          | 358 us: 1.28x slower                                                             |
| fannkuch                 | 317 ms                                                          | 406 ms: 1.28x slower                                                             |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 4.15 ms: 1.28x slower                                                            |
| telco                    | 4.83 ms                                                         | 6.25 ms: 1.29x slower                                                            |
| pprint_safe_repr         | 658 ms                                                          | 856 ms: 1.30x slower                                                             |
| xml_etree_iterparse      | 70.8 ms                                                         | 92.2 ms: 1.30x slower                                                            |
| scimark_lu               | 89.8 ms                                                         | 119 ms: 1.33x slower                                                             |
| xml_etree_process        | 48.1 ms                                                         | 64.0 ms: 1.33x slower                                                            |
| coverage                 | 46.6 ms                                                         | 62.2 ms: 1.34x slower                                                            |
| mako                     | 9.10 ms                                                         | 12.4 ms: 1.36x slower                                                            |
| async_generators         | 241 ms                                                          | 332 ms: 1.38x slower                                                             |
| coroutines               | 17.9 ms                                                         | 24.7 ms: 1.38x slower                                                            |
| spectral_norm            | 80.2 ms                                                         | 111 ms: 1.38x slower                                                             |
| xml_etree_generate       | 61.6 ms                                                         | 89.1 ms: 1.44x slower                                                            |
| unpickle_pure_python     | 189 us                                                          | 275 us: 1.45x slower                                                             |
| bench_mp_pool            | 66.4 ms                                                         | 105 ms: 1.58x slower                                                             |
| unpack_sequence          | 40.0 ns                                                         | 77.6 ns: 1.94x slower                                                            |
| create_gc_cycles         | 694 us                                                          | 1.47 ms: 2.12x slower                                                            |
| gc_traversal             | 1.28 ms                                                         | 2.99 ms: 2.34x slower                                                            |
| logging_silent           | 97.9 ns                                                         | 495 ns: 5.05x slower                                                             |
| Geometric mean           | (ref)                                                           | 1.03x slower                                                                     |

Benchmark hidden because not significant (2): html5lib, deepcopy_reduce
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-pythonperf1_win32-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.023x slower

# HPT report

- Reliability score: 97.48% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown