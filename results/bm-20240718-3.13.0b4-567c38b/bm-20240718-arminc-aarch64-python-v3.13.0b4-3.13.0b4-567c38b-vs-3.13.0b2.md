# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0b4
- machine: linux-aarch64
- commit hash: 567c38b
- commit date: 2024-07-18
- overall geometric mean: 1.00x faster
- HPT reliability: 86.35%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240718-arminc-aarch64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| docutils       | 3.10 sec                                                     | 3.05 sec: 1.01x faster                                       |
| html5lib       | 66.1 ms                                                      | 66.6 ms: 1.01x slower                                        |
| Geometric mean | (ref)                                                        | 1.00x faster                                                 |

Benchmark hidden because not significant (3): 2to3, chameleon, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240718-arminc-aarch64-python-v3.13.0b4-3.13.0b4-567c38b |
|-------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_io_tg        | 1.27 sec                                                     | 1.22 sec: 1.05x faster                                       |
| async_tree_cpu_io_mixed | 791 ms                                                       | 817 ms: 1.03x slower                                         |
| Geometric mean          | (ref)                                                        | 1.01x slower                                                 |

Benchmark hidden because not significant (6): async_tree_io, async_tree_memoization, async_tree_none_tg, async_tree_none, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240718-arminc-aarch64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 114 ms                                                       | 110 ms: 1.03x faster                                         |
| Geometric mean | (ref)                                                        | 1.01x faster                                                 |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240718-arminc-aarch64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_dna      | 259 ms                                                       | 253 ms: 1.02x faster                                         |
| regex_effbot   | 4.98 ms                                                      | 4.90 ms: 1.02x faster                                        |
| regex_v8       | 31.1 ms                                                      | 30.7 ms: 1.01x faster                                        |
| regex_compile  | 128 ms                                                       | 127 ms: 1.00x faster                                         |
| Geometric mean | (ref)                                                        | 1.01x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240718-arminc-aarch64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| tomli_loads          | 2.57 sec                                                     | 2.53 sec: 1.02x faster                                       |
| json_loads           | 32.1 us                                                      | 32.4 us: 1.01x slower                                        |
| unpickle_pure_python | 251 us                                                       | 255 us: 1.02x slower                                         |
| json_dumps           | 13.1 ms                                                      | 13.5 ms: 1.03x slower                                        |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                 |

Benchmark hidden because not significant (5): xml_etree_parse, pickle_pure_python, xml_etree_generate, xml_etree_iterparse, xml_etree_process

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240718-arminc-aarch64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| genshi_xml     | 60.4 ms                                                      | 59.5 ms: 1.01x faster                                        |
| mako           | 13.2 ms                                                      | 13.4 ms: 1.02x slower                                        |
| Geometric mean | (ref)                                                        | 1.00x slower                                                 |

Benchmark hidden because not significant (2): django_template, genshi_text

All benchmarks:
===============

| Benchmark               | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240718-arminc-aarch64-python-v3.13.0b4-3.13.0b4-567c38b |
|-------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| richards                | 55.9 ms                                                      | 53.2 ms: 1.05x faster                                        |
| async_tree_io_tg        | 1.27 sec                                                     | 1.22 sec: 1.05x faster                                       |
| gc_traversal            | 5.17 ms                                                      | 4.98 ms: 1.04x faster                                        |
| telco                   | 10.0 ms                                                      | 9.64 ms: 1.04x faster                                        |
| richards_super          | 62.3 ms                                                      | 60.0 ms: 1.04x faster                                        |
| nbody                   | 114 ms                                                       | 110 ms: 1.03x faster                                         |
| scimark_lu              | 141 ms                                                       | 137 ms: 1.03x faster                                         |
| regex_dna               | 259 ms                                                       | 253 ms: 1.02x faster                                         |
| tomli_loads             | 2.57 sec                                                     | 2.53 sec: 1.02x faster                                       |
| regex_effbot            | 4.98 ms                                                      | 4.90 ms: 1.02x faster                                        |
| docutils                | 3.10 sec                                                     | 3.05 sec: 1.01x faster                                       |
| genshi_xml              | 60.4 ms                                                      | 59.5 ms: 1.01x faster                                        |
| regex_v8                | 31.1 ms                                                      | 30.7 ms: 1.01x faster                                        |
| sympy_sum               | 144 ms                                                       | 142 ms: 1.01x faster                                         |
| coroutines              | 29.0 ms                                                      | 28.7 ms: 1.01x faster                                        |
| pprint_pformat          | 1.93 sec                                                     | 1.92 sec: 1.01x faster                                       |
| bpe_tokeniser           | 5.83 sec                                                     | 5.80 sec: 1.01x faster                                       |
| regex_compile           | 128 ms                                                       | 127 ms: 1.00x faster                                         |
| sqlglot_transpile       | 1.71 ms                                                      | 1.71 ms: 1.00x slower                                        |
| generators              | 37.1 ms                                                      | 37.3 ms: 1.01x slower                                        |
| mdp                     | 3.33 sec                                                     | 3.35 sec: 1.01x slower                                       |
| html5lib                | 66.1 ms                                                      | 66.6 ms: 1.01x slower                                        |
| pprint_safe_repr        | 933 ms                                                       | 941 ms: 1.01x slower                                         |
| fannkuch                | 451 ms                                                       | 455 ms: 1.01x slower                                         |
| json_loads              | 32.1 us                                                      | 32.4 us: 1.01x slower                                        |
| meteor_contest          | 113 ms                                                       | 115 ms: 1.01x slower                                         |
| deepcopy_reduce         | 4.04 us                                                      | 4.10 us: 1.01x slower                                        |
| bench_mp_pool           | 7.03 ms                                                      | 7.14 ms: 1.02x slower                                        |
| unpickle_pure_python    | 251 us                                                       | 255 us: 1.02x slower                                         |
| coverage                | 98.4 ms                                                      | 99.9 ms: 1.02x slower                                        |
| mako                    | 13.2 ms                                                      | 13.4 ms: 1.02x slower                                        |
| json_dumps              | 13.1 ms                                                      | 13.5 ms: 1.03x slower                                        |
| async_tree_cpu_io_mixed | 791 ms                                                       | 817 ms: 1.03x slower                                         |
| bench_thread_pool       | 1.26 ms                                                      | 1.30 ms: 1.03x slower                                        |
| Geometric mean          | (ref)                                                        | 1.00x faster                                                 |

Benchmark hidden because not significant (59): sqlglot_parse, xml_etree_parse, logging_simple, sqlglot_normalize, async_tree_io, async_tree_memoization, sqlglot_optimize, deepcopy_memo, asyncio_tcp, thrift, scimark_monte_carlo, deltablue, tornado_http, scimark_sparse_mat_mult, spectral_norm, python_startup, asyncio_tcp_ssl, chameleon, django_template, logging_format, pickle_pure_python, create_gc_cycles, mypy2, scimark_fft, pidigits, scimark_sor, xml_etree_generate, async_generators, typing_runtime_protocols, float, go, hexiom, pathlib, pycparser, sympy_expand, sympy_str, asyncio_websockets, pyflate, crypto_pyaes, xml_etree_iterparse, deepcopy, sympy_integrate, nqueens, raytrace, dulwich_log, logging_silent, chaos, comprehensions, 2to3, json, pylint, genshi_text, dask, python_startup_no_site, async_tree_none_tg, async_tree_none, xml_etree_process, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg
Ignored benchmarks (9) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 86.35% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x