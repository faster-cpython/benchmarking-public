# Results vs. 3.12.0

- fork: faster-cpython
- ref: make_decref_a_call
- machine: linux-aarch64
- commit hash: 4fee8de
- commit date: 2025-05-19
- overall geometric mean: 1.029x faster
- HPT reliability: 82.97%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250519-arminc-aarch64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 319 ms: 1.04x slower                                                            |
| docutils       | 2.98 sec                                                              | 3.01 sec: 1.01x slower                                                          |
| html5lib       | 65.1 ms                                                               | 63.7 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250519-arminc-aarch64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 473 ms: 1.64x faster                                                            |
| async_tree_memoization_tg  | 740 ms                                                                | 471 ms: 1.57x faster                                                            |
| async_tree_none            | 624 ms                                                                | 399 ms: 1.56x faster                                                            |
| async_tree_io              | 1.41 sec                                                              | 907 ms: 1.56x faster                                                            |
| async_tree_none_tg         | 577 ms                                                                | 383 ms: 1.50x faster                                                            |
| async_tree_io_tg           | 1.40 sec                                                              | 938 ms: 1.50x faster                                                            |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 668 ms: 1.37x faster                                                            |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 661 ms: 1.34x faster                                                            |
| Geometric mean             | (ref)                                                                 | 1.50x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250519-arminc-aarch64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 88.0 ms: 1.05x faster                                                           |
| nbody          | 105 ms                                                                | 121 ms: 1.16x slower                                                            |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250519-arminc-aarch64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.81 ms: 1.22x faster                                                           |
| regex_dna      | 254 ms                                                                | 232 ms: 1.09x faster                                                            |
| regex_compile  | 137 ms                                                                | 128 ms: 1.08x faster                                                            |
| Geometric mean | (ref)                                                                 | 1.10x faster                                                                    |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250519-arminc-aarch64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|--------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads        | 2.59 sec                                                              | 2.56 sec: 1.01x faster                                                          |
| xml_etree_generate | 112 ms                                                                | 116 ms: 1.04x slower                                                            |
| xml_etree_process  | 79.0 ms                                                               | 82.8 ms: 1.05x slower                                                           |
| json_dumps         | 12.3 ms                                                               | 13.7 ms: 1.12x slower                                                           |
| pickle_pure_python | 365 us                                                                | 418 us: 1.14x slower                                                            |
| json_loads         | 30.7 us                                                               | 36.0 us: 1.17x slower                                                           |
| Geometric mean     | (ref)                                                                 | 1.06x slower                                                                    |

Benchmark hidden because not significant (3): xml_etree_parse, xml_etree_iterparse, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250519-arminc-aarch64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.70 ms: 1.04x slower                                                           |
| python_startup         | 11.4 ms                                                               | 15.2 ms: 1.34x slower                                                           |
| Geometric mean         | (ref)                                                                 | 1.18x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250519-arminc-aarch64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_xml      | 60.6 ms                                                               | 63.1 ms: 1.04x slower                                                           |
| django_template | 40.7 ms                                                               | 42.5 ms: 1.05x slower                                                           |
| mako            | 12.9 ms                                                               | 14.5 ms: 1.12x slower                                                           |
| Geometric mean  | (ref)                                                                 | 1.06x slower                                                                    |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250519-arminc-aarch64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.73 sec: 1.98x faster                                                          |
| async_tree_memoization     | 777 ms                                                                | 473 ms: 1.64x faster                                                            |
| async_tree_memoization_tg  | 740 ms                                                                | 471 ms: 1.57x faster                                                            |
| async_tree_none            | 624 ms                                                                | 399 ms: 1.56x faster                                                            |
| async_tree_io              | 1.41 sec                                                              | 907 ms: 1.56x faster                                                            |
| async_tree_none_tg         | 577 ms                                                                | 383 ms: 1.50x faster                                                            |
| async_tree_io_tg           | 1.40 sec                                                              | 938 ms: 1.50x faster                                                            |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 668 ms: 1.37x faster                                                            |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 661 ms: 1.34x faster                                                            |
| deepcopy                   | 446 us                                                                | 342 us: 1.30x faster                                                            |
| deepcopy_memo              | 49.6 us                                                               | 39.1 us: 1.27x faster                                                           |
| regex_effbot               | 4.64 ms                                                               | 3.81 ms: 1.22x faster                                                           |
| go                         | 157 ms                                                                | 130 ms: 1.21x faster                                                            |
| generators                 | 43.5 ms                                                               | 36.9 ms: 1.18x faster                                                           |
| dulwich_log                | 62.0 ms                                                               | 53.5 ms: 1.16x faster                                                           |
| comprehensions             | 25.4 us                                                               | 22.5 us: 1.13x faster                                                           |
| pylint                     | 355 ms                                                                | 315 ms: 1.12x faster                                                            |
| deepcopy_reduce            | 4.10 us                                                               | 3.69 us: 1.11x faster                                                           |
| regex_dna                  | 254 ms                                                                | 232 ms: 1.09x faster                                                            |
| deltablue                  | 4.12 ms                                                               | 3.82 ms: 1.08x faster                                                           |
| regex_compile              | 137 ms                                                                | 128 ms: 1.08x faster                                                            |
| pathlib                    | 24.5 ms                                                               | 23.0 ms: 1.07x faster                                                           |
| sympy_integrate            | 21.6 ms                                                               | 20.5 ms: 1.05x faster                                                           |
| float                      | 92.1 ms                                                               | 88.0 ms: 1.05x faster                                                           |
| raytrace                   | 353 ms                                                                | 340 ms: 1.04x faster                                                            |
| async_generators           | 491 ms                                                                | 480 ms: 1.02x faster                                                            |
| html5lib                   | 65.1 ms                                                               | 63.7 ms: 1.02x faster                                                           |
| tomli_loads                | 2.59 sec                                                              | 2.56 sec: 1.01x faster                                                          |
| docutils                   | 2.98 sec                                                              | 3.01 sec: 1.01x slower                                                          |
| crypto_pyaes               | 86.6 ms                                                               | 88.0 ms: 1.02x slower                                                           |
| asyncio_websockets         | 658 ms                                                                | 670 ms: 1.02x slower                                                            |
| pprint_pformat             | 1.88 sec                                                              | 1.93 sec: 1.03x slower                                                          |
| pycparser                  | 1.26 sec                                                              | 1.29 sec: 1.03x slower                                                          |
| logging_simple             | 7.63 us                                                               | 7.88 us: 1.03x slower                                                           |
| hexiom                     | 6.98 ms                                                               | 7.20 ms: 1.03x slower                                                           |
| pprint_safe_repr           | 916 ms                                                                | 947 ms: 1.03x slower                                                            |
| 2to3                       | 308 ms                                                                | 319 ms: 1.04x slower                                                            |
| xml_etree_generate         | 112 ms                                                                | 116 ms: 1.04x slower                                                            |
| python_startup_no_site     | 8.37 ms                                                               | 8.70 ms: 1.04x slower                                                           |
| genshi_xml                 | 60.6 ms                                                               | 63.1 ms: 1.04x slower                                                           |
| sqlite_synth               | 3.77 us                                                               | 3.94 us: 1.05x slower                                                           |
| django_template            | 40.7 ms                                                               | 42.5 ms: 1.05x slower                                                           |
| bench_thread_pool          | 1.31 ms                                                               | 1.37 ms: 1.05x slower                                                           |
| xml_etree_process          | 79.0 ms                                                               | 82.8 ms: 1.05x slower                                                           |
| logging_format             | 8.34 us                                                               | 8.79 us: 1.05x slower                                                           |
| nqueens                    | 99.2 ms                                                               | 105 ms: 1.05x slower                                                            |
| scimark_fft                | 418 ms                                                                | 446 ms: 1.07x slower                                                            |
| coroutines                 | 29.0 ms                                                               | 31.0 ms: 1.07x slower                                                           |
| meteor_contest             | 112 ms                                                                | 120 ms: 1.08x slower                                                            |
| sympy_expand               | 454 ms                                                                | 489 ms: 1.08x slower                                                            |
| scimark_lu                 | 146 ms                                                                | 157 ms: 1.08x slower                                                            |
| thrift                     | 937 us                                                                | 1.02 ms: 1.09x slower                                                           |
| json_dumps                 | 12.3 ms                                                               | 13.7 ms: 1.12x slower                                                           |
| mako                       | 12.9 ms                                                               | 14.5 ms: 1.12x slower                                                           |
| json                       | 5.54 ms                                                               | 6.22 ms: 1.12x slower                                                           |
| pickle_pure_python         | 365 us                                                                | 418 us: 1.14x slower                                                            |
| fannkuch                   | 443 ms                                                                | 510 ms: 1.15x slower                                                            |
| typing_runtime_protocols   | 181 us                                                                | 209 us: 1.16x slower                                                            |
| nbody                      | 105 ms                                                                | 121 ms: 1.16x slower                                                            |
| telco                      | 8.51 ms                                                               | 9.94 ms: 1.17x slower                                                           |
| json_loads                 | 30.7 us                                                               | 36.0 us: 1.17x slower                                                           |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 7.86 ms: 1.27x slower                                                           |
| coverage                   | 87.3 ms                                                               | 113 ms: 1.29x slower                                                            |
| python_startup             | 11.4 ms                                                               | 15.2 ms: 1.34x slower                                                           |
| gc_traversal               | 4.40 ms                                                               | 6.92 ms: 1.57x slower                                                           |
| create_gc_cycles           | 1.92 ms                                                               | 3.80 ms: 1.98x slower                                                           |
| logging_silent             | 127 ns                                                                | 629 ns: 4.96x slower                                                            |
| bench_mp_pool              | 7.05 ms                                                               | 4.80 sec: 680.84x slower                                                        |
| Geometric mean             | (ref)                                                                 | 1.08x slower                                                                    |

Benchmark hidden because not significant (15): xml_etree_parse, sympy_str, sympy_sum, scimark_monte_carlo, regex_v8, pyflate, spectral_norm, chaos, xml_etree_iterparse, scimark_sor, richards_super, richards, pidigits, unpickle_pure_python, genshi_text
Ignored benchmarks (19) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250519-3.15.0a0-4fee8de/bm-20250519-arminc-aarch64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de.json: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.029x faster

# HPT report

- Reliability score: 82.97% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.08x