# Results vs. 3.12.0

- fork: python
- ref: 155c44b9015089eacc6e
- machine: linux-aarch64
- commit hash: 155c44b
- commit date: 2025-03-12
- overall geometric mean: 1.051x faster
- HPT reliability: 99.97%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250312-arminc-aarch64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 294 ms: 1.05x faster                                                     |
| docutils       | 2.98 sec                                                              | 2.91 sec: 1.03x faster                                                   |
| html5lib       | 65.1 ms                                                               | 63.7 ms: 1.02x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250312-arminc-aarch64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 467 ms: 1.67x faster                                                     |
| async_tree_none            | 624 ms                                                                | 379 ms: 1.65x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 879 ms: 1.60x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 887 ms: 1.58x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 469 ms: 1.58x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 372 ms: 1.55x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 653 ms: 1.40x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 642 ms: 1.38x faster                                                     |
| Geometric mean             | (ref)                                                                 | 1.55x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250312-arminc-aarch64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 87.1 ms: 1.06x faster                                                    |
| nbody          | 105 ms                                                                | 124 ms: 1.18x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.05x slower                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250312-arminc-aarch64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.87 ms: 1.20x faster                                                    |
| regex_compile  | 137 ms                                                                | 125 ms: 1.09x faster                                                     |
| regex_dna      | 254 ms                                                                | 247 ms: 1.03x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.07x faster                                                             |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250312-arminc-aarch64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b |
|---------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse     | 195 ms                                                                | 175 ms: 1.11x faster                                                     |
| xml_etree_iterparse | 150 ms                                                                | 140 ms: 1.07x faster                                                     |
| tomli_loads         | 2.59 sec                                                              | 2.44 sec: 1.06x faster                                                   |
| xml_etree_process   | 79.0 ms                                                               | 79.6 ms: 1.01x slower                                                    |
| pickle_pure_python  | 365 us                                                                | 382 us: 1.05x slower                                                     |
| json_loads          | 30.7 us                                                               | 34.6 us: 1.13x slower                                                    |
| json_dumps          | 12.3 ms                                                               | 14.2 ms: 1.16x slower                                                    |
| Geometric mean      | (ref)                                                                 | 1.01x slower                                                             |

Benchmark hidden because not significant (2): xml_etree_generate, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250312-arminc-aarch64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 10.1 ms: 1.21x slower                                                    |
| python_startup         | 11.4 ms                                                               | 16.1 ms: 1.41x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.31x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250312-arminc-aarch64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml     | 60.6 ms                                                               | 59.9 ms: 1.01x faster                                                    |
| mako           | 12.9 ms                                                               | 14.1 ms: 1.09x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                             |

Benchmark hidden because not significant (2): genshi_text, django_template

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250312-arminc-aarch64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 467 ms: 1.67x faster                                                     |
| async_tree_none            | 624 ms                                                                | 379 ms: 1.65x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 879 ms: 1.60x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 887 ms: 1.58x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 469 ms: 1.58x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 372 ms: 1.55x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 653 ms: 1.40x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 642 ms: 1.38x faster                                                     |
| deepcopy                   | 446 us                                                                | 334 us: 1.33x faster                                                     |
| deepcopy_memo              | 49.6 us                                                               | 37.3 us: 1.33x faster                                                    |
| comprehensions             | 25.4 us                                                               | 20.9 us: 1.21x faster                                                    |
| generators                 | 43.5 ms                                                               | 36.2 ms: 1.20x faster                                                    |
| dulwich_log                | 62.0 ms                                                               | 51.7 ms: 1.20x faster                                                    |
| regex_effbot               | 4.64 ms                                                               | 3.87 ms: 1.20x faster                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 3.44 us: 1.19x faster                                                    |
| go                         | 157 ms                                                                | 135 ms: 1.17x faster                                                     |
| pylint                     | 355 ms                                                                | 312 ms: 1.14x faster                                                     |
| async_generators           | 491 ms                                                                | 434 ms: 1.13x faster                                                     |
| pathlib                    | 24.5 ms                                                               | 22.0 ms: 1.12x faster                                                    |
| xml_etree_parse            | 195 ms                                                                | 175 ms: 1.11x faster                                                     |
| raytrace                   | 353 ms                                                                | 319 ms: 1.11x faster                                                     |
| logging_simple             | 7.63 us                                                               | 6.97 us: 1.10x faster                                                    |
| regex_compile              | 137 ms                                                                | 125 ms: 1.09x faster                                                     |
| sympy_sum                  | 154 ms                                                                | 142 ms: 1.09x faster                                                     |
| logging_format             | 8.34 us                                                               | 7.67 us: 1.09x faster                                                    |
| sqlalchemy_declarative     | 157 ms                                                                | 145 ms: 1.08x faster                                                     |
| sqlalchemy_imperative      | 16.7 ms                                                               | 15.4 ms: 1.08x faster                                                    |
| spectral_norm              | 131 ms                                                                | 121 ms: 1.08x faster                                                     |
| xml_etree_iterparse        | 150 ms                                                                | 140 ms: 1.07x faster                                                     |
| tomli_loads                | 2.59 sec                                                              | 2.44 sec: 1.06x faster                                                   |
| float                      | 92.1 ms                                                               | 87.1 ms: 1.06x faster                                                    |
| 2to3                       | 308 ms                                                                | 294 ms: 1.05x faster                                                     |
| deltablue                  | 4.12 ms                                                               | 3.93 ms: 1.05x faster                                                    |
| sympy_integrate            | 21.6 ms                                                               | 20.9 ms: 1.03x faster                                                    |
| sympy_str                  | 280 ms                                                                | 270 ms: 1.03x faster                                                     |
| chaos                      | 71.4 ms                                                               | 69.1 ms: 1.03x faster                                                    |
| regex_dna                  | 254 ms                                                                | 247 ms: 1.03x faster                                                     |
| docutils                   | 2.98 sec                                                              | 2.91 sec: 1.03x faster                                                   |
| pyflate                    | 559 ms                                                                | 547 ms: 1.02x faster                                                     |
| html5lib                   | 65.1 ms                                                               | 63.7 ms: 1.02x faster                                                    |
| genshi_xml                 | 60.6 ms                                                               | 59.9 ms: 1.01x faster                                                    |
| mdp                        | 3.41 sec                                                              | 3.38 sec: 1.01x faster                                                   |
| meteor_contest             | 112 ms                                                                | 112 ms: 1.00x slower                                                     |
| nqueens                    | 99.2 ms                                                               | 99.7 ms: 1.00x slower                                                    |
| richards_super             | 58.5 ms                                                               | 59.0 ms: 1.01x slower                                                    |
| xml_etree_process          | 79.0 ms                                                               | 79.6 ms: 1.01x slower                                                    |
| sqlite_synth               | 3.77 us                                                               | 3.80 us: 1.01x slower                                                    |
| sympy_expand               | 454 ms                                                                | 462 ms: 1.02x slower                                                     |
| pprint_pformat             | 1.88 sec                                                              | 1.92 sec: 1.02x slower                                                   |
| thrift                     | 937 us                                                                | 956 us: 1.02x slower                                                     |
| pprint_safe_repr           | 916 ms                                                                | 938 ms: 1.02x slower                                                     |
| bench_thread_pool          | 1.31 ms                                                               | 1.35 ms: 1.03x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 7.21 ms: 1.03x slower                                                    |
| logging_silent             | 127 ns                                                                | 132 ns: 1.04x slower                                                     |
| pickle_pure_python         | 365 us                                                                | 382 us: 1.05x slower                                                     |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.50 ms: 1.05x slower                                                    |
| json                       | 5.54 ms                                                               | 5.87 ms: 1.06x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 193 us: 1.07x slower                                                     |
| mako                       | 12.9 ms                                                               | 14.1 ms: 1.09x slower                                                    |
| fannkuch                   | 443 ms                                                                | 492 ms: 1.11x slower                                                     |
| richards                   | 50.9 ms                                                               | 56.7 ms: 1.11x slower                                                    |
| json_loads                 | 30.7 us                                                               | 34.6 us: 1.13x slower                                                    |
| telco                      | 8.51 ms                                                               | 9.63 ms: 1.13x slower                                                    |
| coverage                   | 87.3 ms                                                               | 100 ms: 1.15x slower                                                     |
| json_dumps                 | 12.3 ms                                                               | 14.2 ms: 1.16x slower                                                    |
| nbody                      | 105 ms                                                                | 124 ms: 1.18x slower                                                     |
| python_startup_no_site     | 8.37 ms                                                               | 10.1 ms: 1.21x slower                                                    |
| python_startup             | 11.4 ms                                                               | 16.1 ms: 1.41x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 6.72 ms: 1.53x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 3.66 ms: 1.91x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 3.91 sec: 554.51x slower                                                 |
| Geometric mean             | (ref)                                                                 | 1.03x slower                                                             |

Benchmark hidden because not significant (14): scimark_monte_carlo, genshi_text, xml_etree_generate, asyncio_websockets, pycparser, unpickle_pure_python, django_template, scimark_sor, scimark_fft, crypto_pyaes, coroutines, regex_v8, pidigits, scimark_lu
Ignored benchmarks (17) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250312-3.14.0a5+-155c44b/bm-20250312-arminc-aarch64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.051x faster

# HPT report

- Reliability score: 99.97% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.06x