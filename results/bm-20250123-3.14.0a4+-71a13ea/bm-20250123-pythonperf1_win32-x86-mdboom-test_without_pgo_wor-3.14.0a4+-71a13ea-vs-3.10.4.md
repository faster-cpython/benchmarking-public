# Results vs. 3.10.4

- fork: mdboom
- ref: test_without_pgo_wor
- machine: windows-x86
- commit hash: 71a13ea
- commit date: 2025-01-23
- overall geometric mean: 1.113x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.03x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250123-pythonperf1_win32-x86-mdboom-test_without_pgo_wor-3.14.0a4+-71a13ea |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 256 ms: 1.04x faster                                                            |
| docutils       | 1.95 sec                                                        | 1.85 sec: 1.05x faster                                                          |
| html5lib       | 52.1 ms                                                         | 47.1 ms: 1.10x faster                                                           |
| Geometric mean | (ref)                                                           | 1.06x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250123-pythonperf1_win32-x86-mdboom-test_without_pgo_wor-3.14.0a4+-71a13ea |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io           | 940 ms                                                          | 459 ms: 2.05x faster                                                            |
| async_tree_cpu_io_mixed | 922 ms                                                          | 461 ms: 2.00x faster                                                            |
| async_tree_none         | 394 ms                                                          | 212 ms: 1.86x faster                                                            |
| async_tree_memoization  | 467 ms                                                          | 261 ms: 1.79x faster                                                            |
| Geometric mean          | (ref)                                                           | 1.92x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250123-pythonperf1_win32-x86-mdboom-test_without_pgo_wor-3.14.0a4+-71a13ea |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 200 ms: 2.52x faster                                                            |
| float          | 69.6 ms                                                         | 57.8 ms: 1.21x faster                                                           |
| nbody          | 79.1 ms                                                         | 89.4 ms: 1.13x slower                                                           |
| Geometric mean | (ref)                                                           | 1.39x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250123-pythonperf1_win32-x86-mdboom-test_without_pgo_wor-3.14.0a4+-71a13ea |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 113 ms: 1.16x faster                                                            |
| regex_compile  | 117 ms                                                          | 106 ms: 1.10x faster                                                            |
| regex_effbot   | 1.66 ms                                                         | 1.55 ms: 1.07x faster                                                           |
| regex_v8       | 15.8 ms                                                         | 16.2 ms: 1.03x slower                                                           |
| Geometric mean | (ref)                                                           | 1.07x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250123-pythonperf1_win32-x86-mdboom-test_without_pgo_wor-3.14.0a4+-71a13ea |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 1.91 sec                                                        | 1.69 sec: 1.13x faster                                                          |
| xml_etree_parse      | 120 ms                                                          | 109 ms: 1.10x faster                                                            |
| json_dumps           | 9.82 ms                                                         | 9.25 ms: 1.06x faster                                                           |
| xml_etree_iterparse  | 70.8 ms                                                         | 66.9 ms: 1.06x faster                                                           |
| json_loads           | 22.4 us                                                         | 21.5 us: 1.04x faster                                                           |
| unpickle_pure_python | 189 us                                                          | 185 us: 1.03x faster                                                            |
| xml_etree_process    | 48.1 ms                                                         | 52.4 ms: 1.09x slower                                                           |
| xml_etree_generate   | 61.6 ms                                                         | 67.1 ms: 1.09x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.03x faster                                                                    |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250123-pythonperf1_win32-x86-mdboom-test_without_pgo_wor-3.14.0a4+-71a13ea |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 20.3 ms: 1.12x slower                                                           |
| python_startup         | 22.9 ms                                                         | 26.7 ms: 1.16x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.14x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250123-pythonperf1_win32-x86-mdboom-test_without_pgo_wor-3.14.0a4+-71a13ea |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 7.68 ms: 1.19x faster                                                           |
| django_template | 36.0 ms                                                         | 33.7 ms: 1.07x faster                                                           |
| genshi_xml      | 46.6 ms                                                         | 48.7 ms: 1.04x slower                                                           |
| genshi_text     | 21.0 ms                                                         | 22.1 ms: 1.05x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.04x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250123-pythonperf1_win32-x86-mdboom-test_without_pgo_wor-3.14.0a4+-71a13ea |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits                 | 502 ms                                                          | 200 ms: 2.52x faster                                                            |
| typing_runtime_protocols | 396 us                                                          | 160 us: 2.48x faster                                                            |
| async_tree_io            | 940 ms                                                          | 459 ms: 2.05x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 461 ms: 2.00x faster                                                            |
| async_tree_none          | 394 ms                                                          | 212 ms: 1.86x faster                                                            |
| async_tree_memoization   | 467 ms                                                          | 261 ms: 1.79x faster                                                            |
| pylint                   | 384 ms                                                          | 225 ms: 1.71x faster                                                            |
| deltablue                | 4.04 ms                                                         | 2.75 ms: 1.47x faster                                                           |
| go                       | 146 ms                                                          | 101 ms: 1.44x faster                                                            |
| deepcopy_memo            | 29.6 us                                                         | 21.9 us: 1.35x faster                                                           |
| chaos                    | 74.4 ms                                                         | 56.4 ms: 1.32x faster                                                           |
| crypto_pyaes             | 81.3 ms                                                         | 62.0 ms: 1.31x faster                                                           |
| logging_silent           | 97.9 ns                                                         | 76.4 ns: 1.28x faster                                                           |
| deepcopy                 | 310 us                                                          | 250 us: 1.24x faster                                                            |
| sqlglot_parse            | 1.33 ms                                                         | 1.08 ms: 1.24x faster                                                           |
| pyflate                  | 422 ms                                                          | 341 ms: 1.24x faster                                                            |
| generators               | 31.6 ms                                                         | 26.1 ms: 1.21x faster                                                           |
| pycparser                | 1.04 sec                                                        | 864 ms: 1.21x faster                                                            |
| float                    | 69.6 ms                                                         | 57.8 ms: 1.21x faster                                                           |
| scimark_lu               | 89.8 ms                                                         | 74.6 ms: 1.20x faster                                                           |
| sqlite_synth             | 2.29 us                                                         | 1.91 us: 1.20x faster                                                           |
| sqlglot_transpile        | 1.58 ms                                                         | 1.32 ms: 1.20x faster                                                           |
| comprehensions           | 17.7 us                                                         | 14.9 us: 1.19x faster                                                           |
| mako                     | 9.10 ms                                                         | 7.68 ms: 1.19x faster                                                           |
| hexiom                   | 6.13 ms                                                         | 5.18 ms: 1.18x faster                                                           |
| thrift                   | 902 us                                                          | 770 us: 1.17x faster                                                            |
| regex_dna                | 131 ms                                                          | 113 ms: 1.16x faster                                                            |
| tomli_loads              | 1.91 sec                                                        | 1.69 sec: 1.13x faster                                                          |
| dulwich_log              | 58.5 ms                                                         | 52.2 ms: 1.12x faster                                                           |
| spectral_norm            | 80.2 ms                                                         | 72.0 ms: 1.11x faster                                                           |
| scimark_sor              | 115 ms                                                          | 104 ms: 1.11x faster                                                            |
| html5lib                 | 52.1 ms                                                         | 47.1 ms: 1.10x faster                                                           |
| xml_etree_parse          | 120 ms                                                          | 109 ms: 1.10x faster                                                            |
| sympy_sum                | 122 ms                                                          | 111 ms: 1.10x faster                                                            |
| scimark_monte_carlo      | 61.9 ms                                                         | 56.2 ms: 1.10x faster                                                           |
| regex_compile            | 117 ms                                                          | 106 ms: 1.10x faster                                                            |
| richards_super           | 49.9 ms                                                         | 45.5 ms: 1.10x faster                                                           |
| nqueens                  | 87.1 ms                                                         | 79.5 ms: 1.10x faster                                                           |
| bench_thread_pool        | 1.12 ms                                                         | 1.03 ms: 1.08x faster                                                           |
| raytrace                 | 303 ms                                                          | 281 ms: 1.08x faster                                                            |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.01 ms: 1.08x faster                                                           |
| regex_effbot             | 1.66 ms                                                         | 1.55 ms: 1.07x faster                                                           |
| django_template          | 36.0 ms                                                         | 33.7 ms: 1.07x faster                                                           |
| mdp                      | 1.83 sec                                                        | 1.71 sec: 1.07x faster                                                          |
| json_dumps               | 9.82 ms                                                         | 9.25 ms: 1.06x faster                                                           |
| xml_etree_iterparse      | 70.8 ms                                                         | 66.9 ms: 1.06x faster                                                           |
| docutils                 | 1.95 sec                                                        | 1.85 sec: 1.05x faster                                                          |
| sympy_integrate          | 16.6 ms                                                         | 15.9 ms: 1.04x faster                                                           |
| json_loads               | 22.4 us                                                         | 21.5 us: 1.04x faster                                                           |
| fannkuch                 | 317 ms                                                          | 305 ms: 1.04x faster                                                            |
| 2to3                     | 265 ms                                                          | 256 ms: 1.04x faster                                                            |
| deepcopy_reduce          | 2.68 us                                                         | 2.61 us: 1.03x faster                                                           |
| unpickle_pure_python     | 189 us                                                          | 185 us: 1.03x faster                                                            |
| coroutines               | 17.9 ms                                                         | 17.6 ms: 1.02x faster                                                           |
| sympy_str                | 229 ms                                                          | 226 ms: 1.01x faster                                                            |
| richards                 | 40.3 ms                                                         | 39.9 ms: 1.01x faster                                                           |
| pprint_pformat           | 1.37 sec                                                        | 1.38 sec: 1.01x slower                                                          |
| scimark_fft              | 216 ms                                                          | 219 ms: 1.01x slower                                                            |
| sqlglot_normalize        | 230 ms                                                          | 235 ms: 1.02x slower                                                            |
| pprint_safe_repr         | 658 ms                                                          | 672 ms: 1.02x slower                                                            |
| meteor_contest           | 80.0 ms                                                         | 82.0 ms: 1.03x slower                                                           |
| regex_v8                 | 15.8 ms                                                         | 16.2 ms: 1.03x slower                                                           |
| sympy_expand             | 391 ms                                                          | 402 ms: 1.03x slower                                                            |
| genshi_xml               | 46.6 ms                                                         | 48.7 ms: 1.04x slower                                                           |
| genshi_text              | 21.0 ms                                                         | 22.1 ms: 1.05x slower                                                           |
| pathlib                  | 81.2 ms                                                         | 86.7 ms: 1.07x slower                                                           |
| xml_etree_process        | 48.1 ms                                                         | 52.4 ms: 1.09x slower                                                           |
| xml_etree_generate       | 61.6 ms                                                         | 67.1 ms: 1.09x slower                                                           |
| python_startup_no_site   | 18.1 ms                                                         | 20.3 ms: 1.12x slower                                                           |
| nbody                    | 79.1 ms                                                         | 89.4 ms: 1.13x slower                                                           |
| coverage                 | 46.6 ms                                                         | 53.1 ms: 1.14x slower                                                           |
| logging_format           | 7.91 us                                                         | 9.05 us: 1.14x slower                                                           |
| logging_simple           | 7.29 us                                                         | 8.37 us: 1.15x slower                                                           |
| python_startup           | 22.9 ms                                                         | 26.7 ms: 1.16x slower                                                           |
| async_generators         | 241 ms                                                          | 311 ms: 1.29x slower                                                            |
| gc_traversal             | 1.28 ms                                                         | 1.78 ms: 1.39x slower                                                           |
| bench_mp_pool            | 66.4 ms                                                         | 95.1 ms: 1.43x slower                                                           |
| telco                    | 4.83 ms                                                         | 7.13 ms: 1.48x slower                                                           |
| create_gc_cycles         | 694 us                                                          | 1.05 ms: 1.51x slower                                                           |
| Geometric mean           | (ref)                                                           | 1.11x faster                                                                    |

Benchmark hidden because not significant (3): sqlglot_optimize, pickle_pure_python, json
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250123-3.14.0a4+-71a13ea/bm-20250123-pythonperf1_win32-x86-mdboom-test_without_pgo_wor-3.14.0a4+-71a13ea.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.113x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: unknown