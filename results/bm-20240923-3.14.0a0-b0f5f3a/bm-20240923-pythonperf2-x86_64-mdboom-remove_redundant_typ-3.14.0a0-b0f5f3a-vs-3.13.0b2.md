# Results vs. 3.13.0b2

- fork: mdboom
- ref: remove_redundant_typ
- machine: linux-x86_64
- commit hash: b0f5f3a
- commit date: 2024-09-23
- overall geometric mean: 1.03x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240923-pythonperf2-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 283 ms: 1.03x faster                                                        |
| docutils       | 2.98 sec                                                         | 2.91 sec: 1.03x faster                                                      |
| html5lib       | 74.7 ms                                                          | 71.8 ms: 1.04x faster                                                       |
| tornado_http   | 119 ms                                                           | 116 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                            | 1.03x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240923-pythonperf2-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|---------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization    | 460 ms                                                           | 398 ms: 1.15x faster                                                        |
| async_tree_io_tg          | 900 ms                                                           | 781 ms: 1.15x faster                                                        |
| async_tree_none           | 365 ms                                                           | 319 ms: 1.15x faster                                                        |
| async_tree_none_tg        | 340 ms                                                           | 308 ms: 1.10x faster                                                        |
| async_tree_memoization_tg | 421 ms                                                           | 387 ms: 1.09x faster                                                        |
| async_tree_io             | 873 ms                                                           | 809 ms: 1.08x faster                                                        |
| async_tree_cpu_io_mixed   | 604 ms                                                           | 572 ms: 1.06x faster                                                        |
| Geometric mean            | (ref)                                                            | 1.10x faster                                                                |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240923-pythonperf2-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 80.2 ms                                                          | 78.7 ms: 1.02x faster                                                       |
| pidigits       | 254 ms                                                           | 252 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                            | 1.00x faster                                                                |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240923-pythonperf2-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 249 ms                                                           | 235 ms: 1.06x faster                                                        |
| regex_compile  | 144 ms                                                           | 138 ms: 1.04x faster                                                        |
| regex_v8       | 26.0 ms                                                          | 25.2 ms: 1.03x faster                                                       |
| regex_effbot   | 3.40 ms                                                          | 3.51 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                            | 1.03x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240923-pythonperf2-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|---------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle            | 15.7 us                                                          | 15.0 us: 1.04x faster                                                       |
| xml_etree_iterparse | 103 ms                                                           | 100 ms: 1.02x faster                                                        |
| xml_etree_parse     | 144 ms                                                           | 141 ms: 1.02x faster                                                        |
| xml_etree_process   | 59.7 ms                                                          | 59.1 ms: 1.01x faster                                                       |
| xml_etree_generate  | 85.7 ms                                                          | 85.4 ms: 1.00x faster                                                       |
| pickle_dict         | 32.8 us                                                          | 32.7 us: 1.00x faster                                                       |
| json_loads          | 25.0 us                                                          | 25.1 us: 1.00x slower                                                       |
| pickle              | 10.6 us                                                          | 10.7 us: 1.01x slower                                                       |
| json_dumps          | 10.8 ms                                                          | 11.0 ms: 1.02x slower                                                       |
| pickle_pure_python  | 307 us                                                           | 315 us: 1.02x slower                                                        |
| pickle_list         | 4.44 us                                                          | 4.64 us: 1.04x slower                                                       |
| tomli_loads         | 2.40 sec                                                         | 2.59 sec: 1.08x slower                                                      |
| Geometric mean      | (ref)                                                            | 1.01x slower                                                                |

Benchmark hidden because not significant (2): unpickle_pure_python, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240923-pythonperf2-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                                       |
| python_startup_no_site | 8.85 ms                                                          | 8.96 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                            | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240923-pythonperf2-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|-----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 58.1 ms                                                          | 53.6 ms: 1.08x faster                                                       |
| genshi_text     | 25.9 ms                                                          | 24.1 ms: 1.07x faster                                                       |
| django_template | 39.0 ms                                                          | 40.3 ms: 1.03x slower                                                       |
| Geometric mean  | (ref)                                                            | 1.03x faster                                                                |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240923-pythonperf2-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|---------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy                  | 377 us                                                           | 284 us: 1.33x faster                                                        |
| deepcopy_memo             | 37.3 us                                                          | 30.0 us: 1.24x faster                                                       |
| go                        | 165 ms                                                           | 136 ms: 1.21x faster                                                        |
| deepcopy_reduce           | 3.39 us                                                          | 2.86 us: 1.18x faster                                                       |
| generators                | 33.5 ms                                                          | 28.9 ms: 1.16x faster                                                       |
| async_tree_memoization    | 460 ms                                                           | 398 ms: 1.15x faster                                                        |
| async_tree_io_tg          | 900 ms                                                           | 781 ms: 1.15x faster                                                        |
| async_tree_none           | 365 ms                                                           | 319 ms: 1.15x faster                                                        |
| async_tree_none_tg        | 340 ms                                                           | 308 ms: 1.10x faster                                                        |
| richards_super            | 61.2 ms                                                          | 56.0 ms: 1.09x faster                                                       |
| async_tree_memoization_tg | 421 ms                                                           | 387 ms: 1.09x faster                                                        |
| genshi_xml                | 58.1 ms                                                          | 53.6 ms: 1.08x faster                                                       |
| pathlib                   | 17.1 ms                                                          | 15.8 ms: 1.08x faster                                                       |
| async_tree_io             | 873 ms                                                           | 809 ms: 1.08x faster                                                        |
| genshi_text               | 25.9 ms                                                          | 24.1 ms: 1.07x faster                                                       |
| richards                  | 53.4 ms                                                          | 50.2 ms: 1.06x faster                                                       |
| regex_dna                 | 249 ms                                                           | 235 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed   | 604 ms                                                           | 572 ms: 1.06x faster                                                        |
| create_gc_cycles          | 2.00 ms                                                          | 1.91 ms: 1.05x faster                                                       |
| bpe_tokeniser             | 5.14 sec                                                         | 4.90 sec: 1.05x faster                                                      |
| bench_thread_pool         | 908 us                                                           | 867 us: 1.05x faster                                                        |
| unpickle                  | 15.7 us                                                          | 15.0 us: 1.04x faster                                                       |
| coverage                  | 83.5 ms                                                          | 80.2 ms: 1.04x faster                                                       |
| regex_compile             | 144 ms                                                           | 138 ms: 1.04x faster                                                        |
| html5lib                  | 74.7 ms                                                          | 71.8 ms: 1.04x faster                                                       |
| telco                     | 8.40 ms                                                          | 8.11 ms: 1.04x faster                                                       |
| tornado_http              | 119 ms                                                           | 116 ms: 1.03x faster                                                        |
| regex_v8                  | 26.0 ms                                                          | 25.2 ms: 1.03x faster                                                       |
| 2to3                      | 291 ms                                                           | 283 ms: 1.03x faster                                                        |
| sqlglot_optimize          | 59.5 ms                                                          | 57.9 ms: 1.03x faster                                                       |
| sqlglot_normalize         | 120 ms                                                           | 117 ms: 1.03x faster                                                        |
| hexiom                    | 6.35 ms                                                          | 6.19 ms: 1.03x faster                                                       |
| logging_format            | 7.11 us                                                          | 6.93 us: 1.03x faster                                                       |
| docutils                  | 2.98 sec                                                         | 2.91 sec: 1.03x faster                                                      |
| scimark_fft               | 312 ms                                                           | 304 ms: 1.03x faster                                                        |
| xml_etree_iterparse       | 103 ms                                                           | 100 ms: 1.02x faster                                                        |
| sympy_sum                 | 155 ms                                                           | 152 ms: 1.02x faster                                                        |
| sympy_str                 | 295 ms                                                           | 289 ms: 1.02x faster                                                        |
| pprint_safe_repr          | 818 ms                                                           | 802 ms: 1.02x faster                                                        |
| float                     | 80.2 ms                                                          | 78.7 ms: 1.02x faster                                                       |
| dulwich_log               | 67.3 ms                                                          | 66.1 ms: 1.02x faster                                                       |
| xml_etree_parse           | 144 ms                                                           | 141 ms: 1.02x faster                                                        |
| scimark_lu                | 97.5 ms                                                          | 95.8 ms: 1.02x faster                                                       |
| scimark_sor               | 119 ms                                                           | 117 ms: 1.01x faster                                                        |
| asyncio_websockets        | 395 ms                                                           | 390 ms: 1.01x faster                                                        |
| sqlite_synth              | 2.80 us                                                          | 2.76 us: 1.01x faster                                                       |
| async_generators          | 363 ms                                                           | 358 ms: 1.01x faster                                                        |
| sympy_integrate           | 23.2 ms                                                          | 22.9 ms: 1.01x faster                                                       |
| json                      | 5.35 ms                                                          | 5.29 ms: 1.01x faster                                                       |
| xml_etree_process         | 59.7 ms                                                          | 59.1 ms: 1.01x faster                                                       |
| asyncio_tcp               | 378 ms                                                           | 374 ms: 1.01x faster                                                        |
| spectral_norm             | 97.3 ms                                                          | 96.4 ms: 1.01x faster                                                       |
| pidigits                  | 254 ms                                                           | 252 ms: 1.01x faster                                                        |
| thrift                    | 880 us                                                           | 874 us: 1.01x faster                                                        |
| meteor_contest            | 128 ms                                                           | 128 ms: 1.00x faster                                                        |
| scimark_sparse_mat_mult   | 4.28 ms                                                          | 4.26 ms: 1.00x faster                                                       |
| xml_etree_generate        | 85.7 ms                                                          | 85.4 ms: 1.00x faster                                                       |
| sympy_expand              | 501 ms                                                           | 499 ms: 1.00x faster                                                        |
| asyncio_tcp_ssl           | 1.58 sec                                                         | 1.57 sec: 1.00x faster                                                      |
| pickle_dict               | 32.8 us                                                          | 32.7 us: 1.00x faster                                                       |
| json_loads                | 25.0 us                                                          | 25.1 us: 1.00x slower                                                       |
| coroutines                | 22.0 ms                                                          | 22.1 ms: 1.00x slower                                                       |
| typing_runtime_protocols  | 171 us                                                           | 172 us: 1.01x slower                                                        |
| pickle                    | 10.6 us                                                          | 10.7 us: 1.01x slower                                                       |
| python_startup            | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                                       |
| python_startup_no_site    | 8.85 ms                                                          | 8.96 ms: 1.01x slower                                                       |
| comprehensions            | 17.0 us                                                          | 17.2 us: 1.01x slower                                                       |
| pyflate                   | 482 ms                                                           | 489 ms: 1.02x slower                                                        |
| mdp                       | 2.46 sec                                                         | 2.50 sec: 1.02x slower                                                      |
| fannkuch                  | 353 ms                                                           | 359 ms: 1.02x slower                                                        |
| json_dumps                | 10.8 ms                                                          | 11.0 ms: 1.02x slower                                                       |
| pycparser                 | 1.22 sec                                                         | 1.25 sec: 1.02x slower                                                      |
| sqlglot_parse             | 1.39 ms                                                          | 1.42 ms: 1.02x slower                                                       |
| pickle_pure_python        | 307 us                                                           | 315 us: 1.02x slower                                                        |
| sqlglot_transpile         | 1.76 ms                                                          | 1.81 ms: 1.03x slower                                                       |
| scimark_monte_carlo       | 65.5 ms                                                          | 67.2 ms: 1.03x slower                                                       |
| raytrace                  | 260 ms                                                           | 268 ms: 1.03x slower                                                        |
| regex_effbot              | 3.40 ms                                                          | 3.51 ms: 1.03x slower                                                       |
| django_template           | 39.0 ms                                                          | 40.3 ms: 1.03x slower                                                       |
| gc_traversal              | 4.69 ms                                                          | 4.87 ms: 1.04x slower                                                       |
| logging_silent            | 96.3 ns                                                          | 100 ns: 1.04x slower                                                        |
| pickle_list               | 4.44 us                                                          | 4.64 us: 1.04x slower                                                       |
| chaos                     | 59.6 ms                                                          | 62.6 ms: 1.05x slower                                                       |
| tomli_loads               | 2.40 sec                                                         | 2.59 sec: 1.08x slower                                                      |
| Geometric mean            | (ref)                                                            | 1.03x faster                                                                |

Benchmark hidden because not significant (12): bench_mp_pool, async_tree_cpu_io_mixed_tg, logging_simple, mako, pprint_pformat, unpickle_pure_python, nqueens, crypto_pyaes, deltablue, unpickle_list, nbody, pylint
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240923-3.14.0a0-b0f5f3a/bm-20240923-pythonperf2-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x