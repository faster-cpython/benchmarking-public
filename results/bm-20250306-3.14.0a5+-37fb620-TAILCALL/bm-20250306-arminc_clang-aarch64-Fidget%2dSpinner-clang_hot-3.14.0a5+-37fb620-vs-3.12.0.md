# Results vs. 3.12.0

- fork: Fidget-Spinner
- ref: clang_hot
- machine: linux-aarch64
- commit hash: 37fb620
- commit date: 2025-03-06
- overall geometric mean: 1.057x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250306-arminc-aarch64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 296 ms: 1.04x faster                                                    |
| html5lib       | 65.1 ms                                                               | 60.4 ms: 1.08x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.04x faster                                                            |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250306-arminc-aarch64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 374 ms: 1.67x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 479 ms: 1.62x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 890 ms: 1.58x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 470 ms: 1.58x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 902 ms: 1.57x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 376 ms: 1.53x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 744 ms: 1.23x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 731 ms: 1.21x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.49x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250306-arminc-aarch64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 105 ms                                                                | 117 ms: 1.12x slower                                                    |
| pidigits       | 233 ms                                                                | 305 ms: 1.31x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.12x slower                                                            |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250306-arminc-aarch64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 125 ms: 1.10x faster                                                    |
| regex_effbot   | 4.64 ms                                                               | 4.41 ms: 1.05x faster                                                   |
| regex_v8       | 28.3 ms                                                               | 34.4 ms: 1.21x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                            |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250306-arminc-aarch64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|---------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads         | 2.59 sec                                                              | 2.43 sec: 1.07x faster                                                  |
| xml_etree_generate  | 112 ms                                                                | 107 ms: 1.05x faster                                                    |
| pickle_pure_python  | 365 us                                                                | 378 us: 1.04x slower                                                    |
| xml_etree_iterparse | 150 ms                                                                | 159 ms: 1.06x slower                                                    |
| json_loads          | 30.7 us                                                               | 35.0 us: 1.14x slower                                                   |
| json_dumps          | 12.3 ms                                                               | 14.0 ms: 1.14x slower                                                   |
| xml_etree_parse     | 195 ms                                                                | 224 ms: 1.15x slower                                                    |
| Geometric mean      | (ref)                                                                 | 1.04x slower                                                            |

Benchmark hidden because not significant (2): xml_etree_process, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250306-arminc-aarch64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 9.33 ms: 1.11x slower                                                   |
| python_startup         | 11.4 ms                                                               | 16.5 ms: 1.45x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.27x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250306-arminc-aarch64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 40.7 ms                                                               | 38.2 ms: 1.06x faster                                                   |
| mako            | 12.9 ms                                                               | 13.8 ms: 1.07x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.01x faster                                                            |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250306-arminc-aarch64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 374 ms: 1.67x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 479 ms: 1.62x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 890 ms: 1.58x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 470 ms: 1.58x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 902 ms: 1.57x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 376 ms: 1.53x faster                                                    |
| deepcopy                   | 446 us                                                                | 315 us: 1.42x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 36.4 us: 1.37x faster                                                   |
| comprehensions             | 25.4 us                                                               | 20.0 us: 1.27x faster                                                   |
| deepcopy_reduce            | 4.10 us                                                               | 3.31 us: 1.24x faster                                                   |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 744 ms: 1.23x faster                                                    |
| generators                 | 43.5 ms                                                               | 35.7 ms: 1.22x faster                                                   |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 731 ms: 1.21x faster                                                    |
| spectral_norm              | 131 ms                                                                | 109 ms: 1.20x faster                                                    |
| go                         | 157 ms                                                                | 133 ms: 1.19x faster                                                    |
| pylint                     | 355 ms                                                                | 302 ms: 1.17x faster                                                    |
| async_generators           | 491 ms                                                                | 418 ms: 1.17x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 21.3 ms: 1.15x faster                                                   |
| logging_format             | 8.34 us                                                               | 7.37 us: 1.13x faster                                                   |
| raytrace                   | 353 ms                                                                | 312 ms: 1.13x faster                                                    |
| logging_simple             | 7.63 us                                                               | 6.93 us: 1.10x faster                                                   |
| sympy_sum                  | 154 ms                                                                | 140 ms: 1.10x faster                                                    |
| regex_compile              | 137 ms                                                                | 125 ms: 1.10x faster                                                    |
| sqlalchemy_imperative      | 16.7 ms                                                               | 15.3 ms: 1.09x faster                                                   |
| sqlglot_transpile          | 1.83 ms                                                               | 1.69 ms: 1.08x faster                                                   |
| sqlalchemy_declarative     | 157 ms                                                                | 146 ms: 1.08x faster                                                    |
| html5lib                   | 65.1 ms                                                               | 60.4 ms: 1.08x faster                                                   |
| scimark_fft                | 418 ms                                                                | 391 ms: 1.07x faster                                                    |
| tomli_loads                | 2.59 sec                                                              | 2.43 sec: 1.07x faster                                                  |
| django_template            | 40.7 ms                                                               | 38.2 ms: 1.06x faster                                                   |
| chaos                      | 71.4 ms                                                               | 67.2 ms: 1.06x faster                                                   |
| deltablue                  | 4.12 ms                                                               | 3.91 ms: 1.05x faster                                                   |
| regex_effbot               | 4.64 ms                                                               | 4.41 ms: 1.05x faster                                                   |
| sqlglot_parse              | 1.46 ms                                                               | 1.39 ms: 1.05x faster                                                   |
| xml_etree_generate         | 112 ms                                                                | 107 ms: 1.05x faster                                                    |
| sympy_integrate            | 21.6 ms                                                               | 20.7 ms: 1.04x faster                                                   |
| 2to3                       | 308 ms                                                                | 296 ms: 1.04x faster                                                    |
| pyflate                    | 559 ms                                                                | 542 ms: 1.03x faster                                                    |
| mdp                        | 3.41 sec                                                              | 3.31 sec: 1.03x faster                                                  |
| pprint_pformat             | 1.88 sec                                                              | 1.92 sec: 1.02x slower                                                  |
| asyncio_websockets         | 658 ms                                                                | 675 ms: 1.03x slower                                                    |
| pprint_safe_repr           | 916 ms                                                                | 944 ms: 1.03x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 378 us: 1.04x slower                                                    |
| xml_etree_iterparse        | 150 ms                                                                | 159 ms: 1.06x slower                                                    |
| sqlite_synth               | 3.77 us                                                               | 3.99 us: 1.06x slower                                                   |
| mako                       | 12.9 ms                                                               | 13.8 ms: 1.07x slower                                                   |
| json                       | 5.54 ms                                                               | 5.95 ms: 1.07x slower                                                   |
| coverage                   | 87.3 ms                                                               | 93.9 ms: 1.08x slower                                                   |
| meteor_contest             | 112 ms                                                                | 121 ms: 1.08x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 9.33 ms: 1.11x slower                                                   |
| nbody                      | 105 ms                                                                | 117 ms: 1.12x slower                                                    |
| fannkuch                   | 443 ms                                                                | 498 ms: 1.12x slower                                                    |
| json_loads                 | 30.7 us                                                               | 35.0 us: 1.14x slower                                                   |
| json_dumps                 | 12.3 ms                                                               | 14.0 ms: 1.14x slower                                                   |
| telco                      | 8.51 ms                                                               | 9.73 ms: 1.14x slower                                                   |
| xml_etree_parse            | 195 ms                                                                | 224 ms: 1.15x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 34.4 ms: 1.21x slower                                                   |
| pidigits                   | 233 ms                                                                | 305 ms: 1.31x slower                                                    |
| python_startup             | 11.4 ms                                                               | 16.5 ms: 1.45x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 6.73 ms: 1.53x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 3.68 ms: 1.92x slower                                                   |
| bench_mp_pool              | 7.05 ms                                                               | 7.27 sec: 1030.38x slower                                               |
| Geometric mean             | (ref)                                                                 | 1.04x slower                                                            |

Benchmark hidden because not significant (27): scimark_monte_carlo, float, sympy_str, scimark_lu, logging_silent, scimark_sor, dulwich_log, xml_etree_process, richards, genshi_text, sqlglot_normalize, coroutines, sqlglot_optimize, richards_super, docutils, genshi_xml, sympy_expand, bench_thread_pool, pycparser, scimark_sparse_mat_mult, nqueens, typing_runtime_protocols, unpickle_pure_python, regex_dna, thrift, crypto_pyaes, hexiom
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (7) of results/bm-20250306-3.14.0a5+-37fb620-CLANG/bm-20250306-arminc-aarch64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.057x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.08x