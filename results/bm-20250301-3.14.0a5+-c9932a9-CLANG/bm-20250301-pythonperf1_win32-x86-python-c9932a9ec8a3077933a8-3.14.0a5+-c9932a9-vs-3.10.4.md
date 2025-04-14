# Results vs. 3.10.4

- fork: python
- ref: c9932a9ec8a3077933a8
- machine: windows-x86
- commit hash: c9932a9
- commit date: 2025-03-01
- overall geometric mean: 1.211x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250301-pythonperf1_win32-x86-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 251 ms: 1.06x faster                                                            |
| docutils       | 1.95 sec                                                        | 1.79 sec: 1.09x faster                                                          |
| html5lib       | 52.1 ms                                                         | 43.6 ms: 1.19x faster                                                           |
| Geometric mean | (ref)                                                           | 1.11x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250301-pythonperf1_win32-x86-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io           | 940 ms                                                          | 409 ms: 2.30x faster                                                            |
| async_tree_none         | 394 ms                                                          | 188 ms: 2.09x faster                                                            |
| async_tree_cpu_io_mixed | 922 ms                                                          | 441 ms: 2.09x faster                                                            |
| async_tree_memoization  | 467 ms                                                          | 227 ms: 2.06x faster                                                            |
| Geometric mean          | (ref)                                                           | 2.13x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250301-pythonperf1_win32-x86-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 216 ms: 2.32x faster                                                            |
| float          | 69.6 ms                                                         | 48.8 ms: 1.43x faster                                                           |
| nbody          | 79.1 ms                                                         | 73.5 ms: 1.08x faster                                                           |
| Geometric mean | (ref)                                                           | 1.53x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250301-pythonperf1_win32-x86-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 98.4 ms: 1.19x faster                                                           |
| regex_dna      | 131 ms                                                          | 127 ms: 1.03x faster                                                            |
| regex_v8       | 15.8 ms                                                         | 17.3 ms: 1.10x slower                                                           |
| regex_effbot   | 1.66 ms                                                         | 1.93 ms: 1.16x slower                                                           |
| Geometric mean | (ref)                                                           | 1.01x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250301-pythonperf1_win32-x86-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 7.60 ms: 1.29x faster                                                           |
| tomli_loads          | 1.91 sec                                                        | 1.57 sec: 1.21x faster                                                          |
| pickle_list          | 3.22 us                                                         | 2.68 us: 1.20x faster                                                           |
| unpickle_pure_python | 189 us                                                          | 166 us: 1.14x faster                                                            |
| pickle_dict          | 18.2 us                                                         | 16.1 us: 1.13x faster                                                           |
| pickle_pure_python   | 280 us                                                          | 248 us: 1.13x faster                                                            |
| unpickle_list        | 2.98 us                                                         | 2.66 us: 1.12x faster                                                           |
| xml_etree_parse      | 120 ms                                                          | 113 ms: 1.07x faster                                                            |
| json_loads           | 22.4 us                                                         | 21.5 us: 1.04x faster                                                           |
| xml_etree_process    | 48.1 ms                                                         | 48.9 ms: 1.02x slower                                                           |
| pickle               | 7.83 us                                                         | 8.03 us: 1.03x slower                                                           |
| xml_etree_iterparse  | 70.8 ms                                                         | 72.8 ms: 1.03x slower                                                           |
| unpickle             | 9.82 us                                                         | 10.3 us: 1.05x slower                                                           |
| xml_etree_generate   | 61.6 ms                                                         | 69.5 ms: 1.13x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.07x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250301-pythonperf1_win32-x86-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 22.6 ms: 1.25x slower                                                           |
| python_startup         | 22.9 ms                                                         | 29.6 ms: 1.29x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.27x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250301-pythonperf1_win32-x86-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| django_template | 36.0 ms                                                         | 30.5 ms: 1.18x faster                                                           |
| genshi_text     | 21.0 ms                                                         | 18.2 ms: 1.15x faster                                                           |
| genshi_xml      | 46.6 ms                                                         | 41.6 ms: 1.12x faster                                                           |
| mako            | 9.10 ms                                                         | 8.31 ms: 1.10x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.14x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250301-pythonperf1_win32-x86-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 130 us: 3.04x faster                                                            |
| pidigits                 | 502 ms                                                          | 216 ms: 2.32x faster                                                            |
| pathlib                  | 81.2 ms                                                         | 35.1 ms: 2.32x faster                                                           |
| async_tree_io            | 940 ms                                                          | 409 ms: 2.30x faster                                                            |
| async_tree_none          | 394 ms                                                          | 188 ms: 2.09x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 441 ms: 2.09x faster                                                            |
| async_tree_memoization   | 467 ms                                                          | 227 ms: 2.06x faster                                                            |
| pylint                   | 384 ms                                                          | 214 ms: 1.80x faster                                                            |
| deltablue                | 4.04 ms                                                         | 2.28 ms: 1.77x faster                                                           |
| generators               | 31.6 ms                                                         | 19.6 ms: 1.61x faster                                                           |
| go                       | 146 ms                                                          | 90.7 ms: 1.61x faster                                                           |
| chaos                    | 74.4 ms                                                         | 49.8 ms: 1.49x faster                                                           |
| deepcopy                 | 310 us                                                          | 212 us: 1.46x faster                                                            |
| deepcopy_memo            | 29.6 us                                                         | 20.4 us: 1.45x faster                                                           |
| logging_silent           | 97.9 ns                                                         | 67.9 ns: 1.44x faster                                                           |
| float                    | 69.6 ms                                                         | 48.8 ms: 1.43x faster                                                           |
| scimark_sor              | 115 ms                                                          | 81.4 ms: 1.41x faster                                                           |
| raytrace                 | 303 ms                                                          | 214 ms: 1.41x faster                                                            |
| sqlglot_parse            | 1.33 ms                                                         | 961 us: 1.38x faster                                                            |
| scimark_monte_carlo      | 61.9 ms                                                         | 45.3 ms: 1.37x faster                                                           |
| comprehensions           | 17.7 us                                                         | 13.3 us: 1.34x faster                                                           |
| thrift                   | 902 us                                                          | 678 us: 1.33x faster                                                            |
| asyncio_tcp              | 744 ms                                                          | 560 ms: 1.33x faster                                                            |
| sqlglot_transpile        | 1.58 ms                                                         | 1.20 ms: 1.32x faster                                                           |
| pyflate                  | 422 ms                                                          | 324 ms: 1.30x faster                                                            |
| scimark_lu               | 89.8 ms                                                         | 69.2 ms: 1.30x faster                                                           |
| json_dumps               | 9.82 ms                                                         | 7.60 ms: 1.29x faster                                                           |
| crypto_pyaes             | 81.3 ms                                                         | 63.3 ms: 1.28x faster                                                           |
| spectral_norm            | 80.2 ms                                                         | 62.5 ms: 1.28x faster                                                           |
| hexiom                   | 6.13 ms                                                         | 4.79 ms: 1.28x faster                                                           |
| deepcopy_reduce          | 2.68 us                                                         | 2.10 us: 1.28x faster                                                           |
| pycparser                | 1.04 sec                                                        | 823 ms: 1.27x faster                                                            |
| sqlite_synth             | 2.29 us                                                         | 1.87 us: 1.22x faster                                                           |
| richards_super           | 49.9 ms                                                         | 41.0 ms: 1.22x faster                                                           |
| tomli_loads              | 1.91 sec                                                        | 1.57 sec: 1.21x faster                                                          |
| dulwich_log              | 58.5 ms                                                         | 48.6 ms: 1.20x faster                                                           |
| sympy_sum                | 122 ms                                                          | 102 ms: 1.20x faster                                                            |
| pickle_list              | 3.22 us                                                         | 2.68 us: 1.20x faster                                                           |
| coroutines               | 17.9 ms                                                         | 15.0 ms: 1.20x faster                                                           |
| html5lib                 | 52.1 ms                                                         | 43.6 ms: 1.19x faster                                                           |
| regex_compile            | 117 ms                                                          | 98.4 ms: 1.19x faster                                                           |
| django_template          | 36.0 ms                                                         | 30.5 ms: 1.18x faster                                                           |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.76 ms: 1.17x faster                                                           |
| pprint_pformat           | 1.37 sec                                                        | 1.17 sec: 1.17x faster                                                          |
| pprint_safe_repr         | 658 ms                                                          | 567 ms: 1.16x faster                                                            |
| genshi_text              | 21.0 ms                                                         | 18.2 ms: 1.15x faster                                                           |
| sympy_str                | 229 ms                                                          | 199 ms: 1.15x faster                                                            |
| nqueens                  | 87.1 ms                                                         | 75.7 ms: 1.15x faster                                                           |
| sympy_expand             | 391 ms                                                          | 342 ms: 1.14x faster                                                            |
| unpickle_pure_python     | 189 us                                                          | 166 us: 1.14x faster                                                            |
| pickle_dict              | 18.2 us                                                         | 16.1 us: 1.13x faster                                                           |
| sympy_integrate          | 16.6 ms                                                         | 14.7 ms: 1.13x faster                                                           |
| pickle_pure_python       | 280 us                                                          | 248 us: 1.13x faster                                                            |
| unpickle_list            | 2.98 us                                                         | 2.66 us: 1.12x faster                                                           |
| genshi_xml               | 46.6 ms                                                         | 41.6 ms: 1.12x faster                                                           |
| richards                 | 40.3 ms                                                         | 36.6 ms: 1.10x faster                                                           |
| mako                     | 9.10 ms                                                         | 8.31 ms: 1.10x faster                                                           |
| json                     | 4.76 ms                                                         | 4.36 ms: 1.09x faster                                                           |
| docutils                 | 1.95 sec                                                        | 1.79 sec: 1.09x faster                                                          |
| sqlglot_normalize        | 230 ms                                                          | 212 ms: 1.09x faster                                                            |
| sqlglot_optimize         | 44.7 ms                                                         | 41.5 ms: 1.08x faster                                                           |
| nbody                    | 79.1 ms                                                         | 73.5 ms: 1.08x faster                                                           |
| xml_etree_parse          | 120 ms                                                          | 113 ms: 1.07x faster                                                            |
| 2to3                     | 265 ms                                                          | 251 ms: 1.06x faster                                                            |
| fannkuch                 | 317 ms                                                          | 302 ms: 1.05x faster                                                            |
| json_loads               | 22.4 us                                                         | 21.5 us: 1.04x faster                                                           |
| regex_dna                | 131 ms                                                          | 127 ms: 1.03x faster                                                            |
| scimark_fft              | 216 ms                                                          | 211 ms: 1.03x faster                                                            |
| mdp                      | 1.83 sec                                                        | 1.80 sec: 1.01x faster                                                          |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 17.1 sec: 1.01x slower                                                          |
| xml_etree_process        | 48.1 ms                                                         | 48.9 ms: 1.02x slower                                                           |
| meteor_contest           | 80.0 ms                                                         | 81.9 ms: 1.02x slower                                                           |
| pickle                   | 7.83 us                                                         | 8.03 us: 1.03x slower                                                           |
| async_generators         | 241 ms                                                          | 247 ms: 1.03x slower                                                            |
| xml_etree_iterparse      | 70.8 ms                                                         | 72.8 ms: 1.03x slower                                                           |
| unpack_sequence          | 40.0 ns                                                         | 41.7 ns: 1.04x slower                                                           |
| unpickle                 | 9.82 us                                                         | 10.3 us: 1.05x slower                                                           |
| logging_format           | 7.91 us                                                         | 8.37 us: 1.06x slower                                                           |
| logging_simple           | 7.29 us                                                         | 7.88 us: 1.08x slower                                                           |
| regex_v8                 | 15.8 ms                                                         | 17.3 ms: 1.10x slower                                                           |
| xml_etree_generate       | 61.6 ms                                                         | 69.5 ms: 1.13x slower                                                           |
| regex_effbot             | 1.66 ms                                                         | 1.93 ms: 1.16x slower                                                           |
| bench_thread_pool        | 1.12 ms                                                         | 1.33 ms: 1.19x slower                                                           |
| coverage                 | 46.6 ms                                                         | 57.6 ms: 1.24x slower                                                           |
| telco                    | 4.83 ms                                                         | 6.01 ms: 1.24x slower                                                           |
| python_startup_no_site   | 18.1 ms                                                         | 22.6 ms: 1.25x slower                                                           |
| python_startup           | 22.9 ms                                                         | 29.6 ms: 1.29x slower                                                           |
| bench_mp_pool            | 66.4 ms                                                         | 94.5 ms: 1.42x slower                                                           |
| create_gc_cycles         | 694 us                                                          | 1.16 ms: 1.68x slower                                                           |
| gc_traversal             | 1.28 ms                                                         | 2.44 ms: 1.90x slower                                                           |
| Geometric mean           | (ref)                                                           | 1.19x faster                                                                    |
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (12) of results/bm-20250301-3.14.0a5+-c9932a9-CLANG/bm-20250301-pythonperf1_win32-x86-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.211x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.15x
- 95% likely to have a speedup of 1.14x
- 99% likely to have a speedup of 1.11x

# Memory
- memory change: unknown