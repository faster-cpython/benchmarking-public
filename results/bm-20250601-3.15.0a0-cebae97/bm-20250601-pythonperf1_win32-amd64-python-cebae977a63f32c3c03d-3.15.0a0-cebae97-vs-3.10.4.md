# Results vs. 3.10.4

- fork: python
- ref: cebae977a63f32c3c03d
- machine: windows-amd64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.116x slower
- HPT reliability: 98.88%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 294 ms: 1.11x slower                                                             |
| docutils       | 1.95 sec                                                        | 2.07 sec: 1.06x slower                                                           |
| html5lib       | 52.1 ms                                                         | 50.8 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                           | 1.05x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 447 ms: 2.06x faster                                                             |
| async_tree_io           | 940 ms                                                          | 550 ms: 1.71x faster                                                             |
| async_tree_none         | 394 ms                                                          | 244 ms: 1.61x faster                                                             |
| async_tree_memoization  | 467 ms                                                          | 298 ms: 1.57x faster                                                             |
| Geometric mean          | (ref)                                                           | 1.73x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 145 ms: 3.46x faster                                                             |
| float          | 69.6 ms                                                         | 77.3 ms: 1.11x slower                                                            |
| nbody          | 79.1 ms                                                         | 106 ms: 1.33x slower                                                             |
| Geometric mean | (ref)                                                           | 1.33x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 117 ms: 1.11x faster                                                             |
| regex_v8       | 15.8 ms                                                         | 16.6 ms: 1.05x slower                                                            |
| regex_compile  | 117 ms                                                          | 123 ms: 1.06x slower                                                             |
| regex_effbot   | 1.66 ms                                                         | 1.79 ms: 1.08x slower                                                            |
| Geometric mean | (ref)                                                           | 1.02x slower                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| xml_etree_parse      | 120 ms                                                          | 108 ms: 1.11x faster                                                             |
| json_loads           | 22.4 us                                                         | 20.5 us: 1.09x faster                                                            |
| json_dumps           | 9.82 ms                                                         | 9.00 ms: 1.09x faster                                                            |
| unpickle_list        | 2.98 us                                                         | 3.15 us: 1.06x slower                                                            |
| tomli_loads          | 1.91 sec                                                        | 2.09 sec: 1.10x slower                                                           |
| unpickle             | 9.82 us                                                         | 11.3 us: 1.15x slower                                                            |
| pickle               | 7.83 us                                                         | 9.48 us: 1.21x slower                                                            |
| pickle_list          | 3.22 us                                                         | 3.96 us: 1.23x slower                                                            |
| pickle_dict          | 18.2 us                                                         | 22.5 us: 1.24x slower                                                            |
| xml_etree_iterparse  | 70.8 ms                                                         | 89.3 ms: 1.26x slower                                                            |
| pickle_pure_python   | 280 us                                                          | 358 us: 1.28x slower                                                             |
| xml_etree_process    | 48.1 ms                                                         | 64.9 ms: 1.35x slower                                                            |
| unpickle_pure_python | 189 us                                                          | 275 us: 1.45x slower                                                             |
| xml_etree_generate   | 61.6 ms                                                         | 89.7 ms: 1.46x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.17x slower                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 20.1 ms: 1.11x slower                                                            |
| python_startup         | 22.9 ms                                                         | 27.4 ms: 1.19x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.15x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 36.0 ms                                                         | 37.2 ms: 1.03x slower                                                            |
| genshi_xml      | 46.6 ms                                                         | 49.4 ms: 1.06x slower                                                            |
| genshi_text     | 21.0 ms                                                         | 23.9 ms: 1.14x slower                                                            |
| mako            | 9.10 ms                                                         | 12.6 ms: 1.38x slower                                                            |
| Geometric mean  | (ref)                                                           | 1.15x slower                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|--------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl          | 17.0 sec                                                        | 1.36 sec: 12.48x faster                                                          |
| pidigits                 | 502 ms                                                          | 145 ms: 3.46x faster                                                             |
| typing_runtime_protocols | 396 us                                                          | 155 us: 2.56x faster                                                             |
| pathlib                  | 81.2 ms                                                         | 34.1 ms: 2.38x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 447 ms: 2.06x faster                                                             |
| async_tree_io            | 940 ms                                                          | 550 ms: 1.71x faster                                                             |
| asyncio_tcp              | 744 ms                                                          | 451 ms: 1.65x faster                                                             |
| async_tree_none          | 394 ms                                                          | 244 ms: 1.61x faster                                                             |
| async_tree_memoization   | 467 ms                                                          | 298 ms: 1.57x faster                                                             |
| pylint                   | 384 ms                                                          | 246 ms: 1.56x faster                                                             |
| mdp                      | 1.83 sec                                                        | 1.18 sec: 1.54x faster                                                           |
| json                     | 4.76 ms                                                         | 3.94 ms: 1.21x faster                                                            |
| sqlite_synth             | 2.29 us                                                         | 1.93 us: 1.19x faster                                                            |
| deepcopy                 | 310 us                                                          | 265 us: 1.17x faster                                                             |
| dulwich_log              | 58.5 ms                                                         | 51.4 ms: 1.14x faster                                                            |
| chaos                    | 74.4 ms                                                         | 65.5 ms: 1.14x faster                                                            |
| xml_etree_parse          | 120 ms                                                          | 108 ms: 1.11x faster                                                             |
| bench_thread_pool        | 1.12 ms                                                         | 1.00 ms: 1.11x faster                                                            |
| regex_dna                | 131 ms                                                          | 117 ms: 1.11x faster                                                             |
| json_loads               | 22.4 us                                                         | 20.5 us: 1.09x faster                                                            |
| json_dumps               | 9.82 ms                                                         | 9.00 ms: 1.09x faster                                                            |
| go                       | 146 ms                                                          | 134 ms: 1.09x faster                                                             |
| pycparser                | 1.04 sec                                                        | 977 ms: 1.07x faster                                                             |
| sympy_sum                | 122 ms                                                          | 116 ms: 1.06x faster                                                             |
| crypto_pyaes             | 81.3 ms                                                         | 79.3 ms: 1.03x faster                                                            |
| html5lib                 | 52.1 ms                                                         | 50.8 ms: 1.02x faster                                                            |
| raytrace                 | 303 ms                                                          | 301 ms: 1.00x faster                                                             |
| sympy_str                | 229 ms                                                          | 233 ms: 1.02x slower                                                             |
| deepcopy_reduce          | 2.68 us                                                         | 2.74 us: 1.02x slower                                                            |
| sympy_expand             | 391 ms                                                          | 400 ms: 1.02x slower                                                             |
| django_template          | 36.0 ms                                                         | 37.2 ms: 1.03x slower                                                            |
| regex_v8                 | 15.8 ms                                                         | 16.6 ms: 1.05x slower                                                            |
| unpickle_list            | 2.98 us                                                         | 3.15 us: 1.06x slower                                                            |
| regex_compile            | 117 ms                                                          | 123 ms: 1.06x slower                                                             |
| genshi_xml               | 46.6 ms                                                         | 49.4 ms: 1.06x slower                                                            |
| docutils                 | 1.95 sec                                                        | 2.07 sec: 1.06x slower                                                           |
| deltablue                | 4.04 ms                                                         | 4.32 ms: 1.07x slower                                                            |
| pyflate                  | 422 ms                                                          | 451 ms: 1.07x slower                                                             |
| regex_effbot             | 1.66 ms                                                         | 1.79 ms: 1.08x slower                                                            |
| nqueens                  | 87.1 ms                                                         | 93.9 ms: 1.08x slower                                                            |
| generators               | 31.6 ms                                                         | 34.5 ms: 1.09x slower                                                            |
| tomli_loads              | 1.91 sec                                                        | 2.09 sec: 1.10x slower                                                           |
| comprehensions           | 17.7 us                                                         | 19.6 us: 1.10x slower                                                            |
| 2to3                     | 265 ms                                                          | 294 ms: 1.11x slower                                                             |
| float                    | 69.6 ms                                                         | 77.3 ms: 1.11x slower                                                            |
| python_startup_no_site   | 18.1 ms                                                         | 20.1 ms: 1.11x slower                                                            |
| deepcopy_memo            | 29.6 us                                                         | 33.3 us: 1.13x slower                                                            |
| genshi_text              | 21.0 ms                                                         | 23.9 ms: 1.14x slower                                                            |
| richards_super           | 49.9 ms                                                         | 57.3 ms: 1.15x slower                                                            |
| scimark_sor              | 115 ms                                                          | 133 ms: 1.15x slower                                                             |
| unpickle                 | 9.82 us                                                         | 11.3 us: 1.15x slower                                                            |
| scimark_monte_carlo      | 61.9 ms                                                         | 72.7 ms: 1.17x slower                                                            |
| meteor_contest           | 80.0 ms                                                         | 94.3 ms: 1.18x slower                                                            |
| python_startup           | 22.9 ms                                                         | 27.4 ms: 1.19x slower                                                            |
| hexiom                   | 6.13 ms                                                         | 7.37 ms: 1.20x slower                                                            |
| pickle                   | 7.83 us                                                         | 9.48 us: 1.21x slower                                                            |
| pickle_list              | 3.22 us                                                         | 3.96 us: 1.23x slower                                                            |
| pickle_dict              | 18.2 us                                                         | 22.5 us: 1.24x slower                                                            |
| logging_format           | 7.91 us                                                         | 9.83 us: 1.24x slower                                                            |
| xml_etree_iterparse      | 70.8 ms                                                         | 89.3 ms: 1.26x slower                                                            |
| richards                 | 40.3 ms                                                         | 50.8 ms: 1.26x slower                                                            |
| pprint_pformat           | 1.37 sec                                                        | 1.74 sec: 1.27x slower                                                           |
| scimark_fft              | 216 ms                                                          | 275 ms: 1.27x slower                                                             |
| pickle_pure_python       | 280 us                                                          | 358 us: 1.28x slower                                                             |
| logging_simple           | 7.29 us                                                         | 9.32 us: 1.28x slower                                                            |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 4.15 ms: 1.28x slower                                                            |
| pprint_safe_repr         | 658 ms                                                          | 849 ms: 1.29x slower                                                             |
| telco                    | 4.83 ms                                                         | 6.26 ms: 1.30x slower                                                            |
| scimark_lu               | 89.8 ms                                                         | 118 ms: 1.31x slower                                                             |
| fannkuch                 | 317 ms                                                          | 420 ms: 1.33x slower                                                             |
| nbody                    | 79.1 ms                                                         | 106 ms: 1.33x slower                                                             |
| xml_etree_process        | 48.1 ms                                                         | 64.9 ms: 1.35x slower                                                            |
| mako                     | 9.10 ms                                                         | 12.6 ms: 1.38x slower                                                            |
| async_generators         | 241 ms                                                          | 343 ms: 1.42x slower                                                             |
| coroutines               | 17.9 ms                                                         | 25.6 ms: 1.43x slower                                                            |
| unpickle_pure_python     | 189 us                                                          | 275 us: 1.45x slower                                                             |
| xml_etree_generate       | 61.6 ms                                                         | 89.7 ms: 1.46x slower                                                            |
| spectral_norm            | 80.2 ms                                                         | 117 ms: 1.46x slower                                                             |
| bench_mp_pool            | 66.4 ms                                                         | 103 ms: 1.55x slower                                                             |
| unpack_sequence          | 40.0 ns                                                         | 81.7 ns: 2.04x slower                                                            |
| create_gc_cycles         | 694 us                                                          | 1.47 ms: 2.11x slower                                                            |
| gc_traversal             | 1.28 ms                                                         | 2.88 ms: 2.25x slower                                                            |
| logging_silent           | 97.9 ns                                                         | 487 ns: 4.98x slower                                                             |
| coverage                 | 46.6 ms                                                         | 475 ms: 10.20x slower                                                            |
| thrift                   | 902 us                                                          | 98.7 ms: 109.38x slower                                                          |
| Geometric mean           | (ref)                                                           | 1.12x slower                                                                     |

Benchmark hidden because not significant (1): sympy_integrate
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250601-3.15.0a0-cebae97/bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.116x slower

# HPT report

- Reliability score: 98.88% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown