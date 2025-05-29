# Results vs. 3.10.4

- fork: python
- ref: a3990df6121880e8c678
- machine: windows-x86
- commit hash: a3990df
- commit date: 2025-03-08
- overall geometric mean: 1.196x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250308-pythonperf1_win32-x86-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 252 ms: 1.05x faster                                                            |
| docutils       | 1.95 sec                                                        | 1.82 sec: 1.07x faster                                                          |
| html5lib       | 52.1 ms                                                         | 44.5 ms: 1.17x faster                                                           |
| Geometric mean | (ref)                                                           | 1.10x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250308-pythonperf1_win32-x86-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io           | 940 ms                                                          | 420 ms: 2.24x faster                                                            |
| async_tree_none         | 394 ms                                                          | 193 ms: 2.04x faster                                                            |
| async_tree_cpu_io_mixed | 922 ms                                                          | 457 ms: 2.02x faster                                                            |
| async_tree_memoization  | 467 ms                                                          | 235 ms: 1.99x faster                                                            |
| Geometric mean          | (ref)                                                           | 2.07x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250308-pythonperf1_win32-x86-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 219 ms: 2.29x faster                                                            |
| float          | 69.6 ms                                                         | 48.9 ms: 1.42x faster                                                           |
| nbody          | 79.1 ms                                                         | 72.8 ms: 1.09x faster                                                           |
| Geometric mean | (ref)                                                           | 1.53x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250308-pythonperf1_win32-x86-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 99.1 ms: 1.18x faster                                                           |
| regex_dna      | 131 ms                                                          | 128 ms: 1.02x faster                                                            |
| regex_v8       | 15.8 ms                                                         | 17.3 ms: 1.10x slower                                                           |
| regex_effbot   | 1.66 ms                                                         | 1.95 ms: 1.18x slower                                                           |
| Geometric mean | (ref)                                                           | 1.02x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250308-pythonperf1_win32-x86-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 1.91 sec                                                        | 1.57 sec: 1.22x faster                                                          |
| json_dumps           | 9.82 ms                                                         | 8.13 ms: 1.21x faster                                                           |
| pickle_list          | 3.22 us                                                         | 2.72 us: 1.18x faster                                                           |
| pickle_dict          | 18.2 us                                                         | 15.7 us: 1.16x faster                                                           |
| unpickle_list        | 2.98 us                                                         | 2.60 us: 1.15x faster                                                           |
| unpickle_pure_python | 189 us                                                          | 166 us: 1.14x faster                                                            |
| pickle_pure_python   | 280 us                                                          | 256 us: 1.10x faster                                                            |
| json_loads           | 22.4 us                                                         | 21.5 us: 1.04x faster                                                           |
| xml_etree_parse      | 120 ms                                                          | 115 ms: 1.04x faster                                                            |
| xml_etree_iterparse  | 70.8 ms                                                         | 73.5 ms: 1.04x slower                                                           |
| xml_etree_process    | 48.1 ms                                                         | 50.4 ms: 1.05x slower                                                           |
| unpickle             | 9.82 us                                                         | 10.5 us: 1.07x slower                                                           |
| pickle               | 7.83 us                                                         | 8.47 us: 1.08x slower                                                           |
| xml_etree_generate   | 61.6 ms                                                         | 72.2 ms: 1.17x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.06x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250308-pythonperf1_win32-x86-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 29.5 ms: 1.29x slower                                                           |
| python_startup_no_site | 18.1 ms                                                         | 23.5 ms: 1.30x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.29x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250308-pythonperf1_win32-x86-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 21.0 ms                                                         | 17.9 ms: 1.17x faster                                                           |
| genshi_xml      | 46.6 ms                                                         | 40.7 ms: 1.14x faster                                                           |
| django_template | 36.0 ms                                                         | 32.2 ms: 1.12x faster                                                           |
| mako            | 9.10 ms                                                         | 8.68 ms: 1.05x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.12x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250308-pythonperf1_win32-x86-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 137 us: 2.89x faster                                                            |
| pathlib                  | 81.2 ms                                                         | 35.2 ms: 2.31x faster                                                           |
| pidigits                 | 502 ms                                                          | 219 ms: 2.29x faster                                                            |
| async_tree_io            | 940 ms                                                          | 420 ms: 2.24x faster                                                            |
| async_tree_none          | 394 ms                                                          | 193 ms: 2.04x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 457 ms: 2.02x faster                                                            |
| async_tree_memoization   | 467 ms                                                          | 235 ms: 1.99x faster                                                            |
| deltablue                | 4.04 ms                                                         | 2.28 ms: 1.77x faster                                                           |
| pylint                   | 384 ms                                                          | 217 ms: 1.77x faster                                                            |
| go                       | 146 ms                                                          | 92.0 ms: 1.58x faster                                                           |
| generators               | 31.6 ms                                                         | 20.4 ms: 1.54x faster                                                           |
| chaos                    | 74.4 ms                                                         | 49.5 ms: 1.50x faster                                                           |
| deepcopy_memo            | 29.6 us                                                         | 20.5 us: 1.45x faster                                                           |
| deepcopy                 | 310 us                                                          | 215 us: 1.44x faster                                                            |
| scimark_sor              | 115 ms                                                          | 80.7 ms: 1.43x faster                                                           |
| float                    | 69.6 ms                                                         | 48.9 ms: 1.42x faster                                                           |
| logging_silent           | 97.9 ns                                                         | 69.0 ns: 1.42x faster                                                           |
| raytrace                 | 303 ms                                                          | 215 ms: 1.40x faster                                                            |
| sqlglot_parse            | 1.33 ms                                                         | 977 us: 1.36x faster                                                            |
| scimark_monte_carlo      | 61.9 ms                                                         | 45.8 ms: 1.35x faster                                                           |
| comprehensions           | 17.7 us                                                         | 13.3 us: 1.34x faster                                                           |
| thrift                   | 902 us                                                          | 681 us: 1.33x faster                                                            |
| sqlglot_transpile        | 1.58 ms                                                         | 1.22 ms: 1.30x faster                                                           |
| pyflate                  | 422 ms                                                          | 327 ms: 1.29x faster                                                            |
| coroutines               | 17.9 ms                                                         | 14.1 ms: 1.27x faster                                                           |
| hexiom                   | 6.13 ms                                                         | 4.86 ms: 1.26x faster                                                           |
| crypto_pyaes             | 81.3 ms                                                         | 64.6 ms: 1.26x faster                                                           |
| scimark_lu               | 89.8 ms                                                         | 72.2 ms: 1.24x faster                                                           |
| pycparser                | 1.04 sec                                                        | 841 ms: 1.24x faster                                                            |
| unpack_sequence          | 40.0 ns                                                         | 32.4 ns: 1.24x faster                                                           |
| dulwich_log              | 58.5 ms                                                         | 48.0 ms: 1.22x faster                                                           |
| tomli_loads              | 1.91 sec                                                        | 1.57 sec: 1.22x faster                                                          |
| spectral_norm            | 80.2 ms                                                         | 66.0 ms: 1.22x faster                                                           |
| json_dumps               | 9.82 ms                                                         | 8.13 ms: 1.21x faster                                                           |
| sqlite_synth             | 2.29 us                                                         | 1.90 us: 1.21x faster                                                           |
| nqueens                  | 87.1 ms                                                         | 72.2 ms: 1.21x faster                                                           |
| sympy_sum                | 122 ms                                                          | 102 ms: 1.20x faster                                                            |
| deepcopy_reduce          | 2.68 us                                                         | 2.24 us: 1.20x faster                                                           |
| pickle_list              | 3.22 us                                                         | 2.72 us: 1.18x faster                                                           |
| richards_super           | 49.9 ms                                                         | 42.3 ms: 1.18x faster                                                           |
| regex_compile            | 117 ms                                                          | 99.1 ms: 1.18x faster                                                           |
| genshi_text              | 21.0 ms                                                         | 17.9 ms: 1.17x faster                                                           |
| html5lib                 | 52.1 ms                                                         | 44.5 ms: 1.17x faster                                                           |
| pprint_pformat           | 1.37 sec                                                        | 1.17 sec: 1.17x faster                                                          |
| pickle_dict              | 18.2 us                                                         | 15.7 us: 1.16x faster                                                           |
| asyncio_tcp              | 744 ms                                                          | 644 ms: 1.15x faster                                                            |
| pprint_safe_repr         | 658 ms                                                          | 572 ms: 1.15x faster                                                            |
| unpickle_list            | 2.98 us                                                         | 2.60 us: 1.15x faster                                                           |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.82 ms: 1.15x faster                                                           |
| genshi_xml               | 46.6 ms                                                         | 40.7 ms: 1.14x faster                                                           |
| sympy_expand             | 391 ms                                                          | 343 ms: 1.14x faster                                                            |
| sympy_str                | 229 ms                                                          | 201 ms: 1.14x faster                                                            |
| unpickle_pure_python     | 189 us                                                          | 166 us: 1.14x faster                                                            |
| django_template          | 36.0 ms                                                         | 32.2 ms: 1.12x faster                                                           |
| sympy_integrate          | 16.6 ms                                                         | 15.0 ms: 1.11x faster                                                           |
| json                     | 4.76 ms                                                         | 4.32 ms: 1.10x faster                                                           |
| pickle_pure_python       | 280 us                                                          | 256 us: 1.10x faster                                                            |
| nbody                    | 79.1 ms                                                         | 72.8 ms: 1.09x faster                                                           |
| richards                 | 40.3 ms                                                         | 37.4 ms: 1.08x faster                                                           |
| docutils                 | 1.95 sec                                                        | 1.82 sec: 1.07x faster                                                          |
| sqlglot_optimize         | 44.7 ms                                                         | 42.2 ms: 1.06x faster                                                           |
| sqlglot_normalize        | 230 ms                                                          | 219 ms: 1.05x faster                                                            |
| 2to3                     | 265 ms                                                          | 252 ms: 1.05x faster                                                            |
| mako                     | 9.10 ms                                                         | 8.68 ms: 1.05x faster                                                           |
| fannkuch                 | 317 ms                                                          | 303 ms: 1.05x faster                                                            |
| json_loads               | 22.4 us                                                         | 21.5 us: 1.04x faster                                                           |
| xml_etree_parse          | 120 ms                                                          | 115 ms: 1.04x faster                                                            |
| regex_dna                | 131 ms                                                          | 128 ms: 1.02x faster                                                            |
| scimark_fft              | 216 ms                                                          | 215 ms: 1.01x faster                                                            |
| mdp                      | 1.83 sec                                                        | 1.84 sec: 1.01x slower                                                          |
| meteor_contest           | 80.0 ms                                                         | 81.6 ms: 1.02x slower                                                           |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 17.4 sec: 1.03x slower                                                          |
| async_generators         | 241 ms                                                          | 249 ms: 1.03x slower                                                            |
| xml_etree_iterparse      | 70.8 ms                                                         | 73.5 ms: 1.04x slower                                                           |
| xml_etree_process        | 48.1 ms                                                         | 50.4 ms: 1.05x slower                                                           |
| bench_thread_pool        | 1.12 ms                                                         | 1.18 ms: 1.06x slower                                                           |
| unpickle                 | 9.82 us                                                         | 10.5 us: 1.07x slower                                                           |
| logging_format           | 7.91 us                                                         | 8.49 us: 1.07x slower                                                           |
| pickle                   | 7.83 us                                                         | 8.47 us: 1.08x slower                                                           |
| logging_simple           | 7.29 us                                                         | 7.89 us: 1.08x slower                                                           |
| regex_v8                 | 15.8 ms                                                         | 17.3 ms: 1.10x slower                                                           |
| xml_etree_generate       | 61.6 ms                                                         | 72.2 ms: 1.17x slower                                                           |
| regex_effbot             | 1.66 ms                                                         | 1.95 ms: 1.18x slower                                                           |
| coverage                 | 46.6 ms                                                         | 56.3 ms: 1.21x slower                                                           |
| python_startup           | 22.9 ms                                                         | 29.5 ms: 1.29x slower                                                           |
| telco                    | 4.83 ms                                                         | 6.23 ms: 1.29x slower                                                           |
| python_startup_no_site   | 18.1 ms                                                         | 23.5 ms: 1.30x slower                                                           |
| bench_mp_pool            | 66.4 ms                                                         | 96.0 ms: 1.45x slower                                                           |
| create_gc_cycles         | 694 us                                                          | 1.20 ms: 1.73x slower                                                           |
| gc_traversal             | 1.28 ms                                                         | 2.44 ms: 1.91x slower                                                           |
| Geometric mean           | (ref)                                                           | 1.18x faster                                                                    |
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (12) of results/bm-20250308-3.14.0a5+-a3990df-CLANG/bm-20250308-pythonperf1_win32-x86-python-a3990df6121880e8c678-3.14.0a5+-a3990df.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.196x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.14x
- 95% likely to have a speedup of 1.13x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: unknown