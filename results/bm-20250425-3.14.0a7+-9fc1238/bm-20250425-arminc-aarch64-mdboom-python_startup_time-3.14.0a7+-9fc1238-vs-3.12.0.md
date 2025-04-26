# Results vs. 3.12.0

- fork: mdboom
- ref: python_startup_time
- machine: linux-aarch64
- commit hash: 9fc1238
- commit date: 2025-04-25
- overall geometric mean: 1.074x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250425-arminc-aarch64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 298 ms: 1.03x faster                                                    |
| docutils       | 2.98 sec                                                              | 2.94 sec: 1.02x faster                                                  |
| html5lib       | 65.1 ms                                                               | 61.5 ms: 1.06x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.04x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250425-arminc-aarch64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 464 ms: 1.67x faster                                                    |
| async_tree_none            | 624 ms                                                                | 386 ms: 1.62x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 466 ms: 1.59x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 892 ms: 1.58x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 902 ms: 1.56x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 373 ms: 1.55x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 662 ms: 1.38x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 649 ms: 1.36x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.53x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250425-arminc-aarch64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 83.3 ms: 1.10x faster                                                   |
| pidigits       | 233 ms                                                                | 234 ms: 1.01x slower                                                    |
| nbody          | 105 ms                                                                | 119 ms: 1.14x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250425-arminc-aarch64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.84 ms: 1.21x faster                                                   |
| regex_compile  | 137 ms                                                                | 120 ms: 1.15x faster                                                    |
| regex_dna      | 254 ms                                                                | 236 ms: 1.07x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.11x faster                                                            |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250425-arminc-aarch64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|---------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse     | 195 ms                                                                | 179 ms: 1.09x faster                                                    |
| xml_etree_iterparse | 150 ms                                                                | 141 ms: 1.07x faster                                                    |
| tomli_loads         | 2.59 sec                                                              | 2.44 sec: 1.06x faster                                                  |
| xml_etree_process   | 79.0 ms                                                               | 80.2 ms: 1.02x slower                                                   |
| pickle_pure_python  | 365 us                                                                | 379 us: 1.04x slower                                                    |
| json_loads          | 30.7 us                                                               | 34.2 us: 1.11x slower                                                   |
| json_dumps          | 12.3 ms                                                               | 13.8 ms: 1.13x slower                                                   |
| Geometric mean      | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (2): xml_etree_generate, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250425-arminc-aarch64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 9.08 ms: 1.08x slower                                                   |
| python_startup         | 11.4 ms                                                               | 16.3 ms: 1.44x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.25x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250425-arminc-aarch64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text    | 27.4 ms                                                               | 26.0 ms: 1.06x faster                                                   |
| mako           | 12.9 ms                                                               | 13.7 ms: 1.06x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                            |

Benchmark hidden because not significant (2): django_template, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250425-arminc-aarch64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.62 sec: 2.10x faster                                                  |
| async_tree_memoization     | 777 ms                                                                | 464 ms: 1.67x faster                                                    |
| async_tree_none            | 624 ms                                                                | 386 ms: 1.62x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 466 ms: 1.59x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 892 ms: 1.58x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 902 ms: 1.56x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 373 ms: 1.55x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 662 ms: 1.38x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 649 ms: 1.36x faster                                                    |
| deepcopy                   | 446 us                                                                | 330 us: 1.35x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 38.2 us: 1.30x faster                                                   |
| comprehensions             | 25.4 us                                                               | 21.0 us: 1.21x faster                                                   |
| regex_effbot               | 4.64 ms                                                               | 3.84 ms: 1.21x faster                                                   |
| deepcopy_reduce            | 4.10 us                                                               | 3.40 us: 1.21x faster                                                   |
| go                         | 157 ms                                                                | 131 ms: 1.20x faster                                                    |
| generators                 | 43.5 ms                                                               | 36.5 ms: 1.19x faster                                                   |
| dulwich_log                | 62.0 ms                                                               | 52.6 ms: 1.18x faster                                                   |
| regex_compile              | 137 ms                                                                | 120 ms: 1.15x faster                                                    |
| pylint                     | 355 ms                                                                | 312 ms: 1.14x faster                                                    |
| logging_simple             | 7.63 us                                                               | 6.90 us: 1.11x faster                                                   |
| float                      | 92.1 ms                                                               | 83.3 ms: 1.10x faster                                                   |
| async_generators           | 491 ms                                                                | 446 ms: 1.10x faster                                                    |
| raytrace                   | 353 ms                                                                | 325 ms: 1.09x faster                                                    |
| logging_format             | 8.34 us                                                               | 7.67 us: 1.09x faster                                                   |
| xml_etree_parse            | 195 ms                                                                | 179 ms: 1.09x faster                                                    |
| sympy_sum                  | 154 ms                                                                | 142 ms: 1.08x faster                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 78.5 ms: 1.08x faster                                                   |
| sympy_str                  | 280 ms                                                                | 258 ms: 1.08x faster                                                    |
| sympy_integrate            | 21.6 ms                                                               | 20.0 ms: 1.08x faster                                                   |
| pathlib                    | 24.5 ms                                                               | 22.8 ms: 1.08x faster                                                   |
| sqlalchemy_imperative      | 16.7 ms                                                               | 15.5 ms: 1.08x faster                                                   |
| regex_dna                  | 254 ms                                                                | 236 ms: 1.07x faster                                                    |
| pyflate                    | 559 ms                                                                | 521 ms: 1.07x faster                                                    |
| chaos                      | 71.4 ms                                                               | 66.5 ms: 1.07x faster                                                   |
| xml_etree_iterparse        | 150 ms                                                                | 141 ms: 1.07x faster                                                    |
| sqlalchemy_declarative     | 157 ms                                                                | 147 ms: 1.07x faster                                                    |
| spectral_norm              | 131 ms                                                                | 123 ms: 1.06x faster                                                    |
| tomli_loads                | 2.59 sec                                                              | 2.44 sec: 1.06x faster                                                  |
| html5lib                   | 65.1 ms                                                               | 61.5 ms: 1.06x faster                                                   |
| genshi_text                | 27.4 ms                                                               | 26.0 ms: 1.06x faster                                                   |
| deltablue                  | 4.12 ms                                                               | 3.92 ms: 1.05x faster                                                   |
| crypto_pyaes               | 86.6 ms                                                               | 82.7 ms: 1.05x faster                                                   |
| 2to3                       | 308 ms                                                                | 298 ms: 1.03x faster                                                    |
| nqueens                    | 99.2 ms                                                               | 96.3 ms: 1.03x faster                                                   |
| pprint_safe_repr           | 916 ms                                                                | 898 ms: 1.02x faster                                                    |
| docutils                   | 2.98 sec                                                              | 2.94 sec: 1.02x faster                                                  |
| sqlite_synth               | 3.77 us                                                               | 3.80 us: 1.01x slower                                                   |
| pidigits                   | 233 ms                                                                | 234 ms: 1.01x slower                                                    |
| asyncio_websockets         | 658 ms                                                                | 667 ms: 1.01x slower                                                    |
| xml_etree_process          | 79.0 ms                                                               | 80.2 ms: 1.02x slower                                                   |
| logging_silent             | 127 ns                                                                | 129 ns: 1.02x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 379 us: 1.04x slower                                                    |
| coroutines                 | 29.0 ms                                                               | 30.4 ms: 1.05x slower                                                   |
| bench_thread_pool          | 1.31 ms                                                               | 1.37 ms: 1.05x slower                                                   |
| mako                       | 12.9 ms                                                               | 13.7 ms: 1.06x slower                                                   |
| fannkuch                   | 443 ms                                                                | 471 ms: 1.06x slower                                                    |
| json                       | 5.54 ms                                                               | 6.01 ms: 1.08x slower                                                   |
| python_startup_no_site     | 8.37 ms                                                               | 9.08 ms: 1.08x slower                                                   |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.77 ms: 1.09x slower                                                   |
| telco                      | 8.51 ms                                                               | 9.32 ms: 1.10x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 201 us: 1.11x slower                                                    |
| json_loads                 | 30.7 us                                                               | 34.2 us: 1.11x slower                                                   |
| json_dumps                 | 12.3 ms                                                               | 13.8 ms: 1.13x slower                                                   |
| nbody                      | 105 ms                                                                | 119 ms: 1.14x slower                                                    |
| coverage                   | 87.3 ms                                                               | 102 ms: 1.17x slower                                                    |
| python_startup             | 11.4 ms                                                               | 16.3 ms: 1.44x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 6.59 ms: 1.50x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 3.58 ms: 1.87x slower                                                   |
| bench_mp_pool              | 7.05 ms                                                               | 4.67 sec: 662.43x slower                                                |
| Geometric mean             | (ref)                                                                 | 1.02x slower                                                            |

Benchmark hidden because not significant (15): django_template, regex_v8, scimark_fft, pycparser, scimark_sor, pprint_pformat, xml_etree_generate, sympy_expand, richards_super, genshi_xml, meteor_contest, unpickle_pure_python, scimark_lu, richards, hexiom
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250425-3.14.0a7+-9fc1238/bm-20250425-arminc-aarch64-mdboom-python_startup_time-3.14.0a7+-9fc1238.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.074x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.06x