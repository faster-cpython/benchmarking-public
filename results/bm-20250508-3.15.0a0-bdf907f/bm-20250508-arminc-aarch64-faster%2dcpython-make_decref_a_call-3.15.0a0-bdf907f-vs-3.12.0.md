# Results vs. 3.12.0

- fork: faster-cpython
- ref: make_decref_a_call
- machine: linux-aarch64
- commit hash: bdf907f
- commit date: 2025-05-08
- overall geometric mean: 1.033x faster
- HPT reliability: 81.05%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250508-arminc-aarch64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 315 ms: 1.02x slower                                                            |
| html5lib       | 65.1 ms                                                               | 63.6 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250508-arminc-aarch64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 471 ms: 1.65x faster                                                            |
| async_tree_memoization_tg  | 740 ms                                                                | 469 ms: 1.58x faster                                                            |
| async_tree_io              | 1.41 sec                                                              | 899 ms: 1.57x faster                                                            |
| async_tree_none            | 624 ms                                                                | 401 ms: 1.56x faster                                                            |
| async_tree_none_tg         | 577 ms                                                                | 379 ms: 1.52x faster                                                            |
| async_tree_io_tg           | 1.40 sec                                                              | 935 ms: 1.50x faster                                                            |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 665 ms: 1.37x faster                                                            |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 656 ms: 1.35x faster                                                            |
| Geometric mean             | (ref)                                                                 | 1.51x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250508-arminc-aarch64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 88.6 ms: 1.04x faster                                                           |
| nbody          | 105 ms                                                                | 124 ms: 1.19x slower                                                            |
| Geometric mean | (ref)                                                                 | 1.06x slower                                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250508-arminc-aarch64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.95 ms: 1.17x faster                                                           |
| regex_compile  | 137 ms                                                                | 128 ms: 1.07x faster                                                            |
| regex_dna      | 254 ms                                                                | 238 ms: 1.07x faster                                                            |
| Geometric mean | (ref)                                                                 | 1.08x faster                                                                    |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250508-arminc-aarch64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.59 sec                                                              | 2.55 sec: 1.02x faster                                                          |
| xml_etree_parse      | 195 ms                                                                | 191 ms: 1.02x faster                                                            |
| unpickle_pure_python | 260 us                                                                | 271 us: 1.04x slower                                                            |
| xml_etree_process    | 79.0 ms                                                               | 84.1 ms: 1.07x slower                                                           |
| xml_etree_generate   | 112 ms                                                                | 120 ms: 1.07x slower                                                            |
| pickle_pure_python   | 365 us                                                                | 402 us: 1.10x slower                                                            |
| json_loads           | 30.7 us                                                               | 36.0 us: 1.17x slower                                                           |
| json_dumps           | 12.3 ms                                                               | 15.7 ms: 1.28x slower                                                           |
| Geometric mean       | (ref)                                                                 | 1.07x slower                                                                    |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250508-arminc-aarch64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.72 ms: 1.04x slower                                                           |
| python_startup         | 11.4 ms                                                               | 15.2 ms: 1.34x slower                                                           |
| Geometric mean         | (ref)                                                                 | 1.18x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250508-arminc-aarch64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text    | 27.4 ms                                                               | 28.9 ms: 1.05x slower                                                           |
| genshi_xml     | 60.6 ms                                                               | 64.6 ms: 1.07x slower                                                           |
| mako           | 12.9 ms                                                               | 14.1 ms: 1.09x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.06x slower                                                                    |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250508-arminc-aarch64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.71 sec: 2.00x faster                                                          |
| async_tree_memoization     | 777 ms                                                                | 471 ms: 1.65x faster                                                            |
| async_tree_memoization_tg  | 740 ms                                                                | 469 ms: 1.58x faster                                                            |
| async_tree_io              | 1.41 sec                                                              | 899 ms: 1.57x faster                                                            |
| async_tree_none            | 624 ms                                                                | 401 ms: 1.56x faster                                                            |
| async_tree_none_tg         | 577 ms                                                                | 379 ms: 1.52x faster                                                            |
| async_tree_io_tg           | 1.40 sec                                                              | 935 ms: 1.50x faster                                                            |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 665 ms: 1.37x faster                                                            |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 656 ms: 1.35x faster                                                            |
| deepcopy                   | 446 us                                                                | 346 us: 1.29x faster                                                            |
| deepcopy_memo              | 49.6 us                                                               | 39.4 us: 1.26x faster                                                           |
| go                         | 157 ms                                                                | 130 ms: 1.21x faster                                                            |
| generators                 | 43.5 ms                                                               | 36.8 ms: 1.18x faster                                                           |
| regex_effbot               | 4.64 ms                                                               | 3.95 ms: 1.17x faster                                                           |
| dulwich_log                | 62.0 ms                                                               | 53.8 ms: 1.15x faster                                                           |
| pylint                     | 355 ms                                                                | 314 ms: 1.13x faster                                                            |
| deepcopy_reduce            | 4.10 us                                                               | 3.70 us: 1.11x faster                                                           |
| comprehensions             | 25.4 us                                                               | 22.9 us: 1.11x faster                                                           |
| pathlib                    | 24.5 ms                                                               | 22.8 ms: 1.08x faster                                                           |
| regex_compile              | 137 ms                                                                | 128 ms: 1.07x faster                                                            |
| regex_dna                  | 254 ms                                                                | 238 ms: 1.07x faster                                                            |
| raytrace                   | 353 ms                                                                | 331 ms: 1.07x faster                                                            |
| deltablue                  | 4.12 ms                                                               | 3.89 ms: 1.06x faster                                                           |
| logging_simple             | 7.63 us                                                               | 7.27 us: 1.05x faster                                                           |
| sympy_integrate            | 21.6 ms                                                               | 20.7 ms: 1.04x faster                                                           |
| float                      | 92.1 ms                                                               | 88.6 ms: 1.04x faster                                                           |
| sympy_sum                  | 154 ms                                                                | 149 ms: 1.03x faster                                                            |
| async_generators           | 491 ms                                                                | 475 ms: 1.03x faster                                                            |
| scimark_monte_carlo        | 85.1 ms                                                               | 82.6 ms: 1.03x faster                                                           |
| html5lib                   | 65.1 ms                                                               | 63.6 ms: 1.02x faster                                                           |
| tomli_loads                | 2.59 sec                                                              | 2.55 sec: 1.02x faster                                                          |
| xml_etree_parse            | 195 ms                                                                | 191 ms: 1.02x faster                                                            |
| richards_super             | 58.5 ms                                                               | 58.0 ms: 1.01x faster                                                           |
| 2to3                       | 308 ms                                                                | 315 ms: 1.02x slower                                                            |
| asyncio_websockets         | 658 ms                                                                | 673 ms: 1.02x slower                                                            |
| hexiom                     | 6.98 ms                                                               | 7.17 ms: 1.03x slower                                                           |
| pyflate                    | 559 ms                                                                | 575 ms: 1.03x slower                                                            |
| coroutines                 | 29.0 ms                                                               | 29.9 ms: 1.03x slower                                                           |
| pprint_safe_repr           | 916 ms                                                                | 946 ms: 1.03x slower                                                            |
| pycparser                  | 1.26 sec                                                              | 1.30 sec: 1.03x slower                                                          |
| pprint_pformat             | 1.88 sec                                                              | 1.96 sec: 1.04x slower                                                          |
| bench_thread_pool          | 1.31 ms                                                               | 1.36 ms: 1.04x slower                                                           |
| unpickle_pure_python       | 260 us                                                                | 271 us: 1.04x slower                                                            |
| python_startup_no_site     | 8.37 ms                                                               | 8.72 ms: 1.04x slower                                                           |
| genshi_text                | 27.4 ms                                                               | 28.9 ms: 1.05x slower                                                           |
| meteor_contest             | 112 ms                                                                | 118 ms: 1.05x slower                                                            |
| thrift                     | 937 us                                                                | 987 us: 1.05x slower                                                            |
| xml_etree_process          | 79.0 ms                                                               | 84.1 ms: 1.07x slower                                                           |
| genshi_xml                 | 60.6 ms                                                               | 64.6 ms: 1.07x slower                                                           |
| xml_etree_generate         | 112 ms                                                                | 120 ms: 1.07x slower                                                            |
| sympy_expand               | 454 ms                                                                | 486 ms: 1.07x slower                                                            |
| scimark_fft                | 418 ms                                                                | 450 ms: 1.07x slower                                                            |
| scimark_lu                 | 146 ms                                                                | 157 ms: 1.08x slower                                                            |
| sqlite_synth               | 3.77 us                                                               | 4.07 us: 1.08x slower                                                           |
| nqueens                    | 99.2 ms                                                               | 107 ms: 1.08x slower                                                            |
| mako                       | 12.9 ms                                                               | 14.1 ms: 1.09x slower                                                           |
| pickle_pure_python         | 365 us                                                                | 402 us: 1.10x slower                                                            |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.98 ms: 1.13x slower                                                           |
| typing_runtime_protocols   | 181 us                                                                | 206 us: 1.14x slower                                                            |
| json                       | 5.54 ms                                                               | 6.34 ms: 1.15x slower                                                           |
| fannkuch                   | 443 ms                                                                | 509 ms: 1.15x slower                                                            |
| json_loads                 | 30.7 us                                                               | 36.0 us: 1.17x slower                                                           |
| nbody                      | 105 ms                                                                | 124 ms: 1.19x slower                                                            |
| telco                      | 8.51 ms                                                               | 10.1 ms: 1.19x slower                                                           |
| coverage                   | 87.3 ms                                                               | 110 ms: 1.26x slower                                                            |
| json_dumps                 | 12.3 ms                                                               | 15.7 ms: 1.28x slower                                                           |
| python_startup             | 11.4 ms                                                               | 15.2 ms: 1.34x slower                                                           |
| gc_traversal               | 4.40 ms                                                               | 6.91 ms: 1.57x slower                                                           |
| create_gc_cycles           | 1.92 ms                                                               | 3.71 ms: 1.94x slower                                                           |
| bench_mp_pool              | 7.05 ms                                                               | 2.21 sec: 312.61x slower                                                        |
| Geometric mean             | (ref)                                                                 | 1.05x slower                                                                    |

Benchmark hidden because not significant (13): logging_format, chaos, xml_etree_iterparse, scimark_sor, regex_v8, docutils, spectral_norm, logging_silent, sympy_str, richards, pidigits, crypto_pyaes, django_template
Ignored benchmarks (19) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250508-3.15.0a0-bdf907f/bm-20250508-arminc-aarch64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f.json: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.033x faster

# HPT report

- Reliability score: 81.05% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.08x