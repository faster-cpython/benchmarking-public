# Results vs. 3.12.0

- fork: python
- ref: fba5dded6df3c2b19435
- machine: linux-aarch64
- commit hash: fba5dde
- commit date: 2025-06-17
- overall geometric mean: 1.062x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 298 ms: 1.04x faster                                                    |
| docutils       | 2.98 sec                                                              | 2.94 sec: 1.01x faster                                                  |
| html5lib       | 65.1 ms                                                               | 61.3 ms: 1.06x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.04x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 470 ms: 1.65x faster                                                    |
| async_tree_none            | 624 ms                                                                | 395 ms: 1.58x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 897 ms: 1.57x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 472 ms: 1.57x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 915 ms: 1.53x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 383 ms: 1.50x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 662 ms: 1.38x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 662 ms: 1.34x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.51x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 85.7 ms: 1.07x faster                                                   |
| pidigits       | 233 ms                                                                | 238 ms: 1.02x slower                                                    |
| nbody          | 105 ms                                                                | 119 ms: 1.14x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.99 ms: 1.16x faster                                                   |
| regex_dna      | 254 ms                                                                | 223 ms: 1.14x faster                                                    |
| regex_compile  | 137 ms                                                                | 122 ms: 1.12x faster                                                    |
| regex_v8       | 28.3 ms                                                               | 26.5 ms: 1.07x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.12x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|---------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse     | 195 ms                                                                | 180 ms: 1.08x faster                                                    |
| tomli_loads         | 2.59 sec                                                              | 2.45 sec: 1.06x faster                                                  |
| xml_etree_iterparse | 150 ms                                                                | 142 ms: 1.06x faster                                                    |
| pickle_pure_python  | 365 us                                                                | 385 us: 1.05x slower                                                    |
| json_loads          | 30.7 us                                                               | 32.7 us: 1.07x slower                                                   |
| json_dumps          | 12.3 ms                                                               | 13.6 ms: 1.11x slower                                                   |
| Geometric mean      | (ref)                                                                 | 1.00x slower                                                            |

Benchmark hidden because not significant (3): xml_etree_process, xml_etree_generate, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.54 ms: 1.02x slower                                                   |
| python_startup         | 11.4 ms                                                               | 15.0 ms: 1.32x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.16x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako           | 12.9 ms                                                               | 13.8 ms: 1.07x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (3): django_template, genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.68 sec: 2.03x faster                                                  |
| async_tree_memoization     | 777 ms                                                                | 470 ms: 1.65x faster                                                    |
| async_tree_none            | 624 ms                                                                | 395 ms: 1.58x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 897 ms: 1.57x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 472 ms: 1.57x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 915 ms: 1.53x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 383 ms: 1.50x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 662 ms: 1.38x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 662 ms: 1.34x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 37.6 us: 1.32x faster                                                   |
| deepcopy                   | 446 us                                                                | 338 us: 1.32x faster                                                    |
| comprehensions             | 25.4 us                                                               | 20.4 us: 1.24x faster                                                   |
| go                         | 157 ms                                                                | 130 ms: 1.21x faster                                                    |
| generators                 | 43.5 ms                                                               | 36.0 ms: 1.21x faster                                                   |
| regex_effbot               | 4.64 ms                                                               | 3.99 ms: 1.16x faster                                                   |
| regex_dna                  | 254 ms                                                                | 223 ms: 1.14x faster                                                    |
| dulwich_log                | 62.0 ms                                                               | 54.4 ms: 1.14x faster                                                   |
| pylint                     | 355 ms                                                                | 315 ms: 1.13x faster                                                    |
| regex_compile              | 137 ms                                                                | 122 ms: 1.12x faster                                                    |
| async_generators           | 491 ms                                                                | 442 ms: 1.11x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 22.2 ms: 1.11x faster                                                   |
| deepcopy_reduce            | 4.10 us                                                               | 3.75 us: 1.09x faster                                                   |
| xml_etree_parse            | 195 ms                                                                | 180 ms: 1.08x faster                                                    |
| raytrace                   | 353 ms                                                                | 328 ms: 1.08x faster                                                    |
| float                      | 92.1 ms                                                               | 85.7 ms: 1.07x faster                                                   |
| scimark_monte_carlo        | 85.1 ms                                                               | 79.2 ms: 1.07x faster                                                   |
| regex_v8                   | 28.3 ms                                                               | 26.5 ms: 1.07x faster                                                   |
| sympy_str                  | 280 ms                                                                | 263 ms: 1.06x faster                                                    |
| sympy_integrate            | 21.6 ms                                                               | 20.4 ms: 1.06x faster                                                   |
| html5lib                   | 65.1 ms                                                               | 61.3 ms: 1.06x faster                                                   |
| tomli_loads                | 2.59 sec                                                              | 2.45 sec: 1.06x faster                                                  |
| xml_etree_iterparse        | 150 ms                                                                | 142 ms: 1.06x faster                                                    |
| pyflate                    | 559 ms                                                                | 532 ms: 1.05x faster                                                    |
| sympy_sum                  | 154 ms                                                                | 147 ms: 1.05x faster                                                    |
| spectral_norm              | 131 ms                                                                | 125 ms: 1.05x faster                                                    |
| chaos                      | 71.4 ms                                                               | 68.9 ms: 1.04x faster                                                   |
| 2to3                       | 308 ms                                                                | 298 ms: 1.04x faster                                                    |
| scimark_sor                | 150 ms                                                                | 145 ms: 1.03x faster                                                    |
| hexiom                     | 6.98 ms                                                               | 6.86 ms: 1.02x faster                                                   |
| pycparser                  | 1.26 sec                                                              | 1.24 sec: 1.01x faster                                                  |
| docutils                   | 2.98 sec                                                              | 2.94 sec: 1.01x faster                                                  |
| coroutines                 | 29.0 ms                                                               | 29.4 ms: 1.01x slower                                                   |
| sqlite_synth               | 3.77 us                                                               | 3.82 us: 1.01x slower                                                   |
| python_startup_no_site     | 8.37 ms                                                               | 8.54 ms: 1.02x slower                                                   |
| json                       | 5.54 ms                                                               | 5.65 ms: 1.02x slower                                                   |
| pidigits                   | 233 ms                                                                | 238 ms: 1.02x slower                                                    |
| thrift                     | 937 us                                                                | 961 us: 1.03x slower                                                    |
| richards                   | 50.9 ms                                                               | 52.6 ms: 1.03x slower                                                   |
| scimark_fft                | 418 ms                                                                | 432 ms: 1.03x slower                                                    |
| sympy_expand               | 454 ms                                                                | 469 ms: 1.03x slower                                                    |
| scimark_lu                 | 146 ms                                                                | 153 ms: 1.05x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 385 us: 1.05x slower                                                    |
| json_loads                 | 30.7 us                                                               | 32.7 us: 1.07x slower                                                   |
| mako                       | 12.9 ms                                                               | 13.8 ms: 1.07x slower                                                   |
| fannkuch                   | 443 ms                                                                | 477 ms: 1.08x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 195 us: 1.08x slower                                                    |
| telco                      | 8.51 ms                                                               | 9.23 ms: 1.09x slower                                                   |
| pprint_pformat             | 1.88 sec                                                              | 2.05 sec: 1.09x slower                                                  |
| pprint_safe_repr           | 916 ms                                                                | 1.01 sec: 1.10x slower                                                  |
| json_dumps                 | 12.3 ms                                                               | 13.6 ms: 1.11x slower                                                   |
| nbody                      | 105 ms                                                                | 119 ms: 1.14x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 7.13 ms: 1.15x slower                                                   |
| coverage                   | 87.3 ms                                                               | 103 ms: 1.18x slower                                                    |
| python_startup             | 11.4 ms                                                               | 15.0 ms: 1.32x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 7.00 ms: 1.59x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 3.84 ms: 2.00x slower                                                   |
| logging_silent             | 127 ns                                                                | 643 ns: 5.07x slower                                                    |
| Geometric mean             | (ref)                                                                 | 1.03x faster                                                            |

Benchmark hidden because not significant (14): crypto_pyaes, django_template, deltablue, nqueens, genshi_xml, logging_format, meteor_contest, xml_etree_process, xml_etree_generate, logging_simple, unpickle_pure_python, genshi_text, asyncio_websockets, richards_super
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.062x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.10x