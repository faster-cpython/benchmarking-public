# Results vs. 3.10.4

- fork: Fidget-Spinner
- ref: clang_hot
- machine: windows-x86
- commit hash: 37fb620
- commit date: 2025-03-06
- overall geometric mean: 1.206x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250306-pythonperf1_win32-x86-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 249 ms: 1.06x faster                                                           |
| docutils       | 1.95 sec                                                        | 1.82 sec: 1.07x faster                                                         |
| html5lib       | 52.1 ms                                                         | 44.8 ms: 1.16x faster                                                          |
| Geometric mean | (ref)                                                           | 1.10x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250306-pythonperf1_win32-x86-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|-------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io           | 940 ms                                                          | 410 ms: 2.29x faster                                                           |
| async_tree_none         | 394 ms                                                          | 186 ms: 2.11x faster                                                           |
| async_tree_cpu_io_mixed | 922 ms                                                          | 446 ms: 2.07x faster                                                           |
| async_tree_memoization  | 467 ms                                                          | 229 ms: 2.03x faster                                                           |
| Geometric mean          | (ref)                                                           | 2.12x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250306-pythonperf1_win32-x86-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 219 ms: 2.29x faster                                                           |
| float          | 69.6 ms                                                         | 48.6 ms: 1.43x faster                                                          |
| nbody          | 79.1 ms                                                         | 75.7 ms: 1.04x faster                                                          |
| Geometric mean | (ref)                                                           | 1.51x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250306-pythonperf1_win32-x86-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 97.1 ms: 1.20x faster                                                          |
| regex_dna      | 131 ms                                                          | 128 ms: 1.02x faster                                                           |
| regex_v8       | 15.8 ms                                                         | 17.4 ms: 1.10x slower                                                          |
| regex_effbot   | 1.66 ms                                                         | 1.96 ms: 1.18x slower                                                          |
| Geometric mean | (ref)                                                           | 1.02x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250306-pythonperf1_win32-x86-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 7.86 ms: 1.25x faster                                                          |
| tomli_loads          | 1.91 sec                                                        | 1.53 sec: 1.25x faster                                                         |
| unpickle_pure_python | 189 us                                                          | 166 us: 1.14x faster                                                           |
| pickle_pure_python   | 280 us                                                          | 252 us: 1.11x faster                                                           |
| xml_etree_parse      | 120 ms                                                          | 115 ms: 1.04x faster                                                           |
| json_loads           | 22.4 us                                                         | 21.7 us: 1.03x faster                                                          |
| xml_etree_iterparse  | 70.8 ms                                                         | 72.8 ms: 1.03x slower                                                          |
| xml_etree_process    | 48.1 ms                                                         | 50.0 ms: 1.04x slower                                                          |
| xml_etree_generate   | 61.6 ms                                                         | 70.3 ms: 1.14x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.06x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250306-pythonperf1_win32-x86-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 22.6 ms: 1.25x slower                                                          |
| python_startup         | 22.9 ms                                                         | 29.7 ms: 1.30x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.27x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250306-pythonperf1_win32-x86-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_xml      | 46.6 ms                                                         | 39.6 ms: 1.18x faster                                                          |
| django_template | 36.0 ms                                                         | 31.0 ms: 1.16x faster                                                          |
| genshi_text     | 21.0 ms                                                         | 18.3 ms: 1.15x faster                                                          |
| mako            | 9.10 ms                                                         | 8.56 ms: 1.06x faster                                                          |
| Geometric mean  | (ref)                                                           | 1.14x faster                                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250306-pythonperf1_win32-x86-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|--------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 136 us: 2.91x faster                                                           |
| pathlib                  | 81.2 ms                                                         | 35.4 ms: 2.30x faster                                                          |
| async_tree_io            | 940 ms                                                          | 410 ms: 2.29x faster                                                           |
| pidigits                 | 502 ms                                                          | 219 ms: 2.29x faster                                                           |
| async_tree_none          | 394 ms                                                          | 186 ms: 2.11x faster                                                           |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 446 ms: 2.07x faster                                                           |
| async_tree_memoization   | 467 ms                                                          | 229 ms: 2.03x faster                                                           |
| deltablue                | 4.04 ms                                                         | 2.25 ms: 1.79x faster                                                          |
| pylint                   | 384 ms                                                          | 216 ms: 1.77x faster                                                           |
| go                       | 146 ms                                                          | 90.3 ms: 1.61x faster                                                          |
| generators               | 31.6 ms                                                         | 19.9 ms: 1.59x faster                                                          |
| chaos                    | 74.4 ms                                                         | 49.5 ms: 1.50x faster                                                          |
| deepcopy_memo            | 29.6 us                                                         | 19.9 us: 1.49x faster                                                          |
| logging_silent           | 97.9 ns                                                         | 66.7 ns: 1.47x faster                                                          |
| deepcopy                 | 310 us                                                          | 212 us: 1.47x faster                                                           |
| raytrace                 | 303 ms                                                          | 211 ms: 1.44x faster                                                           |
| float                    | 69.6 ms                                                         | 48.6 ms: 1.43x faster                                                          |
| scimark_sor              | 115 ms                                                          | 82.0 ms: 1.40x faster                                                          |
| sqlglot_parse            | 1.33 ms                                                         | 982 us: 1.35x faster                                                           |
| comprehensions           | 17.7 us                                                         | 13.2 us: 1.34x faster                                                          |
| thrift                   | 902 us                                                          | 679 us: 1.33x faster                                                           |
| pyflate                  | 422 ms                                                          | 324 ms: 1.30x faster                                                           |
| scimark_monte_carlo      | 61.9 ms                                                         | 47.7 ms: 1.30x faster                                                          |
| sqlglot_transpile        | 1.58 ms                                                         | 1.22 ms: 1.30x faster                                                          |
| spectral_norm            | 80.2 ms                                                         | 62.5 ms: 1.28x faster                                                          |
| coroutines               | 17.9 ms                                                         | 14.0 ms: 1.28x faster                                                          |
| crypto_pyaes             | 81.3 ms                                                         | 64.1 ms: 1.27x faster                                                          |
| hexiom                   | 6.13 ms                                                         | 4.87 ms: 1.26x faster                                                          |
| pycparser                | 1.04 sec                                                        | 827 ms: 1.26x faster                                                           |
| json_dumps               | 9.82 ms                                                         | 7.86 ms: 1.25x faster                                                          |
| scimark_lu               | 89.8 ms                                                         | 71.8 ms: 1.25x faster                                                          |
| tomli_loads              | 1.91 sec                                                        | 1.53 sec: 1.25x faster                                                         |
| deepcopy_reduce          | 2.68 us                                                         | 2.16 us: 1.24x faster                                                          |
| richards_super           | 49.9 ms                                                         | 40.9 ms: 1.22x faster                                                          |
| sqlite_synth             | 2.29 us                                                         | 1.90 us: 1.21x faster                                                          |
| regex_compile            | 117 ms                                                          | 97.1 ms: 1.20x faster                                                          |
| dulwich_log              | 58.5 ms                                                         | 48.9 ms: 1.20x faster                                                          |
| sympy_sum                | 122 ms                                                          | 103 ms: 1.19x faster                                                           |
| nqueens                  | 87.1 ms                                                         | 73.2 ms: 1.19x faster                                                          |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.73 ms: 1.19x faster                                                          |
| pprint_pformat           | 1.37 sec                                                        | 1.15 sec: 1.19x faster                                                         |
| pprint_safe_repr         | 658 ms                                                          | 558 ms: 1.18x faster                                                           |
| genshi_xml               | 46.6 ms                                                         | 39.6 ms: 1.18x faster                                                          |
| html5lib                 | 52.1 ms                                                         | 44.8 ms: 1.16x faster                                                          |
| django_template          | 36.0 ms                                                         | 31.0 ms: 1.16x faster                                                          |
| genshi_text              | 21.0 ms                                                         | 18.3 ms: 1.15x faster                                                          |
| sympy_str                | 229 ms                                                          | 200 ms: 1.15x faster                                                           |
| unpickle_pure_python     | 189 us                                                          | 166 us: 1.14x faster                                                           |
| sympy_expand             | 391 ms                                                          | 348 ms: 1.12x faster                                                           |
| pickle_pure_python       | 280 us                                                          | 252 us: 1.11x faster                                                           |
| richards                 | 40.3 ms                                                         | 36.2 ms: 1.11x faster                                                          |
| json                     | 4.76 ms                                                         | 4.35 ms: 1.10x faster                                                          |
| sympy_integrate          | 16.6 ms                                                         | 15.2 ms: 1.09x faster                                                          |
| docutils                 | 1.95 sec                                                        | 1.82 sec: 1.07x faster                                                         |
| sqlglot_normalize        | 230 ms                                                          | 216 ms: 1.07x faster                                                           |
| 2to3                     | 265 ms                                                          | 249 ms: 1.06x faster                                                           |
| mako                     | 9.10 ms                                                         | 8.56 ms: 1.06x faster                                                          |
| fannkuch                 | 317 ms                                                          | 299 ms: 1.06x faster                                                           |
| sqlglot_optimize         | 44.7 ms                                                         | 42.2 ms: 1.06x faster                                                          |
| nbody                    | 79.1 ms                                                         | 75.7 ms: 1.04x faster                                                          |
| xml_etree_parse          | 120 ms                                                          | 115 ms: 1.04x faster                                                           |
| json_loads               | 22.4 us                                                         | 21.7 us: 1.03x faster                                                          |
| regex_dna                | 131 ms                                                          | 128 ms: 1.02x faster                                                           |
| meteor_contest           | 80.0 ms                                                         | 81.9 ms: 1.02x slower                                                          |
| xml_etree_iterparse      | 70.8 ms                                                         | 72.8 ms: 1.03x slower                                                          |
| async_generators         | 241 ms                                                          | 248 ms: 1.03x slower                                                           |
| xml_etree_process        | 48.1 ms                                                         | 50.0 ms: 1.04x slower                                                          |
| logging_format           | 7.91 us                                                         | 8.46 us: 1.07x slower                                                          |
| regex_v8                 | 15.8 ms                                                         | 17.4 ms: 1.10x slower                                                          |
| logging_simple           | 7.29 us                                                         | 8.06 us: 1.11x slower                                                          |
| xml_etree_generate       | 61.6 ms                                                         | 70.3 ms: 1.14x slower                                                          |
| regex_effbot             | 1.66 ms                                                         | 1.96 ms: 1.18x slower                                                          |
| bench_thread_pool        | 1.12 ms                                                         | 1.36 ms: 1.22x slower                                                          |
| coverage                 | 46.6 ms                                                         | 57.1 ms: 1.23x slower                                                          |
| telco                    | 4.83 ms                                                         | 6.00 ms: 1.24x slower                                                          |
| python_startup_no_site   | 18.1 ms                                                         | 22.6 ms: 1.25x slower                                                          |
| python_startup           | 22.9 ms                                                         | 29.7 ms: 1.30x slower                                                          |
| bench_mp_pool            | 66.4 ms                                                         | 95.5 ms: 1.44x slower                                                          |
| create_gc_cycles         | 694 us                                                          | 1.20 ms: 1.73x slower                                                          |
| gc_traversal             | 1.28 ms                                                         | 2.36 ms: 1.84x slower                                                          |
| Geometric mean           | (ref)                                                           | 1.19x faster                                                                   |

Benchmark hidden because not significant (2): mdp, scimark_fft
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250306-3.14.0a5+-37fb620-CLANG/bm-20250306-pythonperf1_win32-x86-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.206x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.15x
- 95% likely to have a speedup of 1.13x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: unknown