# Results vs. 3.10.4

- fork: brandtbucher
- ref: msvc_musttail
- machine: windows-amd64
- commit hash: 06bc3bd
- commit date: 2025-03-07
- overall geometric mean: 1.391x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250307-pythonperf1_win32-amd64-brandtbucher-msvc_musttail-3.14.0a5+-06bc3bd |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 231 ms: 1.15x faster                                                             |
| docutils       | 1.95 sec                                                        | 1.77 sec: 1.10x faster                                                           |
| html5lib       | 52.1 ms                                                         | 38.8 ms: 1.34x faster                                                            |
| Geometric mean | (ref)                                                           | 1.19x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250307-pythonperf1_win32-amd64-brandtbucher-msvc_musttail-3.14.0a5+-06bc3bd |
|-------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 359 ms: 2.57x faster                                                             |
| async_tree_io           | 940 ms                                                          | 384 ms: 2.45x faster                                                             |
| async_tree_none         | 394 ms                                                          | 174 ms: 2.27x faster                                                             |
| async_tree_memoization  | 467 ms                                                          | 210 ms: 2.22x faster                                                             |
| Geometric mean          | (ref)                                                           | 2.37x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250307-pythonperf1_win32-amd64-brandtbucher-msvc_musttail-3.14.0a5+-06bc3bd |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 146 ms: 3.45x faster                                                             |
| float          | 69.6 ms                                                         | 41.4 ms: 1.68x faster                                                            |
| nbody          | 79.1 ms                                                         | 53.1 ms: 1.49x faster                                                            |
| Geometric mean | (ref)                                                           | 2.05x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250307-pythonperf1_win32-amd64-brandtbucher-msvc_musttail-3.14.0a5+-06bc3bd |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 81.9 ms: 1.42x faster                                                            |
| regex_dna      | 131 ms                                                          | 121 ms: 1.08x faster                                                             |
| regex_v8       | 15.8 ms                                                         | 16.3 ms: 1.03x slower                                                            |
| regex_effbot   | 1.66 ms                                                         | 1.85 ms: 1.11x slower                                                            |
| Geometric mean | (ref)                                                           | 1.08x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250307-pythonperf1_win32-amd64-brandtbucher-msvc_musttail-3.14.0a5+-06bc3bd |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 1.91 sec                                                        | 1.26 sec: 1.52x faster                                                           |
| unpickle_pure_python | 189 us                                                          | 148 us: 1.28x faster                                                             |
| json_dumps           | 9.82 ms                                                         | 7.79 ms: 1.26x faster                                                            |
| pickle_pure_python   | 280 us                                                          | 223 us: 1.26x faster                                                             |
| xml_etree_parse      | 120 ms                                                          | 105 ms: 1.15x faster                                                             |
| xml_etree_process    | 48.1 ms                                                         | 44.7 ms: 1.08x faster                                                            |
| json_loads           | 22.4 us                                                         | 21.9 us: 1.02x faster                                                            |
| xml_etree_iterparse  | 70.8 ms                                                         | 70.4 ms: 1.01x faster                                                            |
| xml_etree_generate   | 61.6 ms                                                         | 64.7 ms: 1.05x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.16x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250307-pythonperf1_win32-amd64-brandtbucher-msvc_musttail-3.14.0a5+-06bc3bd |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 19.4 ms: 1.08x slower                                                            |
| python_startup         | 22.9 ms                                                         | 26.4 ms: 1.15x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.11x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250307-pythonperf1_win32-amd64-brandtbucher-msvc_musttail-3.14.0a5+-06bc3bd |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 46.6 ms                                                         | 31.3 ms: 1.49x faster                                                            |
| genshi_text     | 21.0 ms                                                         | 14.5 ms: 1.45x faster                                                            |
| django_template | 36.0 ms                                                         | 25.2 ms: 1.43x faster                                                            |
| mako            | 9.10 ms                                                         | 7.84 ms: 1.16x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.38x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250307-pythonperf1_win32-amd64-brandtbucher-msvc_musttail-3.14.0a5+-06bc3bd |
|--------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 106 us: 3.73x faster                                                             |
| pidigits                 | 502 ms                                                          | 146 ms: 3.45x faster                                                             |
| pathlib                  | 81.2 ms                                                         | 25.1 ms: 3.24x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 359 ms: 2.57x faster                                                             |
| async_tree_io            | 940 ms                                                          | 384 ms: 2.45x faster                                                             |
| async_tree_none          | 394 ms                                                          | 174 ms: 2.27x faster                                                             |
| async_tree_memoization   | 467 ms                                                          | 210 ms: 2.22x faster                                                             |
| deltablue                | 4.04 ms                                                         | 1.91 ms: 2.11x faster                                                            |
| go                       | 146 ms                                                          | 70.4 ms: 2.07x faster                                                            |
| chaos                    | 74.4 ms                                                         | 37.7 ms: 1.97x faster                                                            |
| generators               | 31.6 ms                                                         | 16.3 ms: 1.94x faster                                                            |
| pylint                   | 384 ms                                                          | 205 ms: 1.87x faster                                                             |
| raytrace                 | 303 ms                                                          | 169 ms: 1.79x faster                                                             |
| deepcopy                 | 310 us                                                          | 180 us: 1.72x faster                                                             |
| crypto_pyaes             | 81.3 ms                                                         | 48.0 ms: 1.69x faster                                                            |
| float                    | 69.6 ms                                                         | 41.4 ms: 1.68x faster                                                            |
| scimark_sor              | 115 ms                                                          | 68.6 ms: 1.68x faster                                                            |
| thrift                   | 902 us                                                          | 551 us: 1.64x faster                                                             |
| logging_silent           | 97.9 ns                                                         | 61.1 ns: 1.60x faster                                                            |
| scimark_monte_carlo      | 61.9 ms                                                         | 38.9 ms: 1.59x faster                                                            |
| spectral_norm            | 80.2 ms                                                         | 51.1 ms: 1.57x faster                                                            |
| comprehensions           | 17.7 us                                                         | 11.3 us: 1.57x faster                                                            |
| hexiom                   | 6.13 ms                                                         | 3.92 ms: 1.57x faster                                                            |
| pyflate                  | 422 ms                                                          | 274 ms: 1.54x faster                                                             |
| deepcopy_memo            | 29.6 us                                                         | 19.3 us: 1.54x faster                                                            |
| tomli_loads              | 1.91 sec                                                        | 1.26 sec: 1.52x faster                                                           |
| nbody                    | 79.1 ms                                                         | 53.1 ms: 1.49x faster                                                            |
| genshi_xml               | 46.6 ms                                                         | 31.3 ms: 1.49x faster                                                            |
| pycparser                | 1.04 sec                                                        | 713 ms: 1.46x faster                                                             |
| coroutines               | 17.9 ms                                                         | 12.3 ms: 1.46x faster                                                            |
| nqueens                  | 87.1 ms                                                         | 59.6 ms: 1.46x faster                                                            |
| genshi_text              | 21.0 ms                                                         | 14.5 ms: 1.45x faster                                                            |
| django_template          | 36.0 ms                                                         | 25.2 ms: 1.43x faster                                                            |
| regex_compile            | 117 ms                                                          | 81.9 ms: 1.42x faster                                                            |
| deepcopy_reduce          | 2.68 us                                                         | 1.90 us: 1.41x faster                                                            |
| scimark_lu               | 89.8 ms                                                         | 64.2 ms: 1.40x faster                                                            |
| richards_super           | 49.9 ms                                                         | 35.8 ms: 1.39x faster                                                            |
| dulwich_log              | 58.5 ms                                                         | 42.3 ms: 1.38x faster                                                            |
| sqlite_synth             | 2.29 us                                                         | 1.68 us: 1.37x faster                                                            |
| html5lib                 | 52.1 ms                                                         | 38.8 ms: 1.34x faster                                                            |
| sympy_sum                | 122 ms                                                          | 91.4 ms: 1.34x faster                                                            |
| pprint_pformat           | 1.37 sec                                                        | 1.04 sec: 1.32x faster                                                           |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.47 ms: 1.31x faster                                                            |
| richards                 | 40.3 ms                                                         | 30.9 ms: 1.30x faster                                                            |
| sympy_str                | 229 ms                                                          | 177 ms: 1.29x faster                                                             |
| pprint_safe_repr         | 658 ms                                                          | 510 ms: 1.29x faster                                                             |
| sympy_expand             | 391 ms                                                          | 304 ms: 1.28x faster                                                             |
| scimark_fft              | 216 ms                                                          | 169 ms: 1.28x faster                                                             |
| unpickle_pure_python     | 189 us                                                          | 148 us: 1.28x faster                                                             |
| bench_thread_pool        | 1.12 ms                                                         | 876 us: 1.28x faster                                                             |
| fannkuch                 | 317 ms                                                          | 250 ms: 1.27x faster                                                             |
| mdp                      | 1.83 sec                                                        | 1.44 sec: 1.26x faster                                                           |
| json_dumps               | 9.82 ms                                                         | 7.79 ms: 1.26x faster                                                            |
| json                     | 4.76 ms                                                         | 3.78 ms: 1.26x faster                                                            |
| pickle_pure_python       | 280 us                                                          | 223 us: 1.26x faster                                                             |
| sympy_integrate          | 16.6 ms                                                         | 13.4 ms: 1.24x faster                                                            |
| logging_format           | 7.91 us                                                         | 6.70 us: 1.18x faster                                                            |
| logging_simple           | 7.29 us                                                         | 6.25 us: 1.17x faster                                                            |
| mako                     | 9.10 ms                                                         | 7.84 ms: 1.16x faster                                                            |
| 2to3                     | 265 ms                                                          | 231 ms: 1.15x faster                                                             |
| xml_etree_parse          | 120 ms                                                          | 105 ms: 1.15x faster                                                             |
| async_generators         | 241 ms                                                          | 213 ms: 1.13x faster                                                             |
| docutils                 | 1.95 sec                                                        | 1.77 sec: 1.10x faster                                                           |
| regex_dna                | 131 ms                                                          | 121 ms: 1.08x faster                                                             |
| xml_etree_process        | 48.1 ms                                                         | 44.7 ms: 1.08x faster                                                            |
| meteor_contest           | 80.0 ms                                                         | 74.5 ms: 1.07x faster                                                            |
| json_loads               | 22.4 us                                                         | 21.9 us: 1.02x faster                                                            |
| xml_etree_iterparse      | 70.8 ms                                                         | 70.4 ms: 1.01x faster                                                            |
| regex_v8                 | 15.8 ms                                                         | 16.3 ms: 1.03x slower                                                            |
| xml_etree_generate       | 61.6 ms                                                         | 64.7 ms: 1.05x slower                                                            |
| python_startup_no_site   | 18.1 ms                                                         | 19.4 ms: 1.08x slower                                                            |
| telco                    | 4.83 ms                                                         | 5.26 ms: 1.09x slower                                                            |
| regex_effbot             | 1.66 ms                                                         | 1.85 ms: 1.11x slower                                                            |
| python_startup           | 22.9 ms                                                         | 26.4 ms: 1.15x slower                                                            |
| coverage                 | 46.6 ms                                                         | 55.4 ms: 1.19x slower                                                            |
| bench_mp_pool            | 66.4 ms                                                         | 93.6 ms: 1.41x slower                                                            |
| create_gc_cycles         | 694 us                                                          | 1.34 ms: 1.93x slower                                                            |
| gc_traversal             | 1.28 ms                                                         | 2.83 ms: 2.21x slower                                                            |
| Geometric mean           | (ref)                                                           | 1.38x faster                                                                     |
Ignored benchmarks (20) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250225-3.14.0a5+-f963239/bm-20250307-pythonperf1_win32-amd64-brandtbucher-msvc_musttail-3.14.0a5+-06bc3bd.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.391x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.28x

# Memory
- memory change: unknown