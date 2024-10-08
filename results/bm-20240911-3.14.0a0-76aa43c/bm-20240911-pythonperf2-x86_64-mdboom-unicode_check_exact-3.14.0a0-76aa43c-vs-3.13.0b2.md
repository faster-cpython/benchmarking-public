# Results vs. 3.13.0b2

- fork: mdboom
- ref: unicode_check_exact
- machine: linux-x86_64
- commit hash: 76aa43c
- commit date: 2024-09-11
- overall geometric mean: 1.03x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-pythonperf2-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:----------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 281 ms: 1.04x faster                                                       |
| docutils       | 2.98 sec                                                         | 2.91 sec: 1.02x faster                                                     |
| html5lib       | 74.7 ms                                                          | 72.7 ms: 1.03x faster                                                      |
| tornado_http   | 119 ms                                                           | 116 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                            | 1.03x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-pythonperf2-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------------------|:----------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization     | 460 ms                                                           | 397 ms: 1.16x faster                                                       |
| async_tree_none            | 365 ms                                                           | 319 ms: 1.15x faster                                                       |
| async_tree_io_tg           | 900 ms                                                           | 787 ms: 1.14x faster                                                       |
| async_tree_none_tg         | 340 ms                                                           | 306 ms: 1.11x faster                                                       |
| async_tree_memoization_tg  | 421 ms                                                           | 388 ms: 1.08x faster                                                       |
| async_tree_io              | 873 ms                                                           | 818 ms: 1.07x faster                                                       |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 572 ms: 1.06x faster                                                       |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 545 ms: 1.05x faster                                                       |
| Geometric mean             | (ref)                                                            | 1.10x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-pythonperf2-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:----------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 87.8 ms                                                          | 84.9 ms: 1.03x faster                                                      |
| pidigits       | 254 ms                                                           | 253 ms: 1.00x faster                                                       |
| float          | 80.2 ms                                                          | 80.7 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                            | 1.01x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-pythonperf2-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:----------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                           | 141 ms: 1.02x faster                                                       |
| regex_dna      | 249 ms                                                           | 254 ms: 1.02x slower                                                       |
| regex_v8       | 26.0 ms                                                          | 26.7 ms: 1.02x slower                                                      |
| regex_effbot   | 3.40 ms                                                          | 3.66 ms: 1.08x slower                                                      |
| Geometric mean | (ref)                                                            | 1.02x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-pythonperf2-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------------|:----------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_dict          | 32.8 us                                                          | 29.6 us: 1.11x faster                                                      |
| pickle_list          | 4.44 us                                                          | 4.18 us: 1.06x faster                                                      |
| pickle               | 10.6 us                                                          | 10.2 us: 1.04x faster                                                      |
| unpickle_pure_python | 224 us                                                           | 216 us: 1.04x faster                                                       |
| unpickle             | 15.7 us                                                          | 15.3 us: 1.02x faster                                                      |
| xml_etree_iterparse  | 103 ms                                                           | 101 ms: 1.02x faster                                                       |
| xml_etree_generate   | 85.7 ms                                                          | 84.4 ms: 1.02x faster                                                      |
| xml_etree_process    | 59.7 ms                                                          | 59.1 ms: 1.01x faster                                                      |
| json_dumps           | 10.8 ms                                                          | 10.7 ms: 1.01x faster                                                      |
| xml_etree_parse      | 144 ms                                                           | 145 ms: 1.01x slower                                                       |
| unpickle_list        | 4.70 us                                                          | 4.76 us: 1.01x slower                                                      |
| pickle_pure_python   | 307 us                                                           | 315 us: 1.02x slower                                                       |
| tomli_loads          | 2.40 sec                                                         | 2.51 sec: 1.04x slower                                                     |
| Geometric mean       | (ref)                                                            | 1.02x faster                                                               |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-pythonperf2-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|------------------------|:----------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                                      |
| python_startup_no_site | 8.85 ms                                                          | 8.95 ms: 1.01x slower                                                      |
| Geometric mean         | (ref)                                                            | 1.01x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-pythonperf2-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|-----------------|:----------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 58.1 ms                                                          | 53.0 ms: 1.09x faster                                                      |
| genshi_text     | 25.9 ms                                                          | 24.1 ms: 1.08x faster                                                      |
| django_template | 39.0 ms                                                          | 38.6 ms: 1.01x faster                                                      |
| Geometric mean  | (ref)                                                            | 1.05x faster                                                               |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-pythonperf2-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------------------|:----------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deepcopy                   | 377 us                                                           | 280 us: 1.35x faster                                                       |
| deepcopy_memo              | 37.3 us                                                          | 29.7 us: 1.25x faster                                                      |
| go                         | 165 ms                                                           | 136 ms: 1.21x faster                                                       |
| deepcopy_reduce            | 3.39 us                                                          | 2.86 us: 1.18x faster                                                      |
| async_tree_memoization     | 460 ms                                                           | 397 ms: 1.16x faster                                                       |
| generators                 | 33.5 ms                                                          | 29.1 ms: 1.15x faster                                                      |
| async_tree_none            | 365 ms                                                           | 319 ms: 1.15x faster                                                       |
| async_tree_io_tg           | 900 ms                                                           | 787 ms: 1.14x faster                                                       |
| async_tree_none_tg         | 340 ms                                                           | 306 ms: 1.11x faster                                                       |
| pickle_dict                | 32.8 us                                                          | 29.6 us: 1.11x faster                                                      |
| pathlib                    | 17.1 ms                                                          | 15.6 ms: 1.10x faster                                                      |
| genshi_xml                 | 58.1 ms                                                          | 53.0 ms: 1.09x faster                                                      |
| richards_super             | 61.2 ms                                                          | 56.1 ms: 1.09x faster                                                      |
| async_tree_memoization_tg  | 421 ms                                                           | 388 ms: 1.08x faster                                                       |
| richards                   | 53.4 ms                                                          | 49.6 ms: 1.08x faster                                                      |
| genshi_text                | 25.9 ms                                                          | 24.1 ms: 1.08x faster                                                      |
| async_tree_io              | 873 ms                                                           | 818 ms: 1.07x faster                                                       |
| pickle_list                | 4.44 us                                                          | 4.18 us: 1.06x faster                                                      |
| scimark_fft                | 312 ms                                                           | 295 ms: 1.06x faster                                                       |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 572 ms: 1.06x faster                                                       |
| bench_mp_pool              | 4.91 ms                                                          | 4.66 ms: 1.05x faster                                                      |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 545 ms: 1.05x faster                                                       |
| bpe_tokeniser              | 5.14 sec                                                         | 4.92 sec: 1.04x faster                                                     |
| logging_format             | 7.11 us                                                          | 6.82 us: 1.04x faster                                                      |
| pickle                     | 10.6 us                                                          | 10.2 us: 1.04x faster                                                      |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 4.12 ms: 1.04x faster                                                      |
| bench_thread_pool          | 908 us                                                           | 874 us: 1.04x faster                                                       |
| unpickle_pure_python       | 224 us                                                           | 216 us: 1.04x faster                                                       |
| 2to3                       | 291 ms                                                           | 281 ms: 1.04x faster                                                       |
| nbody                      | 87.8 ms                                                          | 84.9 ms: 1.03x faster                                                      |
| thrift                     | 880 us                                                           | 853 us: 1.03x faster                                                       |
| logging_simple             | 6.40 us                                                          | 6.21 us: 1.03x faster                                                      |
| tornado_http               | 119 ms                                                           | 116 ms: 1.03x faster                                                       |
| asyncio_tcp                | 378 ms                                                           | 367 ms: 1.03x faster                                                       |
| html5lib                   | 74.7 ms                                                          | 72.7 ms: 1.03x faster                                                      |
| crypto_pyaes               | 73.6 ms                                                          | 71.8 ms: 1.03x faster                                                      |
| regex_compile              | 144 ms                                                           | 141 ms: 1.02x faster                                                       |
| async_generators           | 363 ms                                                           | 354 ms: 1.02x faster                                                       |
| scimark_lu                 | 97.5 ms                                                          | 95.2 ms: 1.02x faster                                                      |
| docutils                   | 2.98 sec                                                         | 2.91 sec: 1.02x faster                                                     |
| unpickle                   | 15.7 us                                                          | 15.3 us: 1.02x faster                                                      |
| sqlite_synth               | 2.80 us                                                          | 2.74 us: 1.02x faster                                                      |
| coroutines                 | 22.0 ms                                                          | 21.5 ms: 1.02x faster                                                      |
| sqlglot_optimize           | 59.5 ms                                                          | 58.4 ms: 1.02x faster                                                      |
| json                       | 5.35 ms                                                          | 5.25 ms: 1.02x faster                                                      |
| telco                      | 8.40 ms                                                          | 8.24 ms: 1.02x faster                                                      |
| sympy_sum                  | 155 ms                                                           | 152 ms: 1.02x faster                                                       |
| xml_etree_iterparse        | 103 ms                                                           | 101 ms: 1.02x faster                                                       |
| pprint_safe_repr           | 818 ms                                                           | 804 ms: 1.02x faster                                                       |
| xml_etree_generate         | 85.7 ms                                                          | 84.4 ms: 1.02x faster                                                      |
| asyncio_websockets         | 395 ms                                                           | 389 ms: 1.01x faster                                                       |
| meteor_contest             | 128 ms                                                           | 127 ms: 1.01x faster                                                       |
| sqlglot_normalize          | 120 ms                                                           | 119 ms: 1.01x faster                                                       |
| xml_etree_process          | 59.7 ms                                                          | 59.1 ms: 1.01x faster                                                      |
| dulwich_log                | 67.3 ms                                                          | 66.6 ms: 1.01x faster                                                      |
| hexiom                     | 6.35 ms                                                          | 6.29 ms: 1.01x faster                                                      |
| sympy_str                  | 295 ms                                                           | 292 ms: 1.01x faster                                                       |
| django_template            | 39.0 ms                                                          | 38.6 ms: 1.01x faster                                                      |
| spectral_norm              | 97.3 ms                                                          | 96.4 ms: 1.01x faster                                                      |
| scimark_sor                | 119 ms                                                           | 118 ms: 1.01x faster                                                       |
| pprint_pformat             | 1.66 sec                                                         | 1.65 sec: 1.01x faster                                                     |
| json_dumps                 | 10.8 ms                                                          | 10.7 ms: 1.01x faster                                                      |
| sympy_integrate            | 23.2 ms                                                          | 23.0 ms: 1.01x faster                                                      |
| asyncio_tcp_ssl            | 1.58 sec                                                         | 1.57 sec: 1.00x faster                                                     |
| pidigits                   | 254 ms                                                           | 253 ms: 1.00x faster                                                       |
| nqueens                    | 88.4 ms                                                          | 88.6 ms: 1.00x slower                                                      |
| float                      | 80.2 ms                                                          | 80.7 ms: 1.01x slower                                                      |
| fannkuch                   | 353 ms                                                           | 356 ms: 1.01x slower                                                       |
| scimark_monte_carlo        | 65.5 ms                                                          | 66.2 ms: 1.01x slower                                                      |
| python_startup             | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                                      |
| xml_etree_parse            | 144 ms                                                           | 145 ms: 1.01x slower                                                       |
| python_startup_no_site     | 8.85 ms                                                          | 8.95 ms: 1.01x slower                                                      |
| unpickle_list              | 4.70 us                                                          | 4.76 us: 1.01x slower                                                      |
| mdp                        | 2.46 sec                                                         | 2.50 sec: 1.01x slower                                                     |
| sqlglot_parse              | 1.39 ms                                                          | 1.41 ms: 1.02x slower                                                      |
| sqlglot_transpile          | 1.76 ms                                                          | 1.80 ms: 1.02x slower                                                      |
| regex_dna                  | 249 ms                                                           | 254 ms: 1.02x slower                                                       |
| deltablue                  | 3.37 ms                                                          | 3.44 ms: 1.02x slower                                                      |
| comprehensions             | 17.0 us                                                          | 17.3 us: 1.02x slower                                                      |
| coverage                   | 83.5 ms                                                          | 85.2 ms: 1.02x slower                                                      |
| pickle_pure_python         | 307 us                                                           | 315 us: 1.02x slower                                                       |
| regex_v8                   | 26.0 ms                                                          | 26.7 ms: 1.02x slower                                                      |
| logging_silent             | 96.3 ns                                                          | 98.7 ns: 1.03x slower                                                      |
| chaos                      | 59.6 ms                                                          | 61.2 ms: 1.03x slower                                                      |
| pyflate                    | 482 ms                                                           | 497 ms: 1.03x slower                                                       |
| raytrace                   | 260 ms                                                           | 269 ms: 1.03x slower                                                       |
| tomli_loads                | 2.40 sec                                                         | 2.51 sec: 1.04x slower                                                     |
| gc_traversal               | 4.69 ms                                                          | 4.89 ms: 1.04x slower                                                      |
| regex_effbot               | 3.40 ms                                                          | 3.66 ms: 1.08x slower                                                      |
| Geometric mean             | (ref)                                                            | 1.03x faster                                                               |

Benchmark hidden because not significant (7): mako, create_gc_cycles, typing_runtime_protocols, sympy_expand, json_loads, pycparser, pylint
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240911-3.14.0a0-76aa43c/bm-20240911-pythonperf2-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x