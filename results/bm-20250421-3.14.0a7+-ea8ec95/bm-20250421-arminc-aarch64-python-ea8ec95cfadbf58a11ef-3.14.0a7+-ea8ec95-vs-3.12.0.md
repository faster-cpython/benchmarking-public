# Results vs. 3.12.0

- fork: python
- ref: ea8ec95cfadbf58a11ef
- machine: linux-aarch64
- commit hash: ea8ec95
- commit date: 2025-04-21
- overall geometric mean: 1.064x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250421-arminc-aarch64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 297 ms: 1.04x faster                                                     |
| html5lib       | 65.1 ms                                                               | 62.4 ms: 1.04x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                             |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250421-arminc-aarch64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 481 ms: 1.62x faster                                                     |
| async_tree_none            | 624 ms                                                                | 390 ms: 1.60x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 882 ms: 1.60x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 475 ms: 1.56x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 906 ms: 1.55x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 383 ms: 1.50x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 665 ms: 1.37x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 657 ms: 1.35x faster                                                     |
| Geometric mean             | (ref)                                                                 | 1.51x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250421-arminc-aarch64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 83.3 ms: 1.11x faster                                                    |
| nbody          | 105 ms                                                                | 116 ms: 1.11x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250421-arminc-aarch64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.73 ms: 1.24x faster                                                    |
| regex_compile  | 137 ms                                                                | 124 ms: 1.11x faster                                                     |
| regex_dna      | 254 ms                                                                | 234 ms: 1.09x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.10x faster                                                             |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250421-arminc-aarch64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|---------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse     | 195 ms                                                                | 181 ms: 1.08x faster                                                     |
| tomli_loads         | 2.59 sec                                                              | 2.46 sec: 1.06x faster                                                   |
| xml_etree_iterparse | 150 ms                                                                | 143 ms: 1.05x faster                                                     |
| xml_etree_generate  | 112 ms                                                                | 113 ms: 1.00x slower                                                     |
| xml_etree_process   | 79.0 ms                                                               | 80.0 ms: 1.01x slower                                                    |
| pickle_pure_python  | 365 us                                                                | 381 us: 1.04x slower                                                     |
| json_loads          | 30.7 us                                                               | 34.5 us: 1.13x slower                                                    |
| json_dumps          | 12.3 ms                                                               | 14.2 ms: 1.16x slower                                                    |
| Geometric mean      | (ref)                                                                 | 1.02x slower                                                             |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250421-arminc-aarch64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 10.2 ms: 1.22x slower                                                    |
| python_startup         | 11.4 ms                                                               | 16.2 ms: 1.42x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.32x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250421-arminc-aarch64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text    | 27.4 ms                                                               | 26.5 ms: 1.03x faster                                                    |
| mako           | 12.9 ms                                                               | 14.1 ms: 1.09x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                             |

Benchmark hidden because not significant (2): django_template, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250421-arminc-aarch64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.68 sec: 2.03x faster                                                   |
| async_tree_memoization     | 777 ms                                                                | 481 ms: 1.62x faster                                                     |
| async_tree_none            | 624 ms                                                                | 390 ms: 1.60x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 882 ms: 1.60x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 475 ms: 1.56x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 906 ms: 1.55x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 383 ms: 1.50x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 665 ms: 1.37x faster                                                     |
| deepcopy                   | 446 us                                                                | 329 us: 1.35x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 657 ms: 1.35x faster                                                     |
| deepcopy_memo              | 49.6 us                                                               | 37.6 us: 1.32x faster                                                    |
| regex_effbot               | 4.64 ms                                                               | 3.73 ms: 1.24x faster                                                    |
| dulwich_log                | 62.0 ms                                                               | 51.9 ms: 1.19x faster                                                    |
| go                         | 157 ms                                                                | 132 ms: 1.19x faster                                                     |
| comprehensions             | 25.4 us                                                               | 21.5 us: 1.18x faster                                                    |
| generators                 | 43.5 ms                                                               | 36.8 ms: 1.18x faster                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 3.51 us: 1.17x faster                                                    |
| pylint                     | 355 ms                                                                | 315 ms: 1.13x faster                                                     |
| regex_compile              | 137 ms                                                                | 124 ms: 1.11x faster                                                     |
| float                      | 92.1 ms                                                               | 83.3 ms: 1.11x faster                                                    |
| raytrace                   | 353 ms                                                                | 324 ms: 1.09x faster                                                     |
| logging_simple             | 7.63 us                                                               | 7.01 us: 1.09x faster                                                    |
| regex_dna                  | 254 ms                                                                | 234 ms: 1.09x faster                                                     |
| async_generators           | 491 ms                                                                | 453 ms: 1.08x faster                                                     |
| pathlib                    | 24.5 ms                                                               | 22.7 ms: 1.08x faster                                                    |
| xml_etree_parse            | 195 ms                                                                | 181 ms: 1.08x faster                                                     |
| sympy_sum                  | 154 ms                                                                | 144 ms: 1.08x faster                                                     |
| sqlalchemy_declarative     | 157 ms                                                                | 147 ms: 1.07x faster                                                     |
| sympy_integrate            | 21.6 ms                                                               | 20.3 ms: 1.07x faster                                                    |
| logging_format             | 8.34 us                                                               | 7.82 us: 1.07x faster                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 79.8 ms: 1.07x faster                                                    |
| sqlalchemy_imperative      | 16.7 ms                                                               | 15.7 ms: 1.06x faster                                                    |
| tomli_loads                | 2.59 sec                                                              | 2.46 sec: 1.06x faster                                                   |
| xml_etree_iterparse        | 150 ms                                                                | 143 ms: 1.05x faster                                                     |
| pyflate                    | 559 ms                                                                | 531 ms: 1.05x faster                                                     |
| crypto_pyaes               | 86.6 ms                                                               | 82.5 ms: 1.05x faster                                                    |
| html5lib                   | 65.1 ms                                                               | 62.4 ms: 1.04x faster                                                    |
| deltablue                  | 4.12 ms                                                               | 3.96 ms: 1.04x faster                                                    |
| spectral_norm              | 131 ms                                                                | 126 ms: 1.04x faster                                                     |
| 2to3                       | 308 ms                                                                | 297 ms: 1.04x faster                                                     |
| genshi_text                | 27.4 ms                                                               | 26.5 ms: 1.03x faster                                                    |
| pprint_safe_repr           | 916 ms                                                                | 891 ms: 1.03x faster                                                     |
| pprint_pformat             | 1.88 sec                                                              | 1.83 sec: 1.03x faster                                                   |
| xml_etree_generate         | 112 ms                                                                | 113 ms: 1.00x slower                                                     |
| xml_etree_process          | 79.0 ms                                                               | 80.0 ms: 1.01x slower                                                    |
| asyncio_websockets         | 658 ms                                                                | 672 ms: 1.02x slower                                                     |
| bench_thread_pool          | 1.31 ms                                                               | 1.36 ms: 1.04x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 7.28 ms: 1.04x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 381 us: 1.04x slower                                                     |
| coroutines                 | 29.0 ms                                                               | 30.3 ms: 1.04x slower                                                    |
| fannkuch                   | 443 ms                                                                | 464 ms: 1.05x slower                                                     |
| logging_silent             | 127 ns                                                                | 133 ns: 1.05x slower                                                     |
| richards                   | 50.9 ms                                                               | 53.5 ms: 1.05x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.72 ms: 1.08x slower                                                    |
| mako                       | 12.9 ms                                                               | 14.1 ms: 1.09x slower                                                    |
| json                       | 5.54 ms                                                               | 6.07 ms: 1.10x slower                                                    |
| nbody                      | 105 ms                                                                | 116 ms: 1.11x slower                                                     |
| json_loads                 | 30.7 us                                                               | 34.5 us: 1.13x slower                                                    |
| telco                      | 8.51 ms                                                               | 9.59 ms: 1.13x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 205 us: 1.14x slower                                                     |
| json_dumps                 | 12.3 ms                                                               | 14.2 ms: 1.16x slower                                                    |
| coverage                   | 87.3 ms                                                               | 102 ms: 1.17x slower                                                     |
| python_startup_no_site     | 8.37 ms                                                               | 10.2 ms: 1.22x slower                                                    |
| python_startup             | 11.4 ms                                                               | 16.2 ms: 1.42x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 6.54 ms: 1.49x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 3.54 ms: 1.84x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 4.59 sec: 650.04x slower                                                 |
| Geometric mean             | (ref)                                                                 | 1.03x slower                                                             |

Benchmark hidden because not significant (17): chaos, sympy_str, django_template, nqueens, scimark_sor, scimark_fft, docutils, genshi_xml, richards_super, pycparser, sympy_expand, meteor_contest, pidigits, unpickle_pure_python, sqlite_synth, regex_v8, scimark_lu
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250421-3.14.0a7+-ea8ec95/bm-20250421-arminc-aarch64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.064x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.06x