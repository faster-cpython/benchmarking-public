# Results vs. 3.13.0b2

- fork: python
- ref: 6725c78d376eadb01a9d
- machine: linux-x86_64
- commit hash: 6725c78
- commit date: 2024-06-04
- overall geometric mean: 1.01x slower
- HPT reliability: 97.95%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 305 ms: 1.05x slower                                                         |
| chameleon      | 7.40 ms                                                          | 7.60 ms: 1.03x slower                                                        |
| docutils       | 2.98 sec                                                         | 3.11 sec: 1.04x slower                                                       |
| html5lib       | 74.7 ms                                                          | 73.7 ms: 1.01x faster                                                        |
| tornado_http   | 119 ms                                                           | 123 ms: 1.03x slower                                                         |
| Geometric mean | (ref)                                                            | 1.03x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|---------------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg          | 900 ms                                                           | 844 ms: 1.07x faster                                                         |
| async_tree_none_tg        | 340 ms                                                           | 351 ms: 1.03x slower                                                         |
| async_tree_io             | 873 ms                                                           | 907 ms: 1.04x slower                                                         |
| async_tree_none           | 365 ms                                                           | 379 ms: 1.04x slower                                                         |
| async_tree_memoization_tg | 421 ms                                                           | 438 ms: 1.04x slower                                                         |
| async_tree_cpu_io_mixed   | 604 ms                                                           | 633 ms: 1.05x slower                                                         |
| Geometric mean            | (ref)                                                            | 1.02x slower                                                                 |

Benchmark hidden because not significant (2): async_tree_memoization, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 87.8 ms                                                          | 81.9 ms: 1.07x faster                                                        |
| float          | 80.2 ms                                                          | 76.2 ms: 1.05x faster                                                        |
| pidigits       | 254 ms                                                           | 250 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                            | 1.05x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_v8       | 26.0 ms                                                          | 24.9 ms: 1.05x faster                                                        |
| regex_compile  | 144 ms                                                           | 138 ms: 1.04x faster                                                         |
| regex_dna      | 249 ms                                                           | 243 ms: 1.03x faster                                                         |
| regex_effbot   | 3.40 ms                                                          | 3.70 ms: 1.09x slower                                                        |
| Geometric mean | (ref)                                                            | 1.01x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.40 sec                                                         | 2.09 sec: 1.15x faster                                                       |
| xml_etree_generate   | 85.7 ms                                                          | 81.4 ms: 1.05x faster                                                        |
| unpickle_pure_python | 224 us                                                           | 217 us: 1.04x faster                                                         |
| pickle_dict          | 32.8 us                                                          | 31.8 us: 1.03x faster                                                        |
| xml_etree_iterparse  | 103 ms                                                           | 100.0 ms: 1.03x faster                                                       |
| xml_etree_process    | 59.7 ms                                                          | 58.5 ms: 1.02x faster                                                        |
| json_dumps           | 10.8 ms                                                          | 10.6 ms: 1.02x faster                                                        |
| json_loads           | 25.0 us                                                          | 24.7 us: 1.01x faster                                                        |
| pickle               | 10.6 us                                                          | 10.5 us: 1.01x faster                                                        |
| xml_etree_parse      | 144 ms                                                           | 145 ms: 1.01x slower                                                         |
| pickle_pure_python   | 307 us                                                           | 314 us: 1.02x slower                                                         |
| unpickle_list        | 4.70 us                                                          | 4.81 us: 1.02x slower                                                        |
| pickle_list          | 4.44 us                                                          | 4.56 us: 1.03x slower                                                        |
| Geometric mean       | (ref)                                                            | 1.02x faster                                                                 |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|------------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 13.8 ms: 1.05x slower                                                        |
| python_startup_no_site | 8.85 ms                                                          | 9.44 ms: 1.07x slower                                                        |
| Geometric mean         | (ref)                                                            | 1.06x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|-----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 10.4 ms                                                          | 9.02 ms: 1.15x faster                                                        |
| django_template | 39.0 ms                                                          | 41.3 ms: 1.06x slower                                                        |
| genshi_text     | 25.9 ms                                                          | 27.6 ms: 1.07x slower                                                        |
| genshi_xml      | 58.1 ms                                                          | 64.8 ms: 1.12x slower                                                        |
| Geometric mean  | (ref)                                                            | 1.02x slower                                                                 |

All benchmarks:
===============

| Benchmark                 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|---------------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| spectral_norm             | 97.3 ms                                                          | 82.1 ms: 1.19x faster                                                        |
| richards                  | 53.4 ms                                                          | 45.7 ms: 1.17x faster                                                        |
| richards_super            | 61.2 ms                                                          | 52.6 ms: 1.16x faster                                                        |
| tomli_loads               | 2.40 sec                                                         | 2.09 sec: 1.15x faster                                                       |
| mako                      | 10.4 ms                                                          | 9.02 ms: 1.15x faster                                                        |
| scimark_fft               | 312 ms                                                           | 287 ms: 1.09x faster                                                         |
| nbody                     | 87.8 ms                                                          | 81.9 ms: 1.07x faster                                                        |
| scimark_sparse_mat_mult   | 4.28 ms                                                          | 4.01 ms: 1.07x faster                                                        |
| async_tree_io_tg          | 900 ms                                                           | 844 ms: 1.07x faster                                                         |
| xml_etree_generate        | 85.7 ms                                                          | 81.4 ms: 1.05x faster                                                        |
| crypto_pyaes              | 73.6 ms                                                          | 69.9 ms: 1.05x faster                                                        |
| float                     | 80.2 ms                                                          | 76.2 ms: 1.05x faster                                                        |
| fannkuch                  | 353 ms                                                           | 335 ms: 1.05x faster                                                         |
| regex_v8                  | 26.0 ms                                                          | 24.9 ms: 1.05x faster                                                        |
| regex_compile             | 144 ms                                                           | 138 ms: 1.04x faster                                                         |
| pprint_pformat            | 1.66 sec                                                         | 1.59 sec: 1.04x faster                                                       |
| pprint_safe_repr          | 818 ms                                                           | 784 ms: 1.04x faster                                                         |
| unpickle_pure_python      | 224 us                                                           | 217 us: 1.04x faster                                                         |
| pickle_dict               | 32.8 us                                                          | 31.8 us: 1.03x faster                                                        |
| create_gc_cycles          | 2.00 ms                                                          | 1.95 ms: 1.03x faster                                                        |
| pyflate                   | 482 ms                                                           | 468 ms: 1.03x faster                                                         |
| coverage                  | 83.5 ms                                                          | 81.2 ms: 1.03x faster                                                        |
| xml_etree_iterparse       | 103 ms                                                           | 100.0 ms: 1.03x faster                                                       |
| regex_dna                 | 249 ms                                                           | 243 ms: 1.03x faster                                                         |
| telco                     | 8.40 ms                                                          | 8.22 ms: 1.02x faster                                                        |
| xml_etree_process         | 59.7 ms                                                          | 58.5 ms: 1.02x faster                                                        |
| deepcopy_memo             | 37.3 us                                                          | 36.5 us: 1.02x faster                                                        |
| asyncio_websockets        | 395 ms                                                           | 387 ms: 1.02x faster                                                         |
| sqlite_synth              | 2.80 us                                                          | 2.74 us: 1.02x faster                                                        |
| json_dumps                | 10.8 ms                                                          | 10.6 ms: 1.02x faster                                                        |
| html5lib                  | 74.7 ms                                                          | 73.7 ms: 1.01x faster                                                        |
| pidigits                  | 254 ms                                                           | 250 ms: 1.01x faster                                                         |
| json_loads                | 25.0 us                                                          | 24.7 us: 1.01x faster                                                        |
| logging_format            | 7.11 us                                                          | 7.06 us: 1.01x faster                                                        |
| pickle                    | 10.6 us                                                          | 10.5 us: 1.01x faster                                                        |
| dulwich_log               | 67.3 ms                                                          | 66.9 ms: 1.01x faster                                                        |
| go                        | 165 ms                                                           | 166 ms: 1.01x slower                                                         |
| sqlglot_parse             | 1.39 ms                                                          | 1.40 ms: 1.01x slower                                                        |
| xml_etree_parse           | 144 ms                                                           | 145 ms: 1.01x slower                                                         |
| coroutines                | 22.0 ms                                                          | 22.2 ms: 1.01x slower                                                        |
| meteor_contest            | 128 ms                                                           | 130 ms: 1.02x slower                                                         |
| pycparser                 | 1.22 sec                                                         | 1.24 sec: 1.02x slower                                                       |
| logging_simple            | 6.40 us                                                          | 6.52 us: 1.02x slower                                                        |
| scimark_monte_carlo       | 65.5 ms                                                          | 66.7 ms: 1.02x slower                                                        |
| generators                | 33.5 ms                                                          | 34.2 ms: 1.02x slower                                                        |
| pickle_pure_python        | 307 us                                                           | 314 us: 1.02x slower                                                         |
| pathlib                   | 17.1 ms                                                          | 17.5 ms: 1.02x slower                                                        |
| unpickle_list             | 4.70 us                                                          | 4.81 us: 1.02x slower                                                        |
| thrift                    | 880 us                                                           | 902 us: 1.03x slower                                                         |
| pickle_list               | 4.44 us                                                          | 4.56 us: 1.03x slower                                                        |
| chameleon                 | 7.40 ms                                                          | 7.60 ms: 1.03x slower                                                        |
| sqlglot_transpile         | 1.76 ms                                                          | 1.81 ms: 1.03x slower                                                        |
| async_tree_none_tg        | 340 ms                                                           | 351 ms: 1.03x slower                                                         |
| tornado_http              | 119 ms                                                           | 123 ms: 1.03x slower                                                         |
| dask                      | 391 ms                                                           | 405 ms: 1.04x slower                                                         |
| mdp                       | 2.46 sec                                                         | 2.55 sec: 1.04x slower                                                       |
| async_tree_io             | 873 ms                                                           | 907 ms: 1.04x slower                                                         |
| async_tree_none           | 365 ms                                                           | 379 ms: 1.04x slower                                                         |
| async_tree_memoization_tg | 421 ms                                                           | 438 ms: 1.04x slower                                                         |
| docutils                  | 2.98 sec                                                         | 3.11 sec: 1.04x slower                                                       |
| bench_thread_pool         | 908 us                                                           | 948 us: 1.04x slower                                                         |
| logging_silent            | 96.3 ns                                                          | 101 ns: 1.04x slower                                                         |
| 2to3                      | 291 ms                                                           | 305 ms: 1.05x slower                                                         |
| python_startup            | 13.2 ms                                                          | 13.8 ms: 1.05x slower                                                        |
| sympy_str                 | 295 ms                                                           | 309 ms: 1.05x slower                                                         |
| async_tree_cpu_io_mixed   | 604 ms                                                           | 633 ms: 1.05x slower                                                         |
| gc_traversal              | 4.69 ms                                                          | 4.91 ms: 1.05x slower                                                        |
| sympy_expand              | 501 ms                                                           | 525 ms: 1.05x slower                                                         |
| flaskblogging             | 4.68 ms                                                          | 4.91 ms: 1.05x slower                                                        |
| hexiom                    | 6.35 ms                                                          | 6.70 ms: 1.06x slower                                                        |
| sqlglot_optimize          | 59.5 ms                                                          | 62.9 ms: 1.06x slower                                                        |
| typing_runtime_protocols  | 171 us                                                           | 180 us: 1.06x slower                                                         |
| async_generators          | 363 ms                                                           | 384 ms: 1.06x slower                                                         |
| django_template           | 39.0 ms                                                          | 41.3 ms: 1.06x slower                                                        |
| sympy_sum                 | 155 ms                                                           | 164 ms: 1.06x slower                                                         |
| comprehensions            | 17.0 us                                                          | 18.0 us: 1.06x slower                                                        |
| python_startup_no_site    | 8.85 ms                                                          | 9.44 ms: 1.07x slower                                                        |
| genshi_text               | 25.9 ms                                                          | 27.6 ms: 1.07x slower                                                        |
| deepcopy_reduce           | 3.39 us                                                          | 3.62 us: 1.07x slower                                                        |
| sqlglot_normalize         | 120 ms                                                           | 129 ms: 1.07x slower                                                         |
| deepcopy                  | 377 us                                                           | 405 us: 1.07x slower                                                         |
| chaos                     | 59.6 ms                                                          | 64.7 ms: 1.09x slower                                                        |
| gunicorn                  | 1.04 ms                                                          | 1.13 ms: 1.09x slower                                                        |
| aiohttp                   | 1.07 ms                                                          | 1.17 ms: 1.09x slower                                                        |
| regex_effbot              | 3.40 ms                                                          | 3.70 ms: 1.09x slower                                                        |
| sympy_integrate           | 23.2 ms                                                          | 25.4 ms: 1.10x slower                                                        |
| nqueens                   | 88.4 ms                                                          | 96.9 ms: 1.10x slower                                                        |
| raytrace                  | 260 ms                                                           | 287 ms: 1.10x slower                                                         |
| mypy2                     | 764 ms                                                           | 846 ms: 1.11x slower                                                         |
| pylint                    | 339 ms                                                           | 376 ms: 1.11x slower                                                         |
| genshi_xml                | 58.1 ms                                                          | 64.8 ms: 1.12x slower                                                        |
| deltablue                 | 3.37 ms                                                          | 3.84 ms: 1.14x slower                                                        |
| scimark_lu                | 97.5 ms                                                          | 113 ms: 1.16x slower                                                         |
| scimark_sor               | 119 ms                                                           | 144 ms: 1.22x slower                                                         |
| Geometric mean            | (ref)                                                            | 1.01x slower                                                                 |

Benchmark hidden because not significant (7): bench_mp_pool, async_tree_memoization, unpickle, json, asyncio_tcp_ssl, asyncio_tcp, async_tree_cpu_io_mixed_tg
Ignored benchmarks (1) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: bpe_tokeniser

# HPT report

- Reliability score: 97.95% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.09x