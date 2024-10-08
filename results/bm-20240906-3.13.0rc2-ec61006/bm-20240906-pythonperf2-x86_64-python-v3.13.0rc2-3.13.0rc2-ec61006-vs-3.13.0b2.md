# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0rc2
- machine: linux-x86_64
- commit hash: ec61006
- commit date: 2024-09-06
- overall geometric mean: 1.00x slower
- HPT reliability: 99.88%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-pythonperf2-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:----------------------------------------------------------------:|:------------------------------------------------------------------:|
| chameleon      | 7.40 ms                                                          | 7.37 ms: 1.00x faster                                              |
| docutils       | 2.98 sec                                                         | 3.00 sec: 1.01x slower                                             |
| Geometric mean | (ref)                                                            | 1.00x faster                                                       |

Benchmark hidden because not significant (3): 2to3, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-pythonperf2-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|---------------------------|:----------------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_io_tg          | 900 ms                                                           | 913 ms: 1.01x slower                                               |
| async_tree_cpu_io_mixed   | 604 ms                                                           | 615 ms: 1.02x slower                                               |
| async_tree_memoization_tg | 421 ms                                                           | 434 ms: 1.03x slower                                               |
| Geometric mean            | (ref)                                                            | 1.02x slower                                                       |

Benchmark hidden because not significant (5): async_tree_io, async_tree_none, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-pythonperf2-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:----------------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 80.2 ms                                                          | 80.5 ms: 1.00x slower                                              |
| nbody          | 87.8 ms                                                          | 91.6 ms: 1.04x slower                                              |
| Geometric mean | (ref)                                                            | 1.02x slower                                                       |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-pythonperf2-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:----------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_v8       | 26.0 ms                                                          | 25.4 ms: 1.02x faster                                              |
| regex_dna      | 249 ms                                                           | 248 ms: 1.01x faster                                               |
| regex_compile  | 144 ms                                                           | 143 ms: 1.01x faster                                               |
| regex_effbot   | 3.40 ms                                                          | 3.74 ms: 1.10x slower                                              |
| Geometric mean | (ref)                                                            | 1.02x slower                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-pythonperf2-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------------|:----------------------------------------------------------------:|:------------------------------------------------------------------:|
| json_loads           | 25.0 us                                                          | 23.8 us: 1.05x faster                                              |
| unpickle             | 15.7 us                                                          | 15.0 us: 1.04x faster                                              |
| pickle_dict          | 32.8 us                                                          | 31.7 us: 1.04x faster                                              |
| unpickle_list        | 4.70 us                                                          | 4.56 us: 1.03x faster                                              |
| pickle               | 10.6 us                                                          | 10.5 us: 1.01x faster                                              |
| tomli_loads          | 2.40 sec                                                         | 2.42 sec: 1.01x slower                                             |
| pickle_pure_python   | 307 us                                                           | 311 us: 1.01x slower                                               |
| xml_etree_generate   | 85.7 ms                                                          | 87.4 ms: 1.02x slower                                              |
| xml_etree_process    | 59.7 ms                                                          | 60.9 ms: 1.02x slower                                              |
| unpickle_pure_python | 224 us                                                           | 229 us: 1.02x slower                                               |
| pickle_list          | 4.44 us                                                          | 4.59 us: 1.03x slower                                              |
| json_dumps           | 10.8 ms                                                          | 11.2 ms: 1.04x slower                                              |
| Geometric mean       | (ref)                                                            | 1.00x faster                                                       |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-pythonperf2-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|------------------------|:----------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 8.85 ms                                                          | 8.93 ms: 1.01x slower                                              |
| python_startup         | 13.2 ms                                                          | 13.3 ms: 1.01x slower                                              |
| Geometric mean         | (ref)                                                            | 1.01x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-pythonperf2-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|-----------------|:----------------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_xml      | 58.1 ms                                                          | 57.2 ms: 1.02x faster                                              |
| django_template | 39.0 ms                                                          | 39.3 ms: 1.01x slower                                              |
| genshi_text     | 25.9 ms                                                          | 26.4 ms: 1.02x slower                                              |
| Geometric mean  | (ref)                                                            | 1.00x slower                                                       |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-pythonperf2-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|---------------------------|:----------------------------------------------------------------:|:------------------------------------------------------------------:|
| bench_mp_pool             | 4.91 ms                                                          | 4.61 ms: 1.07x faster                                              |
| json_loads                | 25.0 us                                                          | 23.8 us: 1.05x faster                                              |
| unpickle                  | 15.7 us                                                          | 15.0 us: 1.04x faster                                              |
| gc_traversal              | 4.69 ms                                                          | 4.49 ms: 1.04x faster                                              |
| richards_super            | 61.2 ms                                                          | 58.8 ms: 1.04x faster                                              |
| coverage                  | 83.5 ms                                                          | 80.4 ms: 1.04x faster                                              |
| pickle_dict               | 32.8 us                                                          | 31.7 us: 1.04x faster                                              |
| dulwich_log               | 67.3 ms                                                          | 65.1 ms: 1.03x faster                                              |
| scimark_fft               | 312 ms                                                           | 302 ms: 1.03x faster                                               |
| json                      | 5.35 ms                                                          | 5.19 ms: 1.03x faster                                              |
| unpickle_list             | 4.70 us                                                          | 4.56 us: 1.03x faster                                              |
| richards                  | 53.4 ms                                                          | 52.0 ms: 1.03x faster                                              |
| logging_simple            | 6.40 us                                                          | 6.25 us: 1.02x faster                                              |
| regex_v8                  | 26.0 ms                                                          | 25.4 ms: 1.02x faster                                              |
| logging_format            | 7.11 us                                                          | 6.97 us: 1.02x faster                                              |
| crypto_pyaes              | 73.6 ms                                                          | 72.4 ms: 1.02x faster                                              |
| asyncio_tcp               | 378 ms                                                           | 372 ms: 1.02x faster                                               |
| genshi_xml                | 58.1 ms                                                          | 57.2 ms: 1.02x faster                                              |
| asyncio_websockets        | 395 ms                                                           | 390 ms: 1.01x faster                                               |
| scimark_sor               | 119 ms                                                           | 118 ms: 1.01x faster                                               |
| pickle                    | 10.6 us                                                          | 10.5 us: 1.01x faster                                              |
| regex_dna                 | 249 ms                                                           | 248 ms: 1.01x faster                                               |
| scimark_lu                | 97.5 ms                                                          | 96.9 ms: 1.01x faster                                              |
| regex_compile             | 144 ms                                                           | 143 ms: 1.01x faster                                               |
| hexiom                    | 6.35 ms                                                          | 6.32 ms: 1.00x faster                                              |
| chameleon                 | 7.40 ms                                                          | 7.37 ms: 1.00x faster                                              |
| bpe_tokeniser             | 5.14 sec                                                         | 5.13 sec: 1.00x faster                                             |
| float                     | 80.2 ms                                                          | 80.5 ms: 1.00x slower                                              |
| pathlib                   | 17.1 ms                                                          | 17.2 ms: 1.00x slower                                              |
| spectral_norm             | 97.3 ms                                                          | 97.8 ms: 1.00x slower                                              |
| pprint_safe_repr          | 818 ms                                                           | 823 ms: 1.01x slower                                               |
| logging_silent            | 96.3 ns                                                          | 96.9 ns: 1.01x slower                                              |
| docutils                  | 2.98 sec                                                         | 3.00 sec: 1.01x slower                                             |
| chaos                     | 59.6 ms                                                          | 60.1 ms: 1.01x slower                                              |
| tomli_loads               | 2.40 sec                                                         | 2.42 sec: 1.01x slower                                             |
| meteor_contest            | 128 ms                                                           | 129 ms: 1.01x slower                                               |
| sqlglot_optimize          | 59.5 ms                                                          | 60.1 ms: 1.01x slower                                              |
| django_template           | 39.0 ms                                                          | 39.3 ms: 1.01x slower                                              |
| python_startup_no_site    | 8.85 ms                                                          | 8.93 ms: 1.01x slower                                              |
| pycparser                 | 1.22 sec                                                         | 1.23 sec: 1.01x slower                                             |
| python_startup            | 13.2 ms                                                          | 13.3 ms: 1.01x slower                                              |
| comprehensions            | 17.0 us                                                          | 17.1 us: 1.01x slower                                              |
| deepcopy                  | 377 us                                                           | 381 us: 1.01x slower                                               |
| scimark_monte_carlo       | 65.5 ms                                                          | 66.2 ms: 1.01x slower                                              |
| pickle_pure_python        | 307 us                                                           | 311 us: 1.01x slower                                               |
| pprint_pformat            | 1.66 sec                                                         | 1.68 sec: 1.01x slower                                             |
| deepcopy_memo             | 37.3 us                                                          | 37.7 us: 1.01x slower                                              |
| coroutines                | 22.0 ms                                                          | 22.3 ms: 1.01x slower                                              |
| sympy_integrate           | 23.2 ms                                                          | 23.5 ms: 1.01x slower                                              |
| dask                      | 391 ms                                                           | 396 ms: 1.01x slower                                               |
| generators                | 33.5 ms                                                          | 34.0 ms: 1.01x slower                                              |
| sqlglot_transpile         | 1.76 ms                                                          | 1.79 ms: 1.01x slower                                              |
| async_tree_io_tg          | 900 ms                                                           | 913 ms: 1.01x slower                                               |
| sympy_str                 | 295 ms                                                           | 299 ms: 1.02x slower                                               |
| async_generators          | 363 ms                                                           | 368 ms: 1.02x slower                                               |
| deepcopy_reduce           | 3.39 us                                                          | 3.44 us: 1.02x slower                                              |
| sqlglot_normalize         | 120 ms                                                           | 122 ms: 1.02x slower                                               |
| sympy_expand              | 501 ms                                                           | 509 ms: 1.02x slower                                               |
| sqlglot_parse             | 1.39 ms                                                          | 1.41 ms: 1.02x slower                                              |
| sqlite_synth              | 2.80 us                                                          | 2.84 us: 1.02x slower                                              |
| genshi_text               | 25.9 ms                                                          | 26.4 ms: 1.02x slower                                              |
| async_tree_cpu_io_mixed   | 604 ms                                                           | 615 ms: 1.02x slower                                               |
| xml_etree_generate        | 85.7 ms                                                          | 87.4 ms: 1.02x slower                                              |
| xml_etree_process         | 59.7 ms                                                          | 60.9 ms: 1.02x slower                                              |
| unpickle_pure_python      | 224 us                                                           | 229 us: 1.02x slower                                               |
| aiohttp                   | 1.07 ms                                                          | 1.10 ms: 1.02x slower                                              |
| telco                     | 8.40 ms                                                          | 8.65 ms: 1.03x slower                                              |
| nqueens                   | 88.4 ms                                                          | 91.1 ms: 1.03x slower                                              |
| async_tree_memoization_tg | 421 ms                                                           | 434 ms: 1.03x slower                                               |
| pickle_list               | 4.44 us                                                          | 4.59 us: 1.03x slower                                              |
| mdp                       | 2.46 sec                                                         | 2.55 sec: 1.04x slower                                             |
| typing_runtime_protocols  | 171 us                                                           | 177 us: 1.04x slower                                               |
| json_dumps                | 10.8 ms                                                          | 11.2 ms: 1.04x slower                                              |
| nbody                     | 87.8 ms                                                          | 91.6 ms: 1.04x slower                                              |
| fannkuch                  | 353 ms                                                           | 369 ms: 1.05x slower                                               |
| regex_effbot              | 3.40 ms                                                          | 3.74 ms: 1.10x slower                                              |
| Geometric mean            | (ref)                                                            | 1.00x slower                                                       |

Benchmark hidden because not significant (26): bench_thread_pool, gunicorn, tornado_http, mako, pyflate, asyncio_tcp_ssl, raytrace, create_gc_cycles, html5lib, 2to3, sympy_sum, xml_etree_iterparse, scimark_sparse_mat_mult, pidigits, go, thrift, deltablue, xml_etree_parse, mypy2, async_tree_io, flaskblogging, async_tree_none, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_none_tg, pylint
Ignored benchmarks (1) of results/bm-20240906-3.13.0rc2-ec61006/bm-20240906-pythonperf2-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006.json: unpack_sequence

# HPT report

- Reliability score: 99.88% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x