# Results vs. 3.13.0b2

- fork: python
- ref: c8db0e817e7e0db50153
- machine: linux-x86_64
- commit hash: c8db0e8
- commit date: 2024-10-03
- overall geometric mean: 1.03x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241003-pythonperf2-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 282 ms: 1.03x faster                                                        |
| docutils       | 2.98 sec                                                         | 2.88 sec: 1.03x faster                                                      |
| html5lib       | 74.7 ms                                                          | 70.4 ms: 1.06x faster                                                       |
| tornado_http   | 119 ms                                                           | 116 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                            | 1.04x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241003-pythonperf2-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 900 ms                                                           | 786 ms: 1.14x faster                                                        |
| async_tree_none            | 365 ms                                                           | 320 ms: 1.14x faster                                                        |
| async_tree_memoization     | 460 ms                                                           | 403 ms: 1.14x faster                                                        |
| async_tree_none_tg         | 340 ms                                                           | 308 ms: 1.10x faster                                                        |
| async_tree_memoization_tg  | 421 ms                                                           | 389 ms: 1.08x faster                                                        |
| async_tree_io              | 873 ms                                                           | 819 ms: 1.07x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 574 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 561 ms: 1.02x faster                                                        |
| Geometric mean             | (ref)                                                            | 1.09x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241003-pythonperf2-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 80.2 ms                                                          | 78.0 ms: 1.03x faster                                                       |
| pidigits       | 254 ms                                                           | 253 ms: 1.00x faster                                                        |
| nbody          | 87.8 ms                                                          | 90.6 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                            | 1.00x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241003-pythonperf2-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                           | 140 ms: 1.03x faster                                                        |
| regex_dna      | 249 ms                                                           | 248 ms: 1.00x faster                                                        |
| regex_v8       | 26.0 ms                                                          | 26.2 ms: 1.01x slower                                                       |
| regex_effbot   | 3.40 ms                                                          | 3.48 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                            | 1.00x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241003-pythonperf2-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_dict          | 32.8 us                                                          | 31.6 us: 1.04x faster                                                       |
| unpickle_pure_python | 224 us                                                           | 217 us: 1.03x faster                                                        |
| pickle               | 10.6 us                                                          | 10.4 us: 1.02x faster                                                       |
| unpickle             | 15.7 us                                                          | 15.4 us: 1.02x faster                                                       |
| xml_etree_generate   | 85.7 ms                                                          | 84.7 ms: 1.01x faster                                                       |
| xml_etree_process    | 59.7 ms                                                          | 59.2 ms: 1.01x faster                                                       |
| xml_etree_iterparse  | 103 ms                                                           | 102 ms: 1.01x faster                                                        |
| json_dumps           | 10.8 ms                                                          | 10.8 ms: 1.00x slower                                                       |
| unpickle_list        | 4.70 us                                                          | 4.74 us: 1.01x slower                                                       |
| pickle_pure_python   | 307 us                                                           | 312 us: 1.02x slower                                                        |
| pickle_list          | 4.44 us                                                          | 4.55 us: 1.02x slower                                                       |
| xml_etree_parse      | 144 ms                                                           | 150 ms: 1.05x slower                                                        |
| tomli_loads          | 2.40 sec                                                         | 2.56 sec: 1.07x slower                                                      |
| Geometric mean       | (ref)                                                            | 1.00x slower                                                                |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241003-pythonperf2-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.85 ms                                                          | 8.95 ms: 1.01x slower                                                       |
| python_startup         | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                            | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241003-pythonperf2-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|-----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 58.1 ms                                                          | 54.2 ms: 1.07x faster                                                       |
| genshi_text     | 25.9 ms                                                          | 24.7 ms: 1.05x faster                                                       |
| mako            | 10.4 ms                                                          | 10.3 ms: 1.01x faster                                                       |
| django_template | 39.0 ms                                                          | 40.6 ms: 1.04x slower                                                       |
| Geometric mean  | (ref)                                                            | 1.02x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241003-pythonperf2-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy                   | 377 us                                                           | 282 us: 1.34x faster                                                        |
| deepcopy_memo              | 37.3 us                                                          | 28.8 us: 1.29x faster                                                       |
| go                         | 165 ms                                                           | 132 ms: 1.25x faster                                                        |
| generators                 | 33.5 ms                                                          | 28.8 ms: 1.16x faster                                                       |
| deepcopy_reduce            | 3.39 us                                                          | 2.92 us: 1.16x faster                                                       |
| async_tree_io_tg           | 900 ms                                                           | 786 ms: 1.14x faster                                                        |
| async_tree_none            | 365 ms                                                           | 320 ms: 1.14x faster                                                        |
| async_tree_memoization     | 460 ms                                                           | 403 ms: 1.14x faster                                                        |
| async_tree_none_tg         | 340 ms                                                           | 308 ms: 1.10x faster                                                        |
| richards_super             | 61.2 ms                                                          | 56.4 ms: 1.08x faster                                                       |
| pathlib                    | 17.1 ms                                                          | 15.8 ms: 1.08x faster                                                       |
| async_tree_memoization_tg  | 421 ms                                                           | 389 ms: 1.08x faster                                                        |
| scimark_fft                | 312 ms                                                           | 290 ms: 1.08x faster                                                        |
| genshi_xml                 | 58.1 ms                                                          | 54.2 ms: 1.07x faster                                                       |
| async_tree_io              | 873 ms                                                           | 819 ms: 1.07x faster                                                        |
| richards                   | 53.4 ms                                                          | 50.2 ms: 1.06x faster                                                       |
| html5lib                   | 74.7 ms                                                          | 70.4 ms: 1.06x faster                                                       |
| logging_format             | 7.11 us                                                          | 6.74 us: 1.06x faster                                                       |
| gc_traversal               | 4.69 ms                                                          | 4.45 ms: 1.05x faster                                                       |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 574 ms: 1.05x faster                                                        |
| genshi_text                | 25.9 ms                                                          | 24.7 ms: 1.05x faster                                                       |
| logging_simple             | 6.40 us                                                          | 6.13 us: 1.05x faster                                                       |
| coroutines                 | 22.0 ms                                                          | 21.1 ms: 1.04x faster                                                       |
| scimark_lu                 | 97.5 ms                                                          | 93.7 ms: 1.04x faster                                                       |
| bpe_tokeniser              | 5.14 sec                                                         | 4.95 sec: 1.04x faster                                                      |
| pickle_dict                | 32.8 us                                                          | 31.6 us: 1.04x faster                                                       |
| 2to3                       | 291 ms                                                           | 282 ms: 1.03x faster                                                        |
| docutils                   | 2.98 sec                                                         | 2.88 sec: 1.03x faster                                                      |
| thrift                     | 880 us                                                           | 852 us: 1.03x faster                                                        |
| tornado_http               | 119 ms                                                           | 116 ms: 1.03x faster                                                        |
| unpickle_pure_python       | 224 us                                                           | 217 us: 1.03x faster                                                        |
| regex_compile              | 144 ms                                                           | 140 ms: 1.03x faster                                                        |
| sqlglot_normalize          | 120 ms                                                           | 117 ms: 1.03x faster                                                        |
| float                      | 80.2 ms                                                          | 78.0 ms: 1.03x faster                                                       |
| hexiom                     | 6.35 ms                                                          | 6.19 ms: 1.03x faster                                                       |
| sympy_expand               | 501 ms                                                           | 488 ms: 1.03x faster                                                        |
| sympy_sum                  | 155 ms                                                           | 151 ms: 1.03x faster                                                        |
| telco                      | 8.40 ms                                                          | 8.20 ms: 1.02x faster                                                       |
| crypto_pyaes               | 73.6 ms                                                          | 71.9 ms: 1.02x faster                                                       |
| sympy_str                  | 295 ms                                                           | 289 ms: 1.02x faster                                                        |
| pickle                     | 10.6 us                                                          | 10.4 us: 1.02x faster                                                       |
| unpickle                   | 15.7 us                                                          | 15.4 us: 1.02x faster                                                       |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 561 ms: 1.02x faster                                                        |
| sqlite_synth               | 2.80 us                                                          | 2.74 us: 1.02x faster                                                       |
| dulwich_log                | 67.3 ms                                                          | 66.1 ms: 1.02x faster                                                       |
| coverage                   | 83.5 ms                                                          | 82.0 ms: 1.02x faster                                                       |
| async_generators           | 363 ms                                                           | 357 ms: 1.02x faster                                                        |
| create_gc_cycles           | 2.00 ms                                                          | 1.97 ms: 1.02x faster                                                       |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 4.22 ms: 1.02x faster                                                       |
| sqlglot_optimize           | 59.5 ms                                                          | 58.7 ms: 1.01x faster                                                       |
| meteor_contest             | 128 ms                                                           | 126 ms: 1.01x faster                                                        |
| xml_etree_generate         | 85.7 ms                                                          | 84.7 ms: 1.01x faster                                                       |
| asyncio_tcp                | 378 ms                                                           | 374 ms: 1.01x faster                                                        |
| deltablue                  | 3.37 ms                                                          | 3.34 ms: 1.01x faster                                                       |
| xml_etree_process          | 59.7 ms                                                          | 59.2 ms: 1.01x faster                                                       |
| mako                       | 10.4 ms                                                          | 10.3 ms: 1.01x faster                                                       |
| xml_etree_iterparse        | 103 ms                                                           | 102 ms: 1.01x faster                                                        |
| pprint_safe_repr           | 818 ms                                                           | 814 ms: 1.00x faster                                                        |
| regex_dna                  | 249 ms                                                           | 248 ms: 1.00x faster                                                        |
| pidigits                   | 254 ms                                                           | 253 ms: 1.00x faster                                                        |
| json_dumps                 | 10.8 ms                                                          | 10.8 ms: 1.00x slower                                                       |
| regex_v8                   | 26.0 ms                                                          | 26.2 ms: 1.01x slower                                                       |
| nqueens                    | 88.4 ms                                                          | 88.9 ms: 1.01x slower                                                       |
| pprint_pformat             | 1.66 sec                                                         | 1.67 sec: 1.01x slower                                                      |
| sqlglot_parse              | 1.39 ms                                                          | 1.40 ms: 1.01x slower                                                       |
| unpickle_list              | 4.70 us                                                          | 4.74 us: 1.01x slower                                                       |
| python_startup_no_site     | 8.85 ms                                                          | 8.95 ms: 1.01x slower                                                       |
| python_startup             | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                                       |
| scimark_sor                | 119 ms                                                           | 120 ms: 1.01x slower                                                        |
| sqlglot_transpile          | 1.76 ms                                                          | 1.79 ms: 1.01x slower                                                       |
| comprehensions             | 17.0 us                                                          | 17.2 us: 1.01x slower                                                       |
| pickle_pure_python         | 307 us                                                           | 312 us: 1.02x slower                                                        |
| pyflate                    | 482 ms                                                           | 490 ms: 1.02x slower                                                        |
| regex_effbot               | 3.40 ms                                                          | 3.48 ms: 1.02x slower                                                       |
| logging_silent             | 96.3 ns                                                          | 98.6 ns: 1.02x slower                                                       |
| pickle_list                | 4.44 us                                                          | 4.55 us: 1.02x slower                                                       |
| nbody                      | 87.8 ms                                                          | 90.6 ms: 1.03x slower                                                       |
| raytrace                   | 260 ms                                                           | 269 ms: 1.03x slower                                                        |
| django_template            | 39.0 ms                                                          | 40.6 ms: 1.04x slower                                                       |
| xml_etree_parse            | 144 ms                                                           | 150 ms: 1.05x slower                                                        |
| chaos                      | 59.6 ms                                                          | 62.3 ms: 1.05x slower                                                       |
| tomli_loads                | 2.40 sec                                                         | 2.56 sec: 1.07x slower                                                      |
| bench_mp_pool              | 4.91 ms                                                          | 1.40 sec: 285.46x slower                                                    |
| Geometric mean             | (ref)                                                            | 1.03x slower                                                                |

Benchmark hidden because not significant (13): asyncio_websockets, bench_thread_pool, json, typing_runtime_protocols, fannkuch, spectral_norm, asyncio_tcp_ssl, sympy_integrate, json_loads, mdp, pycparser, scimark_monte_carlo, pylint
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20241003-3.14.0a0-c8db0e8/bm-20241003-pythonperf2-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x