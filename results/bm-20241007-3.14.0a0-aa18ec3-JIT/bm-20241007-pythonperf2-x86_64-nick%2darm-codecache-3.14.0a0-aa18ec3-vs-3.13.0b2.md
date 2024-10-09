# Results vs. 3.13.0b2

- fork: nick-arm
- ref: codecache
- machine: linux-x86_64
- commit hash: aa18ec3
- commit date: 2024-10-07
- overall geometric mean: 1.06x slower
- HPT reliability: 87.14%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------|:----------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 317 ms: 1.09x slower                                                 |
| docutils       | 2.98 sec                                                         | 3.19 sec: 1.07x slower                                               |
| html5lib       | 74.7 ms                                                          | 73.1 ms: 1.02x faster                                                |
| tornado_http   | 119 ms                                                           | 122 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                            | 1.04x slower                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------------------|:----------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_io_tg           | 900 ms                                                           | 792 ms: 1.14x faster                                                 |
| async_tree_memoization     | 460 ms                                                           | 406 ms: 1.13x faster                                                 |
| async_tree_none            | 365 ms                                                           | 327 ms: 1.12x faster                                                 |
| async_tree_none_tg         | 340 ms                                                           | 310 ms: 1.10x faster                                                 |
| async_tree_io              | 873 ms                                                           | 804 ms: 1.09x faster                                                 |
| async_tree_memoization_tg  | 421 ms                                                           | 391 ms: 1.08x faster                                                 |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 549 ms: 1.04x faster                                                 |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 580 ms: 1.04x faster                                                 |
| Geometric mean             | (ref)                                                            | 1.09x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------|:----------------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 80.2 ms                                                          | 75.8 ms: 1.06x faster                                                |
| nbody          | 87.8 ms                                                          | 84.2 ms: 1.04x faster                                                |
| pidigits       | 254 ms                                                           | 250 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                            | 1.04x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------|:----------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_v8       | 26.0 ms                                                          | 24.7 ms: 1.05x faster                                                |
| regex_dna      | 249 ms                                                           | 245 ms: 1.02x faster                                                 |
| regex_effbot   | 3.40 ms                                                          | 3.43 ms: 1.01x slower                                                |
| regex_compile  | 144 ms                                                           | 152 ms: 1.06x slower                                                 |
| Geometric mean | (ref)                                                            | 1.00x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------------|:----------------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 2.40 sec                                                         | 2.17 sec: 1.11x faster                                               |
| xml_etree_generate   | 85.7 ms                                                          | 78.0 ms: 1.10x faster                                                |
| pickle_dict          | 32.8 us                                                          | 30.8 us: 1.07x faster                                                |
| xml_etree_process    | 59.7 ms                                                          | 56.2 ms: 1.06x faster                                                |
| pickle_list          | 4.44 us                                                          | 4.20 us: 1.06x faster                                                |
| json_loads           | 25.0 us                                                          | 23.8 us: 1.05x faster                                                |
| unpickle_pure_python | 224 us                                                           | 215 us: 1.04x faster                                                 |
| xml_etree_iterparse  | 103 ms                                                           | 98.4 ms: 1.04x faster                                                |
| xml_etree_parse      | 144 ms                                                           | 140 ms: 1.03x faster                                                 |
| json_dumps           | 10.8 ms                                                          | 10.5 ms: 1.03x faster                                                |
| pickle               | 10.6 us                                                          | 10.3 us: 1.03x faster                                                |
| unpickle_list        | 4.70 us                                                          | 4.76 us: 1.01x slower                                                |
| pickle_pure_python   | 307 us                                                           | 329 us: 1.07x slower                                                 |
| Geometric mean       | (ref)                                                            | 1.04x faster                                                         |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|------------------------|:----------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                                |
| python_startup_no_site | 8.85 ms                                                          | 8.96 ms: 1.01x slower                                                |
| Geometric mean         | (ref)                                                            | 1.01x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|-----------------|:----------------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 10.4 ms                                                          | 9.20 ms: 1.13x faster                                                |
| django_template | 39.0 ms                                                          | 43.2 ms: 1.11x slower                                                |
| genshi_xml      | 58.1 ms                                                          | 64.4 ms: 1.11x slower                                                |
| genshi_text     | 25.9 ms                                                          | 29.0 ms: 1.12x slower                                                |
| Geometric mean  | (ref)                                                            | 1.05x slower                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------------------|:----------------------------------------------------------------:|:--------------------------------------------------------------------:|
| deepcopy_memo              | 37.3 us                                                          | 27.7 us: 1.34x faster                                                |
| deepcopy                   | 377 us                                                           | 299 us: 1.26x faster                                                 |
| richards                   | 53.4 ms                                                          | 44.2 ms: 1.21x faster                                                |
| richards_super             | 61.2 ms                                                          | 50.6 ms: 1.21x faster                                                |
| spectral_norm              | 97.3 ms                                                          | 83.3 ms: 1.17x faster                                                |
| deepcopy_reduce            | 3.39 us                                                          | 2.96 us: 1.15x faster                                                |
| async_tree_io_tg           | 900 ms                                                           | 792 ms: 1.14x faster                                                 |
| async_tree_memoization     | 460 ms                                                           | 406 ms: 1.13x faster                                                 |
| mako                       | 10.4 ms                                                          | 9.20 ms: 1.13x faster                                                |
| async_tree_none            | 365 ms                                                           | 327 ms: 1.12x faster                                                 |
| scimark_sor                | 119 ms                                                           | 107 ms: 1.11x faster                                                 |
| tomli_loads                | 2.40 sec                                                         | 2.17 sec: 1.11x faster                                               |
| scimark_fft                | 312 ms                                                           | 283 ms: 1.10x faster                                                 |
| xml_etree_generate         | 85.7 ms                                                          | 78.0 ms: 1.10x faster                                                |
| async_tree_none_tg         | 340 ms                                                           | 310 ms: 1.10x faster                                                 |
| bpe_tokeniser              | 5.14 sec                                                         | 4.70 sec: 1.09x faster                                               |
| gc_traversal               | 4.69 ms                                                          | 4.30 ms: 1.09x faster                                                |
| telco                      | 8.40 ms                                                          | 7.71 ms: 1.09x faster                                                |
| pathlib                    | 17.1 ms                                                          | 15.8 ms: 1.09x faster                                                |
| async_tree_io              | 873 ms                                                           | 804 ms: 1.09x faster                                                 |
| pprint_safe_repr           | 818 ms                                                           | 755 ms: 1.08x faster                                                 |
| async_tree_memoization_tg  | 421 ms                                                           | 391 ms: 1.08x faster                                                 |
| go                         | 165 ms                                                           | 154 ms: 1.07x faster                                                 |
| create_gc_cycles           | 2.00 ms                                                          | 1.87 ms: 1.07x faster                                                |
| pickle_dict                | 32.8 us                                                          | 30.8 us: 1.07x faster                                                |
| pyflate                    | 482 ms                                                           | 451 ms: 1.07x faster                                                 |
| xml_etree_process          | 59.7 ms                                                          | 56.2 ms: 1.06x faster                                                |
| pickle_list                | 4.44 us                                                          | 4.20 us: 1.06x faster                                                |
| float                      | 80.2 ms                                                          | 75.8 ms: 1.06x faster                                                |
| pprint_pformat             | 1.66 sec                                                         | 1.58 sec: 1.05x faster                                               |
| regex_v8                   | 26.0 ms                                                          | 24.7 ms: 1.05x faster                                                |
| deltablue                  | 3.37 ms                                                          | 3.21 ms: 1.05x faster                                                |
| json_loads                 | 25.0 us                                                          | 23.8 us: 1.05x faster                                                |
| dulwich_log                | 67.3 ms                                                          | 64.0 ms: 1.05x faster                                                |
| unpickle_pure_python       | 224 us                                                           | 215 us: 1.04x faster                                                 |
| nbody                      | 87.8 ms                                                          | 84.2 ms: 1.04x faster                                                |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 549 ms: 1.04x faster                                                 |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 580 ms: 1.04x faster                                                 |
| xml_etree_iterparse        | 103 ms                                                           | 98.4 ms: 1.04x faster                                                |
| crypto_pyaes               | 73.6 ms                                                          | 70.7 ms: 1.04x faster                                                |
| coroutines                 | 22.0 ms                                                          | 21.2 ms: 1.04x faster                                                |
| coverage                   | 83.5 ms                                                          | 80.7 ms: 1.03x faster                                                |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 4.14 ms: 1.03x faster                                                |
| sqlite_synth               | 2.80 us                                                          | 2.71 us: 1.03x faster                                                |
| json                       | 5.35 ms                                                          | 5.20 ms: 1.03x faster                                                |
| xml_etree_parse            | 144 ms                                                           | 140 ms: 1.03x faster                                                 |
| json_dumps                 | 10.8 ms                                                          | 10.5 ms: 1.03x faster                                                |
| pickle                     | 10.6 us                                                          | 10.3 us: 1.03x faster                                                |
| asyncio_tcp                | 378 ms                                                           | 369 ms: 1.02x faster                                                 |
| html5lib                   | 74.7 ms                                                          | 73.1 ms: 1.02x faster                                                |
| regex_dna                  | 249 ms                                                           | 245 ms: 1.02x faster                                                 |
| asyncio_websockets         | 395 ms                                                           | 389 ms: 1.01x faster                                                 |
| pidigits                   | 254 ms                                                           | 250 ms: 1.01x faster                                                 |
| asyncio_tcp_ssl            | 1.58 sec                                                         | 1.58 sec: 1.00x slower                                               |
| fannkuch                   | 353 ms                                                           | 356 ms: 1.01x slower                                                 |
| logging_format             | 7.11 us                                                          | 7.18 us: 1.01x slower                                                |
| regex_effbot               | 3.40 ms                                                          | 3.43 ms: 1.01x slower                                                |
| python_startup             | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                                |
| unpickle_list              | 4.70 us                                                          | 4.76 us: 1.01x slower                                                |
| python_startup_no_site     | 8.85 ms                                                          | 8.96 ms: 1.01x slower                                                |
| tornado_http               | 119 ms                                                           | 122 ms: 1.02x slower                                                 |
| logging_silent             | 96.3 ns                                                          | 98.9 ns: 1.03x slower                                                |
| logging_simple             | 6.40 us                                                          | 6.61 us: 1.03x slower                                                |
| meteor_contest             | 128 ms                                                           | 133 ms: 1.04x slower                                                 |
| mdp                        | 2.46 sec                                                         | 2.56 sec: 1.04x slower                                               |
| thrift                     | 880 us                                                           | 916 us: 1.04x slower                                                 |
| bench_thread_pool          | 908 us                                                           | 947 us: 1.04x slower                                                 |
| sympy_expand               | 501 ms                                                           | 525 ms: 1.05x slower                                                 |
| scimark_monte_carlo        | 65.5 ms                                                          | 68.7 ms: 1.05x slower                                                |
| async_generators           | 363 ms                                                           | 383 ms: 1.06x slower                                                 |
| regex_compile              | 144 ms                                                           | 152 ms: 1.06x slower                                                 |
| pycparser                  | 1.22 sec                                                         | 1.29 sec: 1.06x slower                                               |
| docutils                   | 2.98 sec                                                         | 3.19 sec: 1.07x slower                                               |
| pickle_pure_python         | 307 us                                                           | 329 us: 1.07x slower                                                 |
| sympy_str                  | 295 ms                                                           | 318 ms: 1.08x slower                                                 |
| sqlglot_normalize          | 120 ms                                                           | 130 ms: 1.08x slower                                                 |
| 2to3                       | 291 ms                                                           | 317 ms: 1.09x slower                                                 |
| sqlglot_parse              | 1.39 ms                                                          | 1.52 ms: 1.10x slower                                                |
| comprehensions             | 17.0 us                                                          | 18.8 us: 1.11x slower                                                |
| typing_runtime_protocols   | 171 us                                                           | 189 us: 1.11x slower                                                 |
| django_template            | 39.0 ms                                                          | 43.2 ms: 1.11x slower                                                |
| genshi_xml                 | 58.1 ms                                                          | 64.4 ms: 1.11x slower                                                |
| hexiom                     | 6.35 ms                                                          | 7.06 ms: 1.11x slower                                                |
| sympy_sum                  | 155 ms                                                           | 173 ms: 1.11x slower                                                 |
| chaos                      | 59.6 ms                                                          | 66.8 ms: 1.12x slower                                                |
| genshi_text                | 25.9 ms                                                          | 29.0 ms: 1.12x slower                                                |
| sqlglot_transpile          | 1.76 ms                                                          | 1.98 ms: 1.12x slower                                                |
| nqueens                    | 88.4 ms                                                          | 101 ms: 1.14x slower                                                 |
| sqlglot_optimize           | 59.5 ms                                                          | 68.7 ms: 1.15x slower                                                |
| sympy_integrate            | 23.2 ms                                                          | 27.2 ms: 1.17x slower                                                |
| generators                 | 33.5 ms                                                          | 39.5 ms: 1.18x slower                                                |
| pylint                     | 339 ms                                                           | 414 ms: 1.22x slower                                                 |
| raytrace                   | 260 ms                                                           | 322 ms: 1.24x slower                                                 |
| bench_mp_pool              | 4.91 ms                                                          | 4.58 sec: 933.88x slower                                             |
| Geometric mean             | (ref)                                                            | 1.06x slower                                                         |

Benchmark hidden because not significant (2): unpickle, scimark_lu
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20241007-3.14.0a0-aa18ec3-JIT/bm-20241007-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3.json: unpack_sequence

# HPT report

- Reliability score: 87.14% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x