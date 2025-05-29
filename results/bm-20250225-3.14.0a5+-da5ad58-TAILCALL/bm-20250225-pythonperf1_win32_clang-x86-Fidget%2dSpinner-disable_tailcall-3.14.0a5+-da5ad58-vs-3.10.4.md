# Results vs. 3.10.4

- fork: Fidget-Spinner
- ref: disable_tailcall
- machine: windows-x86
- commit hash: da5ad58
- commit date: 2025-02-25
- overall geometric mean: 1.287x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250225-pythonperf1_win32-x86-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 229 ms: 1.16x faster                                                                  |
| docutils       | 1.95 sec                                                        | 1.72 sec: 1.13x faster                                                                |
| html5lib       | 52.1 ms                                                         | 41.3 ms: 1.26x faster                                                                 |
| Geometric mean | (ref)                                                           | 1.18x faster                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250225-pythonperf1_win32-x86-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_io           | 940 ms                                                          | 379 ms: 2.48x faster                                                                  |
| async_tree_none         | 394 ms                                                          | 172 ms: 2.29x faster                                                                  |
| async_tree_memoization  | 467 ms                                                          | 213 ms: 2.19x faster                                                                  |
| async_tree_cpu_io_mixed | 922 ms                                                          | 436 ms: 2.12x faster                                                                  |
| Geometric mean          | (ref)                                                           | 2.27x faster                                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250225-pythonperf1_win32-x86-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 217 ms: 2.31x faster                                                                  |
| float          | 69.6 ms                                                         | 45.8 ms: 1.52x faster                                                                 |
| nbody          | 79.1 ms                                                         | 69.2 ms: 1.14x faster                                                                 |
| Geometric mean | (ref)                                                           | 1.59x faster                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250225-pythonperf1_win32-x86-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 88.5 ms: 1.32x faster                                                                 |
| regex_dna      | 131 ms                                                          | 132 ms: 1.01x slower                                                                  |
| regex_v8       | 15.8 ms                                                         | 17.4 ms: 1.11x slower                                                                 |
| regex_effbot   | 1.66 ms                                                         | 1.92 ms: 1.16x slower                                                                 |
| Geometric mean | (ref)                                                           | 1.01x faster                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250225-pythonperf1_win32-x86-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| tomli_loads          | 1.91 sec                                                        | 1.41 sec: 1.36x faster                                                                |
| json_dumps           | 9.82 ms                                                         | 7.52 ms: 1.31x faster                                                                 |
| pickle_pure_python   | 280 us                                                          | 223 us: 1.26x faster                                                                  |
| unpickle_pure_python | 189 us                                                          | 153 us: 1.24x faster                                                                  |
| xml_etree_parse      | 120 ms                                                          | 114 ms: 1.05x faster                                                                  |
| json_loads           | 22.4 us                                                         | 21.3 us: 1.05x faster                                                                 |
| xml_etree_process    | 48.1 ms                                                         | 46.9 ms: 1.03x faster                                                                 |
| xml_etree_iterparse  | 70.8 ms                                                         | 73.1 ms: 1.03x slower                                                                 |
| xml_etree_generate   | 61.6 ms                                                         | 67.2 ms: 1.09x slower                                                                 |
| Geometric mean       | (ref)                                                           | 1.12x faster                                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250225-pythonperf1_win32-x86-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 22.1 ms: 1.22x slower                                                                 |
| python_startup         | 22.9 ms                                                         | 28.6 ms: 1.25x slower                                                                 |
| Geometric mean         | (ref)                                                           | 1.24x slower                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250225-pythonperf1_win32-x86-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| django_template | 36.0 ms                                                         | 27.3 ms: 1.32x faster                                                                 |
| genshi_text     | 21.0 ms                                                         | 16.0 ms: 1.31x faster                                                                 |
| genshi_xml      | 46.6 ms                                                         | 36.0 ms: 1.29x faster                                                                 |
| mako            | 9.10 ms                                                         | 7.82 ms: 1.16x faster                                                                 |
| Geometric mean  | (ref)                                                           | 1.27x faster                                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250225-pythonperf1_win32-x86-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 122 us: 3.23x faster                                                                  |
| async_tree_io            | 940 ms                                                          | 379 ms: 2.48x faster                                                                  |
| pathlib                  | 81.2 ms                                                         | 32.9 ms: 2.47x faster                                                                 |
| pidigits                 | 502 ms                                                          | 217 ms: 2.31x faster                                                                  |
| async_tree_none          | 394 ms                                                          | 172 ms: 2.29x faster                                                                  |
| async_tree_memoization   | 467 ms                                                          | 213 ms: 2.19x faster                                                                  |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 436 ms: 2.12x faster                                                                  |
| deltablue                | 4.04 ms                                                         | 2.00 ms: 2.02x faster                                                                 |
| pylint                   | 384 ms                                                          | 206 ms: 1.86x faster                                                                  |
| generators               | 31.6 ms                                                         | 17.1 ms: 1.85x faster                                                                 |
| go                       | 146 ms                                                          | 79.3 ms: 1.84x faster                                                                 |
| chaos                    | 74.4 ms                                                         | 45.1 ms: 1.65x faster                                                                 |
| deepcopy                 | 310 us                                                          | 190 us: 1.63x faster                                                                  |
| deepcopy_memo            | 29.6 us                                                         | 18.2 us: 1.63x faster                                                                 |
| raytrace                 | 303 ms                                                          | 193 ms: 1.57x faster                                                                  |
| logging_silent           | 97.9 ns                                                         | 63.3 ns: 1.55x faster                                                                 |
| sqlglot_parse            | 1.33 ms                                                         | 871 us: 1.53x faster                                                                  |
| scimark_sor              | 115 ms                                                          | 75.5 ms: 1.52x faster                                                                 |
| float                    | 69.6 ms                                                         | 45.8 ms: 1.52x faster                                                                 |
| comprehensions           | 17.7 us                                                         | 12.3 us: 1.44x faster                                                                 |
| sqlglot_transpile        | 1.58 ms                                                         | 1.10 ms: 1.44x faster                                                                 |
| thrift                   | 902 us                                                          | 631 us: 1.43x faster                                                                  |
| scimark_monte_carlo      | 61.9 ms                                                         | 43.8 ms: 1.41x faster                                                                 |
| pyflate                  | 422 ms                                                          | 300 ms: 1.41x faster                                                                  |
| deepcopy_reduce          | 2.68 us                                                         | 1.92 us: 1.40x faster                                                                 |
| hexiom                   | 6.13 ms                                                         | 4.40 ms: 1.39x faster                                                                 |
| crypto_pyaes             | 81.3 ms                                                         | 58.6 ms: 1.39x faster                                                                 |
| pycparser                | 1.04 sec                                                        | 754 ms: 1.38x faster                                                                  |
| richards_super           | 49.9 ms                                                         | 36.2 ms: 1.38x faster                                                                 |
| tomli_loads              | 1.91 sec                                                        | 1.41 sec: 1.36x faster                                                                |
| spectral_norm            | 80.2 ms                                                         | 59.7 ms: 1.34x faster                                                                 |
| coroutines               | 17.9 ms                                                         | 13.5 ms: 1.33x faster                                                                 |
| django_template          | 36.0 ms                                                         | 27.3 ms: 1.32x faster                                                                 |
| regex_compile            | 117 ms                                                          | 88.5 ms: 1.32x faster                                                                 |
| genshi_text              | 21.0 ms                                                         | 16.0 ms: 1.31x faster                                                                 |
| json_dumps               | 9.82 ms                                                         | 7.52 ms: 1.31x faster                                                                 |
| genshi_xml               | 46.6 ms                                                         | 36.0 ms: 1.29x faster                                                                 |
| dulwich_log              | 58.5 ms                                                         | 45.8 ms: 1.28x faster                                                                 |
| pprint_pformat           | 1.37 sec                                                        | 1.08 sec: 1.27x faster                                                                |
| html5lib                 | 52.1 ms                                                         | 41.3 ms: 1.26x faster                                                                 |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.57 ms: 1.26x faster                                                                 |
| pickle_pure_python       | 280 us                                                          | 223 us: 1.26x faster                                                                  |
| pprint_safe_repr         | 658 ms                                                          | 525 ms: 1.25x faster                                                                  |
| nqueens                  | 87.1 ms                                                         | 69.6 ms: 1.25x faster                                                                 |
| sympy_sum                | 122 ms                                                          | 97.9 ms: 1.25x faster                                                                 |
| sqlite_synth             | 2.29 us                                                         | 1.84 us: 1.24x faster                                                                 |
| richards                 | 40.3 ms                                                         | 32.5 ms: 1.24x faster                                                                 |
| unpickle_pure_python     | 189 us                                                          | 153 us: 1.24x faster                                                                  |
| scimark_lu               | 89.8 ms                                                         | 74.0 ms: 1.21x faster                                                                 |
| sympy_str                | 229 ms                                                          | 191 ms: 1.20x faster                                                                  |
| sympy_expand             | 391 ms                                                          | 327 ms: 1.19x faster                                                                  |
| sqlglot_normalize        | 230 ms                                                          | 195 ms: 1.18x faster                                                                  |
| sympy_integrate          | 16.6 ms                                                         | 14.2 ms: 1.18x faster                                                                 |
| mako                     | 9.10 ms                                                         | 7.82 ms: 1.16x faster                                                                 |
| 2to3                     | 265 ms                                                          | 229 ms: 1.16x faster                                                                  |
| sqlglot_optimize         | 44.7 ms                                                         | 38.6 ms: 1.16x faster                                                                 |
| fannkuch                 | 317 ms                                                          | 277 ms: 1.14x faster                                                                  |
| nbody                    | 79.1 ms                                                         | 69.2 ms: 1.14x faster                                                                 |
| docutils                 | 1.95 sec                                                        | 1.72 sec: 1.13x faster                                                                |
| json                     | 4.76 ms                                                         | 4.28 ms: 1.11x faster                                                                 |
| scimark_fft              | 216 ms                                                          | 196 ms: 1.10x faster                                                                  |
| xml_etree_parse          | 120 ms                                                          | 114 ms: 1.05x faster                                                                  |
| json_loads               | 22.4 us                                                         | 21.3 us: 1.05x faster                                                                 |
| async_generators         | 241 ms                                                          | 231 ms: 1.05x faster                                                                  |
| meteor_contest           | 80.0 ms                                                         | 77.0 ms: 1.04x faster                                                                 |
| logging_format           | 7.91 us                                                         | 7.65 us: 1.03x faster                                                                 |
| xml_etree_process        | 48.1 ms                                                         | 46.9 ms: 1.03x faster                                                                 |
| logging_simple           | 7.29 us                                                         | 7.16 us: 1.02x faster                                                                 |
| mdp                      | 1.83 sec                                                        | 1.79 sec: 1.02x faster                                                                |
| regex_dna                | 131 ms                                                          | 132 ms: 1.01x slower                                                                  |
| xml_etree_iterparse      | 70.8 ms                                                         | 73.1 ms: 1.03x slower                                                                 |
| bench_thread_pool        | 1.12 ms                                                         | 1.18 ms: 1.05x slower                                                                 |
| xml_etree_generate       | 61.6 ms                                                         | 67.2 ms: 1.09x slower                                                                 |
| regex_v8                 | 15.8 ms                                                         | 17.4 ms: 1.11x slower                                                                 |
| regex_effbot             | 1.66 ms                                                         | 1.92 ms: 1.16x slower                                                                 |
| coverage                 | 46.6 ms                                                         | 54.9 ms: 1.18x slower                                                                 |
| telco                    | 4.83 ms                                                         | 5.90 ms: 1.22x slower                                                                 |
| python_startup_no_site   | 18.1 ms                                                         | 22.1 ms: 1.22x slower                                                                 |
| python_startup           | 22.9 ms                                                         | 28.6 ms: 1.25x slower                                                                 |
| bench_mp_pool            | 66.4 ms                                                         | 92.2 ms: 1.39x slower                                                                 |
| create_gc_cycles         | 694 us                                                          | 1.17 ms: 1.68x slower                                                                 |
| gc_traversal             | 1.28 ms                                                         | 2.43 ms: 1.90x slower                                                                 |
| Geometric mean           | (ref)                                                           | 1.28x faster                                                                          |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250225-3.14.0a5+-da5ad58-CLANG/bm-20250225-pythonperf1_win32-x86-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.287x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.22x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: unknown