# Results vs. 3.13.0b2

- fork: mdboom
- ref: simplify_richcompare
- machine: linux-x86_64
- commit hash: 15b187e
- commit date: 2024-08-29
- overall geometric mean: 1.03x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 282 ms: 1.03x faster                                                        |
| docutils       | 2.98 sec                                                         | 2.91 sec: 1.03x faster                                                      |
| html5lib       | 74.7 ms                                                          | 70.0 ms: 1.07x faster                                                       |
| tornado_http   | 119 ms                                                           | 116 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                            | 1.04x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization     | 460 ms                                                           | 395 ms: 1.16x faster                                                        |
| async_tree_none            | 365 ms                                                           | 317 ms: 1.15x faster                                                        |
| async_tree_io_tg           | 900 ms                                                           | 783 ms: 1.15x faster                                                        |
| async_tree_none_tg         | 340 ms                                                           | 307 ms: 1.11x faster                                                        |
| async_tree_memoization_tg  | 421 ms                                                           | 385 ms: 1.09x faster                                                        |
| async_tree_io              | 873 ms                                                           | 816 ms: 1.07x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 569 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 543 ms: 1.06x faster                                                        |
| Geometric mean             | (ref)                                                            | 1.11x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 87.8 ms                                                          | 86.4 ms: 1.02x faster                                                       |
| pidigits       | 254 ms                                                           | 255 ms: 1.00x slower                                                        |
| Geometric mean | (ref)                                                            | 1.00x faster                                                                |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 249 ms                                                           | 238 ms: 1.05x faster                                                        |
| regex_compile  | 144 ms                                                           | 141 ms: 1.02x faster                                                        |
| regex_effbot   | 3.40 ms                                                          | 3.46 ms: 1.02x slower                                                       |
| regex_v8       | 26.0 ms                                                          | 26.9 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                            | 1.01x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 224 us                                                           | 214 us: 1.05x faster                                                        |
| xml_etree_iterparse  | 103 ms                                                           | 101 ms: 1.02x faster                                                        |
| xml_etree_generate   | 85.7 ms                                                          | 85.1 ms: 1.01x faster                                                       |
| json_loads           | 25.0 us                                                          | 25.2 us: 1.00x slower                                                       |
| json_dumps           | 10.8 ms                                                          | 10.9 ms: 1.01x slower                                                       |
| pickle_pure_python   | 307 us                                                           | 312 us: 1.01x slower                                                        |
| xml_etree_parse      | 144 ms                                                           | 147 ms: 1.02x slower                                                        |
| tomli_loads          | 2.40 sec                                                         | 2.55 sec: 1.06x slower                                                      |
| Geometric mean       | (ref)                                                            | 1.00x slower                                                                |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 13.4 ms: 1.02x slower                                                       |
| python_startup_no_site | 8.85 ms                                                          | 9.09 ms: 1.03x slower                                                       |
| Geometric mean         | (ref)                                                            | 1.02x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|-----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 58.1 ms                                                          | 55.5 ms: 1.05x faster                                                       |
| mako            | 10.4 ms                                                          | 10.5 ms: 1.01x slower                                                       |
| django_template | 39.0 ms                                                          | 39.6 ms: 1.02x slower                                                       |
| Geometric mean  | (ref)                                                            | 1.00x faster                                                                |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy                   | 377 us                                                           | 280 us: 1.35x faster                                                        |
| deepcopy_memo              | 37.3 us                                                          | 29.0 us: 1.29x faster                                                       |
| go                         | 165 ms                                                           | 135 ms: 1.22x faster                                                        |
| deepcopy_reduce            | 3.39 us                                                          | 2.88 us: 1.18x faster                                                       |
| generators                 | 33.5 ms                                                          | 28.6 ms: 1.17x faster                                                       |
| async_tree_memoization     | 460 ms                                                           | 395 ms: 1.16x faster                                                        |
| async_tree_none            | 365 ms                                                           | 317 ms: 1.15x faster                                                        |
| async_tree_io_tg           | 900 ms                                                           | 783 ms: 1.15x faster                                                        |
| bench_mp_pool              | 4.91 ms                                                          | 4.37 ms: 1.12x faster                                                       |
| async_tree_none_tg         | 340 ms                                                           | 307 ms: 1.11x faster                                                        |
| async_tree_memoization_tg  | 421 ms                                                           | 385 ms: 1.09x faster                                                        |
| richards_super             | 61.2 ms                                                          | 56.3 ms: 1.09x faster                                                       |
| pathlib                    | 17.1 ms                                                          | 15.8 ms: 1.08x faster                                                       |
| async_tree_io              | 873 ms                                                           | 816 ms: 1.07x faster                                                        |
| html5lib                   | 74.7 ms                                                          | 70.0 ms: 1.07x faster                                                       |
| logging_format             | 7.11 us                                                          | 6.68 us: 1.06x faster                                                       |
| bench_thread_pool          | 908 us                                                           | 853 us: 1.06x faster                                                        |
| richards                   | 53.4 ms                                                          | 50.2 ms: 1.06x faster                                                       |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 569 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 543 ms: 1.06x faster                                                        |
| gc_traversal               | 4.69 ms                                                          | 4.44 ms: 1.06x faster                                                       |
| bpe_tokeniser              | 5.14 sec                                                         | 4.88 sec: 1.05x faster                                                      |
| unpickle_pure_python       | 224 us                                                           | 214 us: 1.05x faster                                                        |
| regex_dna                  | 249 ms                                                           | 238 ms: 1.05x faster                                                        |
| genshi_xml                 | 58.1 ms                                                          | 55.5 ms: 1.05x faster                                                       |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 4.11 ms: 1.04x faster                                                       |
| 2to3                       | 291 ms                                                           | 282 ms: 1.03x faster                                                        |
| pprint_safe_repr           | 818 ms                                                           | 792 ms: 1.03x faster                                                        |
| asyncio_tcp                | 378 ms                                                           | 367 ms: 1.03x faster                                                        |
| scimark_fft                | 312 ms                                                           | 303 ms: 1.03x faster                                                        |
| tornado_http               | 119 ms                                                           | 116 ms: 1.03x faster                                                        |
| logging_simple             | 6.40 us                                                          | 6.23 us: 1.03x faster                                                       |
| docutils                   | 2.98 sec                                                         | 2.91 sec: 1.03x faster                                                      |
| sympy_sum                  | 155 ms                                                           | 151 ms: 1.02x faster                                                        |
| regex_compile              | 144 ms                                                           | 141 ms: 1.02x faster                                                        |
| coroutines                 | 22.0 ms                                                          | 21.5 ms: 1.02x faster                                                       |
| async_generators           | 363 ms                                                           | 355 ms: 1.02x faster                                                        |
| pprint_pformat             | 1.66 sec                                                         | 1.62 sec: 1.02x faster                                                      |
| scimark_lu                 | 97.5 ms                                                          | 95.4 ms: 1.02x faster                                                       |
| sqlglot_optimize           | 59.5 ms                                                          | 58.3 ms: 1.02x faster                                                       |
| spectral_norm              | 97.3 ms                                                          | 95.4 ms: 1.02x faster                                                       |
| pycparser                  | 1.22 sec                                                         | 1.20 sec: 1.02x faster                                                      |
| nbody                      | 87.8 ms                                                          | 86.4 ms: 1.02x faster                                                       |
| xml_etree_iterparse        | 103 ms                                                           | 101 ms: 1.02x faster                                                        |
| sympy_str                  | 295 ms                                                           | 290 ms: 1.02x faster                                                        |
| hexiom                     | 6.35 ms                                                          | 6.26 ms: 1.01x faster                                                       |
| asyncio_websockets         | 395 ms                                                           | 390 ms: 1.01x faster                                                        |
| sympy_integrate            | 23.2 ms                                                          | 22.9 ms: 1.01x faster                                                       |
| sqlglot_normalize          | 120 ms                                                           | 119 ms: 1.01x faster                                                        |
| json                       | 5.35 ms                                                          | 5.31 ms: 1.01x faster                                                       |
| meteor_contest             | 128 ms                                                           | 127 ms: 1.01x faster                                                        |
| xml_etree_generate         | 85.7 ms                                                          | 85.1 ms: 1.01x faster                                                       |
| thrift                     | 880 us                                                           | 874 us: 1.01x faster                                                        |
| sympy_expand               | 501 ms                                                           | 499 ms: 1.00x faster                                                        |
| crypto_pyaes               | 73.6 ms                                                          | 73.4 ms: 1.00x faster                                                       |
| pidigits                   | 254 ms                                                           | 255 ms: 1.00x slower                                                        |
| json_loads                 | 25.0 us                                                          | 25.2 us: 1.00x slower                                                       |
| scimark_monte_carlo        | 65.5 ms                                                          | 65.9 ms: 1.01x slower                                                       |
| json_dumps                 | 10.8 ms                                                          | 10.9 ms: 1.01x slower                                                       |
| typing_runtime_protocols   | 171 us                                                           | 172 us: 1.01x slower                                                        |
| sqlglot_transpile          | 1.76 ms                                                          | 1.78 ms: 1.01x slower                                                       |
| mako                       | 10.4 ms                                                          | 10.5 ms: 1.01x slower                                                       |
| deltablue                  | 3.37 ms                                                          | 3.41 ms: 1.01x slower                                                       |
| sqlglot_parse              | 1.39 ms                                                          | 1.41 ms: 1.01x slower                                                       |
| mdp                        | 2.46 sec                                                         | 2.49 sec: 1.01x slower                                                      |
| pickle_pure_python         | 307 us                                                           | 312 us: 1.01x slower                                                        |
| python_startup             | 13.2 ms                                                          | 13.4 ms: 1.02x slower                                                       |
| django_template            | 39.0 ms                                                          | 39.6 ms: 1.02x slower                                                       |
| regex_effbot               | 3.40 ms                                                          | 3.46 ms: 1.02x slower                                                       |
| coverage                   | 83.5 ms                                                          | 85.2 ms: 1.02x slower                                                       |
| comprehensions             | 17.0 us                                                          | 17.3 us: 1.02x slower                                                       |
| xml_etree_parse            | 144 ms                                                           | 147 ms: 1.02x slower                                                        |
| nqueens                    | 88.4 ms                                                          | 90.4 ms: 1.02x slower                                                       |
| fannkuch                   | 353 ms                                                           | 362 ms: 1.03x slower                                                        |
| python_startup_no_site     | 8.85 ms                                                          | 9.09 ms: 1.03x slower                                                       |
| pyflate                    | 482 ms                                                           | 497 ms: 1.03x slower                                                        |
| regex_v8                   | 26.0 ms                                                          | 26.9 ms: 1.03x slower                                                       |
| chaos                      | 59.6 ms                                                          | 61.8 ms: 1.04x slower                                                       |
| logging_silent             | 96.3 ns                                                          | 100 ns: 1.04x slower                                                        |
| raytrace                   | 260 ms                                                           | 273 ms: 1.05x slower                                                        |
| tomli_loads                | 2.40 sec                                                         | 2.55 sec: 1.06x slower                                                      |
| Geometric mean             | (ref)                                                            | 1.03x faster                                                                |

Benchmark hidden because not significant (8): telco, create_gc_cycles, xml_etree_process, asyncio_tcp_ssl, float, scimark_sor, genshi_text, pylint
Ignored benchmarks (13) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x