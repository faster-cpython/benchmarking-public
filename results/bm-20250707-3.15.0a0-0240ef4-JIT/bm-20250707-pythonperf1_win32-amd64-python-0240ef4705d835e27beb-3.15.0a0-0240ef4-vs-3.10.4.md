# Results vs. 3.10.4

- fork: python
- ref: 0240ef4705d835e27beb
- machine: windows-amd64
- commit hash: 0240ef4
- commit date: 2025-07-07
- overall geometric mean: 1.486x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.40x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250707-pythonperf1_win32-amd64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 216 ms: 1.23x faster                                                             |
| docutils       | 1.95 sec                                                        | 1.65 sec: 1.18x faster                                                           |
| html5lib       | 52.1 ms                                                         | 37.8 ms: 1.38x faster                                                            |
| Geometric mean | (ref)                                                           | 1.26x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250707-pythonperf1_win32-amd64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 |
|-------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 332 ms: 2.78x faster                                                             |
| async_tree_io           | 940 ms                                                          | 394 ms: 2.39x faster                                                             |
| async_tree_none         | 394 ms                                                          | 168 ms: 2.34x faster                                                             |
| async_tree_memoization  | 467 ms                                                          | 204 ms: 2.29x faster                                                             |
| Geometric mean          | (ref)                                                           | 2.44x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250707-pythonperf1_win32-amd64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 147 ms: 3.43x faster                                                             |
| float          | 69.6 ms                                                         | 43.4 ms: 1.60x faster                                                            |
| nbody          | 79.1 ms                                                         | 53.7 ms: 1.47x faster                                                            |
| Geometric mean | (ref)                                                           | 2.01x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250707-pythonperf1_win32-amd64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 78.2 ms: 1.49x faster                                                            |
| regex_dna      | 131 ms                                                          | 118 ms: 1.11x faster                                                             |
| regex_v8       | 15.8 ms                                                         | 14.3 ms: 1.10x faster                                                            |
| regex_effbot   | 1.66 ms                                                         | 1.58 ms: 1.05x faster                                                            |
| Geometric mean | (ref)                                                           | 1.18x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250707-pythonperf1_win32-amd64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| unpickle_pure_python | 189 us                                                          | 108 us: 1.75x faster                                                             |
| tomli_loads          | 1.91 sec                                                        | 1.13 sec: 1.70x faster                                                           |
| json_dumps           | 9.82 ms                                                         | 6.32 ms: 1.55x faster                                                            |
| json_loads           | 22.4 us                                                         | 14.5 us: 1.55x faster                                                            |
| xml_etree_parse      | 120 ms                                                          | 86.1 ms: 1.39x faster                                                            |
| xml_etree_process    | 48.1 ms                                                         | 34.9 ms: 1.38x faster                                                            |
| pickle_pure_python   | 280 us                                                          | 205 us: 1.37x faster                                                             |
| xml_etree_generate   | 61.6 ms                                                         | 49.9 ms: 1.23x faster                                                            |
| xml_etree_iterparse  | 70.8 ms                                                         | 61.7 ms: 1.15x faster                                                            |
| Geometric mean       | (ref)                                                           | 1.44x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250707-pythonperf1_win32-amd64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 19.5 ms: 1.08x slower                                                            |
| python_startup         | 22.9 ms                                                         | 25.6 ms: 1.12x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.10x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250707-pythonperf1_win32-amd64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 5.46 ms: 1.67x faster                                                            |
| django_template | 36.0 ms                                                         | 24.5 ms: 1.47x faster                                                            |
| genshi_text     | 21.0 ms                                                         | 15.1 ms: 1.39x faster                                                            |
| genshi_xml      | 46.6 ms                                                         | 33.7 ms: 1.38x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.47x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250707-pythonperf1_win32-amd64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 |
|--------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 106 us: 3.72x faster                                                             |
| pidigits                 | 502 ms                                                          | 147 ms: 3.43x faster                                                             |
| pathlib                  | 81.2 ms                                                         | 29.1 ms: 2.79x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 332 ms: 2.78x faster                                                             |
| async_tree_io            | 940 ms                                                          | 394 ms: 2.39x faster                                                             |
| async_tree_none          | 394 ms                                                          | 168 ms: 2.34x faster                                                             |
| mdp                      | 1.83 sec                                                        | 793 ms: 2.30x faster                                                             |
| async_tree_memoization   | 467 ms                                                          | 204 ms: 2.29x faster                                                             |
| pylint                   | 384 ms                                                          | 198 ms: 1.94x faster                                                             |
| go                       | 146 ms                                                          | 76.2 ms: 1.91x faster                                                            |
| deltablue                | 4.04 ms                                                         | 2.13 ms: 1.90x faster                                                            |
| chaos                    | 74.4 ms                                                         | 39.9 ms: 1.87x faster                                                            |
| thrift                   | 902 us                                                          | 491 us: 1.84x faster                                                             |
| deepcopy                 | 310 us                                                          | 170 us: 1.82x faster                                                             |
| logging_silent           | 97.9 ns                                                         | 54.4 ns: 1.80x faster                                                            |
| crypto_pyaes             | 81.3 ms                                                         | 45.8 ms: 1.78x faster                                                            |
| unpickle_pure_python     | 189 us                                                          | 108 us: 1.75x faster                                                             |
| comprehensions           | 17.7 us                                                         | 10.5 us: 1.70x faster                                                            |
| tomli_loads              | 1.91 sec                                                        | 1.13 sec: 1.70x faster                                                           |
| raytrace                 | 303 ms                                                          | 179 ms: 1.69x faster                                                             |
| pyflate                  | 422 ms                                                          | 252 ms: 1.67x faster                                                             |
| mako                     | 9.10 ms                                                         | 5.46 ms: 1.67x faster                                                            |
| deepcopy_memo            | 29.6 us                                                         | 18.0 us: 1.65x faster                                                            |
| richards_super           | 49.9 ms                                                         | 30.4 ms: 1.64x faster                                                            |
| generators               | 31.6 ms                                                         | 19.4 ms: 1.62x faster                                                            |
| float                    | 69.6 ms                                                         | 43.4 ms: 1.60x faster                                                            |
| json                     | 4.76 ms                                                         | 2.97 ms: 1.60x faster                                                            |
| json_dumps               | 9.82 ms                                                         | 6.32 ms: 1.55x faster                                                            |
| json_loads               | 22.4 us                                                         | 14.5 us: 1.55x faster                                                            |
| scimark_sor              | 115 ms                                                          | 75.3 ms: 1.53x faster                                                            |
| scimark_monte_carlo      | 61.9 ms                                                         | 40.8 ms: 1.52x faster                                                            |
| richards                 | 40.3 ms                                                         | 26.7 ms: 1.51x faster                                                            |
| hexiom                   | 6.13 ms                                                         | 4.09 ms: 1.50x faster                                                            |
| pycparser                | 1.04 sec                                                        | 698 ms: 1.49x faster                                                             |
| regex_compile            | 117 ms                                                          | 78.2 ms: 1.49x faster                                                            |
| nqueens                  | 87.1 ms                                                         | 58.5 ms: 1.49x faster                                                            |
| pprint_pformat           | 1.37 sec                                                        | 923 ms: 1.48x faster                                                             |
| deepcopy_reduce          | 2.68 us                                                         | 1.82 us: 1.47x faster                                                            |
| nbody                    | 79.1 ms                                                         | 53.7 ms: 1.47x faster                                                            |
| pprint_safe_repr         | 658 ms                                                          | 447 ms: 1.47x faster                                                             |
| django_template          | 36.0 ms                                                         | 24.5 ms: 1.47x faster                                                            |
| scimark_lu               | 89.8 ms                                                         | 61.1 ms: 1.47x faster                                                            |
| sqlite_synth             | 2.29 us                                                         | 1.57 us: 1.46x faster                                                            |
| fannkuch                 | 317 ms                                                          | 219 ms: 1.45x faster                                                             |
| dulwich_log              | 58.5 ms                                                         | 40.8 ms: 1.43x faster                                                            |
| scimark_fft              | 216 ms                                                          | 152 ms: 1.42x faster                                                             |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.29 ms: 1.41x faster                                                            |
| sympy_sum                | 122 ms                                                          | 87.0 ms: 1.41x faster                                                            |
| xml_etree_parse          | 120 ms                                                          | 86.1 ms: 1.39x faster                                                            |
| genshi_text              | 21.0 ms                                                         | 15.1 ms: 1.39x faster                                                            |
| genshi_xml               | 46.6 ms                                                         | 33.7 ms: 1.38x faster                                                            |
| html5lib                 | 52.1 ms                                                         | 37.8 ms: 1.38x faster                                                            |
| xml_etree_process        | 48.1 ms                                                         | 34.9 ms: 1.38x faster                                                            |
| pickle_pure_python       | 280 us                                                          | 205 us: 1.37x faster                                                             |
| sympy_str                | 229 ms                                                          | 170 ms: 1.35x faster                                                             |
| sympy_expand             | 391 ms                                                          | 294 ms: 1.33x faster                                                             |
| sympy_integrate          | 16.6 ms                                                         | 12.6 ms: 1.32x faster                                                            |
| spectral_norm            | 80.2 ms                                                         | 63.5 ms: 1.26x faster                                                            |
| coroutines               | 17.9 ms                                                         | 14.5 ms: 1.24x faster                                                            |
| xml_etree_generate       | 61.6 ms                                                         | 49.9 ms: 1.23x faster                                                            |
| 2to3                     | 265 ms                                                          | 216 ms: 1.23x faster                                                             |
| docutils                 | 1.95 sec                                                        | 1.65 sec: 1.18x faster                                                           |
| logging_format           | 7.91 us                                                         | 6.69 us: 1.18x faster                                                            |
| logging_simple           | 7.29 us                                                         | 6.19 us: 1.18x faster                                                            |
| xml_etree_iterparse      | 70.8 ms                                                         | 61.7 ms: 1.15x faster                                                            |
| meteor_contest           | 80.0 ms                                                         | 71.1 ms: 1.13x faster                                                            |
| telco                    | 4.83 ms                                                         | 4.30 ms: 1.12x faster                                                            |
| regex_dna                | 131 ms                                                          | 118 ms: 1.11x faster                                                             |
| regex_v8                 | 15.8 ms                                                         | 14.3 ms: 1.10x faster                                                            |
| regex_effbot             | 1.66 ms                                                         | 1.58 ms: 1.05x faster                                                            |
| async_generators         | 241 ms                                                          | 243 ms: 1.01x slower                                                             |
| python_startup_no_site   | 18.1 ms                                                         | 19.5 ms: 1.08x slower                                                            |
| coverage                 | 46.6 ms                                                         | 50.6 ms: 1.09x slower                                                            |
| python_startup           | 22.9 ms                                                         | 25.6 ms: 1.12x slower                                                            |
| gc_traversal             | 1.28 ms                                                         | 2.11 ms: 1.65x slower                                                            |
| create_gc_cycles         | 694 us                                                          | 1.31 ms: 1.89x slower                                                            |
| Geometric mean           | (ref)                                                           | 1.49x faster                                                                     |
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250707-3.15.0a0-0240ef4-JIT/bm-20250707-pythonperf1_win32-amd64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.486x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.44x
- 95% likely to have a speedup of 1.42x
- 99% likely to have a speedup of 1.40x

# Memory
- memory change: unknown