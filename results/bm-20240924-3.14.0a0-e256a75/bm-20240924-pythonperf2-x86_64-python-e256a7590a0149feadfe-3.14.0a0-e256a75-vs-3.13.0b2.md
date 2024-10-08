# Results vs. 3.13.0b2

- fork: python
- ref: e256a7590a0149feadfe
- machine: linux-x86_64
- commit hash: e256a75
- commit date: 2024-09-24
- overall geometric mean: 1.03x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-pythonperf2-x86_64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 284 ms: 1.03x faster                                                        |
| docutils       | 2.98 sec                                                         | 2.90 sec: 1.03x faster                                                      |
| html5lib       | 74.7 ms                                                          | 71.4 ms: 1.04x faster                                                       |
| tornado_http   | 119 ms                                                           | 116 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                            | 1.03x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-pythonperf2-x86_64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization     | 460 ms                                                           | 399 ms: 1.15x faster                                                        |
| async_tree_io_tg           | 900 ms                                                           | 785 ms: 1.15x faster                                                        |
| async_tree_none            | 365 ms                                                           | 322 ms: 1.13x faster                                                        |
| async_tree_none_tg         | 340 ms                                                           | 309 ms: 1.10x faster                                                        |
| async_tree_memoization_tg  | 421 ms                                                           | 389 ms: 1.08x faster                                                        |
| async_tree_io              | 873 ms                                                           | 809 ms: 1.08x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 572 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 561 ms: 1.02x faster                                                        |
| Geometric mean             | (ref)                                                            | 1.10x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-pythonperf2-x86_64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 80.2 ms                                                          | 79.6 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                            | 1.00x slower                                                                |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-pythonperf2-x86_64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                           | 139 ms: 1.04x faster                                                        |
| regex_v8       | 26.0 ms                                                          | 25.5 ms: 1.02x faster                                                       |
| regex_dna      | 249 ms                                                           | 248 ms: 1.00x faster                                                        |
| regex_effbot   | 3.40 ms                                                          | 3.58 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                            | 1.00x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-pythonperf2-x86_64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_dict          | 32.8 us                                                          | 30.0 us: 1.10x faster                                                       |
| unpickle_pure_python | 224 us                                                           | 213 us: 1.05x faster                                                        |
| pickle               | 10.6 us                                                          | 10.2 us: 1.05x faster                                                       |
| unpickle             | 15.7 us                                                          | 15.1 us: 1.04x faster                                                       |
| pickle_list          | 4.44 us                                                          | 4.30 us: 1.03x faster                                                       |
| unpickle_list        | 4.70 us                                                          | 4.57 us: 1.03x faster                                                       |
| xml_etree_parse      | 144 ms                                                           | 142 ms: 1.01x faster                                                        |
| xml_etree_generate   | 85.7 ms                                                          | 84.8 ms: 1.01x faster                                                       |
| json_loads           | 25.0 us                                                          | 25.1 us: 1.00x slower                                                       |
| json_dumps           | 10.8 ms                                                          | 10.8 ms: 1.00x slower                                                       |
| pickle_pure_python   | 307 us                                                           | 321 us: 1.05x slower                                                        |
| tomli_loads          | 2.40 sec                                                         | 2.64 sec: 1.10x slower                                                      |
| Geometric mean       | (ref)                                                            | 1.01x faster                                                                |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-pythonperf2-x86_64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.85 ms                                                          | 8.95 ms: 1.01x slower                                                       |
| python_startup         | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                            | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-pythonperf2-x86_64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|-----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 58.1 ms                                                          | 54.4 ms: 1.07x faster                                                       |
| genshi_text     | 25.9 ms                                                          | 24.6 ms: 1.05x faster                                                       |
| django_template | 39.0 ms                                                          | 40.8 ms: 1.05x slower                                                       |
| Geometric mean  | (ref)                                                            | 1.02x faster                                                                |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-pythonperf2-x86_64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy                   | 377 us                                                           | 286 us: 1.32x faster                                                        |
| deepcopy_memo              | 37.3 us                                                          | 30.0 us: 1.24x faster                                                       |
| go                         | 165 ms                                                           | 138 ms: 1.19x faster                                                        |
| deepcopy_reduce            | 3.39 us                                                          | 2.89 us: 1.17x faster                                                       |
| async_tree_memoization     | 460 ms                                                           | 399 ms: 1.15x faster                                                        |
| async_tree_io_tg           | 900 ms                                                           | 785 ms: 1.15x faster                                                        |
| async_tree_none            | 365 ms                                                           | 322 ms: 1.13x faster                                                        |
| generators                 | 33.5 ms                                                          | 29.7 ms: 1.13x faster                                                       |
| async_tree_none_tg         | 340 ms                                                           | 309 ms: 1.10x faster                                                        |
| pickle_dict                | 32.8 us                                                          | 30.0 us: 1.10x faster                                                       |
| richards_super             | 61.2 ms                                                          | 56.0 ms: 1.09x faster                                                       |
| pathlib                    | 17.1 ms                                                          | 15.7 ms: 1.09x faster                                                       |
| async_tree_memoization_tg  | 421 ms                                                           | 389 ms: 1.08x faster                                                        |
| async_tree_io              | 873 ms                                                           | 809 ms: 1.08x faster                                                        |
| richards                   | 53.4 ms                                                          | 49.7 ms: 1.08x faster                                                       |
| genshi_xml                 | 58.1 ms                                                          | 54.4 ms: 1.07x faster                                                       |
| bench_mp_pool              | 4.91 ms                                                          | 4.62 ms: 1.06x faster                                                       |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 572 ms: 1.06x faster                                                        |
| unpickle_pure_python       | 224 us                                                           | 213 us: 1.05x faster                                                        |
| genshi_text                | 25.9 ms                                                          | 24.6 ms: 1.05x faster                                                       |
| bench_thread_pool          | 908 us                                                           | 865 us: 1.05x faster                                                        |
| bpe_tokeniser              | 5.14 sec                                                         | 4.89 sec: 1.05x faster                                                      |
| scimark_fft                | 312 ms                                                           | 298 ms: 1.05x faster                                                        |
| pickle                     | 10.6 us                                                          | 10.2 us: 1.05x faster                                                       |
| html5lib                   | 74.7 ms                                                          | 71.4 ms: 1.04x faster                                                       |
| unpickle                   | 15.7 us                                                          | 15.1 us: 1.04x faster                                                       |
| regex_compile              | 144 ms                                                           | 139 ms: 1.04x faster                                                        |
| pickle_list                | 4.44 us                                                          | 4.30 us: 1.03x faster                                                       |
| tornado_http               | 119 ms                                                           | 116 ms: 1.03x faster                                                        |
| docutils                   | 2.98 sec                                                         | 2.90 sec: 1.03x faster                                                      |
| sqlglot_normalize          | 120 ms                                                           | 117 ms: 1.03x faster                                                        |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 4.16 ms: 1.03x faster                                                       |
| scimark_sor                | 119 ms                                                           | 115 ms: 1.03x faster                                                        |
| unpickle_list              | 4.70 us                                                          | 4.57 us: 1.03x faster                                                       |
| 2to3                       | 291 ms                                                           | 284 ms: 1.03x faster                                                        |
| sqlite_synth               | 2.80 us                                                          | 2.73 us: 1.02x faster                                                       |
| crypto_pyaes               | 73.6 ms                                                          | 71.9 ms: 1.02x faster                                                       |
| asyncio_tcp                | 378 ms                                                           | 369 ms: 1.02x faster                                                        |
| sqlglot_optimize           | 59.5 ms                                                          | 58.3 ms: 1.02x faster                                                       |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 561 ms: 1.02x faster                                                        |
| thrift                     | 880 us                                                           | 863 us: 1.02x faster                                                        |
| regex_v8                   | 26.0 ms                                                          | 25.5 ms: 1.02x faster                                                       |
| sympy_sum                  | 155 ms                                                           | 152 ms: 1.02x faster                                                        |
| pprint_safe_repr           | 818 ms                                                           | 803 ms: 1.02x faster                                                        |
| json                       | 5.35 ms                                                          | 5.26 ms: 1.02x faster                                                       |
| coroutines                 | 22.0 ms                                                          | 21.6 ms: 1.02x faster                                                       |
| asyncio_websockets         | 395 ms                                                           | 389 ms: 1.02x faster                                                        |
| scimark_lu                 | 97.5 ms                                                          | 96.0 ms: 1.02x faster                                                       |
| pprint_pformat             | 1.66 sec                                                         | 1.64 sec: 1.01x faster                                                      |
| sympy_integrate            | 23.2 ms                                                          | 22.8 ms: 1.01x faster                                                       |
| sympy_str                  | 295 ms                                                           | 290 ms: 1.01x faster                                                        |
| async_generators           | 363 ms                                                           | 358 ms: 1.01x faster                                                        |
| xml_etree_parse            | 144 ms                                                           | 142 ms: 1.01x faster                                                        |
| xml_etree_generate         | 85.7 ms                                                          | 84.8 ms: 1.01x faster                                                       |
| coverage                   | 83.5 ms                                                          | 82.6 ms: 1.01x faster                                                       |
| spectral_norm              | 97.3 ms                                                          | 96.4 ms: 1.01x faster                                                       |
| nqueens                    | 88.4 ms                                                          | 87.6 ms: 1.01x faster                                                       |
| float                      | 80.2 ms                                                          | 79.6 ms: 1.01x faster                                                       |
| dulwich_log                | 67.3 ms                                                          | 66.9 ms: 1.01x faster                                                       |
| sympy_expand               | 501 ms                                                           | 498 ms: 1.01x faster                                                        |
| asyncio_tcp_ssl            | 1.58 sec                                                         | 1.57 sec: 1.00x faster                                                      |
| regex_dna                  | 249 ms                                                           | 248 ms: 1.00x faster                                                        |
| hexiom                     | 6.35 ms                                                          | 6.33 ms: 1.00x faster                                                       |
| meteor_contest             | 128 ms                                                           | 128 ms: 1.00x slower                                                        |
| json_loads                 | 25.0 us                                                          | 25.1 us: 1.00x slower                                                       |
| json_dumps                 | 10.8 ms                                                          | 10.8 ms: 1.00x slower                                                       |
| deltablue                  | 3.37 ms                                                          | 3.40 ms: 1.01x slower                                                       |
| scimark_monte_carlo        | 65.5 ms                                                          | 66.0 ms: 1.01x slower                                                       |
| typing_runtime_protocols   | 171 us                                                           | 172 us: 1.01x slower                                                        |
| pycparser                  | 1.22 sec                                                         | 1.23 sec: 1.01x slower                                                      |
| pyflate                    | 482 ms                                                           | 487 ms: 1.01x slower                                                        |
| mdp                        | 2.46 sec                                                         | 2.49 sec: 1.01x slower                                                      |
| python_startup_no_site     | 8.85 ms                                                          | 8.95 ms: 1.01x slower                                                       |
| python_startup             | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                                       |
| comprehensions             | 17.0 us                                                          | 17.2 us: 1.01x slower                                                       |
| logging_format             | 7.11 us                                                          | 7.21 us: 1.01x slower                                                       |
| logging_simple             | 6.40 us                                                          | 6.50 us: 1.01x slower                                                       |
| logging_silent             | 96.3 ns                                                          | 97.9 ns: 1.02x slower                                                       |
| gc_traversal               | 4.69 ms                                                          | 4.78 ms: 1.02x slower                                                       |
| fannkuch                   | 353 ms                                                           | 361 ms: 1.02x slower                                                        |
| sqlglot_transpile          | 1.76 ms                                                          | 1.81 ms: 1.03x slower                                                       |
| sqlglot_parse              | 1.39 ms                                                          | 1.43 ms: 1.03x slower                                                       |
| chaos                      | 59.6 ms                                                          | 62.0 ms: 1.04x slower                                                       |
| pickle_pure_python         | 307 us                                                           | 321 us: 1.05x slower                                                        |
| django_template            | 39.0 ms                                                          | 40.8 ms: 1.05x slower                                                       |
| regex_effbot               | 3.40 ms                                                          | 3.58 ms: 1.05x slower                                                       |
| raytrace                   | 260 ms                                                           | 283 ms: 1.09x slower                                                        |
| tomli_loads                | 2.40 sec                                                         | 2.64 sec: 1.10x slower                                                      |
| Geometric mean             | (ref)                                                            | 1.03x faster                                                                |

Benchmark hidden because not significant (8): telco, pidigits, mako, xml_etree_iterparse, create_gc_cycles, xml_etree_process, nbody, pylint
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240924-3.14.0a0-e256a75/bm-20240924-pythonperf2-x86_64-python-e256a7590a0149feadfe-3.14.0a0-e256a75.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x