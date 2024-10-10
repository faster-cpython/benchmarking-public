# Results vs. 3.13.0b2

- fork: nick-arm
- ref: codecache_rwx
- machine: linux-x86_64
- commit hash: 0442576
- commit date: 2024-10-07
- overall geometric mean: 1.06x slower
- HPT reliability: 82.62%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:----------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 315 ms: 1.08x slower                                                     |
| docutils       | 2.98 sec                                                         | 3.17 sec: 1.06x slower                                                   |
| html5lib       | 74.7 ms                                                          | 73.1 ms: 1.02x faster                                                    |
| tornado_http   | 119 ms                                                           | 123 ms: 1.03x slower                                                     |
| Geometric mean | (ref)                                                            | 1.04x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------------------|:----------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg           | 900 ms                                                           | 782 ms: 1.15x faster                                                     |
| async_tree_memoization     | 460 ms                                                           | 407 ms: 1.13x faster                                                     |
| async_tree_none            | 365 ms                                                           | 329 ms: 1.11x faster                                                     |
| async_tree_none_tg         | 340 ms                                                           | 312 ms: 1.09x faster                                                     |
| async_tree_io              | 873 ms                                                           | 805 ms: 1.09x faster                                                     |
| async_tree_memoization_tg  | 421 ms                                                           | 392 ms: 1.07x faster                                                     |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 547 ms: 1.05x faster                                                     |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 580 ms: 1.04x faster                                                     |
| Geometric mean             | (ref)                                                            | 1.09x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:----------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 80.2 ms                                                          | 75.3 ms: 1.07x faster                                                    |
| nbody          | 87.8 ms                                                          | 83.3 ms: 1.05x faster                                                    |
| pidigits       | 254 ms                                                           | 251 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                            | 1.04x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:----------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_dna      | 249 ms                                                           | 236 ms: 1.06x faster                                                     |
| regex_v8       | 26.0 ms                                                          | 24.8 ms: 1.05x faster                                                    |
| regex_compile  | 144 ms                                                           | 150 ms: 1.04x slower                                                     |
| regex_effbot   | 3.40 ms                                                          | 3.60 ms: 1.06x slower                                                    |
| Geometric mean | (ref)                                                            | 1.00x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------------|:----------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle_dict          | 32.8 us                                                          | 29.8 us: 1.10x faster                                                    |
| tomli_loads          | 2.40 sec                                                         | 2.20 sec: 1.09x faster                                                   |
| xml_etree_generate   | 85.7 ms                                                          | 78.8 ms: 1.09x faster                                                    |
| xml_etree_process    | 59.7 ms                                                          | 56.4 ms: 1.06x faster                                                    |
| unpickle             | 15.7 us                                                          | 14.8 us: 1.06x faster                                                    |
| json_loads           | 25.0 us                                                          | 23.8 us: 1.05x faster                                                    |
| pickle_list          | 4.44 us                                                          | 4.30 us: 1.03x faster                                                    |
| pickle               | 10.6 us                                                          | 10.3 us: 1.03x faster                                                    |
| xml_etree_iterparse  | 103 ms                                                           | 99.8 ms: 1.03x faster                                                    |
| unpickle_pure_python | 224 us                                                           | 219 us: 1.02x faster                                                     |
| pickle_pure_python   | 307 us                                                           | 325 us: 1.06x slower                                                     |
| Geometric mean       | (ref)                                                            | 1.04x faster                                                             |

Benchmark hidden because not significant (3): json_dumps, unpickle_list, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|------------------------|:----------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                                    |
| python_startup_no_site | 8.85 ms                                                          | 8.97 ms: 1.01x slower                                                    |
| Geometric mean         | (ref)                                                            | 1.01x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|-----------------|:----------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 10.4 ms                                                          | 9.15 ms: 1.13x faster                                                    |
| genshi_xml      | 58.1 ms                                                          | 66.2 ms: 1.14x slower                                                    |
| genshi_text     | 25.9 ms                                                          | 29.8 ms: 1.15x slower                                                    |
| django_template | 39.0 ms                                                          | 46.0 ms: 1.18x slower                                                    |
| Geometric mean  | (ref)                                                            | 1.08x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------------------|:----------------------------------------------------------------:|:------------------------------------------------------------------------:|
| deepcopy_memo              | 37.3 us                                                          | 27.3 us: 1.37x faster                                                    |
| deepcopy                   | 377 us                                                           | 300 us: 1.26x faster                                                     |
| spectral_norm              | 97.3 ms                                                          | 82.8 ms: 1.18x faster                                                    |
| async_tree_io_tg           | 900 ms                                                           | 782 ms: 1.15x faster                                                     |
| deepcopy_reduce            | 3.39 us                                                          | 2.95 us: 1.15x faster                                                    |
| mako                       | 10.4 ms                                                          | 9.15 ms: 1.13x faster                                                    |
| async_tree_memoization     | 460 ms                                                           | 407 ms: 1.13x faster                                                     |
| richards                   | 53.4 ms                                                          | 47.3 ms: 1.13x faster                                                    |
| scimark_sor                | 119 ms                                                           | 105 ms: 1.13x faster                                                     |
| scimark_fft                | 312 ms                                                           | 280 ms: 1.11x faster                                                     |
| async_tree_none            | 365 ms                                                           | 329 ms: 1.11x faster                                                     |
| richards_super             | 61.2 ms                                                          | 55.4 ms: 1.10x faster                                                    |
| pickle_dict                | 32.8 us                                                          | 29.8 us: 1.10x faster                                                    |
| telco                      | 8.40 ms                                                          | 7.63 ms: 1.10x faster                                                    |
| tomli_loads                | 2.40 sec                                                         | 2.20 sec: 1.09x faster                                                   |
| async_tree_none_tg         | 340 ms                                                           | 312 ms: 1.09x faster                                                     |
| gc_traversal               | 4.69 ms                                                          | 4.31 ms: 1.09x faster                                                    |
| xml_etree_generate         | 85.7 ms                                                          | 78.8 ms: 1.09x faster                                                    |
| async_tree_io              | 873 ms                                                           | 805 ms: 1.09x faster                                                     |
| bpe_tokeniser              | 5.14 sec                                                         | 4.75 sec: 1.08x faster                                                   |
| pathlib                    | 17.1 ms                                                          | 15.8 ms: 1.08x faster                                                    |
| async_tree_memoization_tg  | 421 ms                                                           | 392 ms: 1.07x faster                                                     |
| pprint_safe_repr           | 818 ms                                                           | 762 ms: 1.07x faster                                                     |
| float                      | 80.2 ms                                                          | 75.3 ms: 1.07x faster                                                    |
| xml_etree_process          | 59.7 ms                                                          | 56.4 ms: 1.06x faster                                                    |
| unpickle                   | 15.7 us                                                          | 14.8 us: 1.06x faster                                                    |
| pyflate                    | 482 ms                                                           | 456 ms: 1.06x faster                                                     |
| regex_dna                  | 249 ms                                                           | 236 ms: 1.06x faster                                                     |
| nbody                      | 87.8 ms                                                          | 83.3 ms: 1.05x faster                                                    |
| json_loads                 | 25.0 us                                                          | 23.8 us: 1.05x faster                                                    |
| create_gc_cycles           | 2.00 ms                                                          | 1.90 ms: 1.05x faster                                                    |
| crypto_pyaes               | 73.6 ms                                                          | 70.0 ms: 1.05x faster                                                    |
| regex_v8                   | 26.0 ms                                                          | 24.8 ms: 1.05x faster                                                    |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 547 ms: 1.05x faster                                                     |
| deltablue                  | 3.37 ms                                                          | 3.23 ms: 1.05x faster                                                    |
| go                         | 165 ms                                                           | 158 ms: 1.04x faster                                                     |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 580 ms: 1.04x faster                                                     |
| dulwich_log                | 67.3 ms                                                          | 64.8 ms: 1.04x faster                                                    |
| pprint_pformat             | 1.66 sec                                                         | 1.60 sec: 1.04x faster                                                   |
| pickle_list                | 4.44 us                                                          | 4.30 us: 1.03x faster                                                    |
| json                       | 5.35 ms                                                          | 5.19 ms: 1.03x faster                                                    |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 4.15 ms: 1.03x faster                                                    |
| pickle                     | 10.6 us                                                          | 10.3 us: 1.03x faster                                                    |
| xml_etree_iterparse        | 103 ms                                                           | 99.8 ms: 1.03x faster                                                    |
| sqlite_synth               | 2.80 us                                                          | 2.73 us: 1.03x faster                                                    |
| unpickle_pure_python       | 224 us                                                           | 219 us: 1.02x faster                                                     |
| html5lib                   | 74.7 ms                                                          | 73.1 ms: 1.02x faster                                                    |
| fannkuch                   | 353 ms                                                           | 346 ms: 1.02x faster                                                     |
| asyncio_tcp                | 378 ms                                                           | 371 ms: 1.02x faster                                                     |
| scimark_lu                 | 97.5 ms                                                          | 96.0 ms: 1.02x faster                                                    |
| asyncio_websockets         | 395 ms                                                           | 390 ms: 1.01x faster                                                     |
| coverage                   | 83.5 ms                                                          | 82.6 ms: 1.01x faster                                                    |
| pidigits                   | 254 ms                                                           | 251 ms: 1.01x faster                                                     |
| asyncio_tcp_ssl            | 1.58 sec                                                         | 1.58 sec: 1.00x slower                                                   |
| coroutines                 | 22.0 ms                                                          | 22.1 ms: 1.01x slower                                                    |
| python_startup             | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                                    |
| python_startup_no_site     | 8.85 ms                                                          | 8.97 ms: 1.01x slower                                                    |
| logging_silent             | 96.3 ns                                                          | 98.1 ns: 1.02x slower                                                    |
| logging_format             | 7.11 us                                                          | 7.28 us: 1.02x slower                                                    |
| tornado_http               | 119 ms                                                           | 123 ms: 1.03x slower                                                     |
| typing_runtime_protocols   | 171 us                                                           | 176 us: 1.03x slower                                                     |
| logging_simple             | 6.40 us                                                          | 6.63 us: 1.03x slower                                                    |
| thrift                     | 880 us                                                           | 913 us: 1.04x slower                                                     |
| bench_thread_pool          | 908 us                                                           | 946 us: 1.04x slower                                                     |
| regex_compile              | 144 ms                                                           | 150 ms: 1.04x slower                                                     |
| meteor_contest             | 128 ms                                                           | 134 ms: 1.05x slower                                                     |
| scimark_monte_carlo        | 65.5 ms                                                          | 68.8 ms: 1.05x slower                                                    |
| async_generators           | 363 ms                                                           | 382 ms: 1.05x slower                                                     |
| mdp                        | 2.46 sec                                                         | 2.60 sec: 1.05x slower                                                   |
| pickle_pure_python         | 307 us                                                           | 325 us: 1.06x slower                                                     |
| regex_effbot               | 3.40 ms                                                          | 3.60 ms: 1.06x slower                                                    |
| docutils                   | 2.98 sec                                                         | 3.17 sec: 1.06x slower                                                   |
| sympy_expand               | 501 ms                                                           | 534 ms: 1.07x slower                                                     |
| pycparser                  | 1.22 sec                                                         | 1.31 sec: 1.07x slower                                                   |
| sympy_str                  | 295 ms                                                           | 318 ms: 1.08x slower                                                     |
| 2to3                       | 291 ms                                                           | 315 ms: 1.08x slower                                                     |
| sqlglot_parse              | 1.39 ms                                                          | 1.51 ms: 1.09x slower                                                    |
| sqlglot_transpile          | 1.76 ms                                                          | 1.94 ms: 1.10x slower                                                    |
| comprehensions             | 17.0 us                                                          | 18.7 us: 1.10x slower                                                    |
| sympy_sum                  | 155 ms                                                           | 172 ms: 1.11x slower                                                     |
| generators                 | 33.5 ms                                                          | 37.3 ms: 1.11x slower                                                    |
| hexiom                     | 6.35 ms                                                          | 7.09 ms: 1.12x slower                                                    |
| sqlglot_normalize          | 120 ms                                                           | 136 ms: 1.13x slower                                                     |
| genshi_xml                 | 58.1 ms                                                          | 66.2 ms: 1.14x slower                                                    |
| chaos                      | 59.6 ms                                                          | 68.0 ms: 1.14x slower                                                    |
| genshi_text                | 25.9 ms                                                          | 29.8 ms: 1.15x slower                                                    |
| nqueens                    | 88.4 ms                                                          | 102 ms: 1.16x slower                                                     |
| sympy_integrate            | 23.2 ms                                                          | 27.0 ms: 1.16x slower                                                    |
| sqlglot_optimize           | 59.5 ms                                                          | 69.6 ms: 1.17x slower                                                    |
| django_template            | 39.0 ms                                                          | 46.0 ms: 1.18x slower                                                    |
| pylint                     | 339 ms                                                           | 407 ms: 1.20x slower                                                     |
| raytrace                   | 260 ms                                                           | 323 ms: 1.24x slower                                                     |
| bench_mp_pool              | 4.91 ms                                                          | 3.26 sec: 663.44x slower                                                 |
| Geometric mean             | (ref)                                                            | 1.06x slower                                                             |

Benchmark hidden because not significant (3): json_dumps, unpickle_list, xml_etree_parse
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20241007-3.14.0a0-0442576-JIT/bm-20241007-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576.json: unpack_sequence

# HPT report

- Reliability score: 82.62% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.06x