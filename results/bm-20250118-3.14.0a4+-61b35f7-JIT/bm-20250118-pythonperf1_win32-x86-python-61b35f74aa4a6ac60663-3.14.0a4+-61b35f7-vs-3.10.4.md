# Results vs. 3.10.4

- fork: python
- ref: 61b35f74aa4a6ac60663
- machine: windows-x86
- commit hash: 61b35f7
- commit date: 2025-01-18
- overall geometric mean: 1.008x slower
- HPT reliability: 91.19%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250118-pythonperf1_win32-x86-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 291 ms: 1.09x slower                                                            |
| docutils       | 1.95 sec                                                        | 2.15 sec: 1.10x slower                                                          |
| html5lib       | 52.1 ms                                                         | 54.7 ms: 1.05x slower                                                           |
| Geometric mean | (ref)                                                           | 1.08x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250118-pythonperf1_win32-x86-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 490 ms: 1.88x faster                                                            |
| async_tree_io           | 940 ms                                                          | 508 ms: 1.85x faster                                                            |
| async_tree_none         | 394 ms                                                          | 238 ms: 1.66x faster                                                            |
| async_tree_memoization  | 467 ms                                                          | 291 ms: 1.60x faster                                                            |
| Geometric mean          | (ref)                                                           | 1.74x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250118-pythonperf1_win32-x86-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 200 ms: 2.51x faster                                                            |
| float          | 69.6 ms                                                         | 56.8 ms: 1.23x faster                                                           |
| nbody          | 79.1 ms                                                         | 112 ms: 1.42x slower                                                            |
| Geometric mean | (ref)                                                           | 1.29x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250118-pythonperf1_win32-x86-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 115 ms: 1.13x faster                                                            |
| regex_effbot   | 1.66 ms                                                         | 1.56 ms: 1.07x faster                                                           |
| regex_v8       | 15.8 ms                                                         | 16.4 ms: 1.04x slower                                                           |
| regex_compile  | 117 ms                                                          | 132 ms: 1.13x slower                                                            |
| Geometric mean | (ref)                                                           | 1.01x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250118-pythonperf1_win32-x86-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_parse      | 120 ms                                                          | 110 ms: 1.09x faster                                                            |
| json_dumps           | 9.82 ms                                                         | 9.55 ms: 1.03x faster                                                           |
| xml_etree_iterparse  | 70.8 ms                                                         | 69.7 ms: 1.02x faster                                                           |
| tomli_loads          | 1.91 sec                                                        | 1.89 sec: 1.01x faster                                                          |
| json_loads           | 22.4 us                                                         | 23.0 us: 1.03x slower                                                           |
| unpickle             | 9.82 us                                                         | 10.9 us: 1.11x slower                                                           |
| unpickle_pure_python | 189 us                                                          | 213 us: 1.12x slower                                                            |
| pickle_dict          | 18.2 us                                                         | 20.8 us: 1.14x slower                                                           |
| pickle_list          | 3.22 us                                                         | 3.72 us: 1.16x slower                                                           |
| xml_etree_process    | 48.1 ms                                                         | 56.6 ms: 1.18x slower                                                           |
| pickle_pure_python   | 280 us                                                          | 335 us: 1.19x slower                                                            |
| pickle               | 7.83 us                                                         | 9.42 us: 1.20x slower                                                           |
| xml_etree_generate   | 61.6 ms                                                         | 77.0 ms: 1.25x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.08x slower                                                                    |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250118-pythonperf1_win32-x86-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 20.4 ms: 1.13x slower                                                           |
| python_startup         | 22.9 ms                                                         | 27.2 ms: 1.19x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.16x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250118-pythonperf1_win32-x86-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 7.39 ms: 1.23x faster                                                           |
| django_template | 36.0 ms                                                         | 40.2 ms: 1.12x slower                                                           |
| genshi_xml      | 46.6 ms                                                         | 61.8 ms: 1.33x slower                                                           |
| genshi_text     | 21.0 ms                                                         | 29.2 ms: 1.39x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.14x slower                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250118-pythonperf1_win32-x86-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits                 | 502 ms                                                          | 200 ms: 2.51x faster                                                            |
| typing_runtime_protocols | 396 us                                                          | 174 us: 2.27x faster                                                            |
| sqlglot_normalize        | 230 ms                                                          | 115 ms: 2.00x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 490 ms: 1.88x faster                                                            |
| async_tree_io            | 940 ms                                                          | 508 ms: 1.85x faster                                                            |
| async_tree_none          | 394 ms                                                          | 238 ms: 1.66x faster                                                            |
| async_tree_memoization   | 467 ms                                                          | 291 ms: 1.60x faster                                                            |
| pylint                   | 384 ms                                                          | 269 ms: 1.42x faster                                                            |
| mako                     | 9.10 ms                                                         | 7.39 ms: 1.23x faster                                                           |
| float                    | 69.6 ms                                                         | 56.8 ms: 1.23x faster                                                           |
| sqlite_synth             | 2.29 us                                                         | 1.92 us: 1.19x faster                                                           |
| deltablue                | 4.04 ms                                                         | 3.41 ms: 1.18x faster                                                           |
| crypto_pyaes             | 81.3 ms                                                         | 70.1 ms: 1.16x faster                                                           |
| deepcopy_memo            | 29.6 us                                                         | 25.5 us: 1.16x faster                                                           |
| regex_dna                | 131 ms                                                          | 115 ms: 1.13x faster                                                            |
| logging_silent           | 97.9 ns                                                         | 88.0 ns: 1.11x faster                                                           |
| scimark_lu               | 89.8 ms                                                         | 80.7 ms: 1.11x faster                                                           |
| xml_etree_parse          | 120 ms                                                          | 110 ms: 1.09x faster                                                            |
| thrift                   | 902 us                                                          | 841 us: 1.07x faster                                                            |
| regex_effbot             | 1.66 ms                                                         | 1.56 ms: 1.07x faster                                                           |
| chaos                    | 74.4 ms                                                         | 70.0 ms: 1.06x faster                                                           |
| pyflate                  | 422 ms                                                          | 399 ms: 1.06x faster                                                            |
| scimark_sor              | 115 ms                                                          | 109 ms: 1.06x faster                                                            |
| go                       | 146 ms                                                          | 139 ms: 1.05x faster                                                            |
| sqlglot_parse            | 1.33 ms                                                         | 1.27 ms: 1.05x faster                                                           |
| pycparser                | 1.04 sec                                                        | 1.00 sec: 1.04x faster                                                          |
| deepcopy                 | 310 us                                                          | 299 us: 1.04x faster                                                            |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.13 ms: 1.04x faster                                                           |
| json_dumps               | 9.82 ms                                                         | 9.55 ms: 1.03x faster                                                           |
| dulwich_log              | 58.5 ms                                                         | 57.0 ms: 1.03x faster                                                           |
| spectral_norm            | 80.2 ms                                                         | 78.3 ms: 1.02x faster                                                           |
| xml_etree_iterparse      | 70.8 ms                                                         | 69.7 ms: 1.02x faster                                                           |
| tomli_loads              | 1.91 sec                                                        | 1.89 sec: 1.01x faster                                                          |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 17.1 sec: 1.01x slower                                                          |
| json_loads               | 22.4 us                                                         | 23.0 us: 1.03x slower                                                           |
| regex_v8                 | 15.8 ms                                                         | 16.4 ms: 1.04x slower                                                           |
| html5lib                 | 52.1 ms                                                         | 54.7 ms: 1.05x slower                                                           |
| richards_super           | 49.9 ms                                                         | 52.9 ms: 1.06x slower                                                           |
| pathlib                  | 81.2 ms                                                         | 86.5 ms: 1.07x slower                                                           |
| comprehensions           | 17.7 us                                                         | 19.1 us: 1.08x slower                                                           |
| scimark_monte_carlo      | 61.9 ms                                                         | 66.9 ms: 1.08x slower                                                           |
| sympy_sum                | 122 ms                                                          | 132 ms: 1.08x slower                                                            |
| mdp                      | 1.83 sec                                                        | 1.99 sec: 1.09x slower                                                          |
| 2to3                     | 265 ms                                                          | 291 ms: 1.09x slower                                                            |
| docutils                 | 1.95 sec                                                        | 2.15 sec: 1.10x slower                                                          |
| unpickle                 | 9.82 us                                                         | 10.9 us: 1.11x slower                                                           |
| raytrace                 | 303 ms                                                          | 337 ms: 1.11x slower                                                            |
| pprint_pformat           | 1.37 sec                                                        | 1.53 sec: 1.12x slower                                                          |
| django_template          | 36.0 ms                                                         | 40.2 ms: 1.12x slower                                                           |
| unpickle_pure_python     | 189 us                                                          | 213 us: 1.12x slower                                                            |
| python_startup_no_site   | 18.1 ms                                                         | 20.4 ms: 1.13x slower                                                           |
| regex_compile            | 117 ms                                                          | 132 ms: 1.13x slower                                                            |
| fannkuch                 | 317 ms                                                          | 359 ms: 1.13x slower                                                            |
| deepcopy_reduce          | 2.68 us                                                         | 3.05 us: 1.14x slower                                                           |
| pickle_dict              | 18.2 us                                                         | 20.8 us: 1.14x slower                                                           |
| scimark_fft              | 216 ms                                                          | 247 ms: 1.14x slower                                                            |
| meteor_contest           | 80.0 ms                                                         | 91.7 ms: 1.15x slower                                                           |
| sympy_str                | 229 ms                                                          | 263 ms: 1.15x slower                                                            |
| pprint_safe_repr         | 658 ms                                                          | 759 ms: 1.15x slower                                                            |
| pickle_list              | 3.22 us                                                         | 3.72 us: 1.16x slower                                                           |
| sympy_expand             | 391 ms                                                          | 452 ms: 1.16x slower                                                            |
| sympy_integrate          | 16.6 ms                                                         | 19.4 ms: 1.16x slower                                                           |
| coverage                 | 46.6 ms                                                         | 54.3 ms: 1.17x slower                                                           |
| richards                 | 40.3 ms                                                         | 47.2 ms: 1.17x slower                                                           |
| xml_etree_process        | 48.1 ms                                                         | 56.6 ms: 1.18x slower                                                           |
| python_startup           | 22.9 ms                                                         | 27.2 ms: 1.19x slower                                                           |
| pickle_pure_python       | 280 us                                                          | 335 us: 1.19x slower                                                            |
| pickle                   | 7.83 us                                                         | 9.42 us: 1.20x slower                                                           |
| coroutines               | 17.9 ms                                                         | 21.8 ms: 1.22x slower                                                           |
| nqueens                  | 87.1 ms                                                         | 106 ms: 1.22x slower                                                            |
| hexiom                   | 6.13 ms                                                         | 7.57 ms: 1.23x slower                                                           |
| sqlglot_optimize         | 44.7 ms                                                         | 55.6 ms: 1.24x slower                                                           |
| xml_etree_generate       | 61.6 ms                                                         | 77.0 ms: 1.25x slower                                                           |
| logging_format           | 7.91 us                                                         | 10.4 us: 1.31x slower                                                           |
| genshi_xml               | 46.6 ms                                                         | 61.8 ms: 1.33x slower                                                           |
| generators               | 31.6 ms                                                         | 42.0 ms: 1.33x slower                                                           |
| logging_simple           | 7.29 us                                                         | 9.77 us: 1.34x slower                                                           |
| genshi_text              | 21.0 ms                                                         | 29.2 ms: 1.39x slower                                                           |
| nbody                    | 79.1 ms                                                         | 112 ms: 1.42x slower                                                            |
| gc_traversal             | 1.28 ms                                                         | 1.82 ms: 1.42x slower                                                           |
| async_generators         | 241 ms                                                          | 345 ms: 1.43x slower                                                            |
| unpack_sequence          | 40.0 ns                                                         | 57.5 ns: 1.44x slower                                                           |
| bench_mp_pool            | 66.4 ms                                                         | 97.5 ms: 1.47x slower                                                           |
| create_gc_cycles         | 694 us                                                          | 1.04 ms: 1.50x slower                                                           |
| telco                    | 4.83 ms                                                         | 7.57 ms: 1.57x slower                                                           |
| Geometric mean           | (ref)                                                           | 1.02x slower                                                                    |

Benchmark hidden because not significant (5): json, sqlglot_transpile, unpickle_list, bench_thread_pool, asyncio_tcp
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (12) of results/bm-20250118-3.14.0a4+-61b35f7-JIT/bm-20250118-pythonperf1_win32-x86-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.008x slower

# HPT report

- Reliability score: 91.19% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown