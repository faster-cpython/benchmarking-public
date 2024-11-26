# Results vs. 3.10.4

- fork: eendebakpt
- ref: int_freelist
- machine: windows-x86
- commit hash: d1e4aa2
- commit date: 2024-11-21
- overall geometric mean: 1.133x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241121-pythonperf1_win32-x86-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 246 ms: 1.08x faster                                                        |
| docutils       | 1.95 sec                                                        | 1.83 sec: 1.06x faster                                                      |
| html5lib       | 52.1 ms                                                         | 44.5 ms: 1.17x faster                                                       |
| Geometric mean | (ref)                                                           | 1.10x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241121-pythonperf1_win32-x86-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|-------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 469 ms: 1.97x faster                                                        |
| async_tree_none         | 394 ms                                                          | 220 ms: 1.79x faster                                                        |
| async_tree_io           | 940 ms                                                          | 527 ms: 1.79x faster                                                        |
| async_tree_memoization  | 467 ms                                                          | 273 ms: 1.71x faster                                                        |
| Geometric mean          | (ref)                                                           | 1.81x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241121-pythonperf1_win32-x86-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 202 ms: 2.48x faster                                                        |
| float          | 69.6 ms                                                         | 62.8 ms: 1.11x faster                                                       |
| nbody          | 79.1 ms                                                         | 93.1 ms: 1.18x slower                                                       |
| Geometric mean | (ref)                                                           | 1.33x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241121-pythonperf1_win32-x86-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 108 ms: 1.08x faster                                                        |
| regex_dna      | 131 ms                                                          | 123 ms: 1.06x faster                                                        |
| regex_v8       | 15.8 ms                                                         | 15.6 ms: 1.01x faster                                                       |
| regex_effbot   | 1.66 ms                                                         | 1.88 ms: 1.13x slower                                                       |
| Geometric mean | (ref)                                                           | 1.01x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241121-pythonperf1_win32-x86-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 8.61 ms: 1.14x faster                                                       |
| tomli_loads          | 1.91 sec                                                        | 1.75 sec: 1.09x faster                                                      |
| unpickle_pure_python | 189 us                                                          | 174 us: 1.09x faster                                                        |
| json_loads           | 22.4 us                                                         | 20.9 us: 1.07x faster                                                       |
| xml_etree_parse      | 120 ms                                                          | 112 ms: 1.07x faster                                                        |
| pickle_pure_python   | 280 us                                                          | 272 us: 1.03x faster                                                        |
| xml_etree_iterparse  | 70.8 ms                                                         | 68.9 ms: 1.03x faster                                                       |
| xml_etree_process    | 48.1 ms                                                         | 49.7 ms: 1.03x slower                                                       |
| xml_etree_generate   | 61.6 ms                                                         | 67.8 ms: 1.10x slower                                                       |
| Geometric mean       | (ref)                                                           | 1.04x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241121-pythonperf1_win32-x86-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 20.0 ms: 1.11x slower                                                       |
| python_startup         | 22.9 ms                                                         | 26.6 ms: 1.16x slower                                                       |
| Geometric mean         | (ref)                                                           | 1.13x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241121-pythonperf1_win32-x86-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 7.68 ms: 1.19x faster                                                       |
| django_template | 36.0 ms                                                         | 31.4 ms: 1.15x faster                                                       |
| Geometric mean  | (ref)                                                           | 1.08x faster                                                                |

Benchmark hidden because not significant (2): genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241121-pythonperf1_win32-x86-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|--------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 143 us: 2.76x faster                                                        |
| pidigits                 | 502 ms                                                          | 202 ms: 2.48x faster                                                        |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 469 ms: 1.97x faster                                                        |
| async_tree_none          | 394 ms                                                          | 220 ms: 1.79x faster                                                        |
| async_tree_io            | 940 ms                                                          | 527 ms: 1.79x faster                                                        |
| async_tree_memoization   | 467 ms                                                          | 273 ms: 1.71x faster                                                        |
| pylint                   | 384 ms                                                          | 229 ms: 1.68x faster                                                        |
| deltablue                | 4.04 ms                                                         | 2.61 ms: 1.55x faster                                                       |
| go                       | 146 ms                                                          | 99.9 ms: 1.46x faster                                                       |
| logging_silent           | 97.9 ns                                                         | 70.9 ns: 1.38x faster                                                       |
| deepcopy_memo            | 29.6 us                                                         | 21.7 us: 1.36x faster                                                       |
| crypto_pyaes             | 81.3 ms                                                         | 61.2 ms: 1.33x faster                                                       |
| generators               | 31.6 ms                                                         | 23.8 ms: 1.33x faster                                                       |
| deepcopy                 | 310 us                                                          | 236 us: 1.31x faster                                                        |
| scimark_lu               | 89.8 ms                                                         | 68.4 ms: 1.31x faster                                                       |
| comprehensions           | 17.7 us                                                         | 13.6 us: 1.30x faster                                                       |
| chaos                    | 74.4 ms                                                         | 58.3 ms: 1.28x faster                                                       |
| sqlglot_parse            | 1.33 ms                                                         | 1.06 ms: 1.26x faster                                                       |
| pycparser                | 1.04 sec                                                        | 837 ms: 1.25x faster                                                        |
| hexiom                   | 6.13 ms                                                         | 5.05 ms: 1.22x faster                                                       |
| sqlglot_transpile        | 1.58 ms                                                         | 1.31 ms: 1.21x faster                                                       |
| thrift                   | 902 us                                                          | 752 us: 1.20x faster                                                        |
| sqlite_synth             | 2.29 us                                                         | 1.92 us: 1.19x faster                                                       |
| mako                     | 9.10 ms                                                         | 7.68 ms: 1.19x faster                                                       |
| dulwich_log              | 58.5 ms                                                         | 49.9 ms: 1.17x faster                                                       |
| html5lib                 | 52.1 ms                                                         | 44.5 ms: 1.17x faster                                                       |
| pyflate                  | 422 ms                                                          | 362 ms: 1.17x faster                                                        |
| sympy_sum                | 122 ms                                                          | 106 ms: 1.16x faster                                                        |
| django_template          | 36.0 ms                                                         | 31.4 ms: 1.15x faster                                                       |
| json_dumps               | 9.82 ms                                                         | 8.61 ms: 1.14x faster                                                       |
| spectral_norm            | 80.2 ms                                                         | 70.8 ms: 1.13x faster                                                       |
| raytrace                 | 303 ms                                                          | 269 ms: 1.13x faster                                                        |
| scimark_sor              | 115 ms                                                          | 103 ms: 1.12x faster                                                        |
| scimark_monte_carlo      | 61.9 ms                                                         | 55.6 ms: 1.11x faster                                                       |
| bench_thread_pool        | 1.12 ms                                                         | 1.01 ms: 1.11x faster                                                       |
| float                    | 69.6 ms                                                         | 62.8 ms: 1.11x faster                                                       |
| richards_super           | 49.9 ms                                                         | 45.0 ms: 1.11x faster                                                       |
| nqueens                  | 87.1 ms                                                         | 78.9 ms: 1.10x faster                                                       |
| json                     | 4.76 ms                                                         | 4.32 ms: 1.10x faster                                                       |
| tomli_loads              | 1.91 sec                                                        | 1.75 sec: 1.09x faster                                                      |
| unpickle_pure_python     | 189 us                                                          | 174 us: 1.09x faster                                                        |
| regex_compile            | 117 ms                                                          | 108 ms: 1.08x faster                                                        |
| deepcopy_reduce          | 2.68 us                                                         | 2.48 us: 1.08x faster                                                       |
| sqlglot_optimize         | 44.7 ms                                                         | 41.3 ms: 1.08x faster                                                       |
| 2to3                     | 265 ms                                                          | 246 ms: 1.08x faster                                                        |
| sympy_integrate          | 16.6 ms                                                         | 15.4 ms: 1.08x faster                                                       |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.01 ms: 1.08x faster                                                       |
| sqlglot_normalize        | 230 ms                                                          | 215 ms: 1.07x faster                                                        |
| sympy_str                | 229 ms                                                          | 214 ms: 1.07x faster                                                        |
| richards                 | 40.3 ms                                                         | 37.6 ms: 1.07x faster                                                       |
| json_loads               | 22.4 us                                                         | 20.9 us: 1.07x faster                                                       |
| xml_etree_parse          | 120 ms                                                          | 112 ms: 1.07x faster                                                        |
| docutils                 | 1.95 sec                                                        | 1.83 sec: 1.06x faster                                                      |
| mdp                      | 1.83 sec                                                        | 1.72 sec: 1.06x faster                                                      |
| regex_dna                | 131 ms                                                          | 123 ms: 1.06x faster                                                        |
| coroutines               | 17.9 ms                                                         | 17.0 ms: 1.06x faster                                                       |
| sympy_expand             | 391 ms                                                          | 374 ms: 1.04x faster                                                        |
| pprint_pformat           | 1.37 sec                                                        | 1.32 sec: 1.04x faster                                                      |
| pprint_safe_repr         | 658 ms                                                          | 635 ms: 1.04x faster                                                        |
| pickle_pure_python       | 280 us                                                          | 272 us: 1.03x faster                                                        |
| xml_etree_iterparse      | 70.8 ms                                                         | 68.9 ms: 1.03x faster                                                       |
| regex_v8                 | 15.8 ms                                                         | 15.6 ms: 1.01x faster                                                       |
| fannkuch                 | 317 ms                                                          | 319 ms: 1.00x slower                                                        |
| meteor_contest           | 80.0 ms                                                         | 81.6 ms: 1.02x slower                                                       |
| pathlib                  | 81.2 ms                                                         | 82.9 ms: 1.02x slower                                                       |
| scimark_fft              | 216 ms                                                          | 222 ms: 1.02x slower                                                        |
| xml_etree_process        | 48.1 ms                                                         | 49.7 ms: 1.03x slower                                                       |
| logging_simple           | 7.29 us                                                         | 7.89 us: 1.08x slower                                                       |
| logging_format           | 7.91 us                                                         | 8.61 us: 1.09x slower                                                       |
| xml_etree_generate       | 61.6 ms                                                         | 67.8 ms: 1.10x slower                                                       |
| python_startup_no_site   | 18.1 ms                                                         | 20.0 ms: 1.11x slower                                                       |
| coverage                 | 46.6 ms                                                         | 51.6 ms: 1.11x slower                                                       |
| regex_effbot             | 1.66 ms                                                         | 1.88 ms: 1.13x slower                                                       |
| python_startup           | 22.9 ms                                                         | 26.6 ms: 1.16x slower                                                       |
| nbody                    | 79.1 ms                                                         | 93.1 ms: 1.18x slower                                                       |
| async_generators         | 241 ms                                                          | 291 ms: 1.21x slower                                                        |
| telco                    | 4.83 ms                                                         | 6.42 ms: 1.33x slower                                                       |
| gc_traversal             | 1.28 ms                                                         | 1.77 ms: 1.38x slower                                                       |
| bench_mp_pool            | 66.4 ms                                                         | 92.1 ms: 1.39x slower                                                       |
| create_gc_cycles         | 694 us                                                          | 1.15 ms: 1.65x slower                                                       |
| Geometric mean           | (ref)                                                           | 1.13x faster                                                                |

Benchmark hidden because not significant (2): genshi_xml, genshi_text
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20241121-3.14.0a1+-d1e4aa2/bm-20241121-pythonperf1_win32-x86-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.133x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: unknown