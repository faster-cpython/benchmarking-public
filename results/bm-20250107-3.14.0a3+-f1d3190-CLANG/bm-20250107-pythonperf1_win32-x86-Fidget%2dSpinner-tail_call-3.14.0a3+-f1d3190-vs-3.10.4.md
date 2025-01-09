# Results vs. 3.10.4

- fork: Fidget-Spinner
- ref: tail_call
- machine: windows-x86
- commit hash: f1d3190
- commit date: 2025-01-07
- overall geometric mean: 1.064x faster
- HPT reliability: 97.06%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf1_win32-x86-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 277 ms: 1.05x slower                                                           |
| html5lib       | 52.1 ms                                                         | 48.9 ms: 1.06x faster                                                          |
| Geometric mean | (ref)                                                           | 1.01x faster                                                                   |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf1_win32-x86-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|-------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io           | 940 ms                                                          | 460 ms: 2.05x faster                                                           |
| async_tree_cpu_io_mixed | 922 ms                                                          | 474 ms: 1.95x faster                                                           |
| async_tree_none         | 394 ms                                                          | 213 ms: 1.85x faster                                                           |
| async_tree_memoization  | 467 ms                                                          | 266 ms: 1.76x faster                                                           |
| Geometric mean          | (ref)                                                           | 1.90x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf1_win32-x86-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 215 ms: 2.33x faster                                                           |
| float          | 69.6 ms                                                         | 58.8 ms: 1.18x faster                                                          |
| nbody          | 79.1 ms                                                         | 95.9 ms: 1.21x slower                                                          |
| Geometric mean | (ref)                                                           | 1.32x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf1_win32-x86-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 112 ms: 1.04x faster                                                           |
| regex_dna      | 131 ms                                                          | 126 ms: 1.03x faster                                                           |
| regex_v8       | 15.8 ms                                                         | 17.7 ms: 1.12x slower                                                          |
| regex_effbot   | 1.66 ms                                                         | 1.94 ms: 1.17x slower                                                          |
| Geometric mean | (ref)                                                           | 1.05x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf1_win32-x86-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 8.57 ms: 1.15x faster                                                          |
| json_loads           | 22.4 us                                                         | 20.8 us: 1.07x faster                                                          |
| tomli_loads          | 1.91 sec                                                        | 1.79 sec: 1.07x faster                                                         |
| xml_etree_parse      | 120 ms                                                          | 112 ms: 1.07x faster                                                           |
| xml_etree_iterparse  | 70.8 ms                                                         | 72.9 ms: 1.03x slower                                                          |
| unpickle_pure_python | 189 us                                                          | 195 us: 1.03x slower                                                           |
| pickle_pure_python   | 280 us                                                          | 301 us: 1.07x slower                                                           |
| xml_etree_process    | 48.1 ms                                                         | 55.4 ms: 1.15x slower                                                          |
| xml_etree_generate   | 61.6 ms                                                         | 75.7 ms: 1.23x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.02x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf1_win32-x86-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 20.8 ms: 1.15x slower                                                          |
| python_startup         | 22.9 ms                                                         | 28.1 ms: 1.22x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.19x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf1_win32-x86-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako           | 9.10 ms                                                         | 8.72 ms: 1.04x faster                                                          |
| genshi_xml     | 46.6 ms                                                         | 48.5 ms: 1.04x slower                                                          |
| genshi_text    | 21.0 ms                                                         | 22.8 ms: 1.09x slower                                                          |
| Geometric mean | (ref)                                                           | 1.02x slower                                                                   |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf1_win32-x86-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|--------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 157 us: 2.52x faster                                                           |
| pidigits                 | 502 ms                                                          | 215 ms: 2.33x faster                                                           |
| async_tree_io            | 940 ms                                                          | 460 ms: 2.05x faster                                                           |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 474 ms: 1.95x faster                                                           |
| async_tree_none          | 394 ms                                                          | 213 ms: 1.85x faster                                                           |
| async_tree_memoization   | 467 ms                                                          | 266 ms: 1.76x faster                                                           |
| pylint                   | 384 ms                                                          | 237 ms: 1.62x faster                                                           |
| deltablue                | 4.04 ms                                                         | 2.90 ms: 1.39x faster                                                          |
| go                       | 146 ms                                                          | 113 ms: 1.29x faster                                                           |
| deepcopy                 | 310 us                                                          | 247 us: 1.25x faster                                                           |
| chaos                    | 74.4 ms                                                         | 59.5 ms: 1.25x faster                                                          |
| thrift                   | 902 us                                                          | 728 us: 1.24x faster                                                           |
| deepcopy_memo            | 29.6 us                                                         | 24.0 us: 1.23x faster                                                          |
| crypto_pyaes             | 81.3 ms                                                         | 67.6 ms: 1.20x faster                                                          |
| logging_silent           | 97.9 ns                                                         | 82.3 ns: 1.19x faster                                                          |
| raytrace                 | 303 ms                                                          | 255 ms: 1.18x faster                                                           |
| float                    | 69.6 ms                                                         | 58.8 ms: 1.18x faster                                                          |
| scimark_lu               | 89.8 ms                                                         | 75.9 ms: 1.18x faster                                                          |
| dulwich_log              | 58.5 ms                                                         | 50.5 ms: 1.16x faster                                                          |
| scimark_monte_carlo      | 61.9 ms                                                         | 53.5 ms: 1.16x faster                                                          |
| sqlite_synth             | 2.29 us                                                         | 1.98 us: 1.16x faster                                                          |
| scimark_sor              | 115 ms                                                          | 99.7 ms: 1.15x faster                                                          |
| sqlglot_parse            | 1.33 ms                                                         | 1.16 ms: 1.15x faster                                                          |
| json_dumps               | 9.82 ms                                                         | 8.57 ms: 1.15x faster                                                          |
| pyflate                  | 422 ms                                                          | 371 ms: 1.14x faster                                                           |
| pycparser                | 1.04 sec                                                        | 925 ms: 1.13x faster                                                           |
| json                     | 4.76 ms                                                         | 4.27 ms: 1.11x faster                                                          |
| sqlglot_transpile        | 1.58 ms                                                         | 1.44 ms: 1.10x faster                                                          |
| sympy_sum                | 122 ms                                                          | 112 ms: 1.10x faster                                                           |
| json_loads               | 22.4 us                                                         | 20.8 us: 1.07x faster                                                          |
| tomli_loads              | 1.91 sec                                                        | 1.79 sec: 1.07x faster                                                         |
| xml_etree_parse          | 120 ms                                                          | 112 ms: 1.07x faster                                                           |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.04 ms: 1.07x faster                                                          |
| comprehensions           | 17.7 us                                                         | 16.7 us: 1.07x faster                                                          |
| html5lib                 | 52.1 ms                                                         | 48.9 ms: 1.06x faster                                                          |
| spectral_norm            | 80.2 ms                                                         | 75.6 ms: 1.06x faster                                                          |
| mako                     | 9.10 ms                                                         | 8.72 ms: 1.04x faster                                                          |
| regex_compile            | 117 ms                                                          | 112 ms: 1.04x faster                                                           |
| generators               | 31.6 ms                                                         | 30.3 ms: 1.04x faster                                                          |
| hexiom                   | 6.13 ms                                                         | 5.91 ms: 1.04x faster                                                          |
| bench_thread_pool        | 1.12 ms                                                         | 1.08 ms: 1.04x faster                                                          |
| deepcopy_reduce          | 2.68 us                                                         | 2.59 us: 1.03x faster                                                          |
| fannkuch                 | 317 ms                                                          | 307 ms: 1.03x faster                                                           |
| regex_dna                | 131 ms                                                          | 126 ms: 1.03x faster                                                           |
| sympy_str                | 229 ms                                                          | 222 ms: 1.03x faster                                                           |
| sympy_expand             | 391 ms                                                          | 383 ms: 1.02x faster                                                           |
| richards_super           | 49.9 ms                                                         | 49.3 ms: 1.01x faster                                                          |
| coroutines               | 17.9 ms                                                         | 17.7 ms: 1.01x faster                                                          |
| pprint_pformat           | 1.37 sec                                                        | 1.41 sec: 1.03x slower                                                         |
| xml_etree_iterparse      | 70.8 ms                                                         | 72.9 ms: 1.03x slower                                                          |
| unpickle_pure_python     | 189 us                                                          | 195 us: 1.03x slower                                                           |
| pprint_safe_repr         | 658 ms                                                          | 683 ms: 1.04x slower                                                           |
| genshi_xml               | 46.6 ms                                                         | 48.5 ms: 1.04x slower                                                          |
| 2to3                     | 265 ms                                                          | 277 ms: 1.05x slower                                                           |
| pathlib                  | 81.2 ms                                                         | 86.4 ms: 1.06x slower                                                          |
| sqlglot_optimize         | 44.7 ms                                                         | 48.0 ms: 1.07x slower                                                          |
| pickle_pure_python       | 280 us                                                          | 301 us: 1.07x slower                                                           |
| richards                 | 40.3 ms                                                         | 43.7 ms: 1.09x slower                                                          |
| sqlglot_normalize        | 230 ms                                                          | 250 ms: 1.09x slower                                                           |
| meteor_contest           | 80.0 ms                                                         | 87.0 ms: 1.09x slower                                                          |
| genshi_text              | 21.0 ms                                                         | 22.8 ms: 1.09x slower                                                          |
| mdp                      | 1.83 sec                                                        | 1.99 sec: 1.09x slower                                                         |
| scimark_fft              | 216 ms                                                          | 237 ms: 1.10x slower                                                           |
| regex_v8                 | 15.8 ms                                                         | 17.7 ms: 1.12x slower                                                          |
| xml_etree_process        | 48.1 ms                                                         | 55.4 ms: 1.15x slower                                                          |
| python_startup_no_site   | 18.1 ms                                                         | 20.8 ms: 1.15x slower                                                          |
| logging_format           | 7.91 us                                                         | 9.16 us: 1.16x slower                                                          |
| regex_effbot             | 1.66 ms                                                         | 1.94 ms: 1.17x slower                                                          |
| logging_simple           | 7.29 us                                                         | 8.54 us: 1.17x slower                                                          |
| nbody                    | 79.1 ms                                                         | 95.9 ms: 1.21x slower                                                          |
| python_startup           | 22.9 ms                                                         | 28.1 ms: 1.22x slower                                                          |
| xml_etree_generate       | 61.6 ms                                                         | 75.7 ms: 1.23x slower                                                          |
| coverage                 | 46.6 ms                                                         | 58.1 ms: 1.25x slower                                                          |
| async_generators         | 241 ms                                                          | 312 ms: 1.29x slower                                                           |
| telco                    | 4.83 ms                                                         | 6.39 ms: 1.32x slower                                                          |
| bench_mp_pool            | 66.4 ms                                                         | 99.3 ms: 1.50x slower                                                          |
| create_gc_cycles         | 694 us                                                          | 1.20 ms: 1.74x slower                                                          |
| gc_traversal             | 1.28 ms                                                         | 2.38 ms: 1.85x slower                                                          |
| Geometric mean           | (ref)                                                           | 1.06x faster                                                                   |

Benchmark hidden because not significant (4): nqueens, sympy_integrate, docutils, django_template
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250107-3.14.0a3+-f1d3190-CLANG/bm-20250107-pythonperf1_win32-x86-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.064x faster

# HPT report

- Reliability score: 97.06% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown