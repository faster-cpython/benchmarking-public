# Results vs. 3.10.4

- fork: python
- ref: 2f60b8f02fe7cb83dd58
- machine: windows-amd64
- commit hash: 2f60b8f
- commit date: 2025-11-01
- overall geometric mean: 1.531x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.43x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 213 ms: 1.24x faster                                                              |
| docutils       | 1.95 sec                                                        | 1.60 sec: 1.22x faster                                                            |
| html5lib       | 52.1 ms                                                         | 35.6 ms: 1.46x faster                                                             |
| Geometric mean | (ref)                                                           | 1.30x faster                                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|-------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 321 ms: 2.88x faster                                                              |
| async_tree_io           | 940 ms                                                          | 358 ms: 2.63x faster                                                              |
| async_tree_memoization  | 467 ms                                                          | 190 ms: 2.46x faster                                                              |
| async_tree_none         | 394 ms                                                          | 164 ms: 2.40x faster                                                              |
| Geometric mean          | (ref)                                                           | 2.58x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 143 ms: 3.51x faster                                                              |
| float          | 69.6 ms                                                         | 38.8 ms: 1.79x faster                                                             |
| nbody          | 79.1 ms                                                         | 53.4 ms: 1.48x faster                                                             |
| Geometric mean | (ref)                                                           | 2.10x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 77.0 ms: 1.52x faster                                                             |
| regex_v8       | 15.8 ms                                                         | 14.0 ms: 1.13x faster                                                             |
| regex_dna      | 131 ms                                                          | 117 ms: 1.11x faster                                                              |
| regex_effbot   | 1.66 ms                                                         | 1.54 ms: 1.08x faster                                                             |
| Geometric mean | (ref)                                                           | 1.20x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| unpickle_pure_python | 189 us                                                          | 105 us: 1.80x faster                                                              |
| json_dumps           | 9.82 ms                                                         | 5.47 ms: 1.80x faster                                                             |
| tomli_loads          | 1.91 sec                                                        | 1.09 sec: 1.75x faster                                                            |
| json_loads           | 22.4 us                                                         | 13.9 us: 1.61x faster                                                             |
| pickle_pure_python   | 280 us                                                          | 196 us: 1.43x faster                                                              |
| xml_etree_parse      | 120 ms                                                          | 85.6 ms: 1.40x faster                                                             |
| xml_etree_process    | 48.1 ms                                                         | 35.0 ms: 1.37x faster                                                             |
| xml_etree_generate   | 61.6 ms                                                         | 48.6 ms: 1.27x faster                                                             |
| xml_etree_iterparse  | 70.8 ms                                                         | 56.5 ms: 1.25x faster                                                             |
| unpickle             | 9.82 us                                                         | 8.47 us: 1.16x faster                                                             |
| unpickle_list        | 2.98 us                                                         | 2.77 us: 1.08x faster                                                             |
| pickle               | 7.83 us                                                         | 7.48 us: 1.05x faster                                                             |
| pickle_list          | 3.22 us                                                         | 3.18 us: 1.01x faster                                                             |
| pickle_dict          | 18.2 us                                                         | 19.8 us: 1.09x slower                                                             |
| Geometric mean       | (ref)                                                           | 1.32x faster                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 19.0 ms: 1.05x slower                                                             |
| python_startup         | 22.9 ms                                                         | 25.2 ms: 1.10x slower                                                             |
| Geometric mean         | (ref)                                                           | 1.08x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 5.23 ms: 1.74x faster                                                             |
| django_template | 36.0 ms                                                         | 23.4 ms: 1.54x faster                                                             |
| genshi_text     | 21.0 ms                                                         | 15.6 ms: 1.34x faster                                                             |
| genshi_xml      | 46.6 ms                                                         | 34.7 ms: 1.34x faster                                                             |
| Geometric mean  | (ref)                                                           | 1.48x faster                                                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|--------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| asyncio_tcp_ssl          | 17.0 sec                                                        | 1.34 sec: 12.69x faster                                                           |
| typing_runtime_protocols | 396 us                                                          | 104 us: 3.80x faster                                                              |
| pidigits                 | 502 ms                                                          | 143 ms: 3.51x faster                                                              |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 321 ms: 2.88x faster                                                              |
| pathlib                  | 81.2 ms                                                         | 28.7 ms: 2.83x faster                                                             |
| async_tree_io            | 940 ms                                                          | 358 ms: 2.63x faster                                                              |
| async_tree_memoization   | 467 ms                                                          | 190 ms: 2.46x faster                                                              |
| async_tree_none          | 394 ms                                                          | 164 ms: 2.40x faster                                                              |
| mdp                      | 1.83 sec                                                        | 779 ms: 2.34x faster                                                              |
| go                       | 146 ms                                                          | 74.3 ms: 1.96x faster                                                             |
| pylint                   | 384 ms                                                          | 198 ms: 1.94x faster                                                              |
| chaos                    | 74.4 ms                                                         | 38.5 ms: 1.93x faster                                                             |
| deepcopy                 | 310 us                                                          | 161 us: 1.93x faster                                                              |
| deltablue                | 4.04 ms                                                         | 2.17 ms: 1.86x faster                                                             |
| thrift                   | 902 us                                                          | 490 us: 1.84x faster                                                              |
| crypto_pyaes             | 81.3 ms                                                         | 44.9 ms: 1.81x faster                                                             |
| unpickle_pure_python     | 189 us                                                          | 105 us: 1.80x faster                                                              |
| logging_silent           | 97.9 ns                                                         | 54.4 ns: 1.80x faster                                                             |
| json_dumps               | 9.82 ms                                                         | 5.47 ms: 1.80x faster                                                             |
| float                    | 69.6 ms                                                         | 38.8 ms: 1.79x faster                                                             |
| raytrace                 | 303 ms                                                          | 169 ms: 1.79x faster                                                              |
| tomli_loads              | 1.91 sec                                                        | 1.09 sec: 1.75x faster                                                            |
| mako                     | 9.10 ms                                                         | 5.23 ms: 1.74x faster                                                             |
| comprehensions           | 17.7 us                                                         | 10.2 us: 1.74x faster                                                             |
| deepcopy_memo            | 29.6 us                                                         | 17.1 us: 1.73x faster                                                             |
| pyflate                  | 422 ms                                                          | 248 ms: 1.70x faster                                                              |
| richards_super           | 49.9 ms                                                         | 29.7 ms: 1.68x faster                                                             |
| generators               | 31.6 ms                                                         | 19.1 ms: 1.65x faster                                                             |
| json                     | 4.76 ms                                                         | 2.91 ms: 1.64x faster                                                             |
| scimark_fft              | 216 ms                                                          | 133 ms: 1.63x faster                                                              |
| asyncio_tcp              | 744 ms                                                          | 458 ms: 1.62x faster                                                              |
| json_loads               | 22.4 us                                                         | 13.9 us: 1.61x faster                                                             |
| pprint_pformat           | 1.37 sec                                                        | 852 ms: 1.61x faster                                                              |
| pycparser                | 1.04 sec                                                        | 653 ms: 1.59x faster                                                              |
| scimark_sor              | 115 ms                                                          | 73.0 ms: 1.58x faster                                                             |
| pprint_safe_repr         | 658 ms                                                          | 418 ms: 1.57x faster                                                              |
| hexiom                   | 6.13 ms                                                         | 3.91 ms: 1.57x faster                                                             |
| deepcopy_reduce          | 2.68 us                                                         | 1.71 us: 1.57x faster                                                             |
| fannkuch                 | 317 ms                                                          | 204 ms: 1.56x faster                                                              |
| scimark_lu               | 89.8 ms                                                         | 57.8 ms: 1.55x faster                                                             |
| richards                 | 40.3 ms                                                         | 26.1 ms: 1.54x faster                                                             |
| django_template          | 36.0 ms                                                         | 23.4 ms: 1.54x faster                                                             |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.12 ms: 1.53x faster                                                             |
| regex_compile            | 117 ms                                                          | 77.0 ms: 1.52x faster                                                             |
| dulwich_log              | 58.5 ms                                                         | 38.7 ms: 1.51x faster                                                             |
| sqlite_synth             | 2.29 us                                                         | 1.55 us: 1.48x faster                                                             |
| nbody                    | 79.1 ms                                                         | 53.4 ms: 1.48x faster                                                             |
| scimark_monte_carlo      | 61.9 ms                                                         | 42.2 ms: 1.47x faster                                                             |
| html5lib                 | 52.1 ms                                                         | 35.6 ms: 1.46x faster                                                             |
| nqueens                  | 87.1 ms                                                         | 60.1 ms: 1.45x faster                                                             |
| sympy_sum                | 122 ms                                                          | 85.0 ms: 1.44x faster                                                             |
| pickle_pure_python       | 280 us                                                          | 196 us: 1.43x faster                                                              |
| xml_etree_parse          | 120 ms                                                          | 85.6 ms: 1.40x faster                                                             |
| xml_etree_process        | 48.1 ms                                                         | 35.0 ms: 1.37x faster                                                             |
| sympy_str                | 229 ms                                                          | 167 ms: 1.37x faster                                                              |
| sympy_expand             | 391 ms                                                          | 287 ms: 1.36x faster                                                              |
| genshi_text              | 21.0 ms                                                         | 15.6 ms: 1.34x faster                                                             |
| bench_thread_pool        | 1.12 ms                                                         | 834 us: 1.34x faster                                                              |
| genshi_xml               | 46.6 ms                                                         | 34.7 ms: 1.34x faster                                                             |
| sympy_integrate          | 16.6 ms                                                         | 12.5 ms: 1.33x faster                                                             |
| xml_etree_generate       | 61.6 ms                                                         | 48.6 ms: 1.27x faster                                                             |
| xml_etree_iterparse      | 70.8 ms                                                         | 56.5 ms: 1.25x faster                                                             |
| 2to3                     | 265 ms                                                          | 213 ms: 1.24x faster                                                              |
| spectral_norm            | 80.2 ms                                                         | 64.8 ms: 1.24x faster                                                             |
| telco                    | 4.83 ms                                                         | 3.90 ms: 1.24x faster                                                             |
| logging_simple           | 7.29 us                                                         | 5.91 us: 1.23x faster                                                             |
| coroutines               | 17.9 ms                                                         | 14.5 ms: 1.23x faster                                                             |
| logging_format           | 7.91 us                                                         | 6.42 us: 1.23x faster                                                             |
| docutils                 | 1.95 sec                                                        | 1.60 sec: 1.22x faster                                                            |
| unpack_sequence          | 40.0 ns                                                         | 33.0 ns: 1.21x faster                                                             |
| unpickle                 | 9.82 us                                                         | 8.47 us: 1.16x faster                                                             |
| meteor_contest           | 80.0 ms                                                         | 69.8 ms: 1.15x faster                                                             |
| regex_v8                 | 15.8 ms                                                         | 14.0 ms: 1.13x faster                                                             |
| regex_dna                | 131 ms                                                          | 117 ms: 1.11x faster                                                              |
| regex_effbot             | 1.66 ms                                                         | 1.54 ms: 1.08x faster                                                             |
| unpickle_list            | 2.98 us                                                         | 2.77 us: 1.08x faster                                                             |
| pickle                   | 7.83 us                                                         | 7.48 us: 1.05x faster                                                             |
| pickle_list              | 3.22 us                                                         | 3.18 us: 1.01x faster                                                             |
| coverage                 | 46.6 ms                                                         | 48.8 ms: 1.05x slower                                                             |
| python_startup_no_site   | 18.1 ms                                                         | 19.0 ms: 1.05x slower                                                             |
| pickle_dict              | 18.2 us                                                         | 19.8 us: 1.09x slower                                                             |
| python_startup           | 22.9 ms                                                         | 25.2 ms: 1.10x slower                                                             |
| bench_mp_pool            | 66.4 ms                                                         | 88.6 ms: 1.34x slower                                                             |
| gc_traversal             | 1.28 ms                                                         | 2.05 ms: 1.60x slower                                                             |
| create_gc_cycles         | 694 us                                                          | 1.30 ms: 1.88x slower                                                             |
| Geometric mean           | (ref)                                                           | 1.52x faster                                                                      |

Benchmark hidden because not significant (1): async_generators
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20251101-3.15.0a1+-2f60b8f-JIT/bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.531x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.48x
- 95% likely to have a speedup of 1.46x
- 99% likely to have a speedup of 1.43x

# Memory
- memory change: unknown