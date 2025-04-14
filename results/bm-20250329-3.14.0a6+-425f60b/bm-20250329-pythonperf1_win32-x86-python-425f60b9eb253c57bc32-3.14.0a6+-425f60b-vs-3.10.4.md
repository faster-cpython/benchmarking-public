# Results vs. 3.10.4

- fork: python
- ref: 425f60b9eb253c57bc32
- machine: windows-x86
- commit hash: 425f60b
- commit date: 2025-03-29
- overall geometric mean: 1.130x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250329-pythonperf1_win32-x86-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| docutils       | 1.95 sec                                                        | 1.88 sec: 1.04x faster                                                          |
| html5lib       | 52.1 ms                                                         | 48.6 ms: 1.07x faster                                                           |
| Geometric mean | (ref)                                                           | 1.04x faster                                                                    |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250329-pythonperf1_win32-x86-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io           | 940 ms                                                          | 470 ms: 2.00x faster                                                            |
| async_tree_cpu_io_mixed | 922 ms                                                          | 466 ms: 1.98x faster                                                            |
| async_tree_memoization  | 467 ms                                                          | 258 ms: 1.81x faster                                                            |
| async_tree_none         | 394 ms                                                          | 221 ms: 1.78x faster                                                            |
| Geometric mean          | (ref)                                                           | 1.89x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250329-pythonperf1_win32-x86-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 200 ms: 2.51x faster                                                            |
| float          | 69.6 ms                                                         | 54.2 ms: 1.28x faster                                                           |
| nbody          | 79.1 ms                                                         | 85.9 ms: 1.09x slower                                                           |
| Geometric mean | (ref)                                                           | 1.44x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250329-pythonperf1_win32-x86-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 119 ms: 1.10x faster                                                            |
| regex_compile  | 117 ms                                                          | 108 ms: 1.08x faster                                                            |
| regex_effbot   | 1.66 ms                                                         | 1.57 ms: 1.06x faster                                                           |
| regex_v8       | 15.8 ms                                                         | 15.1 ms: 1.04x faster                                                           |
| Geometric mean | (ref)                                                           | 1.07x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250329-pythonperf1_win32-x86-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 8.18 ms: 1.20x faster                                                           |
| xml_etree_parse      | 120 ms                                                          | 112 ms: 1.07x faster                                                            |
| tomli_loads          | 1.91 sec                                                        | 1.79 sec: 1.07x faster                                                          |
| xml_etree_iterparse  | 70.8 ms                                                         | 67.4 ms: 1.05x faster                                                           |
| pickle_pure_python   | 280 us                                                          | 271 us: 1.03x faster                                                            |
| json_loads           | 22.4 us                                                         | 21.8 us: 1.03x faster                                                           |
| unpickle_pure_python | 189 us                                                          | 186 us: 1.02x faster                                                            |
| unpickle_list        | 2.98 us                                                         | 3.08 us: 1.03x slower                                                           |
| xml_etree_process    | 48.1 ms                                                         | 52.0 ms: 1.08x slower                                                           |
| xml_etree_generate   | 61.6 ms                                                         | 69.4 ms: 1.13x slower                                                           |
| unpickle             | 9.82 us                                                         | 11.2 us: 1.14x slower                                                           |
| pickle_dict          | 18.2 us                                                         | 21.2 us: 1.16x slower                                                           |
| pickle_list          | 3.22 us                                                         | 3.82 us: 1.19x slower                                                           |
| pickle               | 7.83 us                                                         | 9.35 us: 1.19x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.03x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250329-pythonperf1_win32-x86-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 22.7 ms: 1.25x slower                                                           |
| python_startup         | 22.9 ms                                                         | 28.8 ms: 1.26x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.26x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250329-pythonperf1_win32-x86-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako           | 9.10 ms                                                         | 8.37 ms: 1.09x faster                                                           |
| genshi_text    | 21.0 ms                                                         | 23.0 ms: 1.10x slower                                                           |
| genshi_xml     | 46.6 ms                                                         | 53.8 ms: 1.15x slower                                                           |
| Geometric mean | (ref)                                                           | 1.04x slower                                                                    |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250329-pythonperf1_win32-x86-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 157 us: 2.53x faster                                                            |
| pidigits                 | 502 ms                                                          | 200 ms: 2.51x faster                                                            |
| pathlib                  | 81.2 ms                                                         | 37.7 ms: 2.15x faster                                                           |
| async_tree_io            | 940 ms                                                          | 470 ms: 2.00x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 466 ms: 1.98x faster                                                            |
| async_tree_memoization   | 467 ms                                                          | 258 ms: 1.81x faster                                                            |
| async_tree_none          | 394 ms                                                          | 221 ms: 1.78x faster                                                            |
| mdp                      | 1.83 sec                                                        | 1.03 sec: 1.77x faster                                                          |
| pylint                   | 384 ms                                                          | 227 ms: 1.69x faster                                                            |
| deltablue                | 4.04 ms                                                         | 2.65 ms: 1.52x faster                                                           |
| logging_silent           | 97.9 ns                                                         | 67.0 ns: 1.46x faster                                                           |
| deepcopy_memo            | 29.6 us                                                         | 20.4 us: 1.45x faster                                                           |
| chaos                    | 74.4 ms                                                         | 56.2 ms: 1.32x faster                                                           |
| scimark_lu               | 89.8 ms                                                         | 68.2 ms: 1.32x faster                                                           |
| go                       | 146 ms                                                          | 111 ms: 1.31x faster                                                            |
| float                    | 69.6 ms                                                         | 54.2 ms: 1.28x faster                                                           |
| crypto_pyaes             | 81.3 ms                                                         | 64.4 ms: 1.26x faster                                                           |
| raytrace                 | 303 ms                                                          | 240 ms: 1.26x faster                                                            |
| deepcopy                 | 310 us                                                          | 248 us: 1.25x faster                                                            |
| comprehensions           | 17.7 us                                                         | 14.4 us: 1.24x faster                                                           |
| generators               | 31.6 ms                                                         | 25.6 ms: 1.23x faster                                                           |
| json_dumps               | 9.82 ms                                                         | 8.18 ms: 1.20x faster                                                           |
| sqlite_synth             | 2.29 us                                                         | 1.92 us: 1.19x faster                                                           |
| scimark_sor              | 115 ms                                                          | 96.8 ms: 1.19x faster                                                           |
| hexiom                   | 6.13 ms                                                         | 5.19 ms: 1.18x faster                                                           |
| asyncio_tcp              | 744 ms                                                          | 631 ms: 1.18x faster                                                            |
| scimark_monte_carlo      | 61.9 ms                                                         | 52.7 ms: 1.18x faster                                                           |
| pyflate                  | 422 ms                                                          | 365 ms: 1.15x faster                                                            |
| richards_super           | 49.9 ms                                                         | 43.8 ms: 1.14x faster                                                           |
| pycparser                | 1.04 sec                                                        | 917 ms: 1.14x faster                                                            |
| dulwich_log              | 58.5 ms                                                         | 52.4 ms: 1.12x faster                                                           |
| spectral_norm            | 80.2 ms                                                         | 71.9 ms: 1.12x faster                                                           |
| sympy_sum                | 122 ms                                                          | 112 ms: 1.10x faster                                                            |
| coroutines               | 17.9 ms                                                         | 16.3 ms: 1.10x faster                                                           |
| regex_dna                | 131 ms                                                          | 119 ms: 1.10x faster                                                            |
| mako                     | 9.10 ms                                                         | 8.37 ms: 1.09x faster                                                           |
| regex_compile            | 117 ms                                                          | 108 ms: 1.08x faster                                                            |
| html5lib                 | 52.1 ms                                                         | 48.6 ms: 1.07x faster                                                           |
| xml_etree_parse          | 120 ms                                                          | 112 ms: 1.07x faster                                                            |
| tomli_loads              | 1.91 sec                                                        | 1.79 sec: 1.07x faster                                                          |
| regex_effbot             | 1.66 ms                                                         | 1.57 ms: 1.06x faster                                                           |
| sympy_integrate          | 16.6 ms                                                         | 15.7 ms: 1.06x faster                                                           |
| xml_etree_iterparse      | 70.8 ms                                                         | 67.4 ms: 1.05x faster                                                           |
| nqueens                  | 87.1 ms                                                         | 83.1 ms: 1.05x faster                                                           |
| regex_v8                 | 15.8 ms                                                         | 15.1 ms: 1.04x faster                                                           |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.11 ms: 1.04x faster                                                           |
| richards                 | 40.3 ms                                                         | 38.7 ms: 1.04x faster                                                           |
| docutils                 | 1.95 sec                                                        | 1.88 sec: 1.04x faster                                                          |
| pickle_pure_python       | 280 us                                                          | 271 us: 1.03x faster                                                            |
| json_loads               | 22.4 us                                                         | 21.8 us: 1.03x faster                                                           |
| unpack_sequence          | 40.0 ns                                                         | 39.2 ns: 1.02x faster                                                           |
| unpickle_pure_python     | 189 us                                                          | 186 us: 1.02x faster                                                            |
| deepcopy_reduce          | 2.68 us                                                         | 2.65 us: 1.01x faster                                                           |
| sympy_str                | 229 ms                                                          | 226 ms: 1.01x faster                                                            |
| pprint_pformat           | 1.37 sec                                                        | 1.36 sec: 1.01x faster                                                          |
| sympy_expand             | 391 ms                                                          | 401 ms: 1.03x slower                                                            |
| unpickle_list            | 2.98 us                                                         | 3.08 us: 1.03x slower                                                           |
| meteor_contest           | 80.0 ms                                                         | 83.4 ms: 1.04x slower                                                           |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 17.8 sec: 1.05x slower                                                          |
| scimark_fft              | 216 ms                                                          | 230 ms: 1.07x slower                                                            |
| xml_etree_process        | 48.1 ms                                                         | 52.0 ms: 1.08x slower                                                           |
| nbody                    | 79.1 ms                                                         | 85.9 ms: 1.09x slower                                                           |
| genshi_text              | 21.0 ms                                                         | 23.0 ms: 1.10x slower                                                           |
| xml_etree_generate       | 61.6 ms                                                         | 69.4 ms: 1.13x slower                                                           |
| unpickle                 | 9.82 us                                                         | 11.2 us: 1.14x slower                                                           |
| coverage                 | 46.6 ms                                                         | 53.3 ms: 1.14x slower                                                           |
| genshi_xml               | 46.6 ms                                                         | 53.8 ms: 1.15x slower                                                           |
| bench_thread_pool        | 1.12 ms                                                         | 1.30 ms: 1.16x slower                                                           |
| pickle_dict              | 18.2 us                                                         | 21.2 us: 1.16x slower                                                           |
| pickle_list              | 3.22 us                                                         | 3.82 us: 1.19x slower                                                           |
| pickle                   | 7.83 us                                                         | 9.35 us: 1.19x slower                                                           |
| logging_format           | 7.91 us                                                         | 9.58 us: 1.21x slower                                                           |
| logging_simple           | 7.29 us                                                         | 8.85 us: 1.21x slower                                                           |
| async_generators         | 241 ms                                                          | 299 ms: 1.24x slower                                                            |
| python_startup_no_site   | 18.1 ms                                                         | 22.7 ms: 1.25x slower                                                           |
| python_startup           | 22.9 ms                                                         | 28.8 ms: 1.26x slower                                                           |
| gc_traversal             | 1.28 ms                                                         | 1.82 ms: 1.42x slower                                                           |
| bench_mp_pool            | 66.4 ms                                                         | 95.2 ms: 1.43x slower                                                           |
| telco                    | 4.83 ms                                                         | 7.07 ms: 1.46x slower                                                           |
| create_gc_cycles         | 694 us                                                          | 1.06 ms: 1.53x slower                                                           |
| Geometric mean           | (ref)                                                           | 1.10x faster                                                                    |

Benchmark hidden because not significant (5): json, 2to3, fannkuch, django_template, pprint_safe_repr
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (16) of results/bm-20250329-3.14.0a6+-425f60b/bm-20250329-pythonperf1_win32-x86-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.130x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: unknown