# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0rc2
- machine: linux-aarch64
- commit hash: ec61006
- commit date: 2024-09-06
- overall geometric mean: 1.00x slower
- HPT reliability: 76.73%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (5): 2to3, chameleon, docutils, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_io, async_tree_none_tg, async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_io_tg

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): nbody, pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-arminc-aarch64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_dna      | 259 ms                                                       | 252 ms: 1.03x faster                                           |
| regex_effbot   | 4.98 ms                                                      | 4.88 ms: 1.02x faster                                          |
| Geometric mean | (ref)                                                        | 1.01x faster                                                   |

Benchmark hidden because not significant (2): regex_v8, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-arminc-aarch64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|---------------------|:------------------------------------------------------------:|:--------------------------------------------------------------:|
| json_loads          | 32.1 us                                                      | 31.4 us: 1.02x faster                                          |
| tomli_loads         | 2.57 sec                                                     | 2.55 sec: 1.01x faster                                         |
| xml_etree_generate  | 114 ms                                                       | 113 ms: 1.01x faster                                           |
| pickle_dict         | 37.6 us                                                      | 37.9 us: 1.01x slower                                          |
| xml_etree_iterparse | 147 ms                                                       | 148 ms: 1.01x slower                                           |
| pickle_list         | 5.27 us                                                      | 5.33 us: 1.01x slower                                          |
| json_dumps          | 13.1 ms                                                      | 13.3 ms: 1.02x slower                                          |
| pickle              | 13.4 us                                                      | 13.6 us: 1.02x slower                                          |
| unpickle            | 19.8 us                                                      | 20.3 us: 1.03x slower                                          |
| Geometric mean      | (ref)                                                        | 1.00x slower                                                   |

Benchmark hidden because not significant (5): xml_etree_process, pickle_pure_python, unpickle_pure_python, unpickle_list, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-arminc-aarch64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup | 13.0 ms                                                      | 13.1 ms: 1.01x slower                                          |
| Geometric mean | (ref)                                                        | 1.01x slower                                                   |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-arminc-aarch64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------:|
| genshi_text    | 27.4 ms                                                      | 27.8 ms: 1.01x slower                                          |
| mako           | 13.2 ms                                                      | 13.3 ms: 1.01x slower                                          |
| Geometric mean | (ref)                                                        | 1.01x slower                                                   |

Benchmark hidden because not significant (2): django_template, genshi_xml

All benchmarks:
===============

| Benchmark               | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-arminc-aarch64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|-------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------:|
| richards                | 55.9 ms                                                      | 52.9 ms: 1.06x faster                                          |
| gc_traversal            | 5.17 ms                                                      | 4.92 ms: 1.05x faster                                          |
| richards_super          | 62.3 ms                                                      | 59.5 ms: 1.05x faster                                          |
| logging_simple          | 7.21 us                                                      | 6.96 us: 1.03x faster                                          |
| regex_dna               | 259 ms                                                       | 252 ms: 1.03x faster                                           |
| json_loads              | 32.1 us                                                      | 31.4 us: 1.02x faster                                          |
| regex_effbot            | 4.98 ms                                                      | 4.88 ms: 1.02x faster                                          |
| pyflate                 | 557 ms                                                       | 550 ms: 1.01x faster                                           |
| hexiom                  | 7.08 ms                                                      | 7.00 ms: 1.01x faster                                          |
| tomli_loads             | 2.57 sec                                                     | 2.55 sec: 1.01x faster                                         |
| xml_etree_generate      | 114 ms                                                       | 113 ms: 1.01x faster                                           |
| pprint_pformat          | 1.93 sec                                                     | 1.92 sec: 1.00x faster                                         |
| bpe_tokeniser           | 5.83 sec                                                     | 5.80 sec: 1.00x faster                                         |
| python_startup          | 13.0 ms                                                      | 13.1 ms: 1.01x slower                                          |
| pickle_dict             | 37.6 us                                                      | 37.9 us: 1.01x slower                                          |
| pprint_safe_repr        | 933 ms                                                       | 942 ms: 1.01x slower                                           |
| xml_etree_iterparse     | 147 ms                                                       | 148 ms: 1.01x slower                                           |
| pickle_list             | 5.27 us                                                      | 5.33 us: 1.01x slower                                          |
| asyncio_tcp_ssl         | 2.21 sec                                                     | 2.24 sec: 1.01x slower                                         |
| deepcopy                | 448 us                                                       | 453 us: 1.01x slower                                           |
| raytrace                | 297 ms                                                       | 300 ms: 1.01x slower                                           |
| genshi_text             | 27.4 ms                                                      | 27.8 ms: 1.01x slower                                          |
| bench_thread_pool       | 1.26 ms                                                      | 1.27 ms: 1.01x slower                                          |
| mdp                     | 3.33 sec                                                     | 3.38 sec: 1.01x slower                                         |
| mako                    | 13.2 ms                                                      | 13.3 ms: 1.01x slower                                          |
| fannkuch                | 451 ms                                                       | 458 ms: 1.01x slower                                           |
| json_dumps              | 13.1 ms                                                      | 13.3 ms: 1.02x slower                                          |
| scimark_sparse_mat_mult | 6.55 ms                                                      | 6.67 ms: 1.02x slower                                          |
| deepcopy_reduce         | 4.04 us                                                      | 4.12 us: 1.02x slower                                          |
| pickle                  | 13.4 us                                                      | 13.6 us: 1.02x slower                                          |
| generators              | 37.1 ms                                                      | 38.0 ms: 1.02x slower                                          |
| spectral_norm           | 141 ms                                                       | 145 ms: 1.02x slower                                           |
| unpickle                | 19.8 us                                                      | 20.3 us: 1.03x slower                                          |
| logging_silent          | 133 ns                                                       | 137 ns: 1.03x slower                                           |
| bench_mp_pool           | 7.03 ms                                                      | 7.75 ms: 1.10x slower                                          |
| Geometric mean          | (ref)                                                        | 1.00x slower                                                   |

Benchmark hidden because not significant (66): async_tree_io, xml_etree_process, async_tree_none_tg, pickle_pure_python, async_generators, async_tree_none, scimark_lu, logging_format, mypy2, json, pycparser, sympy_sum, thrift, nbody, sqlite_synth, comprehensions, deltablue, sqlglot_normalize, 2to3, typing_runtime_protocols, sqlglot_parse, async_tree_cpu_io_mixed_tg, sympy_expand, async_tree_memoization_tg, chameleon, async_tree_memoization, go, create_gc_cycles, async_tree_cpu_io_mixed, pathlib, pidigits, docutils, unpickle_pure_python, scimark_monte_carlo, sqlglot_optimize, nqueens, float, scimark_sor, chaos, regex_v8, sympy_str, scimark_fft, crypto_pyaes, meteor_contest, python_startup_no_site, regex_compile, coverage, sympy_integrate, async_tree_io_tg, asyncio_websockets, django_template, coroutines, dask, sqlglot_transpile, telco, unpickle_list, genshi_xml, deepcopy_memo, asyncio_tcp, flaskblogging, aiohttp, tornado_http, xml_etree_parse, html5lib, gunicorn, pylint
Ignored benchmarks (1) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: dulwich_log
Ignored benchmarks (1) of results/bm-20240906-3.13.0rc2-ec61006/bm-20240906-arminc-aarch64-python-v3.13.0rc2-3.13.0rc2-ec61006.json: unpack_sequence

# HPT report

- Reliability score: 76.73% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x