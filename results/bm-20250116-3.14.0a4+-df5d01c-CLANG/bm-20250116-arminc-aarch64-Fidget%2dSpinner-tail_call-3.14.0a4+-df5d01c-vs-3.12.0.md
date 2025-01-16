# Results vs. 3.12.0

- fork: Fidget-Spinner
- ref: tail_call
- machine: linux-aarch64
- commit hash: df5d01c
- commit date: 2025-01-16
- overall geometric mean: 1.062x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250116-arminc-aarch64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 298 ms: 1.03x faster                                                    |
| html5lib       | 65.1 ms                                                               | 60.3 ms: 1.08x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                            |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250116-arminc-aarch64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.40 sec                                                              | 867 ms: 1.62x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 876 ms: 1.61x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 460 ms: 1.61x faster                                                    |
| async_tree_none            | 624 ms                                                                | 388 ms: 1.61x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 487 ms: 1.59x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 368 ms: 1.57x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 755 ms: 1.21x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 735 ms: 1.20x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.49x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250116-arminc-aarch64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 83.8 ms: 1.10x faster                                                   |
| pidigits       | 233 ms                                                                | 302 ms: 1.30x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.07x slower                                                            |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250116-arminc-aarch64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 125 ms: 1.10x faster                                                    |
| regex_v8       | 28.3 ms                                                               | 34.2 ms: 1.21x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                            |

Benchmark hidden because not significant (2): regex_effbot, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250116-arminc-aarch64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|--------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads        | 2.59 sec                                                              | 2.46 sec: 1.05x faster                                                  |
| pickle_pure_python | 365 us                                                                | 388 us: 1.06x slower                                                    |
| xml_etree_parse    | 195 ms                                                                | 207 ms: 1.06x slower                                                    |
| json_loads         | 30.7 us                                                               | 33.2 us: 1.08x slower                                                   |
| json_dumps         | 12.3 ms                                                               | 14.9 ms: 1.22x slower                                                   |
| Geometric mean     | (ref)                                                                 | 1.03x slower                                                            |

Benchmark hidden because not significant (4): xml_etree_generate, unpickle_pure_python, xml_etree_process, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250116-arminc-aarch64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 9.10 ms: 1.09x slower                                                   |
| python_startup         | 11.4 ms                                                               | 16.5 ms: 1.45x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.26x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250116-arminc-aarch64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako           | 12.9 ms                                                               | 14.1 ms: 1.09x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                            |

Benchmark hidden because not significant (3): genshi_text, genshi_xml, django_template

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250116-arminc-aarch64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.40 sec                                                              | 867 ms: 1.62x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 876 ms: 1.61x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 460 ms: 1.61x faster                                                    |
| async_tree_none            | 624 ms                                                                | 388 ms: 1.61x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 487 ms: 1.59x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 368 ms: 1.57x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 36.7 us: 1.35x faster                                                   |
| deepcopy                   | 446 us                                                                | 335 us: 1.33x faster                                                    |
| comprehensions             | 25.4 us                                                               | 20.2 us: 1.26x faster                                                   |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 755 ms: 1.21x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 735 ms: 1.20x faster                                                    |
| go                         | 157 ms                                                                | 132 ms: 1.19x faster                                                    |
| generators                 | 43.5 ms                                                               | 36.6 ms: 1.19x faster                                                   |
| deepcopy_reduce            | 4.10 us                                                               | 3.49 us: 1.18x faster                                                   |
| pathlib                    | 24.5 ms                                                               | 20.9 ms: 1.17x faster                                                   |
| async_generators           | 491 ms                                                                | 419 ms: 1.17x faster                                                    |
| pylint                     | 355 ms                                                                | 303 ms: 1.17x faster                                                    |
| raytrace                   | 353 ms                                                                | 312 ms: 1.13x faster                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 75.3 ms: 1.13x faster                                                   |
| spectral_norm              | 131 ms                                                                | 116 ms: 1.13x faster                                                    |
| logging_simple             | 7.63 us                                                               | 6.86 us: 1.11x faster                                                   |
| scimark_fft                | 418 ms                                                                | 377 ms: 1.11x faster                                                    |
| regex_compile              | 137 ms                                                                | 125 ms: 1.10x faster                                                    |
| float                      | 92.1 ms                                                               | 83.8 ms: 1.10x faster                                                   |
| deltablue                  | 4.12 ms                                                               | 3.76 ms: 1.10x faster                                                   |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 5.67 ms: 1.09x faster                                                   |
| logging_silent             | 127 ns                                                                | 117 ns: 1.08x faster                                                    |
| html5lib                   | 65.1 ms                                                               | 60.3 ms: 1.08x faster                                                   |
| logging_format             | 8.34 us                                                               | 7.75 us: 1.08x faster                                                   |
| sqlalchemy_imperative      | 16.7 ms                                                               | 15.5 ms: 1.08x faster                                                   |
| scimark_lu                 | 146 ms                                                                | 136 ms: 1.07x faster                                                    |
| sympy_str                  | 280 ms                                                                | 261 ms: 1.07x faster                                                    |
| sympy_sum                  | 154 ms                                                                | 144 ms: 1.07x faster                                                    |
| sqlglot_parse              | 1.46 ms                                                               | 1.37 ms: 1.07x faster                                                   |
| richards                   | 50.9 ms                                                               | 47.9 ms: 1.06x faster                                                   |
| scimark_sor                | 150 ms                                                                | 141 ms: 1.06x faster                                                    |
| chaos                      | 71.4 ms                                                               | 67.5 ms: 1.06x faster                                                   |
| dulwich_log                | 62.0 ms                                                               | 58.7 ms: 1.06x faster                                                   |
| tomli_loads                | 2.59 sec                                                              | 2.46 sec: 1.05x faster                                                  |
| pyflate                    | 559 ms                                                                | 531 ms: 1.05x faster                                                    |
| sqlalchemy_declarative     | 157 ms                                                                | 150 ms: 1.05x faster                                                    |
| mdp                        | 3.41 sec                                                              | 3.27 sec: 1.04x faster                                                  |
| 2to3                       | 308 ms                                                                | 298 ms: 1.03x faster                                                    |
| sympy_integrate            | 21.6 ms                                                               | 20.9 ms: 1.03x faster                                                   |
| coroutines                 | 29.0 ms                                                               | 28.2 ms: 1.03x faster                                                   |
| nqueens                    | 99.2 ms                                                               | 101 ms: 1.02x slower                                                    |
| asyncio_websockets         | 658 ms                                                                | 675 ms: 1.03x slower                                                    |
| sympy_expand               | 454 ms                                                                | 476 ms: 1.05x slower                                                    |
| pprint_pformat             | 1.88 sec                                                              | 1.98 sec: 1.05x slower                                                  |
| json                       | 5.54 ms                                                               | 5.85 ms: 1.06x slower                                                   |
| pprint_safe_repr           | 916 ms                                                                | 970 ms: 1.06x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 388 us: 1.06x slower                                                    |
| meteor_contest             | 112 ms                                                                | 119 ms: 1.06x slower                                                    |
| xml_etree_parse            | 195 ms                                                                | 207 ms: 1.06x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 194 us: 1.08x slower                                                    |
| telco                      | 8.51 ms                                                               | 9.16 ms: 1.08x slower                                                   |
| json_loads                 | 30.7 us                                                               | 33.2 us: 1.08x slower                                                   |
| python_startup_no_site     | 8.37 ms                                                               | 9.10 ms: 1.09x slower                                                   |
| mako                       | 12.9 ms                                                               | 14.1 ms: 1.09x slower                                                   |
| sqlite_synth               | 3.77 us                                                               | 4.13 us: 1.09x slower                                                   |
| fannkuch                   | 443 ms                                                                | 487 ms: 1.10x slower                                                    |
| coverage                   | 87.3 ms                                                               | 98.5 ms: 1.13x slower                                                   |
| regex_v8                   | 28.3 ms                                                               | 34.2 ms: 1.21x slower                                                   |
| json_dumps                 | 12.3 ms                                                               | 14.9 ms: 1.22x slower                                                   |
| pidigits                   | 233 ms                                                                | 302 ms: 1.30x slower                                                    |
| python_startup             | 11.4 ms                                                               | 16.5 ms: 1.45x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 6.67 ms: 1.52x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 3.70 ms: 1.93x slower                                                   |
| bench_mp_pool              | 7.05 ms                                                               | 6.83 sec: 968.77x slower                                                |
| Geometric mean             | (ref)                                                                 | 1.04x slower                                                            |

Benchmark hidden because not significant (20): regex_effbot, richards_super, genshi_text, xml_etree_generate, unpickle_pure_python, xml_etree_process, sqlglot_transpile, crypto_pyaes, genshi_xml, docutils, pycparser, xml_etree_iterparse, hexiom, django_template, bench_thread_pool, sqlglot_optimize, nbody, thrift, sqlglot_normalize, regex_dna
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (7) of results/bm-20250116-3.14.0a4+-df5d01c-CLANG/bm-20250116-arminc-aarch64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.062x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.08x