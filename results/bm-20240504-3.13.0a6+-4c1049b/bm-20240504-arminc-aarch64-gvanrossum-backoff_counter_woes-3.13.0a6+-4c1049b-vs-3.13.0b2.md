# Results vs. 3.13.0b2

- fork: gvanrossum
- ref: backoff_counter_woes
- machine: linux-aarch64
- commit hash: 4c1049b
- commit date: 2024-05-04
- overall geometric mean: 1.00x slower
- HPT reliability: 98.39%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240504-arminc-aarch64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| chameleon      | 8.95 ms                                                      | 9.33 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                 |

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240504-arminc-aarch64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.27 sec                                                     | 1.24 sec: 1.03x faster                                                       |
| async_tree_memoization_tg  | 604 ms                                                       | 589 ms: 1.03x faster                                                         |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 787 ms: 1.03x slower                                                         |
| Geometric mean             | (ref)                                                        | 1.01x faster                                                                 |

Benchmark hidden because not significant (5): async_tree_none_tg, async_tree_none, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240504-arminc-aarch64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 114 ms                                                       | 111 ms: 1.03x faster                                                         |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                 |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240504-arminc-aarch64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_dna      | 259 ms                                                       | 246 ms: 1.05x faster                                                         |
| regex_effbot   | 4.98 ms                                                      | 4.85 ms: 1.03x faster                                                        |
| regex_compile  | 128 ms                                                       | 129 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                 |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240504-arminc-aarch64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_process    | 80.8 ms                                                      | 79.8 ms: 1.01x faster                                                        |
| xml_etree_generate   | 114 ms                                                       | 113 ms: 1.01x faster                                                         |
| pickle_list          | 5.27 us                                                      | 5.31 us: 1.01x slower                                                        |
| json_dumps           | 13.1 ms                                                      | 13.2 ms: 1.01x slower                                                        |
| unpickle_pure_python | 251 us                                                       | 254 us: 1.01x slower                                                         |
| pickle               | 13.4 us                                                      | 13.5 us: 1.01x slower                                                        |
| json_loads           | 32.1 us                                                      | 32.6 us: 1.01x slower                                                        |
| tomli_loads          | 2.57 sec                                                     | 2.62 sec: 1.02x slower                                                       |
| xml_etree_iterparse  | 147 ms                                                       | 150 ms: 1.02x slower                                                         |
| unpickle_list        | 6.52 us                                                      | 6.67 us: 1.02x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                                 |

Benchmark hidden because not significant (4): pickle_pure_python, xml_etree_parse, pickle_dict, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240504-arminc-aarch64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                      | 12.5 ms: 1.04x faster                                                        |
| python_startup_no_site | 8.60 ms                                                      | 8.42 ms: 1.02x faster                                                        |
| Geometric mean         | (ref)                                                        | 1.03x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240504-arminc-aarch64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako           | 13.2 ms                                                      | 13.2 ms: 1.00x slower                                                        |
| genshi_text    | 27.4 ms                                                      | 27.7 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                 |

Benchmark hidden because not significant (2): django_template, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240504-arminc-aarch64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_dna                  | 259 ms                                                       | 246 ms: 1.05x faster                                                         |
| asyncio_tcp                | 584 ms                                                       | 562 ms: 1.04x faster                                                         |
| python_startup             | 13.0 ms                                                      | 12.5 ms: 1.04x faster                                                        |
| chaos                      | 68.3 ms                                                      | 66.2 ms: 1.03x faster                                                        |
| nbody                      | 114 ms                                                       | 111 ms: 1.03x faster                                                         |
| async_tree_io_tg           | 1.27 sec                                                     | 1.24 sec: 1.03x faster                                                       |
| regex_effbot               | 4.98 ms                                                      | 4.85 ms: 1.03x faster                                                        |
| async_tree_memoization_tg  | 604 ms                                                       | 589 ms: 1.03x faster                                                         |
| spectral_norm              | 141 ms                                                       | 138 ms: 1.03x faster                                                         |
| telco                      | 10.0 ms                                                      | 9.78 ms: 1.02x faster                                                        |
| python_startup_no_site     | 8.60 ms                                                      | 8.42 ms: 1.02x faster                                                        |
| thrift                     | 962 us                                                       | 945 us: 1.02x faster                                                         |
| gc_traversal               | 5.17 ms                                                      | 5.09 ms: 1.02x faster                                                        |
| scimark_lu                 | 141 ms                                                       | 139 ms: 1.01x faster                                                         |
| deepcopy_memo              | 50.8 us                                                      | 50.1 us: 1.01x faster                                                        |
| xml_etree_process          | 80.8 ms                                                      | 79.8 ms: 1.01x faster                                                        |
| scimark_monte_carlo        | 82.3 ms                                                      | 81.3 ms: 1.01x faster                                                        |
| go                         | 161 ms                                                       | 159 ms: 1.01x faster                                                         |
| raytrace                   | 297 ms                                                       | 295 ms: 1.01x faster                                                         |
| mdp                        | 3.33 sec                                                     | 3.31 sec: 1.01x faster                                                       |
| pprint_pformat             | 1.93 sec                                                     | 1.92 sec: 1.01x faster                                                       |
| xml_etree_generate         | 114 ms                                                       | 113 ms: 1.01x faster                                                         |
| mako                       | 13.2 ms                                                      | 13.2 ms: 1.00x slower                                                        |
| pprint_safe_repr           | 933 ms                                                       | 939 ms: 1.01x slower                                                         |
| pickle_list                | 5.27 us                                                      | 5.31 us: 1.01x slower                                                        |
| regex_compile              | 128 ms                                                       | 129 ms: 1.01x slower                                                         |
| genshi_text                | 27.4 ms                                                      | 27.7 ms: 1.01x slower                                                        |
| logging_silent             | 133 ns                                                       | 135 ns: 1.01x slower                                                         |
| json_dumps                 | 13.1 ms                                                      | 13.2 ms: 1.01x slower                                                        |
| unpickle_pure_python       | 251 us                                                       | 254 us: 1.01x slower                                                         |
| pickle                     | 13.4 us                                                      | 13.5 us: 1.01x slower                                                        |
| deepcopy_reduce            | 4.04 us                                                      | 4.08 us: 1.01x slower                                                        |
| sympy_integrate            | 20.9 ms                                                      | 21.1 ms: 1.01x slower                                                        |
| sqlglot_transpile          | 1.71 ms                                                      | 1.73 ms: 1.01x slower                                                        |
| logging_format             | 7.82 us                                                      | 7.93 us: 1.01x slower                                                        |
| sympy_str                  | 265 ms                                                       | 269 ms: 1.01x slower                                                         |
| json_loads                 | 32.1 us                                                      | 32.6 us: 1.01x slower                                                        |
| tomli_loads                | 2.57 sec                                                     | 2.62 sec: 1.02x slower                                                       |
| xml_etree_iterparse        | 147 ms                                                       | 150 ms: 1.02x slower                                                         |
| pathlib                    | 22.8 ms                                                      | 23.3 ms: 1.02x slower                                                        |
| unpickle_list              | 6.52 us                                                      | 6.67 us: 1.02x slower                                                        |
| flaskblogging              | 4.70 ms                                                      | 4.83 ms: 1.03x slower                                                        |
| fannkuch                   | 451 ms                                                       | 464 ms: 1.03x slower                                                         |
| coverage                   | 98.4 ms                                                      | 101 ms: 1.03x slower                                                         |
| coroutines                 | 29.0 ms                                                      | 29.8 ms: 1.03x slower                                                        |
| crypto_pyaes               | 82.0 ms                                                      | 84.3 ms: 1.03x slower                                                        |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 787 ms: 1.03x slower                                                         |
| gunicorn                   | 1.19 ms                                                      | 1.22 ms: 1.03x slower                                                        |
| json                       | 5.64 ms                                                      | 5.83 ms: 1.03x slower                                                        |
| generators                 | 37.1 ms                                                      | 38.4 ms: 1.03x slower                                                        |
| chameleon                  | 8.95 ms                                                      | 9.33 ms: 1.04x slower                                                        |
| typing_runtime_protocols   | 193 us                                                       | 202 us: 1.04x slower                                                         |
| create_gc_cycles           | 2.33 ms                                                      | 2.45 ms: 1.05x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.00x slower                                                                 |

Benchmark hidden because not significant (47): async_tree_none_tg, sqlglot_parse, sqlglot_normalize, deltablue, comprehensions, django_template, pickle_pure_python, async_generators, async_tree_none, sqlglot_optimize, async_tree_cpu_io_mixed, 2to3, scimark_fft, scimark_sparse_mat_mult, async_tree_io, pidigits, richards, html5lib, async_tree_memoization, meteor_contest, sympy_expand, xml_etree_parse, richards_super, regex_v8, pickle_dict, float, scimark_sor, pycparser, asyncio_tcp_ssl, unpickle, deepcopy, sqlite_synth, nqueens, docutils, asyncio_websockets, aiohttp, sympy_sum, pyflate, bench_thread_pool, bench_mp_pool, genshi_xml, tornado_http, hexiom, dask, dulwich_log, logging_simple, pylint
Ignored benchmarks (2) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: bpe_tokeniser, mypy2

# HPT report

- Reliability score: 98.39% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.99x