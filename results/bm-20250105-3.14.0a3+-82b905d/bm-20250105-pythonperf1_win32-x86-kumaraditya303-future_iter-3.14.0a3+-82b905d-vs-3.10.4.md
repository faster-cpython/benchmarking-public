# Results vs. 3.10.4

- fork: kumaraditya303
- ref: future_iter
- machine: windows-x86
- commit hash: 82b905d
- commit date: 2025-01-05
- overall geometric mean: 1.175x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250105-pythonperf1_win32-x86-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 245 ms: 1.08x faster                                                           |
| docutils       | 1.95 sec                                                        | 1.79 sec: 1.09x faster                                                         |
| html5lib       | 52.1 ms                                                         | 43.3 ms: 1.20x faster                                                          |
| Geometric mean | (ref)                                                           | 1.12x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250105-pythonperf1_win32-x86-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|-------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io           | 940 ms                                                          | 434 ms: 2.17x faster                                                           |
| async_tree_cpu_io_mixed | 922 ms                                                          | 433 ms: 2.13x faster                                                           |
| async_tree_none         | 394 ms                                                          | 197 ms: 2.00x faster                                                           |
| async_tree_memoization  | 467 ms                                                          | 241 ms: 1.94x faster                                                           |
| Geometric mean          | (ref)                                                           | 2.06x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250105-pythonperf1_win32-x86-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 196 ms: 2.56x faster                                                           |
| float          | 69.6 ms                                                         | 53.8 ms: 1.29x faster                                                          |
| nbody          | 79.1 ms                                                         | 83.5 ms: 1.06x slower                                                          |
| Geometric mean | (ref)                                                           | 1.46x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250105-pythonperf1_win32-x86-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 101 ms: 1.16x faster                                                           |
| regex_dna      | 131 ms                                                          | 117 ms: 1.12x faster                                                           |
| regex_effbot   | 1.66 ms                                                         | 1.58 ms: 1.05x faster                                                          |
| regex_v8       | 15.8 ms                                                         | 16.0 ms: 1.02x slower                                                          |
| Geometric mean | (ref)                                                           | 1.07x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250105-pythonperf1_win32-x86-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| xml_etree_parse      | 120 ms                                                          | 95.4 ms: 1.26x faster                                                          |
| tomli_loads          | 1.91 sec                                                        | 1.55 sec: 1.23x faster                                                         |
| unpickle_pure_python | 189 us                                                          | 168 us: 1.13x faster                                                           |
| xml_etree_iterparse  | 70.8 ms                                                         | 63.6 ms: 1.11x faster                                                          |
| pickle_pure_python   | 280 us                                                          | 252 us: 1.11x faster                                                           |
| json_dumps           | 9.82 ms                                                         | 9.09 ms: 1.08x faster                                                          |
| json_loads           | 22.4 us                                                         | 20.7 us: 1.08x faster                                                          |
| xml_etree_generate   | 61.6 ms                                                         | 66.3 ms: 1.08x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.10x faster                                                                   |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250105-pythonperf1_win32-x86-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 19.2 ms: 1.06x slower                                                          |
| python_startup         | 22.9 ms                                                         | 25.4 ms: 1.11x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.09x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250105-pythonperf1_win32-x86-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 7.48 ms: 1.22x faster                                                          |
| django_template | 36.0 ms                                                         | 31.2 ms: 1.15x faster                                                          |
| genshi_xml      | 46.6 ms                                                         | 44.5 ms: 1.05x faster                                                          |
| genshi_text     | 21.0 ms                                                         | 20.4 ms: 1.03x faster                                                          |
| Geometric mean  | (ref)                                                           | 1.11x faster                                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250105-pythonperf1_win32-x86-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|--------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 138 us: 2.87x faster                                                           |
| pidigits                 | 502 ms                                                          | 196 ms: 2.56x faster                                                           |
| async_tree_io            | 940 ms                                                          | 434 ms: 2.17x faster                                                           |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 433 ms: 2.13x faster                                                           |
| async_tree_none          | 394 ms                                                          | 197 ms: 2.00x faster                                                           |
| async_tree_memoization   | 467 ms                                                          | 241 ms: 1.94x faster                                                           |
| pylint                   | 384 ms                                                          | 216 ms: 1.78x faster                                                           |
| deltablue                | 4.04 ms                                                         | 2.52 ms: 1.60x faster                                                          |
| go                       | 146 ms                                                          | 94.1 ms: 1.55x faster                                                          |
| logging_silent           | 97.9 ns                                                         | 69.7 ns: 1.41x faster                                                          |
| chaos                    | 74.4 ms                                                         | 53.9 ms: 1.38x faster                                                          |
| deepcopy_memo            | 29.6 us                                                         | 21.5 us: 1.38x faster                                                          |
| scimark_lu               | 89.8 ms                                                         | 66.0 ms: 1.36x faster                                                          |
| crypto_pyaes             | 81.3 ms                                                         | 59.9 ms: 1.36x faster                                                          |
| deepcopy                 | 310 us                                                          | 234 us: 1.33x faster                                                           |
| comprehensions           | 17.7 us                                                         | 13.5 us: 1.31x faster                                                          |
| sqlglot_parse            | 1.33 ms                                                         | 1.03 ms: 1.29x faster                                                          |
| float                    | 69.6 ms                                                         | 53.8 ms: 1.29x faster                                                          |
| raytrace                 | 303 ms                                                          | 235 ms: 1.29x faster                                                           |
| generators               | 31.6 ms                                                         | 24.5 ms: 1.29x faster                                                          |
| pycparser                | 1.04 sec                                                        | 819 ms: 1.27x faster                                                           |
| pyflate                  | 422 ms                                                          | 333 ms: 1.27x faster                                                           |
| xml_etree_parse          | 120 ms                                                          | 95.4 ms: 1.26x faster                                                          |
| hexiom                   | 6.13 ms                                                         | 4.91 ms: 1.25x faster                                                          |
| sqlglot_transpile        | 1.58 ms                                                         | 1.27 ms: 1.24x faster                                                          |
| scimark_sor              | 115 ms                                                          | 93.1 ms: 1.24x faster                                                          |
| tomli_loads              | 1.91 sec                                                        | 1.55 sec: 1.23x faster                                                         |
| thrift                   | 902 us                                                          | 735 us: 1.23x faster                                                           |
| richards_super           | 49.9 ms                                                         | 40.7 ms: 1.23x faster                                                          |
| scimark_monte_carlo      | 61.9 ms                                                         | 50.5 ms: 1.23x faster                                                          |
| mako                     | 9.10 ms                                                         | 7.48 ms: 1.22x faster                                                          |
| html5lib                 | 52.1 ms                                                         | 43.3 ms: 1.20x faster                                                          |
| sqlite_synth             | 2.29 us                                                         | 1.91 us: 1.20x faster                                                          |
| spectral_norm            | 80.2 ms                                                         | 68.1 ms: 1.18x faster                                                          |
| dulwich_log              | 58.5 ms                                                         | 50.3 ms: 1.16x faster                                                          |
| sympy_sum                | 122 ms                                                          | 106 ms: 1.16x faster                                                           |
| regex_compile            | 117 ms                                                          | 101 ms: 1.16x faster                                                           |
| richards                 | 40.3 ms                                                         | 34.8 ms: 1.16x faster                                                          |
| django_template          | 36.0 ms                                                         | 31.2 ms: 1.15x faster                                                          |
| nqueens                  | 87.1 ms                                                         | 76.6 ms: 1.14x faster                                                          |
| json                     | 4.76 ms                                                         | 4.21 ms: 1.13x faster                                                          |
| unpickle_pure_python     | 189 us                                                          | 168 us: 1.13x faster                                                           |
| regex_dna                | 131 ms                                                          | 117 ms: 1.12x faster                                                           |
| xml_etree_iterparse      | 70.8 ms                                                         | 63.6 ms: 1.11x faster                                                          |
| pickle_pure_python       | 280 us                                                          | 252 us: 1.11x faster                                                           |
| bench_thread_pool        | 1.12 ms                                                         | 1.01 ms: 1.11x faster                                                          |
| coroutines               | 17.9 ms                                                         | 16.3 ms: 1.10x faster                                                          |
| pprint_pformat           | 1.37 sec                                                        | 1.25 sec: 1.10x faster                                                         |
| deepcopy_reduce          | 2.68 us                                                         | 2.46 us: 1.09x faster                                                          |
| sympy_integrate          | 16.6 ms                                                         | 15.3 ms: 1.09x faster                                                          |
| docutils                 | 1.95 sec                                                        | 1.79 sec: 1.09x faster                                                         |
| fannkuch                 | 317 ms                                                          | 292 ms: 1.09x faster                                                           |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.98 ms: 1.09x faster                                                          |
| pprint_safe_repr         | 658 ms                                                          | 608 ms: 1.08x faster                                                           |
| 2to3                     | 265 ms                                                          | 245 ms: 1.08x faster                                                           |
| json_dumps               | 9.82 ms                                                         | 9.09 ms: 1.08x faster                                                          |
| json_loads               | 22.4 us                                                         | 20.7 us: 1.08x faster                                                          |
| sympy_str                | 229 ms                                                          | 214 ms: 1.07x faster                                                           |
| mdp                      | 1.83 sec                                                        | 1.71 sec: 1.07x faster                                                         |
| sqlglot_optimize         | 44.7 ms                                                         | 42.3 ms: 1.06x faster                                                          |
| regex_effbot             | 1.66 ms                                                         | 1.58 ms: 1.05x faster                                                          |
| genshi_xml               | 46.6 ms                                                         | 44.5 ms: 1.05x faster                                                          |
| sqlglot_normalize        | 230 ms                                                          | 221 ms: 1.04x faster                                                           |
| sympy_expand             | 391 ms                                                          | 379 ms: 1.03x faster                                                           |
| genshi_text              | 21.0 ms                                                         | 20.4 ms: 1.03x faster                                                          |
| meteor_contest           | 80.0 ms                                                         | 80.9 ms: 1.01x slower                                                          |
| regex_v8                 | 15.8 ms                                                         | 16.0 ms: 1.02x slower                                                          |
| scimark_fft              | 216 ms                                                          | 222 ms: 1.03x slower                                                           |
| pathlib                  | 81.2 ms                                                         | 84.3 ms: 1.04x slower                                                          |
| nbody                    | 79.1 ms                                                         | 83.5 ms: 1.06x slower                                                          |
| logging_format           | 7.91 us                                                         | 8.38 us: 1.06x slower                                                          |
| python_startup_no_site   | 18.1 ms                                                         | 19.2 ms: 1.06x slower                                                          |
| logging_simple           | 7.29 us                                                         | 7.80 us: 1.07x slower                                                          |
| xml_etree_generate       | 61.6 ms                                                         | 66.3 ms: 1.08x slower                                                          |
| python_startup           | 22.9 ms                                                         | 25.4 ms: 1.11x slower                                                          |
| coverage                 | 46.6 ms                                                         | 52.3 ms: 1.12x slower                                                          |
| mypy2                    | 590 ms                                                          | 690 ms: 1.17x slower                                                           |
| async_generators         | 241 ms                                                          | 290 ms: 1.20x slower                                                           |
| bench_mp_pool            | 66.4 ms                                                         | 87.0 ms: 1.31x slower                                                          |
| telco                    | 4.83 ms                                                         | 6.68 ms: 1.38x slower                                                          |
| gc_traversal             | 1.28 ms                                                         | 1.79 ms: 1.39x slower                                                          |
| create_gc_cycles         | 694 us                                                          | 1.05 ms: 1.51x slower                                                          |
| Geometric mean           | (ref)                                                           | 1.17x faster                                                                   |

Benchmark hidden because not significant (1): xml_etree_process
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250105-3.14.0a3+-82b905d/bm-20250105-pythonperf1_win32-x86-kumaraditya303-future_iter-3.14.0a3+-82b905d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.175x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: unknown