# Results vs. 3.10.4

- fork: python
- ref: a852c7bdd48979218a0c
- machine: windows-amd64
- commit hash: a852c7b
- commit date: 2025-07-26
- overall geometric mean: 1.272x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 231 ms: 1.15x faster                                                             |
| docutils       | 1.95 sec                                                        | 3.03 sec: 1.55x slower                                                           |
| html5lib       | 52.1 ms                                                         | 41.4 ms: 1.26x faster                                                            |
| Geometric mean | (ref)                                                           | 1.02x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|-------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 334 ms: 2.76x faster                                                             |
| async_tree_io           | 940 ms                                                          | 365 ms: 2.57x faster                                                             |
| async_tree_none         | 394 ms                                                          | 176 ms: 2.24x faster                                                             |
| async_tree_memoization  | 467 ms                                                          | 218 ms: 2.14x faster                                                             |
| Geometric mean          | (ref)                                                           | 2.42x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 138 ms: 3.64x faster                                                             |
| float          | 69.6 ms                                                         | 46.9 ms: 1.48x faster                                                            |
| nbody          | 79.1 ms                                                         | 83.7 ms: 1.06x slower                                                            |
| Geometric mean | (ref)                                                           | 1.72x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 95.2 ms: 1.23x faster                                                            |
| regex_v8       | 15.8 ms                                                         | 12.9 ms: 1.22x faster                                                            |
| regex_dna      | 131 ms                                                          | 112 ms: 1.16x faster                                                             |
| regex_effbot   | 1.66 ms                                                         | 1.52 ms: 1.09x faster                                                            |
| Geometric mean | (ref)                                                           | 1.17x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 6.75 ms: 1.46x faster                                                            |
| json_loads           | 22.4 us                                                         | 15.8 us: 1.42x faster                                                            |
| xml_etree_parse      | 120 ms                                                          | 93.4 ms: 1.28x faster                                                            |
| unpickle_pure_python | 189 us                                                          | 158 us: 1.20x faster                                                             |
| pickle_pure_python   | 280 us                                                          | 237 us: 1.18x faster                                                             |
| xml_etree_iterparse  | 70.8 ms                                                         | 59.9 ms: 1.18x faster                                                            |
| xml_etree_process    | 48.1 ms                                                         | 44.4 ms: 1.08x faster                                                            |
| pickle_list          | 3.22 us                                                         | 3.09 us: 1.04x faster                                                            |
| xml_etree_generate   | 61.6 ms                                                         | 63.2 ms: 1.02x slower                                                            |
| pickle               | 7.83 us                                                         | 8.18 us: 1.04x slower                                                            |
| unpickle_list        | 2.98 us                                                         | 3.12 us: 1.05x slower                                                            |
| pickle_dict          | 18.2 us                                                         | 20.3 us: 1.11x slower                                                            |
| unpickle             | 9.82 us                                                         | 11.0 us: 1.12x slower                                                            |
| tomli_loads          | 1.91 sec                                                        | 2.83 sec: 1.48x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.07x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 20.2 ms: 1.12x slower                                                            |
| python_startup         | 22.9 ms                                                         | 27.2 ms: 1.19x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.15x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 36.0 ms                                                         | 27.3 ms: 1.32x faster                                                            |
| genshi_xml      | 46.6 ms                                                         | 40.7 ms: 1.14x faster                                                            |
| genshi_text     | 21.0 ms                                                         | 19.6 ms: 1.07x faster                                                            |
| mako            | 9.10 ms                                                         | 9.64 ms: 1.06x slower                                                            |
| Geometric mean  | (ref)                                                           | 1.11x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|--------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl          | 17.0 sec                                                        | 2.33 sec: 7.30x faster                                                           |
| pidigits                 | 502 ms                                                          | 138 ms: 3.64x faster                                                             |
| typing_runtime_protocols | 396 us                                                          | 137 us: 2.88x faster                                                             |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 334 ms: 2.76x faster                                                             |
| async_tree_io            | 940 ms                                                          | 365 ms: 2.57x faster                                                             |
| pathlib                  | 81.2 ms                                                         | 33.9 ms: 2.40x faster                                                            |
| async_tree_none          | 394 ms                                                          | 176 ms: 2.24x faster                                                             |
| async_tree_memoization   | 467 ms                                                          | 218 ms: 2.14x faster                                                             |
| pylint                   | 384 ms                                                          | 208 ms: 1.84x faster                                                             |
| sqlite_synth             | 2.29 us                                                         | 1.35 us: 1.70x faster                                                            |
| deltablue                | 4.04 ms                                                         | 2.52 ms: 1.60x faster                                                            |
| thrift                   | 902 us                                                          | 573 us: 1.57x faster                                                             |
| go                       | 146 ms                                                          | 93.0 ms: 1.57x faster                                                            |
| asyncio_tcp              | 744 ms                                                          | 475 ms: 1.57x faster                                                             |
| chaos                    | 74.4 ms                                                         | 47.6 ms: 1.56x faster                                                            |
| json                     | 4.76 ms                                                         | 3.08 ms: 1.55x faster                                                            |
| deepcopy                 | 310 us                                                          | 204 us: 1.52x faster                                                             |
| logging_silent           | 97.9 ns                                                         | 64.8 ns: 1.51x faster                                                            |
| mdp                      | 1.83 sec                                                        | 1.22 sec: 1.50x faster                                                           |
| float                    | 69.6 ms                                                         | 46.9 ms: 1.48x faster                                                            |
| json_dumps               | 9.82 ms                                                         | 6.75 ms: 1.46x faster                                                            |
| crypto_pyaes             | 81.3 ms                                                         | 56.9 ms: 1.43x faster                                                            |
| pycparser                | 1.04 sec                                                        | 729 ms: 1.43x faster                                                             |
| json_loads               | 22.4 us                                                         | 15.8 us: 1.42x faster                                                            |
| comprehensions           | 17.7 us                                                         | 12.5 us: 1.42x faster                                                            |
| deepcopy_memo            | 29.6 us                                                         | 21.2 us: 1.40x faster                                                            |
| raytrace                 | 303 ms                                                          | 218 ms: 1.39x faster                                                             |
| generators               | 31.6 ms                                                         | 22.7 ms: 1.39x faster                                                            |
| scimark_lu               | 89.8 ms                                                         | 65.3 ms: 1.38x faster                                                            |
| pyflate                  | 422 ms                                                          | 313 ms: 1.35x faster                                                             |
| django_template          | 36.0 ms                                                         | 27.3 ms: 1.32x faster                                                            |
| hexiom                   | 6.13 ms                                                         | 4.68 ms: 1.31x faster                                                            |
| scimark_sor              | 115 ms                                                          | 88.3 ms: 1.30x faster                                                            |
| dulwich_log              | 58.5 ms                                                         | 45.5 ms: 1.29x faster                                                            |
| xml_etree_parse          | 120 ms                                                          | 93.4 ms: 1.28x faster                                                            |
| richards_super           | 49.9 ms                                                         | 39.4 ms: 1.27x faster                                                            |
| html5lib                 | 52.1 ms                                                         | 41.4 ms: 1.26x faster                                                            |
| coroutines               | 17.9 ms                                                         | 14.3 ms: 1.25x faster                                                            |
| sympy_sum                | 122 ms                                                          | 98.2 ms: 1.25x faster                                                            |
| deepcopy_reduce          | 2.68 us                                                         | 2.18 us: 1.23x faster                                                            |
| regex_compile            | 117 ms                                                          | 95.2 ms: 1.23x faster                                                            |
| regex_v8                 | 15.8 ms                                                         | 12.9 ms: 1.22x faster                                                            |
| nqueens                  | 87.1 ms                                                         | 71.4 ms: 1.22x faster                                                            |
| sympy_str                | 229 ms                                                          | 189 ms: 1.21x faster                                                             |
| richards                 | 40.3 ms                                                         | 33.4 ms: 1.21x faster                                                            |
| scimark_monte_carlo      | 61.9 ms                                                         | 51.5 ms: 1.20x faster                                                            |
| unpickle_pure_python     | 189 us                                                          | 158 us: 1.20x faster                                                             |
| sympy_expand             | 391 ms                                                          | 326 ms: 1.20x faster                                                             |
| pickle_pure_python       | 280 us                                                          | 237 us: 1.18x faster                                                             |
| xml_etree_iterparse      | 70.8 ms                                                         | 59.9 ms: 1.18x faster                                                            |
| pprint_safe_repr         | 658 ms                                                          | 566 ms: 1.16x faster                                                             |
| regex_dna                | 131 ms                                                          | 112 ms: 1.16x faster                                                             |
| sympy_integrate          | 16.6 ms                                                         | 14.4 ms: 1.16x faster                                                            |
| 2to3                     | 265 ms                                                          | 231 ms: 1.15x faster                                                             |
| genshi_xml               | 46.6 ms                                                         | 40.7 ms: 1.14x faster                                                            |
| regex_effbot             | 1.66 ms                                                         | 1.52 ms: 1.09x faster                                                            |
| spectral_norm            | 80.2 ms                                                         | 73.7 ms: 1.09x faster                                                            |
| xml_etree_process        | 48.1 ms                                                         | 44.4 ms: 1.08x faster                                                            |
| genshi_text              | 21.0 ms                                                         | 19.6 ms: 1.07x faster                                                            |
| logging_format           | 7.91 us                                                         | 7.41 us: 1.07x faster                                                            |
| logging_simple           | 7.29 us                                                         | 6.85 us: 1.06x faster                                                            |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.05 ms: 1.06x faster                                                            |
| pickle_list              | 3.22 us                                                         | 3.09 us: 1.04x faster                                                            |
| gc_traversal             | 1.28 ms                                                         | 1.23 ms: 1.04x faster                                                            |
| scimark_fft              | 216 ms                                                          | 211 ms: 1.02x faster                                                             |
| xml_etree_generate       | 61.6 ms                                                         | 63.2 ms: 1.02x slower                                                            |
| unpack_sequence          | 40.0 ns                                                         | 41.4 ns: 1.03x slower                                                            |
| pickle                   | 7.83 us                                                         | 8.18 us: 1.04x slower                                                            |
| unpickle_list            | 2.98 us                                                         | 3.12 us: 1.05x slower                                                            |
| nbody                    | 79.1 ms                                                         | 83.7 ms: 1.06x slower                                                            |
| mako                     | 9.10 ms                                                         | 9.64 ms: 1.06x slower                                                            |
| telco                    | 4.83 ms                                                         | 5.24 ms: 1.08x slower                                                            |
| meteor_contest           | 80.0 ms                                                         | 87.4 ms: 1.09x slower                                                            |
| async_generators         | 241 ms                                                          | 268 ms: 1.11x slower                                                             |
| pickle_dict              | 18.2 us                                                         | 20.3 us: 1.11x slower                                                            |
| python_startup_no_site   | 18.1 ms                                                         | 20.2 ms: 1.12x slower                                                            |
| unpickle                 | 9.82 us                                                         | 11.0 us: 1.12x slower                                                            |
| python_startup           | 22.9 ms                                                         | 27.2 ms: 1.19x slower                                                            |
| bench_mp_pool            | 66.4 ms                                                         | 79.9 ms: 1.20x slower                                                            |
| pprint_pformat           | 1.37 sec                                                        | 1.80 sec: 1.31x slower                                                           |
| coverage                 | 46.6 ms                                                         | 68.4 ms: 1.47x slower                                                            |
| tomli_loads              | 1.91 sec                                                        | 2.83 sec: 1.48x slower                                                           |
| create_gc_cycles         | 694 us                                                          | 1.04 ms: 1.50x slower                                                            |
| docutils                 | 1.95 sec                                                        | 3.03 sec: 1.55x slower                                                           |
| Geometric mean           | (ref)                                                           | 1.26x faster                                                                     |

Benchmark hidden because not significant (2): fannkuch, bench_thread_pool
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250726-3.15.0a0-a852c7b-NOGIL/bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.272x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.16x

# Memory
- memory change: unknown