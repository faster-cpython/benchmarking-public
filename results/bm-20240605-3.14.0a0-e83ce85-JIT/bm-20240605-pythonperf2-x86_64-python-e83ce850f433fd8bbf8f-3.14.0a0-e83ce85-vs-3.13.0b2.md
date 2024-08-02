# Results vs. 3.13.0b2

- fork: python
- ref: e83ce850f433fd8bbf8f
- machine: linux-x86_64
- commit hash: e83ce85
- commit date: 2024-06-05
- overall geometric mean: 1.01x slower
- HPT reliability: 97.56%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240605-pythonperf2-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 305 ms: 1.05x slower                                                        |
| docutils       | 2.98 sec                                                         | 3.11 sec: 1.04x slower                                                      |
| html5lib       | 74.7 ms                                                          | 73.0 ms: 1.02x faster                                                       |
| tornado_http   | 119 ms                                                           | 123 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                            | 1.02x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240605-pythonperf2-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|---------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg          | 900 ms                                                           | 918 ms: 1.02x slower                                                        |
| async_tree_none_tg        | 340 ms                                                           | 352 ms: 1.03x slower                                                        |
| async_tree_none           | 365 ms                                                           | 380 ms: 1.04x slower                                                        |
| async_tree_cpu_io_mixed   | 604 ms                                                           | 629 ms: 1.04x slower                                                        |
| async_tree_memoization_tg | 421 ms                                                           | 439 ms: 1.04x slower                                                        |
| async_tree_memoization    | 460 ms                                                           | 482 ms: 1.05x slower                                                        |
| Geometric mean            | (ref)                                                            | 1.03x slower                                                                |

Benchmark hidden because not significant (2): async_tree_io, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240605-pythonperf2-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 80.2 ms                                                          | 73.2 ms: 1.09x faster                                                       |
| nbody          | 87.8 ms                                                          | 81.1 ms: 1.08x faster                                                       |
| pidigits       | 254 ms                                                           | 251 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                            | 1.06x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240605-pythonperf2-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                           | 137 ms: 1.05x faster                                                        |
| regex_dna      | 249 ms                                                           | 240 ms: 1.04x faster                                                        |
| regex_v8       | 26.0 ms                                                          | 25.9 ms: 1.00x faster                                                       |
| regex_effbot   | 3.40 ms                                                          | 3.54 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                            | 1.01x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240605-pythonperf2-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|----------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.40 sec                                                         | 2.11 sec: 1.14x faster                                                      |
| xml_etree_generate   | 85.7 ms                                                          | 81.1 ms: 1.06x faster                                                       |
| unpickle_pure_python | 224 us                                                           | 216 us: 1.04x faster                                                        |
| xml_etree_process    | 59.7 ms                                                          | 58.1 ms: 1.03x faster                                                       |
| xml_etree_iterparse  | 103 ms                                                           | 99.8 ms: 1.03x faster                                                       |
| unpickle             | 15.7 us                                                          | 15.5 us: 1.01x faster                                                       |
| json_dumps           | 10.8 ms                                                          | 10.7 ms: 1.00x faster                                                       |
| xml_etree_parse      | 144 ms                                                           | 144 ms: 1.00x slower                                                        |
| pickle_dict          | 32.8 us                                                          | 33.3 us: 1.01x slower                                                       |
| pickle               | 10.6 us                                                          | 10.8 us: 1.02x slower                                                       |
| pickle_list          | 4.44 us                                                          | 4.59 us: 1.03x slower                                                       |
| pickle_pure_python   | 307 us                                                           | 318 us: 1.03x slower                                                        |
| unpickle_list        | 4.70 us                                                          | 4.96 us: 1.06x slower                                                       |
| Geometric mean       | (ref)                                                            | 1.01x faster                                                                |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240605-pythonperf2-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 13.8 ms: 1.05x slower                                                       |
| python_startup_no_site | 8.85 ms                                                          | 9.46 ms: 1.07x slower                                                       |
| Geometric mean         | (ref)                                                            | 1.06x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240605-pythonperf2-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|-----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 10.4 ms                                                          | 9.19 ms: 1.13x faster                                                       |
| django_template | 39.0 ms                                                          | 41.8 ms: 1.07x slower                                                       |
| genshi_text     | 25.9 ms                                                          | 29.5 ms: 1.14x slower                                                       |
| genshi_xml      | 58.1 ms                                                          | 66.8 ms: 1.15x slower                                                       |
| Geometric mean  | (ref)                                                            | 1.06x slower                                                                |

All benchmarks:
===============

| Benchmark                 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240605-pythonperf2-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|---------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| richards                  | 53.4 ms                                                          | 44.2 ms: 1.21x faster                                                       |
| richards_super            | 61.2 ms                                                          | 51.8 ms: 1.18x faster                                                       |
| tomli_loads               | 2.40 sec                                                         | 2.11 sec: 1.14x faster                                                      |
| mako                      | 10.4 ms                                                          | 9.19 ms: 1.13x faster                                                       |
| spectral_norm             | 97.3 ms                                                          | 86.5 ms: 1.12x faster                                                       |
| scimark_fft               | 312 ms                                                           | 284 ms: 1.10x faster                                                        |
| float                     | 80.2 ms                                                          | 73.2 ms: 1.09x faster                                                       |
| scimark_sparse_mat_mult   | 4.28 ms                                                          | 3.95 ms: 1.08x faster                                                       |
| nbody                     | 87.8 ms                                                          | 81.1 ms: 1.08x faster                                                       |
| gc_traversal              | 4.69 ms                                                          | 4.38 ms: 1.07x faster                                                       |
| pathlib                   | 17.1 ms                                                          | 16.0 ms: 1.07x faster                                                       |
| coverage                  | 83.5 ms                                                          | 78.8 ms: 1.06x faster                                                       |
| xml_etree_generate        | 85.7 ms                                                          | 81.1 ms: 1.06x faster                                                       |
| crypto_pyaes              | 73.6 ms                                                          | 69.9 ms: 1.05x faster                                                       |
| regex_compile             | 144 ms                                                           | 137 ms: 1.05x faster                                                        |
| unpickle_pure_python      | 224 us                                                           | 216 us: 1.04x faster                                                        |
| regex_dna                 | 249 ms                                                           | 240 ms: 1.04x faster                                                        |
| dulwich_log               | 67.3 ms                                                          | 65.3 ms: 1.03x faster                                                       |
| xml_etree_process         | 59.7 ms                                                          | 58.1 ms: 1.03x faster                                                       |
| go                        | 165 ms                                                           | 161 ms: 1.03x faster                                                        |
| pyflate                   | 482 ms                                                           | 469 ms: 1.03x faster                                                        |
| xml_etree_iterparse       | 103 ms                                                           | 99.8 ms: 1.03x faster                                                       |
| fannkuch                  | 353 ms                                                           | 344 ms: 1.03x faster                                                        |
| coroutines                | 22.0 ms                                                          | 21.5 ms: 1.02x faster                                                       |
| html5lib                  | 74.7 ms                                                          | 73.0 ms: 1.02x faster                                                       |
| pprint_safe_repr          | 818 ms                                                           | 799 ms: 1.02x faster                                                        |
| create_gc_cycles          | 2.00 ms                                                          | 1.96 ms: 1.02x faster                                                       |
| asyncio_websockets        | 395 ms                                                           | 388 ms: 1.02x faster                                                        |
| telco                     | 8.40 ms                                                          | 8.27 ms: 1.02x faster                                                       |
| unpickle                  | 15.7 us                                                          | 15.5 us: 1.01x faster                                                       |
| pidigits                  | 254 ms                                                           | 251 ms: 1.01x faster                                                        |
| pprint_pformat            | 1.66 sec                                                         | 1.65 sec: 1.01x faster                                                      |
| json                      | 5.35 ms                                                          | 5.32 ms: 1.01x faster                                                       |
| json_dumps                | 10.8 ms                                                          | 10.7 ms: 1.00x faster                                                       |
| regex_v8                  | 26.0 ms                                                          | 25.9 ms: 1.00x faster                                                       |
| scimark_monte_carlo       | 65.5 ms                                                          | 65.7 ms: 1.00x slower                                                       |
| xml_etree_parse           | 144 ms                                                           | 144 ms: 1.00x slower                                                        |
| deepcopy_memo             | 37.3 us                                                          | 37.5 us: 1.00x slower                                                       |
| logging_format            | 7.11 us                                                          | 7.16 us: 1.01x slower                                                       |
| meteor_contest            | 128 ms                                                           | 129 ms: 1.01x slower                                                        |
| asyncio_tcp               | 378 ms                                                           | 382 ms: 1.01x slower                                                        |
| pickle_dict               | 32.8 us                                                          | 33.3 us: 1.01x slower                                                       |
| pickle                    | 10.6 us                                                          | 10.8 us: 1.02x slower                                                       |
| async_tree_io_tg          | 900 ms                                                           | 918 ms: 1.02x slower                                                        |
| generators                | 33.5 ms                                                          | 34.3 ms: 1.02x slower                                                       |
| sqlglot_parse             | 1.39 ms                                                          | 1.42 ms: 1.02x slower                                                       |
| logging_simple            | 6.40 us                                                          | 6.58 us: 1.03x slower                                                       |
| pickle_list               | 4.44 us                                                          | 4.59 us: 1.03x slower                                                       |
| tornado_http              | 119 ms                                                           | 123 ms: 1.03x slower                                                        |
| async_tree_none_tg        | 340 ms                                                           | 352 ms: 1.03x slower                                                        |
| pickle_pure_python        | 307 us                                                           | 318 us: 1.03x slower                                                        |
| mdp                       | 2.46 sec                                                         | 2.55 sec: 1.04x slower                                                      |
| dask                      | 391 ms                                                           | 405 ms: 1.04x slower                                                        |
| thrift                    | 880 us                                                           | 914 us: 1.04x slower                                                        |
| sqlglot_transpile         | 1.76 ms                                                          | 1.83 ms: 1.04x slower                                                       |
| regex_effbot              | 3.40 ms                                                          | 3.54 ms: 1.04x slower                                                       |
| async_tree_none           | 365 ms                                                           | 380 ms: 1.04x slower                                                        |
| async_tree_cpu_io_mixed   | 604 ms                                                           | 629 ms: 1.04x slower                                                        |
| docutils                  | 2.98 sec                                                         | 3.11 sec: 1.04x slower                                                      |
| async_tree_memoization_tg | 421 ms                                                           | 439 ms: 1.04x slower                                                        |
| 2to3                      | 291 ms                                                           | 305 ms: 1.05x slower                                                        |
| python_startup            | 13.2 ms                                                          | 13.8 ms: 1.05x slower                                                       |
| bench_thread_pool         | 908 us                                                           | 951 us: 1.05x slower                                                        |
| pycparser                 | 1.22 sec                                                         | 1.28 sec: 1.05x slower                                                      |
| async_tree_memoization    | 460 ms                                                           | 482 ms: 1.05x slower                                                        |
| sqlglot_normalize         | 120 ms                                                           | 127 ms: 1.06x slower                                                        |
| unpickle_list             | 4.70 us                                                          | 4.96 us: 1.06x slower                                                       |
| sympy_str                 | 295 ms                                                           | 312 ms: 1.06x slower                                                        |
| sympy_expand              | 501 ms                                                           | 531 ms: 1.06x slower                                                        |
| hexiom                    | 6.35 ms                                                          | 6.76 ms: 1.06x slower                                                       |
| sqlglot_optimize          | 59.5 ms                                                          | 63.3 ms: 1.06x slower                                                       |
| deepcopy_reduce           | 3.39 us                                                          | 3.62 us: 1.07x slower                                                       |
| python_startup_no_site    | 8.85 ms                                                          | 9.46 ms: 1.07x slower                                                       |
| sympy_sum                 | 155 ms                                                           | 166 ms: 1.07x slower                                                        |
| comprehensions            | 17.0 us                                                          | 18.2 us: 1.07x slower                                                       |
| django_template           | 39.0 ms                                                          | 41.8 ms: 1.07x slower                                                       |
| typing_runtime_protocols  | 171 us                                                           | 184 us: 1.08x slower                                                        |
| deepcopy                  | 377 us                                                           | 411 us: 1.09x slower                                                        |
| scimark_sor               | 119 ms                                                           | 130 ms: 1.09x slower                                                        |
| async_generators          | 363 ms                                                           | 399 ms: 1.10x slower                                                        |
| sympy_integrate           | 23.2 ms                                                          | 25.6 ms: 1.10x slower                                                       |
| deltablue                 | 3.37 ms                                                          | 3.75 ms: 1.11x slower                                                       |
| logging_silent            | 96.3 ns                                                          | 107 ns: 1.11x slower                                                        |
| pylint                    | 339 ms                                                           | 380 ms: 1.12x slower                                                        |
| chaos                     | 59.6 ms                                                          | 66.8 ms: 1.12x slower                                                       |
| raytrace                  | 260 ms                                                           | 292 ms: 1.12x slower                                                        |
| nqueens                   | 88.4 ms                                                          | 99.7 ms: 1.13x slower                                                       |
| genshi_text               | 25.9 ms                                                          | 29.5 ms: 1.14x slower                                                       |
| genshi_xml                | 58.1 ms                                                          | 66.8 ms: 1.15x slower                                                       |
| scimark_lu                | 97.5 ms                                                          | 113 ms: 1.16x slower                                                        |
| Geometric mean            | (ref)                                                            | 1.01x slower                                                                |

Benchmark hidden because not significant (6): sqlite_synth, asyncio_tcp_ssl, json_loads, bench_mp_pool, async_tree_io, async_tree_cpu_io_mixed_tg
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, bpe_tokeniser, chameleon, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 97.56% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.09x