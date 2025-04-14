# Results vs. 3.10.4

- fork: python
- ref: 425f60b9eb253c57bc32
- machine: windows-x86
- commit hash: 425f60b
- commit date: 2025-03-29
- overall geometric mean: 1.009x faster
- HPT reliability: 65.99%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250329-pythonperf1_win32-x86-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 278 ms: 1.05x slower                                                            |
| docutils       | 1.95 sec                                                        | 3.16 sec: 1.62x slower                                                          |
| Geometric mean | (ref)                                                           | 1.19x slower                                                                    |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250329-pythonperf1_win32-x86-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io           | 940 ms                                                          | 445 ms: 2.12x faster                                                            |
| async_tree_cpu_io_mixed | 922 ms                                                          | 459 ms: 2.01x faster                                                            |
| async_tree_none         | 394 ms                                                          | 215 ms: 1.83x faster                                                            |
| async_tree_memoization  | 467 ms                                                          | 265 ms: 1.76x faster                                                            |
| Geometric mean          | (ref)                                                           | 1.92x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250329-pythonperf1_win32-x86-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 187 ms: 2.68x faster                                                            |
| float          | 69.6 ms                                                         | 62.5 ms: 1.11x faster                                                           |
| nbody          | 79.1 ms                                                         | 133 ms: 1.68x slower                                                            |
| Geometric mean | (ref)                                                           | 1.21x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250329-pythonperf1_win32-x86-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 107 ms: 1.22x faster                                                            |
| regex_v8       | 15.8 ms                                                         | 13.5 ms: 1.17x faster                                                           |
| regex_effbot   | 1.66 ms                                                         | 1.54 ms: 1.08x faster                                                           |
| regex_compile  | 117 ms                                                          | 127 ms: 1.09x slower                                                            |
| Geometric mean | (ref)                                                           | 1.09x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250329-pythonperf1_win32-x86-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_parse      | 120 ms                                                          | 107 ms: 1.13x faster                                                            |
| json_dumps           | 9.82 ms                                                         | 8.81 ms: 1.12x faster                                                           |
| xml_etree_iterparse  | 70.8 ms                                                         | 67.0 ms: 1.06x faster                                                           |
| pickle_pure_python   | 280 us                                                          | 301 us: 1.07x slower                                                            |
| unpickle_pure_python | 189 us                                                          | 210 us: 1.11x slower                                                            |
| xml_etree_process    | 48.1 ms                                                         | 54.8 ms: 1.14x slower                                                           |
| json_loads           | 22.4 us                                                         | 25.6 us: 1.14x slower                                                           |
| xml_etree_generate   | 61.6 ms                                                         | 73.3 ms: 1.19x slower                                                           |
| pickle_list          | 3.22 us                                                         | 3.87 us: 1.20x slower                                                           |
| unpickle_list        | 2.98 us                                                         | 3.64 us: 1.22x slower                                                           |
| unpickle             | 9.82 us                                                         | 12.3 us: 1.25x slower                                                           |
| pickle               | 7.83 us                                                         | 10.3 us: 1.32x slower                                                           |
| pickle_dict          | 18.2 us                                                         | 24.3 us: 1.33x slower                                                           |
| tomli_loads          | 1.91 sec                                                        | 3.64 sec: 1.91x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.17x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250329-pythonperf1_win32-x86-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 29.8 ms: 1.30x slower                                                           |
| python_startup_no_site | 18.1 ms                                                         | 23.8 ms: 1.32x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.31x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250329-pythonperf1_win32-x86-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| django_template | 36.0 ms                                                         | 38.8 ms: 1.08x slower                                                           |
| genshi_xml      | 46.6 ms                                                         | 59.6 ms: 1.28x slower                                                           |
| mako            | 9.10 ms                                                         | 11.7 ms: 1.28x slower                                                           |
| genshi_text     | 21.0 ms                                                         | 27.2 ms: 1.30x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.23x slower                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250329-pythonperf1_win32-x86-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits                 | 502 ms                                                          | 187 ms: 2.68x faster                                                            |
| typing_runtime_protocols | 396 us                                                          | 180 us: 2.20x faster                                                            |
| pathlib                  | 81.2 ms                                                         | 37.8 ms: 2.15x faster                                                           |
| async_tree_io            | 940 ms                                                          | 445 ms: 2.12x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 459 ms: 2.01x faster                                                            |
| async_tree_none          | 394 ms                                                          | 215 ms: 1.83x faster                                                            |
| async_tree_memoization   | 467 ms                                                          | 265 ms: 1.76x faster                                                            |
| pylint                   | 384 ms                                                          | 249 ms: 1.54x faster                                                            |
| sqlite_synth             | 2.29 us                                                         | 1.61 us: 1.42x faster                                                           |
| deltablue                | 4.04 ms                                                         | 3.11 ms: 1.30x faster                                                           |
| generators               | 31.6 ms                                                         | 25.9 ms: 1.22x faster                                                           |
| asyncio_tcp              | 744 ms                                                          | 610 ms: 1.22x faster                                                            |
| regex_dna                | 131 ms                                                          | 107 ms: 1.22x faster                                                            |
| logging_silent           | 97.9 ns                                                         | 80.9 ns: 1.21x faster                                                           |
| mdp                      | 1.83 sec                                                        | 1.52 sec: 1.20x faster                                                          |
| gc_traversal             | 1.28 ms                                                         | 1.07 ms: 1.19x faster                                                           |
| regex_v8                 | 15.8 ms                                                         | 13.5 ms: 1.17x faster                                                           |
| thrift                   | 902 us                                                          | 793 us: 1.14x faster                                                            |
| xml_etree_parse          | 120 ms                                                          | 107 ms: 1.13x faster                                                            |
| chaos                    | 74.4 ms                                                         | 66.4 ms: 1.12x faster                                                           |
| json_dumps               | 9.82 ms                                                         | 8.81 ms: 1.12x faster                                                           |
| float                    | 69.6 ms                                                         | 62.5 ms: 1.11x faster                                                           |
| deepcopy                 | 310 us                                                          | 280 us: 1.11x faster                                                            |
| deepcopy_memo            | 29.6 us                                                         | 27.0 us: 1.09x faster                                                           |
| go                       | 146 ms                                                          | 133 ms: 1.09x faster                                                            |
| crypto_pyaes             | 81.3 ms                                                         | 74.7 ms: 1.09x faster                                                           |
| raytrace                 | 303 ms                                                          | 280 ms: 1.08x faster                                                            |
| regex_effbot             | 1.66 ms                                                         | 1.54 ms: 1.08x faster                                                           |
| dulwich_log              | 58.5 ms                                                         | 54.3 ms: 1.08x faster                                                           |
| scimark_lu               | 89.8 ms                                                         | 83.4 ms: 1.08x faster                                                           |
| scimark_sor              | 115 ms                                                          | 108 ms: 1.06x faster                                                            |
| comprehensions           | 17.7 us                                                         | 16.8 us: 1.06x faster                                                           |
| xml_etree_iterparse      | 70.8 ms                                                         | 67.0 ms: 1.06x faster                                                           |
| coroutines               | 17.9 ms                                                         | 17.1 ms: 1.05x faster                                                           |
| pyflate                  | 422 ms                                                          | 417 ms: 1.01x faster                                                            |
| hexiom                   | 6.13 ms                                                         | 6.07 ms: 1.01x faster                                                           |
| sympy_sum                | 122 ms                                                          | 125 ms: 1.02x slower                                                            |
| nqueens                  | 87.1 ms                                                         | 90.0 ms: 1.03x slower                                                           |
| 2to3                     | 265 ms                                                          | 278 ms: 1.05x slower                                                            |
| richards_super           | 49.9 ms                                                         | 52.7 ms: 1.06x slower                                                           |
| pickle_pure_python       | 280 us                                                          | 301 us: 1.07x slower                                                            |
| django_template          | 36.0 ms                                                         | 38.8 ms: 1.08x slower                                                           |
| spectral_norm            | 80.2 ms                                                         | 86.9 ms: 1.08x slower                                                           |
| regex_compile            | 117 ms                                                          | 127 ms: 1.09x slower                                                            |
| sympy_integrate          | 16.6 ms                                                         | 18.1 ms: 1.09x slower                                                           |
| sympy_str                | 229 ms                                                          | 250 ms: 1.09x slower                                                            |
| sympy_expand             | 391 ms                                                          | 431 ms: 1.10x slower                                                            |
| unpickle_pure_python     | 189 us                                                          | 210 us: 1.11x slower                                                            |
| scimark_monte_carlo      | 61.9 ms                                                         | 69.1 ms: 1.12x slower                                                           |
| deepcopy_reduce          | 2.68 us                                                         | 3.02 us: 1.13x slower                                                           |
| pycparser                | 1.04 sec                                                        | 1.18 sec: 1.13x slower                                                          |
| xml_etree_process        | 48.1 ms                                                         | 54.8 ms: 1.14x slower                                                           |
| json_loads               | 22.4 us                                                         | 25.6 us: 1.14x slower                                                           |
| bench_thread_pool        | 1.12 ms                                                         | 1.29 ms: 1.15x slower                                                           |
| xml_etree_generate       | 61.6 ms                                                         | 73.3 ms: 1.19x slower                                                           |
| richards                 | 40.3 ms                                                         | 47.9 ms: 1.19x slower                                                           |
| pickle_list              | 3.22 us                                                         | 3.87 us: 1.20x slower                                                           |
| meteor_contest           | 80.0 ms                                                         | 96.3 ms: 1.20x slower                                                           |
| unpickle_list            | 2.98 us                                                         | 3.64 us: 1.22x slower                                                           |
| fannkuch                 | 317 ms                                                          | 389 ms: 1.23x slower                                                            |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.98 ms: 1.23x slower                                                           |
| bench_mp_pool            | 66.4 ms                                                         | 82.2 ms: 1.24x slower                                                           |
| unpickle                 | 9.82 us                                                         | 12.3 us: 1.25x slower                                                           |
| create_gc_cycles         | 694 us                                                          | 872 us: 1.26x slower                                                            |
| logging_format           | 7.91 us                                                         | 10.0 us: 1.27x slower                                                           |
| logging_simple           | 7.29 us                                                         | 9.31 us: 1.28x slower                                                           |
| genshi_xml               | 46.6 ms                                                         | 59.6 ms: 1.28x slower                                                           |
| mako                     | 9.10 ms                                                         | 11.7 ms: 1.28x slower                                                           |
| python_startup           | 22.9 ms                                                         | 29.8 ms: 1.30x slower                                                           |
| genshi_text              | 21.0 ms                                                         | 27.2 ms: 1.30x slower                                                           |
| unpack_sequence          | 40.0 ns                                                         | 52.1 ns: 1.30x slower                                                           |
| async_generators         | 241 ms                                                          | 313 ms: 1.30x slower                                                            |
| pprint_safe_repr         | 658 ms                                                          | 857 ms: 1.30x slower                                                            |
| python_startup_no_site   | 18.1 ms                                                         | 23.8 ms: 1.32x slower                                                           |
| pickle                   | 7.83 us                                                         | 10.3 us: 1.32x slower                                                           |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 22.6 sec: 1.33x slower                                                          |
| scimark_fft              | 216 ms                                                          | 288 ms: 1.33x slower                                                            |
| pickle_dict              | 18.2 us                                                         | 24.3 us: 1.33x slower                                                           |
| telco                    | 4.83 ms                                                         | 7.44 ms: 1.54x slower                                                           |
| coverage                 | 46.6 ms                                                         | 74.0 ms: 1.59x slower                                                           |
| docutils                 | 1.95 sec                                                        | 3.16 sec: 1.62x slower                                                          |
| nbody                    | 79.1 ms                                                         | 133 ms: 1.68x slower                                                            |
| pprint_pformat           | 1.37 sec                                                        | 2.49 sec: 1.82x slower                                                          |
| tomli_loads              | 1.91 sec                                                        | 3.64 sec: 1.91x slower                                                          |
| Geometric mean           | (ref)                                                           | 1.02x slower                                                                    |

Benchmark hidden because not significant (2): html5lib, json
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250329-3.14.0a6+-425f60b-NOGIL/bm-20250329-pythonperf1_win32-x86-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.009x faster

# HPT report

- Reliability score: 65.99% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown