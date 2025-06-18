# Results vs. 3.10.4

- fork: python
- ref: fba5dded6df3c2b19435
- machine: windows-amd64
- commit hash: fba5dde
- commit date: 2025-06-17
- overall geometric mean: 1.026x faster
- HPT reliability: 54.74%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf1_win32-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 288 ms: 1.09x slower                                                             |
| docutils       | 1.95 sec                                                        | 2.11 sec: 1.08x slower                                                           |
| html5lib       | 52.1 ms                                                         | 53.0 ms: 1.02x slower                                                            |
| Geometric mean | (ref)                                                           | 1.06x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf1_win32-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 433 ms: 2.13x faster                                                             |
| async_tree_io           | 940 ms                                                          | 536 ms: 1.76x faster                                                             |
| async_tree_none         | 394 ms                                                          | 235 ms: 1.67x faster                                                             |
| async_tree_memoization  | 467 ms                                                          | 288 ms: 1.62x faster                                                             |
| Geometric mean          | (ref)                                                           | 1.78x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf1_win32-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 147 ms: 3.42x faster                                                             |
| nbody          | 79.1 ms                                                         | 53.4 ms: 1.48x faster                                                            |
| float          | 69.6 ms                                                         | 78.5 ms: 1.13x slower                                                            |
| Geometric mean | (ref)                                                           | 1.65x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf1_win32-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 117 ms: 1.11x faster                                                             |
| regex_effbot   | 1.66 ms                                                         | 1.74 ms: 1.04x slower                                                            |
| regex_compile  | 117 ms                                                          | 122 ms: 1.05x slower                                                             |
| regex_v8       | 15.8 ms                                                         | 16.7 ms: 1.06x slower                                                            |
| Geometric mean | (ref)                                                           | 1.01x slower                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf1_win32-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 1.91 sec                                                        | 1.59 sec: 1.20x faster                                                           |
| unpickle_pure_python | 189 us                                                          | 158 us: 1.20x faster                                                             |
| xml_etree_parse      | 120 ms                                                          | 105 ms: 1.14x faster                                                             |
| json_dumps           | 9.82 ms                                                         | 8.68 ms: 1.13x faster                                                            |
| json_loads           | 22.4 us                                                         | 20.8 us: 1.08x faster                                                            |
| unpickle_list        | 2.98 us                                                         | 3.13 us: 1.05x slower                                                            |
| xml_etree_process    | 48.1 ms                                                         | 53.0 ms: 1.10x slower                                                            |
| xml_etree_generate   | 61.6 ms                                                         | 72.2 ms: 1.17x slower                                                            |
| pickle_pure_python   | 280 us                                                          | 329 us: 1.17x slower                                                             |
| unpickle             | 9.82 us                                                         | 11.7 us: 1.19x slower                                                            |
| pickle_list          | 3.22 us                                                         | 3.95 us: 1.23x slower                                                            |
| pickle               | 7.83 us                                                         | 9.73 us: 1.24x slower                                                            |
| pickle_dict          | 18.2 us                                                         | 22.7 us: 1.24x slower                                                            |
| xml_etree_iterparse  | 70.8 ms                                                         | 88.1 ms: 1.24x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.06x slower                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf1_win32-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 20.0 ms: 1.11x slower                                                            |
| python_startup         | 22.9 ms                                                         | 27.3 ms: 1.19x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.15x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf1_win32-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 7.12 ms: 1.28x faster                                                            |
| django_template | 36.0 ms                                                         | 38.7 ms: 1.07x slower                                                            |
| genshi_xml      | 46.6 ms                                                         | 51.1 ms: 1.10x slower                                                            |
| genshi_text     | 21.0 ms                                                         | 25.4 ms: 1.21x slower                                                            |
| Geometric mean  | (ref)                                                           | 1.03x slower                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf1_win32-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|--------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl          | 17.0 sec                                                        | 1.51 sec: 11.25x faster                                                          |
| pidigits                 | 502 ms                                                          | 147 ms: 3.42x faster                                                             |
| typing_runtime_protocols | 396 us                                                          | 144 us: 2.74x faster                                                             |
| pathlib                  | 81.2 ms                                                         | 34.9 ms: 2.33x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 433 ms: 2.13x faster                                                             |
| async_tree_io            | 940 ms                                                          | 536 ms: 1.76x faster                                                             |
| async_tree_none          | 394 ms                                                          | 235 ms: 1.67x faster                                                             |
| async_tree_memoization   | 467 ms                                                          | 288 ms: 1.62x faster                                                             |
| pylint                   | 384 ms                                                          | 253 ms: 1.52x faster                                                             |
| mdp                      | 1.83 sec                                                        | 1.20 sec: 1.52x faster                                                           |
| nbody                    | 79.1 ms                                                         | 53.4 ms: 1.48x faster                                                            |
| sqlite_synth             | 2.29 us                                                         | 1.74 us: 1.32x faster                                                            |
| crypto_pyaes             | 81.3 ms                                                         | 62.2 ms: 1.31x faster                                                            |
| asyncio_tcp              | 744 ms                                                          | 570 ms: 1.30x faster                                                             |
| mako                     | 9.10 ms                                                         | 7.12 ms: 1.28x faster                                                            |
| thrift                   | 902 us                                                          | 719 us: 1.25x faster                                                             |
| tomli_loads              | 1.91 sec                                                        | 1.59 sec: 1.20x faster                                                           |
| unpickle_pure_python     | 189 us                                                          | 158 us: 1.20x faster                                                             |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.72 ms: 1.19x faster                                                            |
| scimark_fft              | 216 ms                                                          | 184 ms: 1.17x faster                                                             |
| json                     | 4.76 ms                                                         | 4.07 ms: 1.17x faster                                                            |
| xml_etree_parse          | 120 ms                                                          | 105 ms: 1.14x faster                                                             |
| bench_thread_pool        | 1.12 ms                                                         | 984 us: 1.14x faster                                                             |
| deepcopy                 | 310 us                                                          | 273 us: 1.14x faster                                                             |
| json_dumps               | 9.82 ms                                                         | 8.68 ms: 1.13x faster                                                            |
| chaos                    | 74.4 ms                                                         | 65.9 ms: 1.13x faster                                                            |
| comprehensions           | 17.7 us                                                         | 15.9 us: 1.12x faster                                                            |
| fannkuch                 | 317 ms                                                          | 284 ms: 1.12x faster                                                             |
| dulwich_log              | 58.5 ms                                                         | 52.4 ms: 1.12x faster                                                            |
| regex_dna                | 131 ms                                                          | 117 ms: 1.11x faster                                                             |
| pycparser                | 1.04 sec                                                        | 958 ms: 1.09x faster                                                             |
| pyflate                  | 422 ms                                                          | 390 ms: 1.08x faster                                                             |
| json_loads               | 22.4 us                                                         | 20.8 us: 1.08x faster                                                            |
| go                       | 146 ms                                                          | 136 ms: 1.07x faster                                                             |
| sympy_sum                | 122 ms                                                          | 116 ms: 1.05x faster                                                             |
| raytrace                 | 303 ms                                                          | 306 ms: 1.01x slower                                                             |
| html5lib                 | 52.1 ms                                                         | 53.0 ms: 1.02x slower                                                            |
| pprint_safe_repr         | 658 ms                                                          | 671 ms: 1.02x slower                                                             |
| sympy_integrate          | 16.6 ms                                                         | 17.0 ms: 1.02x slower                                                            |
| sympy_str                | 229 ms                                                          | 236 ms: 1.03x slower                                                             |
| meteor_contest           | 80.0 ms                                                         | 83.0 ms: 1.04x slower                                                            |
| regex_effbot             | 1.66 ms                                                         | 1.74 ms: 1.04x slower                                                            |
| regex_compile            | 117 ms                                                          | 122 ms: 1.05x slower                                                             |
| unpickle_list            | 2.98 us                                                         | 3.13 us: 1.05x slower                                                            |
| sympy_expand             | 391 ms                                                          | 410 ms: 1.05x slower                                                             |
| nqueens                  | 87.1 ms                                                         | 91.8 ms: 1.05x slower                                                            |
| deepcopy_reduce          | 2.68 us                                                         | 2.83 us: 1.06x slower                                                            |
| regex_v8                 | 15.8 ms                                                         | 16.7 ms: 1.06x slower                                                            |
| django_template          | 36.0 ms                                                         | 38.7 ms: 1.07x slower                                                            |
| docutils                 | 1.95 sec                                                        | 2.11 sec: 1.08x slower                                                           |
| 2to3                     | 265 ms                                                          | 288 ms: 1.09x slower                                                             |
| genshi_xml               | 46.6 ms                                                         | 51.1 ms: 1.10x slower                                                            |
| xml_etree_process        | 48.1 ms                                                         | 53.0 ms: 1.10x slower                                                            |
| python_startup_no_site   | 18.1 ms                                                         | 20.0 ms: 1.11x slower                                                            |
| deltablue                | 4.04 ms                                                         | 4.52 ms: 1.12x slower                                                            |
| float                    | 69.6 ms                                                         | 78.5 ms: 1.13x slower                                                            |
| telco                    | 4.83 ms                                                         | 5.44 ms: 1.13x slower                                                            |
| xml_etree_generate       | 61.6 ms                                                         | 72.2 ms: 1.17x slower                                                            |
| pickle_pure_python       | 280 us                                                          | 329 us: 1.17x slower                                                             |
| unpickle                 | 9.82 us                                                         | 11.7 us: 1.19x slower                                                            |
| scimark_sor              | 115 ms                                                          | 137 ms: 1.19x slower                                                             |
| python_startup           | 22.9 ms                                                         | 27.3 ms: 1.19x slower                                                            |
| deepcopy_memo            | 29.6 us                                                         | 35.5 us: 1.20x slower                                                            |
| scimark_monte_carlo      | 61.9 ms                                                         | 74.8 ms: 1.21x slower                                                            |
| genshi_text              | 21.0 ms                                                         | 25.4 ms: 1.21x slower                                                            |
| generators               | 31.6 ms                                                         | 38.2 ms: 1.21x slower                                                            |
| richards_super           | 49.9 ms                                                         | 60.6 ms: 1.21x slower                                                            |
| pickle_list              | 3.22 us                                                         | 3.95 us: 1.23x slower                                                            |
| pickle                   | 7.83 us                                                         | 9.73 us: 1.24x slower                                                            |
| pickle_dict              | 18.2 us                                                         | 22.7 us: 1.24x slower                                                            |
| xml_etree_iterparse      | 70.8 ms                                                         | 88.1 ms: 1.24x slower                                                            |
| logging_format           | 7.91 us                                                         | 10.1 us: 1.28x slower                                                            |
| hexiom                   | 6.13 ms                                                         | 7.98 ms: 1.30x slower                                                            |
| logging_simple           | 7.29 us                                                         | 9.59 us: 1.32x slower                                                            |
| richards                 | 40.3 ms                                                         | 53.9 ms: 1.34x slower                                                            |
| coverage                 | 46.6 ms                                                         | 62.6 ms: 1.34x slower                                                            |
| scimark_lu               | 89.8 ms                                                         | 126 ms: 1.40x slower                                                             |
| spectral_norm            | 80.2 ms                                                         | 115 ms: 1.44x slower                                                             |
| async_generators         | 241 ms                                                          | 354 ms: 1.47x slower                                                             |
| coroutines               | 17.9 ms                                                         | 26.8 ms: 1.50x slower                                                            |
| bench_mp_pool            | 66.4 ms                                                         | 106 ms: 1.60x slower                                                             |
| unpack_sequence          | 40.0 ns                                                         | 77.8 ns: 1.94x slower                                                            |
| create_gc_cycles         | 694 us                                                          | 1.47 ms: 2.12x slower                                                            |
| gc_traversal             | 1.28 ms                                                         | 2.99 ms: 2.34x slower                                                            |
| logging_silent           | 97.9 ns                                                         | 507 ns: 5.18x slower                                                             |
| Geometric mean           | (ref)                                                           | 1.02x faster                                                                     |

Benchmark hidden because not significant (1): pprint_pformat
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250617-3.15.0a0-fba5dde-JIT/bm-20250617-pythonperf1_win32-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.026x faster

# HPT report

- Reliability score: 54.74% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown