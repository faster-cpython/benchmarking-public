# Results vs. 3.13.0b2

- fork: mdboom
- ref: pysequence_tuple
- machine: linux-x86_64
- commit hash: 3b5fdc8
- commit date: 2024-09-11
- overall geometric mean: 1.02x faster
- HPT reliability: 99.94%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-pythonperf2-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:----------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 287 ms: 1.02x faster                                                    |
| docutils       | 2.98 sec                                                         | 2.91 sec: 1.03x faster                                                  |
| html5lib       | 74.7 ms                                                          | 72.9 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                            | 1.02x faster                                                            |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-pythonperf2-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|---------------------------|:----------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io_tg          | 900 ms                                                           | 784 ms: 1.15x faster                                                    |
| async_tree_memoization    | 460 ms                                                           | 403 ms: 1.14x faster                                                    |
| async_tree_none           | 365 ms                                                           | 326 ms: 1.12x faster                                                    |
| async_tree_none_tg        | 340 ms                                                           | 312 ms: 1.09x faster                                                    |
| async_tree_io             | 873 ms                                                           | 807 ms: 1.08x faster                                                    |
| async_tree_memoization_tg | 421 ms                                                           | 392 ms: 1.07x faster                                                    |
| async_tree_cpu_io_mixed   | 604 ms                                                           | 580 ms: 1.04x faster                                                    |
| Geometric mean            | (ref)                                                            | 1.09x faster                                                            |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-pythonperf2-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:----------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 87.8 ms                                                          | 85.3 ms: 1.03x faster                                                   |
| pidigits       | 254 ms                                                           | 254 ms: 1.00x slower                                                    |
| Geometric mean | (ref)                                                            | 1.01x faster                                                            |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-pythonperf2-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:----------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 249 ms                                                           | 240 ms: 1.04x faster                                                    |
| regex_compile  | 144 ms                                                           | 140 ms: 1.03x faster                                                    |
| regex_v8       | 26.0 ms                                                          | 25.8 ms: 1.01x faster                                                   |
| regex_effbot   | 3.40 ms                                                          | 3.46 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                            | 1.01x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-pythonperf2-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------------|:----------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_dict          | 32.8 us                                                          | 29.8 us: 1.10x faster                                                   |
| pickle_list          | 4.44 us                                                          | 4.13 us: 1.08x faster                                                   |
| pickle               | 10.6 us                                                          | 10.2 us: 1.04x faster                                                   |
| unpickle             | 15.7 us                                                          | 15.5 us: 1.01x faster                                                   |
| xml_etree_iterparse  | 103 ms                                                           | 101 ms: 1.01x faster                                                    |
| xml_etree_process    | 59.7 ms                                                          | 59.2 ms: 1.01x faster                                                   |
| xml_etree_generate   | 85.7 ms                                                          | 85.3 ms: 1.01x faster                                                   |
| json_loads           | 25.0 us                                                          | 24.9 us: 1.00x faster                                                   |
| unpickle_pure_python | 224 us                                                           | 226 us: 1.00x slower                                                    |
| pickle_pure_python   | 307 us                                                           | 315 us: 1.02x slower                                                    |
| json_dumps           | 10.8 ms                                                          | 11.1 ms: 1.03x slower                                                   |
| tomli_loads          | 2.40 sec                                                         | 2.56 sec: 1.07x slower                                                  |
| Geometric mean       | (ref)                                                            | 1.01x faster                                                            |

Benchmark hidden because not significant (2): unpickle_list, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-pythonperf2-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|------------------------|:----------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                                   |
| python_startup_no_site | 8.85 ms                                                          | 8.95 ms: 1.01x slower                                                   |
| Geometric mean         | (ref)                                                            | 1.01x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-pythonperf2-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|-----------------|:----------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 58.1 ms                                                          | 54.2 ms: 1.07x faster                                                   |
| genshi_text     | 25.9 ms                                                          | 25.2 ms: 1.03x faster                                                   |
| django_template | 39.0 ms                                                          | 41.3 ms: 1.06x slower                                                   |
| Geometric mean  | (ref)                                                            | 1.01x faster                                                            |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-pythonperf2-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|---------------------------|:----------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy                  | 377 us                                                           | 287 us: 1.32x faster                                                    |
| deepcopy_memo             | 37.3 us                                                          | 29.7 us: 1.26x faster                                                   |
| go                        | 165 ms                                                           | 139 ms: 1.19x faster                                                    |
| deepcopy_reduce           | 3.39 us                                                          | 2.87 us: 1.18x faster                                                   |
| async_tree_io_tg          | 900 ms                                                           | 784 ms: 1.15x faster                                                    |
| async_tree_memoization    | 460 ms                                                           | 403 ms: 1.14x faster                                                    |
| generators                | 33.5 ms                                                          | 29.7 ms: 1.13x faster                                                   |
| async_tree_none           | 365 ms                                                           | 326 ms: 1.12x faster                                                    |
| pickle_dict               | 32.8 us                                                          | 29.8 us: 1.10x faster                                                   |
| pathlib                   | 17.1 ms                                                          | 15.6 ms: 1.09x faster                                                   |
| async_tree_none_tg        | 340 ms                                                           | 312 ms: 1.09x faster                                                    |
| async_tree_io             | 873 ms                                                           | 807 ms: 1.08x faster                                                    |
| coverage                  | 83.5 ms                                                          | 77.4 ms: 1.08x faster                                                   |
| pickle_list               | 4.44 us                                                          | 4.13 us: 1.08x faster                                                   |
| async_tree_memoization_tg | 421 ms                                                           | 392 ms: 1.07x faster                                                    |
| genshi_xml                | 58.1 ms                                                          | 54.2 ms: 1.07x faster                                                   |
| gc_traversal              | 4.69 ms                                                          | 4.42 ms: 1.06x faster                                                   |
| bench_thread_pool         | 908 us                                                           | 859 us: 1.06x faster                                                    |
| richards_super            | 61.2 ms                                                          | 57.9 ms: 1.06x faster                                                   |
| pickle                    | 10.6 us                                                          | 10.2 us: 1.04x faster                                                   |
| async_tree_cpu_io_mixed   | 604 ms                                                           | 580 ms: 1.04x faster                                                    |
| regex_dna                 | 249 ms                                                           | 240 ms: 1.04x faster                                                    |
| bpe_tokeniser             | 5.14 sec                                                         | 4.97 sec: 1.03x faster                                                  |
| regex_compile             | 144 ms                                                           | 140 ms: 1.03x faster                                                    |
| create_gc_cycles          | 2.00 ms                                                          | 1.95 ms: 1.03x faster                                                   |
| nbody                     | 87.8 ms                                                          | 85.3 ms: 1.03x faster                                                   |
| asyncio_tcp               | 378 ms                                                           | 367 ms: 1.03x faster                                                    |
| richards                  | 53.4 ms                                                          | 52.0 ms: 1.03x faster                                                   |
| genshi_text               | 25.9 ms                                                          | 25.2 ms: 1.03x faster                                                   |
| docutils                  | 2.98 sec                                                         | 2.91 sec: 1.03x faster                                                  |
| html5lib                  | 74.7 ms                                                          | 72.9 ms: 1.02x faster                                                   |
| scimark_fft               | 312 ms                                                           | 305 ms: 1.02x faster                                                    |
| sqlglot_normalize         | 120 ms                                                           | 118 ms: 1.02x faster                                                    |
| sqlglot_optimize          | 59.5 ms                                                          | 58.5 ms: 1.02x faster                                                   |
| json                      | 5.35 ms                                                          | 5.26 ms: 1.02x faster                                                   |
| 2to3                      | 291 ms                                                           | 287 ms: 1.02x faster                                                    |
| thrift                    | 880 us                                                           | 868 us: 1.01x faster                                                    |
| crypto_pyaes              | 73.6 ms                                                          | 72.6 ms: 1.01x faster                                                   |
| unpickle                  | 15.7 us                                                          | 15.5 us: 1.01x faster                                                   |
| sqlite_synth              | 2.80 us                                                          | 2.76 us: 1.01x faster                                                   |
| xml_etree_iterparse       | 103 ms                                                           | 101 ms: 1.01x faster                                                    |
| hexiom                    | 6.35 ms                                                          | 6.29 ms: 1.01x faster                                                   |
| xml_etree_process         | 59.7 ms                                                          | 59.2 ms: 1.01x faster                                                   |
| meteor_contest            | 128 ms                                                           | 127 ms: 1.01x faster                                                    |
| sympy_sum                 | 155 ms                                                           | 153 ms: 1.01x faster                                                    |
| regex_v8                  | 26.0 ms                                                          | 25.8 ms: 1.01x faster                                                   |
| async_generators          | 363 ms                                                           | 360 ms: 1.01x faster                                                    |
| scimark_sparse_mat_mult   | 4.28 ms                                                          | 4.25 ms: 1.01x faster                                                   |
| sympy_str                 | 295 ms                                                           | 293 ms: 1.01x faster                                                    |
| xml_etree_generate        | 85.7 ms                                                          | 85.3 ms: 1.01x faster                                                   |
| scimark_sor               | 119 ms                                                           | 118 ms: 1.00x faster                                                    |
| json_loads                | 25.0 us                                                          | 24.9 us: 1.00x faster                                                   |
| spectral_norm             | 97.3 ms                                                          | 97.1 ms: 1.00x faster                                                   |
| asyncio_tcp_ssl           | 1.58 sec                                                         | 1.58 sec: 1.00x faster                                                  |
| pprint_pformat            | 1.66 sec                                                         | 1.67 sec: 1.00x slower                                                  |
| pidigits                  | 254 ms                                                           | 254 ms: 1.00x slower                                                    |
| pyflate                   | 482 ms                                                           | 484 ms: 1.00x slower                                                    |
| unpickle_pure_python      | 224 us                                                           | 226 us: 1.00x slower                                                    |
| sympy_expand              | 501 ms                                                           | 504 ms: 1.01x slower                                                    |
| scimark_lu                | 97.5 ms                                                          | 98.1 ms: 1.01x slower                                                   |
| typing_runtime_protocols  | 171 us                                                           | 172 us: 1.01x slower                                                    |
| logging_simple            | 6.40 us                                                          | 6.47 us: 1.01x slower                                                   |
| python_startup            | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                                   |
| python_startup_no_site    | 8.85 ms                                                          | 8.95 ms: 1.01x slower                                                   |
| coroutines                | 22.0 ms                                                          | 22.3 ms: 1.01x slower                                                   |
| mdp                       | 2.46 sec                                                         | 2.51 sec: 1.02x slower                                                  |
| regex_effbot              | 3.40 ms                                                          | 3.46 ms: 1.02x slower                                                   |
| pickle_pure_python        | 307 us                                                           | 315 us: 1.02x slower                                                    |
| nqueens                   | 88.4 ms                                                          | 90.5 ms: 1.02x slower                                                   |
| logging_silent            | 96.3 ns                                                          | 98.8 ns: 1.03x slower                                                   |
| comprehensions            | 17.0 us                                                          | 17.4 us: 1.03x slower                                                   |
| pycparser                 | 1.22 sec                                                         | 1.26 sec: 1.03x slower                                                  |
| json_dumps                | 10.8 ms                                                          | 11.1 ms: 1.03x slower                                                   |
| sqlglot_transpile         | 1.76 ms                                                          | 1.84 ms: 1.04x slower                                                   |
| deltablue                 | 3.37 ms                                                          | 3.51 ms: 1.04x slower                                                   |
| scimark_monte_carlo       | 65.5 ms                                                          | 68.3 ms: 1.04x slower                                                   |
| sqlglot_parse             | 1.39 ms                                                          | 1.46 ms: 1.05x slower                                                   |
| django_template           | 39.0 ms                                                          | 41.3 ms: 1.06x slower                                                   |
| chaos                     | 59.6 ms                                                          | 63.2 ms: 1.06x slower                                                   |
| tomli_loads               | 2.40 sec                                                         | 2.56 sec: 1.07x slower                                                  |
| raytrace                  | 260 ms                                                           | 278 ms: 1.07x slower                                                    |
| fannkuch                  | 353 ms                                                           | 380 ms: 1.08x slower                                                    |
| Geometric mean            | (ref)                                                            | 1.02x faster                                                            |

Benchmark hidden because not significant (14): bench_mp_pool, tornado_http, unpickle_list, asyncio_websockets, telco, async_tree_cpu_io_mixed_tg, pprint_safe_repr, dulwich_log, xml_etree_parse, mako, sympy_integrate, logging_format, float, pylint
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240911-3.14.0a0-3b5fdc8/bm-20240911-pythonperf2-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8.json: unpack_sequence

# HPT report

- Reliability score: 99.94% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x