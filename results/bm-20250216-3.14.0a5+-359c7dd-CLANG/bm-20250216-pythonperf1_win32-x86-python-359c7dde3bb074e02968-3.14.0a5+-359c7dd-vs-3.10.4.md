# Results vs. 3.10.4

- fork: python
- ref: 359c7dde3bb074e02968
- machine: windows-x86
- commit hash: 359c7dd
- commit date: 2025-02-16
- overall geometric mean: 1.283x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 234 ms: 1.13x faster                                                            |
| docutils       | 1.95 sec                                                        | 1.72 sec: 1.14x faster                                                          |
| html5lib       | 52.1 ms                                                         | 40.2 ms: 1.30x faster                                                           |
| Geometric mean | (ref)                                                           | 1.19x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io           | 940 ms                                                          | 385 ms: 2.44x faster                                                            |
| async_tree_none         | 394 ms                                                          | 176 ms: 2.24x faster                                                            |
| async_tree_memoization  | 467 ms                                                          | 217 ms: 2.15x faster                                                            |
| async_tree_cpu_io_mixed | 922 ms                                                          | 432 ms: 2.13x faster                                                            |
| Geometric mean          | (ref)                                                           | 2.24x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 216 ms: 2.33x faster                                                            |
| float          | 69.6 ms                                                         | 45.8 ms: 1.52x faster                                                           |
| nbody          | 79.1 ms                                                         | 71.3 ms: 1.11x faster                                                           |
| Geometric mean | (ref)                                                           | 1.58x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 90.1 ms: 1.29x faster                                                           |
| regex_dna      | 131 ms                                                          | 132 ms: 1.01x slower                                                            |
| regex_v8       | 15.8 ms                                                         | 17.4 ms: 1.11x slower                                                           |
| regex_effbot   | 1.66 ms                                                         | 1.95 ms: 1.17x slower                                                           |
| Geometric mean | (ref)                                                           | 1.00x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 1.91 sec                                                        | 1.42 sec: 1.35x faster                                                          |
| json_dumps           | 9.82 ms                                                         | 7.66 ms: 1.28x faster                                                           |
| pickle_pure_python   | 280 us                                                          | 224 us: 1.25x faster                                                            |
| unpickle_pure_python | 189 us                                                          | 155 us: 1.22x faster                                                            |
| pickle_list          | 3.22 us                                                         | 2.63 us: 1.22x faster                                                           |
| unpickle_list        | 2.98 us                                                         | 2.59 us: 1.15x faster                                                           |
| xml_etree_parse      | 120 ms                                                          | 110 ms: 1.09x faster                                                            |
| pickle_dict          | 18.2 us                                                         | 17.3 us: 1.05x faster                                                           |
| json_loads           | 22.4 us                                                         | 21.5 us: 1.04x faster                                                           |
| xml_etree_process    | 48.1 ms                                                         | 47.0 ms: 1.03x faster                                                           |
| xml_etree_iterparse  | 70.8 ms                                                         | 72.3 ms: 1.02x slower                                                           |
| unpickle             | 9.82 us                                                         | 10.2 us: 1.03x slower                                                           |
| pickle               | 7.83 us                                                         | 8.17 us: 1.04x slower                                                           |
| xml_etree_generate   | 61.6 ms                                                         | 67.2 ms: 1.09x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.10x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 22.1 ms: 1.22x slower                                                           |
| python_startup         | 22.9 ms                                                         | 28.6 ms: 1.25x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.24x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_xml      | 46.6 ms                                                         | 35.0 ms: 1.33x faster                                                           |
| django_template | 36.0 ms                                                         | 27.5 ms: 1.31x faster                                                           |
| genshi_text     | 21.0 ms                                                         | 16.1 ms: 1.30x faster                                                           |
| mako            | 9.10 ms                                                         | 7.91 ms: 1.15x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.27x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 124 us: 3.18x faster                                                            |
| pathlib                  | 81.2 ms                                                         | 31.8 ms: 2.55x faster                                                           |
| async_tree_io            | 940 ms                                                          | 385 ms: 2.44x faster                                                            |
| pidigits                 | 502 ms                                                          | 216 ms: 2.33x faster                                                            |
| async_tree_none          | 394 ms                                                          | 176 ms: 2.24x faster                                                            |
| async_tree_memoization   | 467 ms                                                          | 217 ms: 2.15x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 432 ms: 2.13x faster                                                            |
| deltablue                | 4.04 ms                                                         | 2.03 ms: 1.99x faster                                                           |
| pylint                   | 384 ms                                                          | 204 ms: 1.88x faster                                                            |
| go                       | 146 ms                                                          | 79.6 ms: 1.83x faster                                                           |
| generators               | 31.6 ms                                                         | 18.2 ms: 1.73x faster                                                           |
| deepcopy                 | 310 us                                                          | 187 us: 1.66x faster                                                            |
| deepcopy_memo            | 29.6 us                                                         | 18.0 us: 1.64x faster                                                           |
| chaos                    | 74.4 ms                                                         | 45.8 ms: 1.62x faster                                                           |
| raytrace                 | 303 ms                                                          | 193 ms: 1.57x faster                                                            |
| sqlglot_parse            | 1.33 ms                                                         | 870 us: 1.53x faster                                                            |
| float                    | 69.6 ms                                                         | 45.8 ms: 1.52x faster                                                           |
| scimark_sor              | 115 ms                                                          | 76.4 ms: 1.51x faster                                                           |
| crypto_pyaes             | 81.3 ms                                                         | 56.1 ms: 1.45x faster                                                           |
| sqlglot_transpile        | 1.58 ms                                                         | 1.09 ms: 1.45x faster                                                           |
| logging_silent           | 97.9 ns                                                         | 68.0 ns: 1.44x faster                                                           |
| comprehensions           | 17.7 us                                                         | 12.5 us: 1.42x faster                                                           |
| deepcopy_reduce          | 2.68 us                                                         | 1.90 us: 1.41x faster                                                           |
| thrift                   | 902 us                                                          | 640 us: 1.41x faster                                                            |
| richards_super           | 49.9 ms                                                         | 35.5 ms: 1.41x faster                                                           |
| scimark_monte_carlo      | 61.9 ms                                                         | 44.2 ms: 1.40x faster                                                           |
| hexiom                   | 6.13 ms                                                         | 4.40 ms: 1.40x faster                                                           |
| pyflate                  | 422 ms                                                          | 303 ms: 1.39x faster                                                            |
| pycparser                | 1.04 sec                                                        | 767 ms: 1.36x faster                                                            |
| tomli_loads              | 1.91 sec                                                        | 1.42 sec: 1.35x faster                                                          |
| genshi_xml               | 46.6 ms                                                         | 35.0 ms: 1.33x faster                                                           |
| django_template          | 36.0 ms                                                         | 27.5 ms: 1.31x faster                                                           |
| genshi_text              | 21.0 ms                                                         | 16.1 ms: 1.30x faster                                                           |
| richards                 | 40.3 ms                                                         | 31.0 ms: 1.30x faster                                                           |
| asyncio_tcp              | 744 ms                                                          | 573 ms: 1.30x faster                                                            |
| html5lib                 | 52.1 ms                                                         | 40.2 ms: 1.30x faster                                                           |
| regex_compile            | 117 ms                                                          | 90.1 ms: 1.29x faster                                                           |
| nqueens                  | 87.1 ms                                                         | 67.6 ms: 1.29x faster                                                           |
| coroutines               | 17.9 ms                                                         | 14.0 ms: 1.28x faster                                                           |
| json_dumps               | 9.82 ms                                                         | 7.66 ms: 1.28x faster                                                           |
| pprint_pformat           | 1.37 sec                                                        | 1.07 sec: 1.27x faster                                                          |
| pprint_safe_repr         | 658 ms                                                          | 518 ms: 1.27x faster                                                            |
| unpack_sequence          | 40.0 ns                                                         | 31.7 ns: 1.26x faster                                                           |
| dulwich_log              | 58.5 ms                                                         | 46.4 ms: 1.26x faster                                                           |
| sympy_sum                | 122 ms                                                          | 97.5 ms: 1.26x faster                                                           |
| pickle_pure_python       | 280 us                                                          | 224 us: 1.25x faster                                                            |
| spectral_norm            | 80.2 ms                                                         | 64.8 ms: 1.24x faster                                                           |
| sqlite_synth             | 2.29 us                                                         | 1.86 us: 1.23x faster                                                           |
| scimark_lu               | 89.8 ms                                                         | 73.0 ms: 1.23x faster                                                           |
| unpickle_pure_python     | 189 us                                                          | 155 us: 1.22x faster                                                            |
| pickle_list              | 3.22 us                                                         | 2.63 us: 1.22x faster                                                           |
| sympy_str                | 229 ms                                                          | 189 ms: 1.21x faster                                                            |
| sympy_expand             | 391 ms                                                          | 324 ms: 1.21x faster                                                            |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.74 ms: 1.18x faster                                                           |
| sympy_integrate          | 16.6 ms                                                         | 14.1 ms: 1.18x faster                                                           |
| sqlglot_normalize        | 230 ms                                                          | 196 ms: 1.17x faster                                                            |
| sqlglot_optimize         | 44.7 ms                                                         | 38.3 ms: 1.17x faster                                                           |
| unpickle_list            | 2.98 us                                                         | 2.59 us: 1.15x faster                                                           |
| mako                     | 9.10 ms                                                         | 7.91 ms: 1.15x faster                                                           |
| json                     | 4.76 ms                                                         | 4.14 ms: 1.15x faster                                                           |
| docutils                 | 1.95 sec                                                        | 1.72 sec: 1.14x faster                                                          |
| 2to3                     | 265 ms                                                          | 234 ms: 1.13x faster                                                            |
| fannkuch                 | 317 ms                                                          | 284 ms: 1.12x faster                                                            |
| nbody                    | 79.1 ms                                                         | 71.3 ms: 1.11x faster                                                           |
| xml_etree_parse          | 120 ms                                                          | 110 ms: 1.09x faster                                                            |
| scimark_fft              | 216 ms                                                          | 200 ms: 1.08x faster                                                            |
| bench_thread_pool        | 1.12 ms                                                         | 1.04 ms: 1.07x faster                                                           |
| meteor_contest           | 80.0 ms                                                         | 75.7 ms: 1.06x faster                                                           |
| pickle_dict              | 18.2 us                                                         | 17.3 us: 1.05x faster                                                           |
| json_loads               | 22.4 us                                                         | 21.5 us: 1.04x faster                                                           |
| mdp                      | 1.83 sec                                                        | 1.77 sec: 1.03x faster                                                          |
| async_generators         | 241 ms                                                          | 235 ms: 1.03x faster                                                            |
| xml_etree_process        | 48.1 ms                                                         | 47.0 ms: 1.03x faster                                                           |
| regex_dna                | 131 ms                                                          | 132 ms: 1.01x slower                                                            |
| xml_etree_iterparse      | 70.8 ms                                                         | 72.3 ms: 1.02x slower                                                           |
| unpickle                 | 9.82 us                                                         | 10.2 us: 1.03x slower                                                           |
| pickle                   | 7.83 us                                                         | 8.17 us: 1.04x slower                                                           |
| xml_etree_generate       | 61.6 ms                                                         | 67.2 ms: 1.09x slower                                                           |
| regex_v8                 | 15.8 ms                                                         | 17.4 ms: 1.11x slower                                                           |
| regex_effbot             | 1.66 ms                                                         | 1.95 ms: 1.17x slower                                                           |
| telco                    | 4.83 ms                                                         | 5.81 ms: 1.20x slower                                                           |
| coverage                 | 46.6 ms                                                         | 56.3 ms: 1.21x slower                                                           |
| python_startup_no_site   | 18.1 ms                                                         | 22.1 ms: 1.22x slower                                                           |
| python_startup           | 22.9 ms                                                         | 28.6 ms: 1.25x slower                                                           |
| bench_mp_pool            | 66.4 ms                                                         | 91.5 ms: 1.38x slower                                                           |
| create_gc_cycles         | 694 us                                                          | 1.18 ms: 1.70x slower                                                           |
| gc_traversal             | 1.28 ms                                                         | 2.36 ms: 1.84x slower                                                           |
| Geometric mean           | (ref)                                                           | 1.26x faster                                                                    |

Benchmark hidden because not significant (3): logging_format, asyncio_tcp_ssl, logging_simple
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (12) of results/bm-20250216-3.14.0a5+-359c7dd-CLANG/bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.283x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: unknown