# Results vs. 3.12.0

- fork: zooba
- ref: gh_91349
- machine: linux-aarch64
- commit hash: 548daa7
- commit date: 2025-03-19
- overall geometric mean: 1.042x faster
- HPT reliability: 99.62%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250319-arminc-aarch64-zooba-gh_91349-3.14.0a6+-548daa7 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 301 ms: 1.02x faster                                        |
| docutils       | 2.98 sec                                                              | 3.07 sec: 1.03x slower                                      |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250319-arminc-aarch64-zooba-gh_91349-3.14.0a6+-548daa7 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 468 ms: 1.66x faster                                        |
| async_tree_none            | 624 ms                                                                | 383 ms: 1.63x faster                                        |
| async_tree_io              | 1.41 sec                                                              | 884 ms: 1.60x faster                                        |
| async_tree_memoization_tg  | 740 ms                                                                | 467 ms: 1.58x faster                                        |
| async_tree_none_tg         | 577 ms                                                                | 370 ms: 1.56x faster                                        |
| async_tree_io_tg           | 1.40 sec                                                              | 918 ms: 1.53x faster                                        |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 658 ms: 1.39x faster                                        |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 648 ms: 1.36x faster                                        |
| Geometric mean             | (ref)                                                                 | 1.54x faster                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250319-arminc-aarch64-zooba-gh_91349-3.14.0a6+-548daa7 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------:|
| float          | 92.1 ms                                                               | 87.0 ms: 1.06x faster                                       |
| pidigits       | 233 ms                                                                | 237 ms: 1.02x slower                                        |
| nbody          | 105 ms                                                                | 125 ms: 1.20x slower                                        |
| Geometric mean | (ref)                                                                 | 1.05x slower                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250319-arminc-aarch64-zooba-gh_91349-3.14.0a6+-548daa7 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.01 ms: 1.16x faster                                       |
| regex_compile  | 137 ms                                                                | 127 ms: 1.08x faster                                        |
| regex_dna      | 254 ms                                                                | 247 ms: 1.03x faster                                        |
| Geometric mean | (ref)                                                                 | 1.06x faster                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250319-arminc-aarch64-zooba-gh_91349-3.14.0a6+-548daa7 |
|---------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------:|
| xml_etree_parse     | 195 ms                                                                | 176 ms: 1.11x faster                                        |
| xml_etree_iterparse | 150 ms                                                                | 141 ms: 1.07x faster                                        |
| tomli_loads         | 2.59 sec                                                              | 2.45 sec: 1.06x faster                                      |
| xml_etree_process   | 79.0 ms                                                               | 79.4 ms: 1.01x slower                                       |
| pickle_pure_python  | 365 us                                                                | 386 us: 1.06x slower                                        |
| json_loads          | 30.7 us                                                               | 35.2 us: 1.15x slower                                       |
| json_dumps          | 12.3 ms                                                               | 14.1 ms: 1.15x slower                                       |
| Geometric mean      | (ref)                                                                 | 1.02x slower                                                |

Benchmark hidden because not significant (2): xml_etree_generate, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250319-arminc-aarch64-zooba-gh_91349-3.14.0a6+-548daa7 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 10.2 ms: 1.21x slower                                       |
| python_startup         | 11.4 ms                                                               | 16.1 ms: 1.42x slower                                       |
| Geometric mean         | (ref)                                                                 | 1.31x slower                                                |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250319-arminc-aarch64-zooba-gh_91349-3.14.0a6+-548daa7 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------:|
| genshi_text    | 27.4 ms                                                               | 27.0 ms: 1.02x faster                                       |
| mako           | 12.9 ms                                                               | 14.1 ms: 1.10x slower                                       |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                |

Benchmark hidden because not significant (2): genshi_xml, django_template

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250319-arminc-aarch64-zooba-gh_91349-3.14.0a6+-548daa7 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 468 ms: 1.66x faster                                        |
| async_tree_none            | 624 ms                                                                | 383 ms: 1.63x faster                                        |
| async_tree_io              | 1.41 sec                                                              | 884 ms: 1.60x faster                                        |
| async_tree_memoization_tg  | 740 ms                                                                | 467 ms: 1.58x faster                                        |
| async_tree_none_tg         | 577 ms                                                                | 370 ms: 1.56x faster                                        |
| async_tree_io_tg           | 1.40 sec                                                              | 918 ms: 1.53x faster                                        |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 658 ms: 1.39x faster                                        |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 648 ms: 1.36x faster                                        |
| deepcopy                   | 446 us                                                                | 341 us: 1.31x faster                                        |
| deepcopy_memo              | 49.6 us                                                               | 39.1 us: 1.27x faster                                       |
| dulwich_log                | 62.0 ms                                                               | 51.2 ms: 1.21x faster                                       |
| generators                 | 43.5 ms                                                               | 36.3 ms: 1.20x faster                                       |
| comprehensions             | 25.4 us                                                               | 21.3 us: 1.19x faster                                       |
| regex_effbot               | 4.64 ms                                                               | 4.01 ms: 1.16x faster                                       |
| deepcopy_reduce            | 4.10 us                                                               | 3.59 us: 1.14x faster                                       |
| pylint                     | 355 ms                                                                | 311 ms: 1.14x faster                                        |
| go                         | 157 ms                                                                | 140 ms: 1.13x faster                                        |
| pathlib                    | 24.5 ms                                                               | 22.1 ms: 1.11x faster                                       |
| xml_etree_parse            | 195 ms                                                                | 176 ms: 1.11x faster                                        |
| raytrace                   | 353 ms                                                                | 321 ms: 1.10x faster                                        |
| async_generators           | 491 ms                                                                | 451 ms: 1.09x faster                                        |
| regex_compile              | 137 ms                                                                | 127 ms: 1.08x faster                                        |
| sqlalchemy_declarative     | 157 ms                                                                | 146 ms: 1.08x faster                                        |
| logging_simple             | 7.63 us                                                               | 7.10 us: 1.08x faster                                       |
| xml_etree_iterparse        | 150 ms                                                                | 141 ms: 1.07x faster                                        |
| logging_format             | 8.34 us                                                               | 7.84 us: 1.06x faster                                       |
| float                      | 92.1 ms                                                               | 87.0 ms: 1.06x faster                                       |
| sympy_sum                  | 154 ms                                                                | 146 ms: 1.06x faster                                        |
| tomli_loads                | 2.59 sec                                                              | 2.45 sec: 1.06x faster                                      |
| spectral_norm              | 131 ms                                                                | 125 ms: 1.05x faster                                        |
| regex_dna                  | 254 ms                                                                | 247 ms: 1.03x faster                                        |
| 2to3                       | 308 ms                                                                | 301 ms: 1.02x faster                                        |
| mdp                        | 3.41 sec                                                              | 3.34 sec: 1.02x faster                                      |
| genshi_text                | 27.4 ms                                                               | 27.0 ms: 1.02x faster                                       |
| pyflate                    | 559 ms                                                                | 561 ms: 1.00x slower                                        |
| xml_etree_process          | 79.0 ms                                                               | 79.4 ms: 1.01x slower                                       |
| meteor_contest             | 112 ms                                                                | 113 ms: 1.01x slower                                        |
| sqlite_synth               | 3.77 us                                                               | 3.82 us: 1.01x slower                                       |
| pycparser                  | 1.26 sec                                                              | 1.27 sec: 1.01x slower                                      |
| pidigits                   | 233 ms                                                                | 237 ms: 1.02x slower                                        |
| pprint_pformat             | 1.88 sec                                                              | 1.92 sec: 1.02x slower                                      |
| richards                   | 50.9 ms                                                               | 52.0 ms: 1.02x slower                                       |
| asyncio_websockets         | 658 ms                                                                | 672 ms: 1.02x slower                                        |
| pprint_safe_repr           | 916 ms                                                                | 940 ms: 1.03x slower                                        |
| docutils                   | 2.98 sec                                                              | 3.07 sec: 1.03x slower                                      |
| bench_thread_pool          | 1.31 ms                                                               | 1.35 ms: 1.03x slower                                       |
| nqueens                    | 99.2 ms                                                               | 103 ms: 1.04x slower                                        |
| sympy_expand               | 454 ms                                                                | 473 ms: 1.04x slower                                        |
| logging_silent             | 127 ns                                                                | 133 ns: 1.05x slower                                        |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.54 ms: 1.06x slower                                       |
| pickle_pure_python         | 365 us                                                                | 386 us: 1.06x slower                                        |
| json                       | 5.54 ms                                                               | 5.97 ms: 1.08x slower                                       |
| scimark_lu                 | 146 ms                                                                | 157 ms: 1.08x slower                                        |
| hexiom                     | 6.98 ms                                                               | 7.57 ms: 1.09x slower                                       |
| typing_runtime_protocols   | 181 us                                                                | 197 us: 1.09x slower                                        |
| mako                       | 12.9 ms                                                               | 14.1 ms: 1.10x slower                                       |
| fannkuch                   | 443 ms                                                                | 500 ms: 1.13x slower                                        |
| coverage                   | 87.3 ms                                                               | 99.7 ms: 1.14x slower                                       |
| json_loads                 | 30.7 us                                                               | 35.2 us: 1.15x slower                                       |
| json_dumps                 | 12.3 ms                                                               | 14.1 ms: 1.15x slower                                       |
| telco                      | 8.51 ms                                                               | 9.93 ms: 1.17x slower                                       |
| nbody                      | 105 ms                                                                | 125 ms: 1.20x slower                                        |
| python_startup_no_site     | 8.37 ms                                                               | 10.2 ms: 1.21x slower                                       |
| python_startup             | 11.4 ms                                                               | 16.1 ms: 1.42x slower                                       |
| gc_traversal               | 4.40 ms                                                               | 6.59 ms: 1.50x slower                                       |
| create_gc_cycles           | 1.92 ms                                                               | 3.60 ms: 1.88x slower                                       |
| bench_mp_pool              | 7.05 ms                                                               | 3.19 sec: 452.06x slower                                    |
| Geometric mean             | (ref)                                                                 | 1.04x slower                                                |

Benchmark hidden because not significant (18): sqlalchemy_imperative, deltablue, sympy_str, html5lib, sympy_integrate, chaos, genshi_xml, thrift, scimark_monte_carlo, django_template, scimark_sor, xml_etree_generate, scimark_fft, regex_v8, richards_super, coroutines, crypto_pyaes, unpickle_pure_python
Ignored benchmarks (17) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250319-3.14.0a6+-548daa7/bm-20250319-arminc-aarch64-zooba-gh_91349-3.14.0a6+-548daa7.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.042x faster

# HPT report

- Reliability score: 99.62% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.06x