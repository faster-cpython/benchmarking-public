# Results vs. 3.12.0

- fork: faster-cpython
- ref: tstate_in_dealloc
- machine: linux-aarch64
- commit hash: 49ac4ce
- commit date: 2025-04-09
- overall geometric mean: 1.064x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250409-arminc-aarch64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 300 ms: 1.03x faster                                                            |
| docutils       | 2.98 sec                                                              | 2.92 sec: 1.02x faster                                                          |
| html5lib       | 65.1 ms                                                               | 63.2 ms: 1.03x faster                                                           |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250409-arminc-aarch64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 464 ms: 1.68x faster                                                            |
| async_tree_io              | 1.41 sec                                                              | 878 ms: 1.61x faster                                                            |
| async_tree_none            | 624 ms                                                                | 389 ms: 1.60x faster                                                            |
| async_tree_memoization_tg  | 740 ms                                                                | 465 ms: 1.59x faster                                                            |
| async_tree_io_tg           | 1.40 sec                                                              | 893 ms: 1.57x faster                                                            |
| async_tree_none_tg         | 577 ms                                                                | 367 ms: 1.57x faster                                                            |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 665 ms: 1.37x faster                                                            |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 646 ms: 1.37x faster                                                            |
| Geometric mean             | (ref)                                                                 | 1.54x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250409-arminc-aarch64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 86.0 ms: 1.07x faster                                                           |
| nbody          | 105 ms                                                                | 123 ms: 1.17x slower                                                            |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250409-arminc-aarch64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.94 ms: 1.18x faster                                                           |
| regex_compile  | 137 ms                                                                | 123 ms: 1.11x faster                                                            |
| regex_dna      | 254 ms                                                                | 242 ms: 1.05x faster                                                            |
| regex_v8       | 28.3 ms                                                               | 28.0 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                                 | 1.09x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250409-arminc-aarch64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|---------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_parse     | 195 ms                                                                | 175 ms: 1.12x faster                                                            |
| xml_etree_iterparse | 150 ms                                                                | 141 ms: 1.06x faster                                                            |
| tomli_loads         | 2.59 sec                                                              | 2.45 sec: 1.06x faster                                                          |
| pickle_pure_python  | 365 us                                                                | 371 us: 1.02x slower                                                            |
| json_dumps          | 12.3 ms                                                               | 13.9 ms: 1.14x slower                                                           |
| json_loads          | 30.7 us                                                               | 34.9 us: 1.14x slower                                                           |
| Geometric mean      | (ref)                                                                 | 1.01x slower                                                                    |

Benchmark hidden because not significant (3): xml_etree_generate, xml_etree_process, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250409-arminc-aarch64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 10.2 ms: 1.21x slower                                                           |
| python_startup         | 11.4 ms                                                               | 16.1 ms: 1.42x slower                                                           |
| Geometric mean         | (ref)                                                                 | 1.31x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250409-arminc-aarch64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako           | 12.9 ms                                                               | 14.1 ms: 1.09x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                                    |

Benchmark hidden because not significant (3): django_template, genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250409-arminc-aarch64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.66 sec: 2.06x faster                                                          |
| async_tree_memoization     | 777 ms                                                                | 464 ms: 1.68x faster                                                            |
| async_tree_io              | 1.41 sec                                                              | 878 ms: 1.61x faster                                                            |
| async_tree_none            | 624 ms                                                                | 389 ms: 1.60x faster                                                            |
| async_tree_memoization_tg  | 740 ms                                                                | 465 ms: 1.59x faster                                                            |
| async_tree_io_tg           | 1.40 sec                                                              | 893 ms: 1.57x faster                                                            |
| async_tree_none_tg         | 577 ms                                                                | 367 ms: 1.57x faster                                                            |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 665 ms: 1.37x faster                                                            |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 646 ms: 1.37x faster                                                            |
| deepcopy                   | 446 us                                                                | 328 us: 1.36x faster                                                            |
| deepcopy_memo              | 49.6 us                                                               | 38.0 us: 1.31x faster                                                           |
| generators                 | 43.5 ms                                                               | 36.0 ms: 1.21x faster                                                           |
| deepcopy_reduce            | 4.10 us                                                               | 3.42 us: 1.20x faster                                                           |
| go                         | 157 ms                                                                | 132 ms: 1.19x faster                                                            |
| comprehensions             | 25.4 us                                                               | 21.5 us: 1.18x faster                                                           |
| regex_effbot               | 4.64 ms                                                               | 3.94 ms: 1.18x faster                                                           |
| dulwich_log                | 62.0 ms                                                               | 52.7 ms: 1.18x faster                                                           |
| xml_etree_parse            | 195 ms                                                                | 175 ms: 1.12x faster                                                            |
| regex_compile              | 137 ms                                                                | 123 ms: 1.11x faster                                                            |
| pylint                     | 355 ms                                                                | 321 ms: 1.10x faster                                                            |
| sympy_sum                  | 154 ms                                                                | 141 ms: 1.09x faster                                                            |
| raytrace                   | 353 ms                                                                | 324 ms: 1.09x faster                                                            |
| logging_simple             | 7.63 us                                                               | 7.07 us: 1.08x faster                                                           |
| deltablue                  | 4.12 ms                                                               | 3.83 ms: 1.08x faster                                                           |
| sympy_integrate            | 21.6 ms                                                               | 20.1 ms: 1.07x faster                                                           |
| pathlib                    | 24.5 ms                                                               | 22.9 ms: 1.07x faster                                                           |
| logging_format             | 8.34 us                                                               | 7.79 us: 1.07x faster                                                           |
| float                      | 92.1 ms                                                               | 86.0 ms: 1.07x faster                                                           |
| sqlalchemy_imperative      | 16.7 ms                                                               | 15.6 ms: 1.07x faster                                                           |
| xml_etree_iterparse        | 150 ms                                                                | 141 ms: 1.06x faster                                                            |
| async_generators           | 491 ms                                                                | 462 ms: 1.06x faster                                                            |
| sqlalchemy_declarative     | 157 ms                                                                | 148 ms: 1.06x faster                                                            |
| tomli_loads                | 2.59 sec                                                              | 2.45 sec: 1.06x faster                                                          |
| scimark_monte_carlo        | 85.1 ms                                                               | 80.6 ms: 1.06x faster                                                           |
| chaos                      | 71.4 ms                                                               | 67.8 ms: 1.05x faster                                                           |
| regex_dna                  | 254 ms                                                                | 242 ms: 1.05x faster                                                            |
| sympy_str                  | 280 ms                                                                | 268 ms: 1.04x faster                                                            |
| scimark_lu                 | 146 ms                                                                | 140 ms: 1.04x faster                                                            |
| spectral_norm              | 131 ms                                                                | 126 ms: 1.03x faster                                                            |
| html5lib                   | 65.1 ms                                                               | 63.2 ms: 1.03x faster                                                           |
| 2to3                       | 308 ms                                                                | 300 ms: 1.03x faster                                                            |
| pyflate                    | 559 ms                                                                | 547 ms: 1.02x faster                                                            |
| docutils                   | 2.98 sec                                                              | 2.92 sec: 1.02x faster                                                          |
| pprint_safe_repr           | 916 ms                                                                | 902 ms: 1.02x faster                                                            |
| regex_v8                   | 28.3 ms                                                               | 28.0 ms: 1.01x faster                                                           |
| pprint_pformat             | 1.88 sec                                                              | 1.86 sec: 1.01x faster                                                          |
| crypto_pyaes               | 86.6 ms                                                               | 85.9 ms: 1.01x faster                                                           |
| asyncio_websockets         | 658 ms                                                                | 667 ms: 1.01x slower                                                            |
| pickle_pure_python         | 365 us                                                                | 371 us: 1.02x slower                                                            |
| sqlite_synth               | 3.77 us                                                               | 3.85 us: 1.02x slower                                                           |
| bench_thread_pool          | 1.31 ms                                                               | 1.35 ms: 1.03x slower                                                           |
| scimark_fft                | 418 ms                                                                | 433 ms: 1.04x slower                                                            |
| coroutines                 | 29.0 ms                                                               | 30.2 ms: 1.04x slower                                                           |
| fannkuch                   | 443 ms                                                                | 479 ms: 1.08x slower                                                            |
| json                       | 5.54 ms                                                               | 5.99 ms: 1.08x slower                                                           |
| mako                       | 12.9 ms                                                               | 14.1 ms: 1.09x slower                                                           |
| typing_runtime_protocols   | 181 us                                                                | 198 us: 1.09x slower                                                            |
| telco                      | 8.51 ms                                                               | 9.37 ms: 1.10x slower                                                           |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.82 ms: 1.10x slower                                                           |
| json_dumps                 | 12.3 ms                                                               | 13.9 ms: 1.14x slower                                                           |
| json_loads                 | 30.7 us                                                               | 34.9 us: 1.14x slower                                                           |
| nbody                      | 105 ms                                                                | 123 ms: 1.17x slower                                                            |
| coverage                   | 87.3 ms                                                               | 103 ms: 1.19x slower                                                            |
| python_startup_no_site     | 8.37 ms                                                               | 10.2 ms: 1.21x slower                                                           |
| python_startup             | 11.4 ms                                                               | 16.1 ms: 1.42x slower                                                           |
| gc_traversal               | 4.40 ms                                                               | 6.72 ms: 1.53x slower                                                           |
| create_gc_cycles           | 1.92 ms                                                               | 3.64 ms: 1.90x slower                                                           |
| bench_mp_pool              | 7.05 ms                                                               | 2.46 sec: 348.93x slower                                                        |
| Geometric mean             | (ref)                                                                 | 1.02x slower                                                                    |

Benchmark hidden because not significant (16): django_template, scimark_sor, richards_super, genshi_text, pycparser, logging_silent, nqueens, sympy_expand, meteor_contest, xml_etree_generate, richards, pidigits, genshi_xml, xml_etree_process, unpickle_pure_python, hexiom
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250409-3.14.0a7+-49ac4ce/bm-20250409-arminc-aarch64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.064x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.06x