# Results vs. 3.10.4

- fork: python
- ref: e82c2ca2a59235bc1965
- machine: windows-x86
- commit hash: e82c2ca
- commit date: 2025-03-15
- overall geometric mean: 1.112x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.03x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250315-pythonperf1_win32-x86-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 264 ms: 1.01x faster                                                            |
| docutils       | 1.95 sec                                                        | 1.88 sec: 1.04x faster                                                          |
| html5lib       | 52.1 ms                                                         | 48.8 ms: 1.07x faster                                                           |
| Geometric mean | (ref)                                                           | 1.04x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250315-pythonperf1_win32-x86-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io           | 940 ms                                                          | 481 ms: 1.96x faster                                                            |
| async_tree_cpu_io_mixed | 922 ms                                                          | 481 ms: 1.92x faster                                                            |
| async_tree_none         | 394 ms                                                          | 224 ms: 1.75x faster                                                            |
| async_tree_memoization  | 467 ms                                                          | 269 ms: 1.73x faster                                                            |
| Geometric mean          | (ref)                                                           | 1.84x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250315-pythonperf1_win32-x86-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 204 ms: 2.46x faster                                                            |
| float          | 69.6 ms                                                         | 54.9 ms: 1.27x faster                                                           |
| nbody          | 79.1 ms                                                         | 82.5 ms: 1.04x slower                                                           |
| Geometric mean | (ref)                                                           | 1.44x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250315-pythonperf1_win32-x86-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 109 ms: 1.07x faster                                                            |
| regex_effbot   | 1.66 ms                                                         | 1.59 ms: 1.05x faster                                                           |
| regex_dna      | 131 ms                                                          | 126 ms: 1.04x faster                                                            |
| regex_v8       | 15.8 ms                                                         | 15.3 ms: 1.03x faster                                                           |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250315-pythonperf1_win32-x86-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 8.48 ms: 1.16x faster                                                           |
| xml_etree_parse      | 120 ms                                                          | 108 ms: 1.11x faster                                                            |
| tomli_loads          | 1.91 sec                                                        | 1.78 sec: 1.07x faster                                                          |
| xml_etree_iterparse  | 70.8 ms                                                         | 66.3 ms: 1.07x faster                                                           |
| unpickle_pure_python | 189 us                                                          | 182 us: 1.04x faster                                                            |
| json_loads           | 22.4 us                                                         | 22.2 us: 1.01x faster                                                           |
| unpickle_list        | 2.98 us                                                         | 3.04 us: 1.02x slower                                                           |
| pickle_pure_python   | 280 us                                                          | 291 us: 1.04x slower                                                            |
| xml_etree_process    | 48.1 ms                                                         | 53.3 ms: 1.11x slower                                                           |
| unpickle             | 9.82 us                                                         | 11.2 us: 1.14x slower                                                           |
| pickle_dict          | 18.2 us                                                         | 21.3 us: 1.17x slower                                                           |
| pickle               | 7.83 us                                                         | 9.14 us: 1.17x slower                                                           |
| xml_etree_generate   | 61.6 ms                                                         | 72.2 ms: 1.17x slower                                                           |
| pickle_list          | 3.22 us                                                         | 3.90 us: 1.21x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.04x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250315-pythonperf1_win32-x86-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 22.8 ms: 1.26x slower                                                           |
| python_startup         | 22.9 ms                                                         | 29.0 ms: 1.26x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.26x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250315-pythonperf1_win32-x86-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 8.18 ms: 1.11x faster                                                           |
| django_template | 36.0 ms                                                         | 35.4 ms: 1.02x faster                                                           |
| genshi_text     | 21.0 ms                                                         | 23.9 ms: 1.14x slower                                                           |
| genshi_xml      | 46.6 ms                                                         | 54.3 ms: 1.16x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.04x slower                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250315-pythonperf1_win32-x86-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 150 us: 2.63x faster                                                            |
| pidigits                 | 502 ms                                                          | 204 ms: 2.46x faster                                                            |
| pathlib                  | 81.2 ms                                                         | 37.9 ms: 2.14x faster                                                           |
| async_tree_io            | 940 ms                                                          | 481 ms: 1.96x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 481 ms: 1.92x faster                                                            |
| async_tree_none          | 394 ms                                                          | 224 ms: 1.75x faster                                                            |
| async_tree_memoization   | 467 ms                                                          | 269 ms: 1.73x faster                                                            |
| pylint                   | 384 ms                                                          | 231 ms: 1.66x faster                                                            |
| logging_silent           | 97.9 ns                                                         | 67.3 ns: 1.45x faster                                                           |
| deltablue                | 4.04 ms                                                         | 2.79 ms: 1.45x faster                                                           |
| deepcopy_memo            | 29.6 us                                                         | 21.5 us: 1.38x faster                                                           |
| scimark_lu               | 89.8 ms                                                         | 66.4 ms: 1.35x faster                                                           |
| go                       | 146 ms                                                          | 111 ms: 1.31x faster                                                            |
| float                    | 69.6 ms                                                         | 54.9 ms: 1.27x faster                                                           |
| generators               | 31.6 ms                                                         | 25.0 ms: 1.26x faster                                                           |
| deepcopy                 | 310 us                                                          | 249 us: 1.24x faster                                                            |
| scimark_sor              | 115 ms                                                          | 93.5 ms: 1.23x faster                                                           |
| crypto_pyaes             | 81.3 ms                                                         | 66.1 ms: 1.23x faster                                                           |
| chaos                    | 74.4 ms                                                         | 60.9 ms: 1.22x faster                                                           |
| comprehensions           | 17.7 us                                                         | 14.7 us: 1.21x faster                                                           |
| pyflate                  | 422 ms                                                          | 357 ms: 1.18x faster                                                            |
| hexiom                   | 6.13 ms                                                         | 5.21 ms: 1.18x faster                                                           |
| sqlite_synth             | 2.29 us                                                         | 1.95 us: 1.17x faster                                                           |
| richards_super           | 49.9 ms                                                         | 42.7 ms: 1.17x faster                                                           |
| scimark_monte_carlo      | 61.9 ms                                                         | 53.1 ms: 1.17x faster                                                           |
| json_dumps               | 9.82 ms                                                         | 8.48 ms: 1.16x faster                                                           |
| thrift                   | 902 us                                                          | 779 us: 1.16x faster                                                            |
| asyncio_tcp              | 744 ms                                                          | 646 ms: 1.15x faster                                                            |
| raytrace                 | 303 ms                                                          | 266 ms: 1.14x faster                                                            |
| dulwich_log              | 58.5 ms                                                         | 52.1 ms: 1.12x faster                                                           |
| mako                     | 9.10 ms                                                         | 8.18 ms: 1.11x faster                                                           |
| xml_etree_parse          | 120 ms                                                          | 108 ms: 1.11x faster                                                            |
| pycparser                | 1.04 sec                                                        | 939 ms: 1.11x faster                                                            |
| sympy_sum                | 122 ms                                                          | 111 ms: 1.10x faster                                                            |
| spectral_norm            | 80.2 ms                                                         | 72.9 ms: 1.10x faster                                                           |
| coroutines               | 17.9 ms                                                         | 16.6 ms: 1.08x faster                                                           |
| richards                 | 40.3 ms                                                         | 37.5 ms: 1.07x faster                                                           |
| regex_compile            | 117 ms                                                          | 109 ms: 1.07x faster                                                            |
| tomli_loads              | 1.91 sec                                                        | 1.78 sec: 1.07x faster                                                          |
| xml_etree_iterparse      | 70.8 ms                                                         | 66.3 ms: 1.07x faster                                                           |
| mdp                      | 1.83 sec                                                        | 1.71 sec: 1.07x faster                                                          |
| html5lib                 | 52.1 ms                                                         | 48.8 ms: 1.07x faster                                                           |
| regex_effbot             | 1.66 ms                                                         | 1.59 ms: 1.05x faster                                                           |
| unpickle_pure_python     | 189 us                                                          | 182 us: 1.04x faster                                                            |
| regex_dna                | 131 ms                                                          | 126 ms: 1.04x faster                                                            |
| docutils                 | 1.95 sec                                                        | 1.88 sec: 1.04x faster                                                          |
| nqueens                  | 87.1 ms                                                         | 84.6 ms: 1.03x faster                                                           |
| sympy_integrate          | 16.6 ms                                                         | 16.2 ms: 1.03x faster                                                           |
| regex_v8                 | 15.8 ms                                                         | 15.3 ms: 1.03x faster                                                           |
| sympy_str                | 229 ms                                                          | 225 ms: 1.02x faster                                                            |
| django_template          | 36.0 ms                                                         | 35.4 ms: 1.02x faster                                                           |
| unpack_sequence          | 40.0 ns                                                         | 39.7 ns: 1.01x faster                                                           |
| json_loads               | 22.4 us                                                         | 22.2 us: 1.01x faster                                                           |
| 2to3                     | 265 ms                                                          | 264 ms: 1.01x faster                                                            |
| fannkuch                 | 317 ms                                                          | 321 ms: 1.01x slower                                                            |
| pprint_safe_repr         | 658 ms                                                          | 667 ms: 1.01x slower                                                            |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 17.3 sec: 1.02x slower                                                          |
| unpickle_list            | 2.98 us                                                         | 3.04 us: 1.02x slower                                                           |
| deepcopy_reduce          | 2.68 us                                                         | 2.74 us: 1.02x slower                                                           |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.32 ms: 1.02x slower                                                           |
| sympy_expand             | 391 ms                                                          | 401 ms: 1.03x slower                                                            |
| pickle_pure_python       | 280 us                                                          | 291 us: 1.04x slower                                                            |
| nbody                    | 79.1 ms                                                         | 82.5 ms: 1.04x slower                                                           |
| meteor_contest           | 80.0 ms                                                         | 84.9 ms: 1.06x slower                                                           |
| scimark_fft              | 216 ms                                                          | 231 ms: 1.07x slower                                                            |
| xml_etree_process        | 48.1 ms                                                         | 53.3 ms: 1.11x slower                                                           |
| genshi_text              | 21.0 ms                                                         | 23.9 ms: 1.14x slower                                                           |
| unpickle                 | 9.82 us                                                         | 11.2 us: 1.14x slower                                                           |
| coverage                 | 46.6 ms                                                         | 53.3 ms: 1.14x slower                                                           |
| bench_thread_pool        | 1.12 ms                                                         | 1.29 ms: 1.15x slower                                                           |
| genshi_xml               | 46.6 ms                                                         | 54.3 ms: 1.16x slower                                                           |
| pickle_dict              | 18.2 us                                                         | 21.3 us: 1.17x slower                                                           |
| pickle                   | 7.83 us                                                         | 9.14 us: 1.17x slower                                                           |
| xml_etree_generate       | 61.6 ms                                                         | 72.2 ms: 1.17x slower                                                           |
| logging_simple           | 7.29 us                                                         | 8.79 us: 1.21x slower                                                           |
| pickle_list              | 3.22 us                                                         | 3.90 us: 1.21x slower                                                           |
| logging_format           | 7.91 us                                                         | 9.67 us: 1.22x slower                                                           |
| python_startup_no_site   | 18.1 ms                                                         | 22.8 ms: 1.26x slower                                                           |
| python_startup           | 22.9 ms                                                         | 29.0 ms: 1.26x slower                                                           |
| async_generators         | 241 ms                                                          | 311 ms: 1.29x slower                                                            |
| gc_traversal             | 1.28 ms                                                         | 1.81 ms: 1.41x slower                                                           |
| telco                    | 4.83 ms                                                         | 6.92 ms: 1.43x slower                                                           |
| bench_mp_pool            | 66.4 ms                                                         | 96.0 ms: 1.45x slower                                                           |
| create_gc_cycles         | 694 us                                                          | 1.06 ms: 1.53x slower                                                           |
| Geometric mean           | (ref)                                                           | 1.09x faster                                                                    |

Benchmark hidden because not significant (2): json, pprint_pformat
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250315-3.14.0a6+-e82c2ca/bm-20250315-pythonperf1_win32-x86-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.112x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: unknown