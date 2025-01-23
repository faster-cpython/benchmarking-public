# Results vs. 3.10.4

- fork: mdboom
- ref: aa_test_2025_2
- machine: windows-x86
- commit hash: 8ffb2c1
- commit date: 2025-01-23
- overall geometric mean: 1.116x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250123-pythonperf1_win32-x86-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 254 ms: 1.05x faster                                                      |
| docutils       | 1.95 sec                                                        | 1.86 sec: 1.05x faster                                                    |
| html5lib       | 52.1 ms                                                         | 46.9 ms: 1.11x faster                                                     |
| Geometric mean | (ref)                                                           | 1.07x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250123-pythonperf1_win32-x86-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io           | 940 ms                                                          | 462 ms: 2.04x faster                                                      |
| async_tree_cpu_io_mixed | 922 ms                                                          | 455 ms: 2.03x faster                                                      |
| async_tree_none         | 394 ms                                                          | 212 ms: 1.86x faster                                                      |
| async_tree_memoization  | 467 ms                                                          | 261 ms: 1.79x faster                                                      |
| Geometric mean          | (ref)                                                           | 1.93x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250123-pythonperf1_win32-x86-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 202 ms: 2.49x faster                                                      |
| float          | 69.6 ms                                                         | 57.8 ms: 1.20x faster                                                     |
| nbody          | 79.1 ms                                                         | 87.3 ms: 1.10x slower                                                     |
| Geometric mean | (ref)                                                           | 1.40x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250123-pythonperf1_win32-x86-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 107 ms: 1.09x faster                                                      |
| regex_dna      | 131 ms                                                          | 123 ms: 1.06x faster                                                      |
| regex_effbot   | 1.66 ms                                                         | 1.59 ms: 1.05x faster                                                     |
| regex_v8       | 15.8 ms                                                         | 16.6 ms: 1.05x slower                                                     |
| Geometric mean | (ref)                                                           | 1.04x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250123-pythonperf1_win32-x86-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 1.91 sec                                                        | 1.66 sec: 1.15x faster                                                    |
| xml_etree_parse      | 120 ms                                                          | 108 ms: 1.11x faster                                                      |
| json_loads           | 22.4 us                                                         | 21.3 us: 1.05x faster                                                     |
| xml_etree_iterparse  | 70.8 ms                                                         | 67.4 ms: 1.05x faster                                                     |
| json_dumps           | 9.82 ms                                                         | 9.41 ms: 1.04x faster                                                     |
| unpickle_pure_python | 189 us                                                          | 186 us: 1.02x faster                                                      |
| pickle_pure_python   | 280 us                                                          | 286 us: 1.02x slower                                                      |
| xml_etree_process    | 48.1 ms                                                         | 52.4 ms: 1.09x slower                                                     |
| xml_etree_generate   | 61.6 ms                                                         | 69.3 ms: 1.12x slower                                                     |
| Geometric mean       | (ref)                                                           | 1.02x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250123-pythonperf1_win32-x86-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 20.0 ms: 1.11x slower                                                     |
| python_startup         | 22.9 ms                                                         | 26.8 ms: 1.17x slower                                                     |
| Geometric mean         | (ref)                                                           | 1.14x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250123-pythonperf1_win32-x86-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 7.81 ms: 1.17x faster                                                     |
| django_template | 36.0 ms                                                         | 34.2 ms: 1.05x faster                                                     |
| genshi_text     | 21.0 ms                                                         | 22.0 ms: 1.05x slower                                                     |
| Geometric mean  | (ref)                                                           | 1.04x faster                                                              |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250123-pythonperf1_win32-x86-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pidigits                 | 502 ms                                                          | 202 ms: 2.49x faster                                                      |
| typing_runtime_protocols | 396 us                                                          | 159 us: 2.49x faster                                                      |
| async_tree_io            | 940 ms                                                          | 462 ms: 2.04x faster                                                      |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 455 ms: 2.03x faster                                                      |
| async_tree_none          | 394 ms                                                          | 212 ms: 1.86x faster                                                      |
| async_tree_memoization   | 467 ms                                                          | 261 ms: 1.79x faster                                                      |
| pylint                   | 384 ms                                                          | 226 ms: 1.70x faster                                                      |
| deltablue                | 4.04 ms                                                         | 2.71 ms: 1.49x faster                                                     |
| go                       | 146 ms                                                          | 101 ms: 1.44x faster                                                      |
| deepcopy_memo            | 29.6 us                                                         | 21.6 us: 1.37x faster                                                     |
| logging_silent           | 97.9 ns                                                         | 74.5 ns: 1.31x faster                                                     |
| crypto_pyaes             | 81.3 ms                                                         | 62.4 ms: 1.30x faster                                                     |
| deepcopy                 | 310 us                                                          | 245 us: 1.27x faster                                                      |
| chaos                    | 74.4 ms                                                         | 59.3 ms: 1.25x faster                                                     |
| sqlglot_parse            | 1.33 ms                                                         | 1.07 ms: 1.24x faster                                                     |
| pyflate                  | 422 ms                                                          | 341 ms: 1.24x faster                                                      |
| comprehensions           | 17.7 us                                                         | 14.4 us: 1.23x faster                                                     |
| generators               | 31.6 ms                                                         | 26.0 ms: 1.21x faster                                                     |
| float                    | 69.6 ms                                                         | 57.8 ms: 1.20x faster                                                     |
| thrift                   | 902 us                                                          | 749 us: 1.20x faster                                                      |
| scimark_lu               | 89.8 ms                                                         | 74.9 ms: 1.20x faster                                                     |
| sqlglot_transpile        | 1.58 ms                                                         | 1.32 ms: 1.20x faster                                                     |
| pycparser                | 1.04 sec                                                        | 869 ms: 1.20x faster                                                      |
| sqlite_synth             | 2.29 us                                                         | 1.94 us: 1.18x faster                                                     |
| hexiom                   | 6.13 ms                                                         | 5.25 ms: 1.17x faster                                                     |
| mako                     | 9.10 ms                                                         | 7.81 ms: 1.17x faster                                                     |
| tomli_loads              | 1.91 sec                                                        | 1.66 sec: 1.15x faster                                                    |
| richards_super           | 49.9 ms                                                         | 43.5 ms: 1.15x faster                                                     |
| scimark_sor              | 115 ms                                                          | 103 ms: 1.12x faster                                                      |
| scimark_monte_carlo      | 61.9 ms                                                         | 55.3 ms: 1.12x faster                                                     |
| dulwich_log              | 58.5 ms                                                         | 52.3 ms: 1.12x faster                                                     |
| sympy_sum                | 122 ms                                                          | 110 ms: 1.11x faster                                                      |
| html5lib                 | 52.1 ms                                                         | 46.9 ms: 1.11x faster                                                     |
| xml_etree_parse          | 120 ms                                                          | 108 ms: 1.11x faster                                                      |
| spectral_norm            | 80.2 ms                                                         | 72.5 ms: 1.11x faster                                                     |
| nqueens                  | 87.1 ms                                                         | 79.4 ms: 1.10x faster                                                     |
| bench_thread_pool        | 1.12 ms                                                         | 1.02 ms: 1.10x faster                                                     |
| regex_compile            | 117 ms                                                          | 107 ms: 1.09x faster                                                      |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.01 ms: 1.08x faster                                                     |
| coroutines               | 17.9 ms                                                         | 16.9 ms: 1.06x faster                                                     |
| regex_dna                | 131 ms                                                          | 123 ms: 1.06x faster                                                      |
| mdp                      | 1.83 sec                                                        | 1.72 sec: 1.06x faster                                                    |
| fannkuch                 | 317 ms                                                          | 299 ms: 1.06x faster                                                      |
| json                     | 4.76 ms                                                         | 4.50 ms: 1.06x faster                                                     |
| django_template          | 36.0 ms                                                         | 34.2 ms: 1.05x faster                                                     |
| json_loads               | 22.4 us                                                         | 21.3 us: 1.05x faster                                                     |
| xml_etree_iterparse      | 70.8 ms                                                         | 67.4 ms: 1.05x faster                                                     |
| docutils                 | 1.95 sec                                                        | 1.86 sec: 1.05x faster                                                    |
| regex_effbot             | 1.66 ms                                                         | 1.59 ms: 1.05x faster                                                     |
| 2to3                     | 265 ms                                                          | 254 ms: 1.05x faster                                                      |
| json_dumps               | 9.82 ms                                                         | 9.41 ms: 1.04x faster                                                     |
| deepcopy_reduce          | 2.68 us                                                         | 2.57 us: 1.04x faster                                                     |
| sympy_integrate          | 16.6 ms                                                         | 16.0 ms: 1.04x faster                                                     |
| richards                 | 40.3 ms                                                         | 38.7 ms: 1.04x faster                                                     |
| sympy_str                | 229 ms                                                          | 222 ms: 1.03x faster                                                      |
| raytrace                 | 303 ms                                                          | 293 ms: 1.03x faster                                                      |
| unpickle_pure_python     | 189 us                                                          | 186 us: 1.02x faster                                                      |
| pprint_pformat           | 1.37 sec                                                        | 1.35 sec: 1.02x faster                                                    |
| pprint_safe_repr         | 658 ms                                                          | 650 ms: 1.01x faster                                                      |
| sqlglot_optimize         | 44.7 ms                                                         | 44.5 ms: 1.00x faster                                                     |
| sympy_expand             | 391 ms                                                          | 392 ms: 1.00x slower                                                      |
| sqlglot_normalize        | 230 ms                                                          | 233 ms: 1.01x slower                                                      |
| pickle_pure_python       | 280 us                                                          | 286 us: 1.02x slower                                                      |
| meteor_contest           | 80.0 ms                                                         | 82.3 ms: 1.03x slower                                                     |
| genshi_text              | 21.0 ms                                                         | 22.0 ms: 1.05x slower                                                     |
| regex_v8                 | 15.8 ms                                                         | 16.6 ms: 1.05x slower                                                     |
| scimark_fft              | 216 ms                                                          | 228 ms: 1.05x slower                                                      |
| pathlib                  | 81.2 ms                                                         | 86.1 ms: 1.06x slower                                                     |
| xml_etree_process        | 48.1 ms                                                         | 52.4 ms: 1.09x slower                                                     |
| nbody                    | 79.1 ms                                                         | 87.3 ms: 1.10x slower                                                     |
| python_startup_no_site   | 18.1 ms                                                         | 20.0 ms: 1.11x slower                                                     |
| xml_etree_generate       | 61.6 ms                                                         | 69.3 ms: 1.12x slower                                                     |
| logging_format           | 7.91 us                                                         | 9.05 us: 1.14x slower                                                     |
| logging_simple           | 7.29 us                                                         | 8.42 us: 1.16x slower                                                     |
| coverage                 | 46.6 ms                                                         | 53.8 ms: 1.16x slower                                                     |
| python_startup           | 22.9 ms                                                         | 26.8 ms: 1.17x slower                                                     |
| async_generators         | 241 ms                                                          | 303 ms: 1.26x slower                                                      |
| gc_traversal             | 1.28 ms                                                         | 1.79 ms: 1.40x slower                                                     |
| bench_mp_pool            | 66.4 ms                                                         | 94.8 ms: 1.43x slower                                                     |
| telco                    | 4.83 ms                                                         | 7.09 ms: 1.47x slower                                                     |
| create_gc_cycles         | 694 us                                                          | 1.05 ms: 1.52x slower                                                     |
| Geometric mean           | (ref)                                                           | 1.11x faster                                                              |

Benchmark hidden because not significant (1): genshi_xml
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250123-3.14.0a4+-8ffb2c1/bm-20250123-pythonperf1_win32-x86-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.116x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: unknown