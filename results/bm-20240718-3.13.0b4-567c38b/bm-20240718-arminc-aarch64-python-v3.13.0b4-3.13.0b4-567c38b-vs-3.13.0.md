# Results vs. 3.13.0

- fork: python
- ref: v3.13.0b4
- machine: linux-aarch64
- commit hash: 567c38b
- commit date: 2024-07-18
- overall geometric mean: 1.011x faster
- HPT reliability: 55.49%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240718-arminc-aarch64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| chameleon      | 9.08 ms                                                  | 8.93 ms: 1.02x faster                                        |
| docutils       | 2.89 sec                                                 | 3.05 sec: 1.06x slower                                       |
| Geometric mean | (ref)                                                    | 1.01x slower                                                 |

Benchmark hidden because not significant (3): 2to3, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240718-arminc-aarch64-python-v3.13.0b4-3.13.0b4-567c38b |
|---------------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_memoization_tg | 649 ms                                                   | 619 ms: 1.05x faster                                         |
| coroutines                | 28.5 ms                                                  | 28.7 ms: 1.01x slower                                        |
| async_tree_none_tg        | 470 ms                                                   | 484 ms: 1.03x slower                                         |
| async_tree_cpu_io_mixed   | 766 ms                                                   | 817 ms: 1.07x slower                                         |
| async_tree_io_tg          | 1.13 sec                                                 | 1.22 sec: 1.07x slower                                       |
| async_tree_io             | 1.11 sec                                                 | 1.21 sec: 1.09x slower                                       |
| Geometric mean            | (ref)                                                    | 1.02x slower                                                 |

Benchmark hidden because not significant (5): async_tree_memoization, async_generators, asyncio_websockets, async_tree_none, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240718-arminc-aarch64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 114 ms                                                   | 110 ms: 1.04x faster                                         |
| float          | 93.3 ms                                                  | 91.6 ms: 1.02x faster                                        |
| Geometric mean | (ref)                                                    | 1.02x faster                                                 |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240718-arminc-aarch64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| regex_v8       | 31.8 ms                                                  | 30.7 ms: 1.04x faster                                        |
| Geometric mean | (ref)                                                    | 1.01x faster                                                 |

Benchmark hidden because not significant (3): regex_dna, regex_compile, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240718-arminc-aarch64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| xml_etree_parse      | 197 ms                                                   | 189 ms: 1.04x faster                                         |
| tomli_loads          | 2.54 sec                                                 | 2.53 sec: 1.00x faster                                       |
| unpickle_pure_python | 251 us                                                   | 255 us: 1.02x slower                                         |
| json_loads           | 31.7 us                                                  | 32.4 us: 1.02x slower                                        |
| Geometric mean       | (ref)                                                    | 1.00x slower                                                 |

Benchmark hidden because not significant (5): xml_etree_iterparse, json_dumps, pickle_pure_python, xml_etree_generate, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240718-arminc-aarch64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup | 15.4 ms                                                  | 12.9 ms: 1.19x faster                                        |
| Geometric mean | (ref)                                                    | 1.09x faster                                                 |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240718-arminc-aarch64-python-v3.13.0b4-3.13.0b4-567c38b |
|-----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| django_template | 41.6 ms                                                  | 42.2 ms: 1.01x slower                                        |
| Geometric mean  | (ref)                                                    | 1.00x slower                                                 |

Benchmark hidden because not significant (3): genshi_xml, mako, genshi_text

All benchmarks:
===============

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240718-arminc-aarch64-python-v3.13.0b4-3.13.0b4-567c38b |
|---------------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| mypy2                     | 1.15 sec                                                 | 766 ms: 1.50x faster                                         |
| create_gc_cycles          | 3.35 ms                                                  | 2.33 ms: 1.44x faster                                        |
| python_startup            | 15.4 ms                                                  | 12.9 ms: 1.19x faster                                        |
| gc_traversal              | 5.77 ms                                                  | 4.98 ms: 1.16x faster                                        |
| bench_mp_pool             | 7.68 ms                                                  | 7.14 ms: 1.08x faster                                        |
| async_tree_memoization_tg | 649 ms                                                   | 619 ms: 1.05x faster                                         |
| pycparser                 | 1.27 sec                                                 | 1.23 sec: 1.04x faster                                       |
| xml_etree_parse           | 197 ms                                                   | 189 ms: 1.04x faster                                         |
| nbody                     | 114 ms                                                   | 110 ms: 1.04x faster                                         |
| regex_v8                  | 31.8 ms                                                  | 30.7 ms: 1.04x faster                                        |
| scimark_monte_carlo       | 83.6 ms                                                  | 81.8 ms: 1.02x faster                                        |
| float                     | 93.3 ms                                                  | 91.6 ms: 1.02x faster                                        |
| chameleon                 | 9.08 ms                                                  | 8.93 ms: 1.02x faster                                        |
| scimark_lu                | 139 ms                                                   | 137 ms: 1.02x faster                                         |
| bpe_tokeniser             | 5.87 sec                                                 | 5.80 sec: 1.01x faster                                       |
| thrift                    | 968 us                                                   | 956 us: 1.01x faster                                         |
| fannkuch                  | 461 ms                                                   | 455 ms: 1.01x faster                                         |
| sympy_sum                 | 144 ms                                                   | 142 ms: 1.01x faster                                         |
| telco                     | 9.74 ms                                                  | 9.64 ms: 1.01x faster                                        |
| generators                | 37.6 ms                                                  | 37.3 ms: 1.01x faster                                        |
| tomli_loads               | 2.54 sec                                                 | 2.53 sec: 1.00x faster                                       |
| mdp                       | 3.34 sec                                                 | 3.35 sec: 1.00x slower                                       |
| coroutines                | 28.5 ms                                                  | 28.7 ms: 1.01x slower                                        |
| pyflate                   | 556 ms                                                   | 560 ms: 1.01x slower                                         |
| go                        | 160 ms                                                   | 161 ms: 1.01x slower                                         |
| sqlglot_normalize         | 127 ms                                                   | 128 ms: 1.01x slower                                         |
| sympy_str                 | 264 ms                                                   | 267 ms: 1.01x slower                                         |
| deltablue                 | 3.82 ms                                                  | 3.86 ms: 1.01x slower                                        |
| pprint_pformat            | 1.90 sec                                                 | 1.92 sec: 1.01x slower                                       |
| meteor_contest            | 114 ms                                                   | 115 ms: 1.01x slower                                         |
| chaos                     | 68.0 ms                                                  | 68.9 ms: 1.01x slower                                        |
| django_template           | 41.6 ms                                                  | 42.2 ms: 1.01x slower                                        |
| pprint_safe_repr          | 926 ms                                                   | 941 ms: 1.02x slower                                         |
| comprehensions            | 20.4 us                                                  | 20.7 us: 1.02x slower                                        |
| unpickle_pure_python      | 251 us                                                   | 255 us: 1.02x slower                                         |
| json_loads                | 31.7 us                                                  | 32.4 us: 1.02x slower                                        |
| async_tree_none_tg        | 470 ms                                                   | 484 ms: 1.03x slower                                         |
| docutils                  | 2.89 sec                                                 | 3.05 sec: 1.06x slower                                       |
| async_tree_cpu_io_mixed   | 766 ms                                                   | 817 ms: 1.07x slower                                         |
| async_tree_io_tg          | 1.13 sec                                                 | 1.22 sec: 1.07x slower                                       |
| async_tree_io             | 1.11 sec                                                 | 1.21 sec: 1.09x slower                                       |
| Geometric mean            | (ref)                                                    | 1.01x faster                                                 |

Benchmark hidden because not significant (48): async_tree_memoization, crypto_pyaes, genshi_xml, spectral_norm, xml_etree_iterparse, sqlglot_transpile, richards, json, json_dumps, tornado_http, nqueens, scimark_fft, pylint, hexiom, raytrace, regex_dna, richards_super, scimark_sor, logging_format, python_startup_no_site, sqlglot_optimize, async_generators, deepcopy_memo, scimark_sparse_mat_mult, mako, regex_compile, genshi_text, regex_effbot, pidigits, pickle_pure_python, typing_runtime_protocols, asyncio_websockets, html5lib, xml_etree_generate, async_tree_none, pathlib, sympy_expand, deepcopy_reduce, coverage, logging_simple, sympy_integrate, deepcopy, sqlglot_parse, logging_silent, 2to3, async_tree_cpu_io_mixed_tg, bench_thread_pool, xml_etree_process
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240718-3.13.0b4-567c38b/bm-20240718-arminc-aarch64-python-v3.13.0b4-3.13.0b4-567c38b.json: asyncio_tcp, asyncio_tcp_ssl, dask, dulwich_log

- Geometric mean (including insignificant results): 1.011x faster
# HPT report

- Reliability score: 55.49% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.91x