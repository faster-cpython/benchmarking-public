# Results vs. 3.10.4

- fork: mdboom
- ref: aa_test_2025
- machine: windows-x86
- commit hash: 4844db8
- commit date: 2025-01-21
- overall geometric mean: 1.120x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250121-pythonperf1_win32-x86-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 256 ms: 1.04x faster                                                    |
| docutils       | 1.95 sec                                                        | 1.86 sec: 1.05x faster                                                  |
| html5lib       | 52.1 ms                                                         | 48.5 ms: 1.07x faster                                                   |
| Geometric mean | (ref)                                                           | 1.05x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250121-pythonperf1_win32-x86-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|-------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 940 ms                                                          | 463 ms: 2.03x faster                                                    |
| async_tree_cpu_io_mixed | 922 ms                                                          | 456 ms: 2.02x faster                                                    |
| async_tree_none         | 394 ms                                                          | 216 ms: 1.82x faster                                                    |
| async_tree_memoization  | 467 ms                                                          | 267 ms: 1.75x faster                                                    |
| Geometric mean          | (ref)                                                           | 1.90x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250121-pythonperf1_win32-x86-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 202 ms: 2.49x faster                                                    |
| float          | 69.6 ms                                                         | 56.5 ms: 1.23x faster                                                   |
| nbody          | 79.1 ms                                                         | 90.0 ms: 1.14x slower                                                   |
| Geometric mean | (ref)                                                           | 1.39x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250121-pythonperf1_win32-x86-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 117 ms: 1.12x faster                                                    |
| regex_compile  | 117 ms                                                          | 107 ms: 1.09x faster                                                    |
| regex_effbot   | 1.66 ms                                                         | 1.58 ms: 1.05x faster                                                   |
| regex_v8       | 15.8 ms                                                         | 15.5 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                           | 1.07x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250121-pythonperf1_win32-x86-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 1.91 sec                                                        | 1.71 sec: 1.11x faster                                                  |
| xml_etree_parse      | 120 ms                                                          | 109 ms: 1.10x faster                                                    |
| xml_etree_iterparse  | 70.8 ms                                                         | 66.8 ms: 1.06x faster                                                   |
| json_loads           | 22.4 us                                                         | 21.4 us: 1.05x faster                                                   |
| json_dumps           | 9.82 ms                                                         | 9.40 ms: 1.05x faster                                                   |
| unpickle_pure_python | 189 us                                                          | 185 us: 1.02x faster                                                    |
| pickle_pure_python   | 280 us                                                          | 286 us: 1.02x slower                                                    |
| xml_etree_process    | 48.1 ms                                                         | 50.9 ms: 1.06x slower                                                   |
| xml_etree_generate   | 61.6 ms                                                         | 67.9 ms: 1.10x slower                                                   |
| Geometric mean       | (ref)                                                           | 1.02x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250121-pythonperf1_win32-x86-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 20.1 ms: 1.11x slower                                                   |
| python_startup         | 22.9 ms                                                         | 27.0 ms: 1.18x slower                                                   |
| Geometric mean         | (ref)                                                           | 1.14x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250121-pythonperf1_win32-x86-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|-----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 7.69 ms: 1.18x faster                                                   |
| django_template | 36.0 ms                                                         | 33.4 ms: 1.08x faster                                                   |
| genshi_xml      | 46.6 ms                                                         | 46.2 ms: 1.01x faster                                                   |
| genshi_text     | 21.0 ms                                                         | 21.5 ms: 1.03x slower                                                   |
| Geometric mean  | (ref)                                                           | 1.06x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250121-pythonperf1_win32-x86-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|--------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 157 us: 2.53x faster                                                    |
| pidigits                 | 502 ms                                                          | 202 ms: 2.49x faster                                                    |
| async_tree_io            | 940 ms                                                          | 463 ms: 2.03x faster                                                    |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 456 ms: 2.02x faster                                                    |
| async_tree_none          | 394 ms                                                          | 216 ms: 1.82x faster                                                    |
| async_tree_memoization   | 467 ms                                                          | 267 ms: 1.75x faster                                                    |
| pylint                   | 384 ms                                                          | 225 ms: 1.70x faster                                                    |
| deltablue                | 4.04 ms                                                         | 2.70 ms: 1.49x faster                                                   |
| go                       | 146 ms                                                          | 98.5 ms: 1.48x faster                                                   |
| deepcopy_memo            | 29.6 us                                                         | 21.5 us: 1.37x faster                                                   |
| deepcopy                 | 310 us                                                          | 235 us: 1.32x faster                                                    |
| chaos                    | 74.4 ms                                                         | 56.6 ms: 1.32x faster                                                   |
| logging_silent           | 97.9 ns                                                         | 74.6 ns: 1.31x faster                                                   |
| crypto_pyaes             | 81.3 ms                                                         | 63.0 ms: 1.29x faster                                                   |
| pyflate                  | 422 ms                                                          | 340 ms: 1.24x faster                                                    |
| float                    | 69.6 ms                                                         | 56.5 ms: 1.23x faster                                                   |
| sqlglot_parse            | 1.33 ms                                                         | 1.08 ms: 1.23x faster                                                   |
| generators               | 31.6 ms                                                         | 25.7 ms: 1.23x faster                                                   |
| comprehensions           | 17.7 us                                                         | 14.6 us: 1.22x faster                                                   |
| pycparser                | 1.04 sec                                                        | 867 ms: 1.20x faster                                                    |
| scimark_lu               | 89.8 ms                                                         | 75.2 ms: 1.19x faster                                                   |
| sqlglot_transpile        | 1.58 ms                                                         | 1.33 ms: 1.19x faster                                                   |
| thrift                   | 902 us                                                          | 762 us: 1.18x faster                                                    |
| mako                     | 9.10 ms                                                         | 7.69 ms: 1.18x faster                                                   |
| sqlite_synth             | 2.29 us                                                         | 1.94 us: 1.18x faster                                                   |
| hexiom                   | 6.13 ms                                                         | 5.21 ms: 1.18x faster                                                   |
| scimark_sor              | 115 ms                                                          | 99.7 ms: 1.15x faster                                                   |
| scimark_monte_carlo      | 61.9 ms                                                         | 54.1 ms: 1.14x faster                                                   |
| richards_super           | 49.9 ms                                                         | 43.6 ms: 1.14x faster                                                   |
| regex_dna                | 131 ms                                                          | 117 ms: 1.12x faster                                                    |
| tomli_loads              | 1.91 sec                                                        | 1.71 sec: 1.11x faster                                                  |
| spectral_norm            | 80.2 ms                                                         | 72.0 ms: 1.11x faster                                                   |
| dulwich_log              | 58.5 ms                                                         | 52.6 ms: 1.11x faster                                                   |
| nqueens                  | 87.1 ms                                                         | 78.6 ms: 1.11x faster                                                   |
| xml_etree_parse          | 120 ms                                                          | 109 ms: 1.10x faster                                                    |
| sympy_sum                | 122 ms                                                          | 112 ms: 1.10x faster                                                    |
| regex_compile            | 117 ms                                                          | 107 ms: 1.09x faster                                                    |
| raytrace                 | 303 ms                                                          | 280 ms: 1.08x faster                                                    |
| django_template          | 36.0 ms                                                         | 33.4 ms: 1.08x faster                                                   |
| bench_thread_pool        | 1.12 ms                                                         | 1.04 ms: 1.08x faster                                                   |
| html5lib                 | 52.1 ms                                                         | 48.5 ms: 1.07x faster                                                   |
| mdp                      | 1.83 sec                                                        | 1.71 sec: 1.07x faster                                                  |
| xml_etree_iterparse      | 70.8 ms                                                         | 66.8 ms: 1.06x faster                                                   |
| richards                 | 40.3 ms                                                         | 38.0 ms: 1.06x faster                                                   |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.06 ms: 1.06x faster                                                   |
| fannkuch                 | 317 ms                                                          | 300 ms: 1.06x faster                                                    |
| regex_effbot             | 1.66 ms                                                         | 1.58 ms: 1.05x faster                                                   |
| sympy_integrate          | 16.6 ms                                                         | 15.9 ms: 1.05x faster                                                   |
| docutils                 | 1.95 sec                                                        | 1.86 sec: 1.05x faster                                                  |
| json_loads               | 22.4 us                                                         | 21.4 us: 1.05x faster                                                   |
| json_dumps               | 9.82 ms                                                         | 9.40 ms: 1.05x faster                                                   |
| deepcopy_reduce          | 2.68 us                                                         | 2.57 us: 1.04x faster                                                   |
| coroutines               | 17.9 ms                                                         | 17.3 ms: 1.04x faster                                                   |
| 2to3                     | 265 ms                                                          | 256 ms: 1.04x faster                                                    |
| sqlglot_optimize         | 44.7 ms                                                         | 43.5 ms: 1.03x faster                                                   |
| unpickle_pure_python     | 189 us                                                          | 185 us: 1.02x faster                                                    |
| sqlglot_normalize        | 230 ms                                                          | 225 ms: 1.02x faster                                                    |
| sympy_str                | 229 ms                                                          | 224 ms: 1.02x faster                                                    |
| regex_v8                 | 15.8 ms                                                         | 15.5 ms: 1.02x faster                                                   |
| pprint_safe_repr         | 658 ms                                                          | 650 ms: 1.01x faster                                                    |
| genshi_xml               | 46.6 ms                                                         | 46.2 ms: 1.01x faster                                                   |
| pprint_pformat           | 1.37 sec                                                        | 1.36 sec: 1.00x faster                                                  |
| sympy_expand             | 391 ms                                                          | 397 ms: 1.02x slower                                                    |
| meteor_contest           | 80.0 ms                                                         | 81.7 ms: 1.02x slower                                                   |
| pickle_pure_python       | 280 us                                                          | 286 us: 1.02x slower                                                    |
| genshi_text              | 21.0 ms                                                         | 21.5 ms: 1.03x slower                                                   |
| scimark_fft              | 216 ms                                                          | 228 ms: 1.05x slower                                                    |
| xml_etree_process        | 48.1 ms                                                         | 50.9 ms: 1.06x slower                                                   |
| pathlib                  | 81.2 ms                                                         | 87.8 ms: 1.08x slower                                                   |
| xml_etree_generate       | 61.6 ms                                                         | 67.9 ms: 1.10x slower                                                   |
| python_startup_no_site   | 18.1 ms                                                         | 20.1 ms: 1.11x slower                                                   |
| logging_format           | 7.91 us                                                         | 8.85 us: 1.12x slower                                                   |
| logging_simple           | 7.29 us                                                         | 8.23 us: 1.13x slower                                                   |
| nbody                    | 79.1 ms                                                         | 90.0 ms: 1.14x slower                                                   |
| coverage                 | 46.6 ms                                                         | 54.4 ms: 1.17x slower                                                   |
| python_startup           | 22.9 ms                                                         | 27.0 ms: 1.18x slower                                                   |
| async_generators         | 241 ms                                                          | 300 ms: 1.25x slower                                                    |
| gc_traversal             | 1.28 ms                                                         | 1.78 ms: 1.39x slower                                                   |
| telco                    | 4.83 ms                                                         | 6.84 ms: 1.42x slower                                                   |
| bench_mp_pool            | 66.4 ms                                                         | 94.7 ms: 1.43x slower                                                   |
| create_gc_cycles         | 694 us                                                          | 1.06 ms: 1.53x slower                                                   |
| Geometric mean           | (ref)                                                           | 1.11x faster                                                            |

Benchmark hidden because not significant (1): json
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250121-3.14.0a4+-4844db8/bm-20250121-pythonperf1_win32-x86-mdboom-aa_test_2025-3.14.0a4+-4844db8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.120x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: unknown