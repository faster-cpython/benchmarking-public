# Results vs. 3.10.4

- fork: python
- ref: 2f60b8f02fe7cb83dd58
- machine: windows-amd64
- commit hash: 2f60b8f
- commit date: 2025-11-01
- overall geometric mean: 1.353x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 213 ms: 1.24x faster                                                              |
| docutils       | 1.95 sec                                                        | 2.70 sec: 1.39x slower                                                            |
| html5lib       | 52.1 ms                                                         | 38.4 ms: 1.35x faster                                                             |
| Geometric mean | (ref)                                                           | 1.07x faster                                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|-------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_io           | 940 ms                                                          | 332 ms: 2.83x faster                                                              |
| async_tree_cpu_io_mixed | 922 ms                                                          | 331 ms: 2.79x faster                                                              |
| async_tree_none         | 394 ms                                                          | 165 ms: 2.38x faster                                                              |
| async_tree_memoization  | 467 ms                                                          | 199 ms: 2.34x faster                                                              |
| Geometric mean          | (ref)                                                           | 2.58x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 135 ms: 3.73x faster                                                              |
| float          | 69.6 ms                                                         | 44.1 ms: 1.58x faster                                                             |
| nbody          | 79.1 ms                                                         | 76.7 ms: 1.03x faster                                                             |
| Geometric mean | (ref)                                                           | 1.83x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 88.1 ms: 1.32x faster                                                             |
| regex_v8       | 15.8 ms                                                         | 13.2 ms: 1.19x faster                                                             |
| regex_dna      | 131 ms                                                          | 114 ms: 1.15x faster                                                              |
| regex_effbot   | 1.66 ms                                                         | 1.53 ms: 1.09x faster                                                             |
| Geometric mean | (ref)                                                           | 1.18x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 5.95 ms: 1.65x faster                                                             |
| json_loads           | 22.4 us                                                         | 15.6 us: 1.43x faster                                                             |
| xml_etree_parse      | 120 ms                                                          | 89.0 ms: 1.35x faster                                                             |
| unpickle_pure_python | 189 us                                                          | 148 us: 1.28x faster                                                              |
| pickle_pure_python   | 280 us                                                          | 224 us: 1.25x faster                                                              |
| xml_etree_iterparse  | 70.8 ms                                                         | 60.4 ms: 1.17x faster                                                             |
| xml_etree_process    | 48.1 ms                                                         | 43.1 ms: 1.12x faster                                                             |
| pickle_list          | 3.22 us                                                         | 3.02 us: 1.07x faster                                                             |
| xml_etree_generate   | 61.6 ms                                                         | 60.4 ms: 1.02x faster                                                             |
| pickle_dict          | 18.2 us                                                         | 19.9 us: 1.09x slower                                                             |
| tomli_loads          | 1.91 sec                                                        | 2.26 sec: 1.18x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.13x faster                                                                      |

Benchmark hidden because not significant (3): pickle, unpickle_list, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 19.0 ms: 1.05x slower                                                             |
| python_startup         | 22.9 ms                                                         | 25.2 ms: 1.10x slower                                                             |
| Geometric mean         | (ref)                                                           | 1.07x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| django_template | 36.0 ms                                                         | 25.8 ms: 1.39x faster                                                             |
| genshi_xml      | 46.6 ms                                                         | 38.0 ms: 1.23x faster                                                             |
| genshi_text     | 21.0 ms                                                         | 18.4 ms: 1.14x faster                                                             |
| mako            | 9.10 ms                                                         | 9.61 ms: 1.06x slower                                                             |
| Geometric mean  | (ref)                                                           | 1.16x faster                                                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|--------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| asyncio_tcp_ssl          | 17.0 sec                                                        | 2.28 sec: 7.45x faster                                                            |
| pidigits                 | 502 ms                                                          | 135 ms: 3.73x faster                                                              |
| typing_runtime_protocols | 396 us                                                          | 121 us: 3.27x faster                                                              |
| async_tree_io            | 940 ms                                                          | 332 ms: 2.83x faster                                                              |
| pathlib                  | 81.2 ms                                                         | 28.8 ms: 2.82x faster                                                             |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 331 ms: 2.79x faster                                                              |
| async_tree_none          | 394 ms                                                          | 165 ms: 2.38x faster                                                              |
| async_tree_memoization   | 467 ms                                                          | 199 ms: 2.34x faster                                                              |
| pylint                   | 384 ms                                                          | 202 ms: 1.90x faster                                                              |
| mdp                      | 1.83 sec                                                        | 973 ms: 1.88x faster                                                              |
| deltablue                | 4.04 ms                                                         | 2.31 ms: 1.75x faster                                                             |
| deepcopy                 | 310 us                                                          | 182 us: 1.71x faster                                                              |
| go                       | 146 ms                                                          | 85.6 ms: 1.70x faster                                                             |
| logging_silent           | 97.9 ns                                                         | 58.3 ns: 1.68x faster                                                             |
| chaos                    | 74.4 ms                                                         | 44.7 ms: 1.66x faster                                                             |
| json_dumps               | 9.82 ms                                                         | 5.95 ms: 1.65x faster                                                             |
| sqlite_synth             | 2.29 us                                                         | 1.40 us: 1.64x faster                                                             |
| thrift                   | 902 us                                                          | 562 us: 1.60x faster                                                              |
| float                    | 69.6 ms                                                         | 44.1 ms: 1.58x faster                                                             |
| json                     | 4.76 ms                                                         | 3.03 ms: 1.57x faster                                                             |
| deepcopy_memo            | 29.6 us                                                         | 18.9 us: 1.57x faster                                                             |
| comprehensions           | 17.7 us                                                         | 11.5 us: 1.55x faster                                                             |
| pycparser                | 1.04 sec                                                        | 686 ms: 1.52x faster                                                              |
| generators               | 31.6 ms                                                         | 21.1 ms: 1.50x faster                                                             |
| raytrace                 | 303 ms                                                          | 203 ms: 1.49x faster                                                              |
| dulwich_log              | 58.5 ms                                                         | 39.8 ms: 1.47x faster                                                             |
| crypto_pyaes             | 81.3 ms                                                         | 56.5 ms: 1.44x faster                                                             |
| json_loads               | 22.4 us                                                         | 15.6 us: 1.43x faster                                                             |
| scimark_lu               | 89.8 ms                                                         | 63.2 ms: 1.42x faster                                                             |
| pyflate                  | 422 ms                                                          | 297 ms: 1.42x faster                                                              |
| asyncio_tcp              | 744 ms                                                          | 528 ms: 1.41x faster                                                              |
| django_template          | 36.0 ms                                                         | 25.8 ms: 1.39x faster                                                             |
| hexiom                   | 6.13 ms                                                         | 4.44 ms: 1.38x faster                                                             |
| richards_super           | 49.9 ms                                                         | 36.6 ms: 1.36x faster                                                             |
| scimark_sor              | 115 ms                                                          | 84.8 ms: 1.36x faster                                                             |
| html5lib                 | 52.1 ms                                                         | 38.4 ms: 1.35x faster                                                             |
| xml_etree_parse          | 120 ms                                                          | 89.0 ms: 1.35x faster                                                             |
| deepcopy_reduce          | 2.68 us                                                         | 2.00 us: 1.34x faster                                                             |
| sympy_sum                | 122 ms                                                          | 91.5 ms: 1.34x faster                                                             |
| regex_compile            | 117 ms                                                          | 88.1 ms: 1.32x faster                                                             |
| sympy_str                | 229 ms                                                          | 178 ms: 1.29x faster                                                              |
| sympy_expand             | 391 ms                                                          | 303 ms: 1.29x faster                                                              |
| richards                 | 40.3 ms                                                         | 31.3 ms: 1.28x faster                                                             |
| unpickle_pure_python     | 189 us                                                          | 148 us: 1.28x faster                                                              |
| scimark_monte_carlo      | 61.9 ms                                                         | 49.3 ms: 1.26x faster                                                             |
| pickle_pure_python       | 280 us                                                          | 224 us: 1.25x faster                                                              |
| 2to3                     | 265 ms                                                          | 213 ms: 1.24x faster                                                              |
| pprint_safe_repr         | 658 ms                                                          | 535 ms: 1.23x faster                                                              |
| genshi_xml               | 46.6 ms                                                         | 38.0 ms: 1.23x faster                                                             |
| sympy_integrate          | 16.6 ms                                                         | 13.7 ms: 1.22x faster                                                             |
| nqueens                  | 87.1 ms                                                         | 72.1 ms: 1.21x faster                                                             |
| coroutines               | 17.9 ms                                                         | 14.9 ms: 1.21x faster                                                             |
| regex_v8                 | 15.8 ms                                                         | 13.2 ms: 1.19x faster                                                             |
| xml_etree_iterparse      | 70.8 ms                                                         | 60.4 ms: 1.17x faster                                                             |
| spectral_norm            | 80.2 ms                                                         | 69.1 ms: 1.16x faster                                                             |
| regex_dna                | 131 ms                                                          | 114 ms: 1.15x faster                                                              |
| unpack_sequence          | 40.0 ns                                                         | 35.0 ns: 1.15x faster                                                             |
| logging_format           | 7.91 us                                                         | 6.92 us: 1.14x faster                                                             |
| logging_simple           | 7.29 us                                                         | 6.40 us: 1.14x faster                                                             |
| genshi_text              | 21.0 ms                                                         | 18.4 ms: 1.14x faster                                                             |
| scimark_fft              | 216 ms                                                          | 192 ms: 1.13x faster                                                              |
| xml_etree_process        | 48.1 ms                                                         | 43.1 ms: 1.12x faster                                                             |
| gc_traversal             | 1.28 ms                                                         | 1.15 ms: 1.11x faster                                                             |
| bench_thread_pool        | 1.12 ms                                                         | 1.01 ms: 1.11x faster                                                             |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.94 ms: 1.10x faster                                                             |
| regex_effbot             | 1.66 ms                                                         | 1.53 ms: 1.09x faster                                                             |
| pickle_list              | 3.22 us                                                         | 3.02 us: 1.07x faster                                                             |
| fannkuch                 | 317 ms                                                          | 299 ms: 1.06x faster                                                              |
| nbody                    | 79.1 ms                                                         | 76.7 ms: 1.03x faster                                                             |
| xml_etree_generate       | 61.6 ms                                                         | 60.4 ms: 1.02x faster                                                             |
| telco                    | 4.83 ms                                                         | 4.85 ms: 1.00x slower                                                             |
| python_startup_no_site   | 18.1 ms                                                         | 19.0 ms: 1.05x slower                                                             |
| mako                     | 9.10 ms                                                         | 9.61 ms: 1.06x slower                                                             |
| async_generators         | 241 ms                                                          | 256 ms: 1.06x slower                                                              |
| meteor_contest           | 80.0 ms                                                         | 85.1 ms: 1.06x slower                                                             |
| bench_mp_pool            | 66.4 ms                                                         | 72.3 ms: 1.09x slower                                                             |
| pickle_dict              | 18.2 us                                                         | 19.9 us: 1.09x slower                                                             |
| python_startup           | 22.9 ms                                                         | 25.2 ms: 1.10x slower                                                             |
| pprint_pformat           | 1.37 sec                                                        | 1.54 sec: 1.13x slower                                                            |
| tomli_loads              | 1.91 sec                                                        | 2.26 sec: 1.18x slower                                                            |
| docutils                 | 1.95 sec                                                        | 2.70 sec: 1.39x slower                                                            |
| coverage                 | 46.6 ms                                                         | 66.3 ms: 1.42x slower                                                             |
| create_gc_cycles         | 694 us                                                          | 1.01 ms: 1.46x slower                                                             |
| Geometric mean           | (ref)                                                           | 1.34x faster                                                                      |

Benchmark hidden because not significant (3): pickle, unpickle_list, unpickle
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20251101-3.15.0a1+-2f60b8f-NOGIL/bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.353x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: unknown