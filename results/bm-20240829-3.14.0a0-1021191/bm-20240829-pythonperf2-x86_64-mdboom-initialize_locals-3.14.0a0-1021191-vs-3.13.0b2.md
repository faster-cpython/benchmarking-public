# Results vs. 3.13.0b2

- fork: mdboom
- ref: initialize_locals
- machine: linux-x86_64
- commit hash: 1021191
- commit date: 2024-08-29
- overall geometric mean: 1.02x faster
- HPT reliability: 99.94%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-pythonperf2-x86_64-mdboom-initialize_locals-3.14.0a0-1021191 |
|----------------|:----------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 284 ms: 1.03x faster                                                     |
| docutils       | 2.98 sec                                                         | 2.93 sec: 1.02x faster                                                   |
| html5lib       | 74.7 ms                                                          | 71.2 ms: 1.05x faster                                                    |
| tornado_http   | 119 ms                                                           | 117 ms: 1.02x faster                                                     |
| Geometric mean | (ref)                                                            | 1.03x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-pythonperf2-x86_64-mdboom-initialize_locals-3.14.0a0-1021191 |
|----------------------------|:----------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization     | 460 ms                                                           | 402 ms: 1.14x faster                                                     |
| async_tree_io_tg           | 900 ms                                                           | 792 ms: 1.14x faster                                                     |
| async_tree_none            | 365 ms                                                           | 323 ms: 1.13x faster                                                     |
| async_tree_none_tg         | 340 ms                                                           | 311 ms: 1.09x faster                                                     |
| async_tree_io              | 873 ms                                                           | 806 ms: 1.08x faster                                                     |
| async_tree_memoization_tg  | 421 ms                                                           | 392 ms: 1.07x faster                                                     |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 575 ms: 1.05x faster                                                     |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 551 ms: 1.04x faster                                                     |
| Geometric mean             | (ref)                                                            | 1.09x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-pythonperf2-x86_64-mdboom-initialize_locals-3.14.0a0-1021191 |
|----------------|:----------------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 87.8 ms                                                          | 84.8 ms: 1.04x faster                                                    |
| float          | 80.2 ms                                                          | 78.4 ms: 1.02x faster                                                    |
| Geometric mean | (ref)                                                            | 1.02x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-pythonperf2-x86_64-mdboom-initialize_locals-3.14.0a0-1021191 |
|----------------|:----------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_dna      | 249 ms                                                           | 235 ms: 1.06x faster                                                     |
| regex_compile  | 144 ms                                                           | 142 ms: 1.02x faster                                                     |
| regex_effbot   | 3.40 ms                                                          | 3.50 ms: 1.03x slower                                                    |
| regex_v8       | 26.0 ms                                                          | 26.9 ms: 1.04x slower                                                    |
| Geometric mean | (ref)                                                            | 1.00x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-pythonperf2-x86_64-mdboom-initialize_locals-3.14.0a0-1021191 |
|----------------------|:----------------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 224 us                                                           | 219 us: 1.03x faster                                                     |
| xml_etree_iterparse  | 103 ms                                                           | 101 ms: 1.01x faster                                                     |
| json_loads           | 25.0 us                                                          | 24.9 us: 1.01x faster                                                    |
| xml_etree_process    | 59.7 ms                                                          | 59.5 ms: 1.00x faster                                                    |
| json_dumps           | 10.8 ms                                                          | 11.0 ms: 1.02x slower                                                    |
| pickle_pure_python   | 307 us                                                           | 318 us: 1.04x slower                                                     |
| tomli_loads          | 2.40 sec                                                         | 2.58 sec: 1.07x slower                                                   |
| Geometric mean       | (ref)                                                            | 1.01x slower                                                             |

Benchmark hidden because not significant (2): xml_etree_generate, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-pythonperf2-x86_64-mdboom-initialize_locals-3.14.0a0-1021191 |
|------------------------|:----------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 13.4 ms: 1.02x slower                                                    |
| python_startup_no_site | 8.85 ms                                                          | 9.09 ms: 1.03x slower                                                    |
| Geometric mean         | (ref)                                                            | 1.02x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-pythonperf2-x86_64-mdboom-initialize_locals-3.14.0a0-1021191 |
|-----------------|:----------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml      | 58.1 ms                                                          | 53.6 ms: 1.08x faster                                                    |
| genshi_text     | 25.9 ms                                                          | 24.9 ms: 1.04x faster                                                    |
| django_template | 39.0 ms                                                          | 41.2 ms: 1.06x slower                                                    |
| Geometric mean  | (ref)                                                            | 1.02x faster                                                             |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-pythonperf2-x86_64-mdboom-initialize_locals-3.14.0a0-1021191 |
|----------------------------|:----------------------------------------------------------------:|:------------------------------------------------------------------------:|
| deepcopy                   | 377 us                                                           | 287 us: 1.31x faster                                                     |
| deepcopy_memo              | 37.3 us                                                          | 29.9 us: 1.24x faster                                                    |
| go                         | 165 ms                                                           | 137 ms: 1.21x faster                                                     |
| deepcopy_reduce            | 3.39 us                                                          | 2.91 us: 1.16x faster                                                    |
| generators                 | 33.5 ms                                                          | 29.1 ms: 1.15x faster                                                    |
| async_tree_memoization     | 460 ms                                                           | 402 ms: 1.14x faster                                                     |
| async_tree_io_tg           | 900 ms                                                           | 792 ms: 1.14x faster                                                     |
| async_tree_none            | 365 ms                                                           | 323 ms: 1.13x faster                                                     |
| async_tree_none_tg         | 340 ms                                                           | 311 ms: 1.09x faster                                                     |
| bench_mp_pool              | 4.91 ms                                                          | 4.53 ms: 1.08x faster                                                    |
| genshi_xml                 | 58.1 ms                                                          | 53.6 ms: 1.08x faster                                                    |
| async_tree_io              | 873 ms                                                           | 806 ms: 1.08x faster                                                     |
| richards_super             | 61.2 ms                                                          | 56.5 ms: 1.08x faster                                                    |
| pathlib                    | 17.1 ms                                                          | 15.9 ms: 1.08x faster                                                    |
| async_tree_memoization_tg  | 421 ms                                                           | 392 ms: 1.07x faster                                                     |
| richards                   | 53.4 ms                                                          | 50.0 ms: 1.07x faster                                                    |
| regex_dna                  | 249 ms                                                           | 235 ms: 1.06x faster                                                     |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 575 ms: 1.05x faster                                                     |
| html5lib                   | 74.7 ms                                                          | 71.2 ms: 1.05x faster                                                    |
| logging_format             | 7.11 us                                                          | 6.78 us: 1.05x faster                                                    |
| bench_thread_pool          | 908 us                                                           | 866 us: 1.05x faster                                                     |
| gc_traversal               | 4.69 ms                                                          | 4.47 ms: 1.05x faster                                                    |
| bpe_tokeniser              | 5.14 sec                                                         | 4.91 sec: 1.05x faster                                                   |
| coverage                   | 83.5 ms                                                          | 80.1 ms: 1.04x faster                                                    |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 551 ms: 1.04x faster                                                     |
| genshi_text                | 25.9 ms                                                          | 24.9 ms: 1.04x faster                                                    |
| nbody                      | 87.8 ms                                                          | 84.8 ms: 1.04x faster                                                    |
| 2to3                       | 291 ms                                                           | 284 ms: 1.03x faster                                                     |
| pprint_safe_repr           | 818 ms                                                           | 795 ms: 1.03x faster                                                     |
| pyflate                    | 482 ms                                                           | 469 ms: 1.03x faster                                                     |
| coroutines                 | 22.0 ms                                                          | 21.4 ms: 1.03x faster                                                    |
| unpickle_pure_python       | 224 us                                                           | 219 us: 1.03x faster                                                     |
| tornado_http               | 119 ms                                                           | 117 ms: 1.02x faster                                                     |
| hexiom                     | 6.35 ms                                                          | 6.20 ms: 1.02x faster                                                    |
| float                      | 80.2 ms                                                          | 78.4 ms: 1.02x faster                                                    |
| asyncio_tcp                | 378 ms                                                           | 369 ms: 1.02x faster                                                     |
| pprint_pformat             | 1.66 sec                                                         | 1.62 sec: 1.02x faster                                                   |
| logging_simple             | 6.40 us                                                          | 6.27 us: 1.02x faster                                                    |
| asyncio_websockets         | 395 ms                                                           | 387 ms: 1.02x faster                                                     |
| scimark_lu                 | 97.5 ms                                                          | 95.6 ms: 1.02x faster                                                    |
| docutils                   | 2.98 sec                                                         | 2.93 sec: 1.02x faster                                                   |
| regex_compile              | 144 ms                                                           | 142 ms: 1.02x faster                                                     |
| xml_etree_iterparse        | 103 ms                                                           | 101 ms: 1.01x faster                                                     |
| sympy_sum                  | 155 ms                                                           | 153 ms: 1.01x faster                                                     |
| json                       | 5.35 ms                                                          | 5.30 ms: 1.01x faster                                                    |
| meteor_contest             | 128 ms                                                           | 127 ms: 1.01x faster                                                     |
| thrift                     | 880 us                                                           | 872 us: 1.01x faster                                                     |
| spectral_norm              | 97.3 ms                                                          | 96.5 ms: 1.01x faster                                                    |
| json_loads                 | 25.0 us                                                          | 24.9 us: 1.01x faster                                                    |
| fannkuch                   | 353 ms                                                           | 351 ms: 1.01x faster                                                     |
| xml_etree_process          | 59.7 ms                                                          | 59.5 ms: 1.00x faster                                                    |
| sqlglot_optimize           | 59.5 ms                                                          | 59.7 ms: 1.00x slower                                                    |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 4.30 ms: 1.00x slower                                                    |
| crypto_pyaes               | 73.6 ms                                                          | 73.9 ms: 1.00x slower                                                    |
| sympy_expand               | 501 ms                                                           | 506 ms: 1.01x slower                                                     |
| deltablue                  | 3.37 ms                                                          | 3.42 ms: 1.01x slower                                                    |
| python_startup             | 13.2 ms                                                          | 13.4 ms: 1.02x slower                                                    |
| nqueens                    | 88.4 ms                                                          | 89.9 ms: 1.02x slower                                                    |
| json_dumps                 | 10.8 ms                                                          | 11.0 ms: 1.02x slower                                                    |
| scimark_monte_carlo        | 65.5 ms                                                          | 66.7 ms: 1.02x slower                                                    |
| async_generators           | 363 ms                                                           | 371 ms: 1.02x slower                                                     |
| typing_runtime_protocols   | 171 us                                                           | 175 us: 1.02x slower                                                     |
| pycparser                  | 1.22 sec                                                         | 1.25 sec: 1.03x slower                                                   |
| python_startup_no_site     | 8.85 ms                                                          | 9.09 ms: 1.03x slower                                                    |
| mdp                        | 2.46 sec                                                         | 2.53 sec: 1.03x slower                                                   |
| regex_effbot               | 3.40 ms                                                          | 3.50 ms: 1.03x slower                                                    |
| sqlglot_parse              | 1.39 ms                                                          | 1.44 ms: 1.03x slower                                                    |
| sqlglot_transpile          | 1.76 ms                                                          | 1.83 ms: 1.03x slower                                                    |
| pickle_pure_python         | 307 us                                                           | 318 us: 1.04x slower                                                     |
| regex_v8                   | 26.0 ms                                                          | 26.9 ms: 1.04x slower                                                    |
| comprehensions             | 17.0 us                                                          | 17.6 us: 1.04x slower                                                    |
| chaos                      | 59.6 ms                                                          | 61.8 ms: 1.04x slower                                                    |
| logging_silent             | 96.3 ns                                                          | 101 ns: 1.05x slower                                                     |
| django_template            | 39.0 ms                                                          | 41.2 ms: 1.06x slower                                                    |
| tomli_loads                | 2.40 sec                                                         | 2.58 sec: 1.07x slower                                                   |
| raytrace                   | 260 ms                                                           | 285 ms: 1.09x slower                                                     |
| Geometric mean             | (ref)                                                            | 1.02x faster                                                             |

Benchmark hidden because not significant (13): create_gc_cycles, telco, mako, pidigits, asyncio_tcp_ssl, sympy_integrate, sqlglot_normalize, xml_etree_generate, sympy_str, scimark_sor, scimark_fft, xml_etree_parse, pylint
Ignored benchmarks (13) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.94% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x