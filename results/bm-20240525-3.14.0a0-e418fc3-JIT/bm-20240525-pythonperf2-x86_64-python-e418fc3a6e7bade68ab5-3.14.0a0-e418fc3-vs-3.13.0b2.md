# Results vs. 3.13.0b2

- fork: python
- ref: e418fc3a6e7bade68ab5
- machine: linux-x86_64
- commit hash: e418fc3
- commit date: 2024-05-25
- overall geometric mean: 1.02x slower
- HPT reliability: 98.13%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 305 ms: 1.05x slower                                                        |
| chameleon      | 7.40 ms                                                          | 7.68 ms: 1.04x slower                                                       |
| docutils       | 2.98 sec                                                         | 3.13 sec: 1.05x slower                                                      |
| html5lib       | 74.7 ms                                                          | 74.3 ms: 1.00x faster                                                       |
| tornado_http   | 119 ms                                                           | 124 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                            | 1.03x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|---------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg | 421 ms                                                           | 432 ms: 1.03x slower                                                        |
| async_tree_none           | 365 ms                                                           | 376 ms: 1.03x slower                                                        |
| async_tree_cpu_io_mixed   | 604 ms                                                           | 624 ms: 1.03x slower                                                        |
| async_tree_io             | 873 ms                                                           | 903 ms: 1.03x slower                                                        |
| Geometric mean            | (ref)                                                            | 1.02x slower                                                                |

Benchmark hidden because not significant (4): async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 80.2 ms                                                          | 74.2 ms: 1.08x faster                                                       |
| nbody          | 87.8 ms                                                          | 81.6 ms: 1.08x faster                                                       |
| pidigits       | 254 ms                                                           | 250 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                            | 1.06x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                           | 138 ms: 1.04x faster                                                        |
| regex_dna      | 249 ms                                                           | 243 ms: 1.03x faster                                                        |
| regex_v8       | 26.0 ms                                                          | 26.0 ms: 1.00x faster                                                       |
| regex_effbot   | 3.40 ms                                                          | 3.67 ms: 1.08x slower                                                       |
| Geometric mean | (ref)                                                            | 1.00x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.40 sec                                                         | 2.12 sec: 1.13x faster                                                      |
| xml_etree_generate   | 85.7 ms                                                          | 81.8 ms: 1.05x faster                                                       |
| xml_etree_process    | 59.7 ms                                                          | 58.0 ms: 1.03x faster                                                       |
| pickle_dict          | 32.8 us                                                          | 32.0 us: 1.03x faster                                                       |
| json_loads           | 25.0 us                                                          | 24.5 us: 1.02x faster                                                       |
| unpickle             | 15.7 us                                                          | 15.4 us: 1.02x faster                                                       |
| xml_etree_iterparse  | 103 ms                                                           | 101 ms: 1.02x faster                                                        |
| json_dumps           | 10.8 ms                                                          | 10.6 ms: 1.02x faster                                                       |
| unpickle_pure_python | 224 us                                                           | 222 us: 1.01x faster                                                        |
| pickle               | 10.6 us                                                          | 10.7 us: 1.01x slower                                                       |
| unpickle_list        | 4.70 us                                                          | 4.79 us: 1.02x slower                                                       |
| pickle_pure_python   | 307 us                                                           | 318 us: 1.03x slower                                                        |
| xml_etree_parse      | 144 ms                                                           | 149 ms: 1.04x slower                                                        |
| Geometric mean       | (ref)                                                            | 1.02x faster                                                                |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 13.8 ms: 1.05x slower                                                       |
| python_startup_no_site | 8.85 ms                                                          | 9.48 ms: 1.07x slower                                                       |
| Geometric mean         | (ref)                                                            | 1.06x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|-----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 10.4 ms                                                          | 9.14 ms: 1.13x faster                                                       |
| django_template | 39.0 ms                                                          | 41.4 ms: 1.06x slower                                                       |
| genshi_xml      | 58.1 ms                                                          | 64.8 ms: 1.12x slower                                                       |
| genshi_text     | 25.9 ms                                                          | 29.1 ms: 1.12x slower                                                       |
| Geometric mean  | (ref)                                                            | 1.04x slower                                                                |

All benchmarks:
===============

| Benchmark                 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|---------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| richards_super            | 61.2 ms                                                          | 52.7 ms: 1.16x faster                                                       |
| richards                  | 53.4 ms                                                          | 46.1 ms: 1.16x faster                                                       |
| spectral_norm             | 97.3 ms                                                          | 84.3 ms: 1.16x faster                                                       |
| mako                      | 10.4 ms                                                          | 9.14 ms: 1.13x faster                                                       |
| tomli_loads               | 2.40 sec                                                         | 2.12 sec: 1.13x faster                                                      |
| scimark_sparse_mat_mult   | 4.28 ms                                                          | 3.91 ms: 1.10x faster                                                       |
| scimark_fft               | 312 ms                                                           | 288 ms: 1.08x faster                                                        |
| float                     | 80.2 ms                                                          | 74.2 ms: 1.08x faster                                                       |
| nbody                     | 87.8 ms                                                          | 81.6 ms: 1.08x faster                                                       |
| pathlib                   | 17.1 ms                                                          | 16.2 ms: 1.06x faster                                                       |
| fannkuch                  | 353 ms                                                           | 336 ms: 1.05x faster                                                        |
| crypto_pyaes              | 73.6 ms                                                          | 70.2 ms: 1.05x faster                                                       |
| xml_etree_generate        | 85.7 ms                                                          | 81.8 ms: 1.05x faster                                                       |
| regex_compile             | 144 ms                                                           | 138 ms: 1.04x faster                                                        |
| pyflate                   | 482 ms                                                           | 463 ms: 1.04x faster                                                        |
| xml_etree_process         | 59.7 ms                                                          | 58.0 ms: 1.03x faster                                                       |
| telco                     | 8.40 ms                                                          | 8.17 ms: 1.03x faster                                                       |
| regex_dna                 | 249 ms                                                           | 243 ms: 1.03x faster                                                        |
| go                        | 165 ms                                                           | 161 ms: 1.03x faster                                                        |
| pickle_dict               | 32.8 us                                                          | 32.0 us: 1.03x faster                                                       |
| json_loads                | 25.0 us                                                          | 24.5 us: 1.02x faster                                                       |
| coroutines                | 22.0 ms                                                          | 21.5 ms: 1.02x faster                                                       |
| unpickle                  | 15.7 us                                                          | 15.4 us: 1.02x faster                                                       |
| pprint_safe_repr          | 818 ms                                                           | 802 ms: 1.02x faster                                                        |
| xml_etree_iterparse       | 103 ms                                                           | 101 ms: 1.02x faster                                                        |
| json_dumps                | 10.8 ms                                                          | 10.6 ms: 1.02x faster                                                       |
| logging_format            | 7.11 us                                                          | 7.01 us: 1.01x faster                                                       |
| asyncio_websockets        | 395 ms                                                           | 390 ms: 1.01x faster                                                        |
| sqlite_synth              | 2.80 us                                                          | 2.76 us: 1.01x faster                                                       |
| pidigits                  | 254 ms                                                           | 250 ms: 1.01x faster                                                        |
| unpickle_pure_python      | 224 us                                                           | 222 us: 1.01x faster                                                        |
| json                      | 5.35 ms                                                          | 5.30 ms: 1.01x faster                                                       |
| html5lib                  | 74.7 ms                                                          | 74.3 ms: 1.00x faster                                                       |
| dulwich_log               | 67.3 ms                                                          | 67.0 ms: 1.00x faster                                                       |
| regex_v8                  | 26.0 ms                                                          | 26.0 ms: 1.00x faster                                                       |
| meteor_contest            | 128 ms                                                           | 129 ms: 1.00x slower                                                        |
| logging_simple            | 6.40 us                                                          | 6.45 us: 1.01x slower                                                       |
| pickle                    | 10.6 us                                                          | 10.7 us: 1.01x slower                                                       |
| deepcopy_memo             | 37.3 us                                                          | 37.8 us: 1.01x slower                                                       |
| unpickle_list             | 4.70 us                                                          | 4.79 us: 1.02x slower                                                       |
| coverage                  | 83.5 ms                                                          | 85.2 ms: 1.02x slower                                                       |
| sqlglot_parse             | 1.39 ms                                                          | 1.42 ms: 1.02x slower                                                       |
| generators                | 33.5 ms                                                          | 34.4 ms: 1.03x slower                                                       |
| async_tree_memoization_tg | 421 ms                                                           | 432 ms: 1.03x slower                                                        |
| thrift                    | 880 us                                                           | 904 us: 1.03x slower                                                        |
| async_tree_none           | 365 ms                                                           | 376 ms: 1.03x slower                                                        |
| async_tree_cpu_io_mixed   | 604 ms                                                           | 624 ms: 1.03x slower                                                        |
| sqlglot_transpile         | 1.76 ms                                                          | 1.82 ms: 1.03x slower                                                       |
| pickle_pure_python        | 307 us                                                           | 318 us: 1.03x slower                                                        |
| async_tree_io             | 873 ms                                                           | 903 ms: 1.03x slower                                                        |
| scimark_monte_carlo       | 65.5 ms                                                          | 68.0 ms: 1.04x slower                                                       |
| chameleon                 | 7.40 ms                                                          | 7.68 ms: 1.04x slower                                                       |
| xml_etree_parse           | 144 ms                                                           | 149 ms: 1.04x slower                                                        |
| tornado_http              | 119 ms                                                           | 124 ms: 1.04x slower                                                        |
| dask                      | 391 ms                                                           | 406 ms: 1.04x slower                                                        |
| gc_traversal              | 4.69 ms                                                          | 4.89 ms: 1.04x slower                                                       |
| mdp                       | 2.46 sec                                                         | 2.57 sec: 1.05x slower                                                      |
| python_startup            | 13.2 ms                                                          | 13.8 ms: 1.05x slower                                                       |
| 2to3                      | 291 ms                                                           | 305 ms: 1.05x slower                                                        |
| pycparser                 | 1.22 sec                                                         | 1.28 sec: 1.05x slower                                                      |
| async_generators          | 363 ms                                                           | 380 ms: 1.05x slower                                                        |
| docutils                  | 2.98 sec                                                         | 3.13 sec: 1.05x slower                                                      |
| hexiom                    | 6.35 ms                                                          | 6.70 ms: 1.06x slower                                                       |
| comprehensions            | 17.0 us                                                          | 17.9 us: 1.06x slower                                                       |
| bench_thread_pool         | 908 us                                                           | 961 us: 1.06x slower                                                        |
| flaskblogging             | 4.68 ms                                                          | 4.96 ms: 1.06x slower                                                       |
| sqlglot_optimize          | 59.5 ms                                                          | 63.1 ms: 1.06x slower                                                       |
| django_template           | 39.0 ms                                                          | 41.4 ms: 1.06x slower                                                       |
| sqlglot_normalize         | 120 ms                                                           | 128 ms: 1.06x slower                                                        |
| sympy_expand              | 501 ms                                                           | 533 ms: 1.06x slower                                                        |
| sympy_str                 | 295 ms                                                           | 314 ms: 1.07x slower                                                        |
| sympy_sum                 | 155 ms                                                           | 166 ms: 1.07x slower                                                        |
| python_startup_no_site    | 8.85 ms                                                          | 9.48 ms: 1.07x slower                                                       |
| chaos                     | 59.6 ms                                                          | 64.4 ms: 1.08x slower                                                       |
| regex_effbot              | 3.40 ms                                                          | 3.67 ms: 1.08x slower                                                       |
| typing_runtime_protocols  | 171 us                                                           | 185 us: 1.09x slower                                                        |
| raytrace                  | 260 ms                                                           | 284 ms: 1.09x slower                                                        |
| scimark_sor               | 119 ms                                                           | 130 ms: 1.10x slower                                                        |
| deltablue                 | 3.37 ms                                                          | 3.73 ms: 1.10x slower                                                       |
| deepcopy_reduce           | 3.39 us                                                          | 3.74 us: 1.10x slower                                                       |
| logging_silent            | 96.3 ns                                                          | 107 ns: 1.11x slower                                                        |
| nqueens                   | 88.4 ms                                                          | 98.4 ms: 1.11x slower                                                       |
| sympy_integrate           | 23.2 ms                                                          | 25.8 ms: 1.11x slower                                                       |
| genshi_xml                | 58.1 ms                                                          | 64.8 ms: 1.12x slower                                                       |
| pylint                    | 339 ms                                                           | 380 ms: 1.12x slower                                                        |
| genshi_text               | 25.9 ms                                                          | 29.1 ms: 1.12x slower                                                       |
| deepcopy                  | 377 us                                                           | 427 us: 1.13x slower                                                        |
| scimark_lu                | 97.5 ms                                                          | 119 ms: 1.22x slower                                                        |
| Geometric mean            | (ref)                                                            | 1.02x slower                                                                |

Benchmark hidden because not significant (10): bench_mp_pool, create_gc_cycles, asyncio_tcp, pprint_pformat, pickle_list, asyncio_tcp_ssl, async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_none_tg
Ignored benchmarks (4) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, bpe_tokeniser, gunicorn, mypy2

# HPT report

- Reliability score: 98.13% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.09x