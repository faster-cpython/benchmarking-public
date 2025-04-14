# Results vs. 3.12.0

- fork: faster-cpython
- ref: immortal_stickiness
- machine: linux-aarch64
- commit hash: 2a08194
- commit date: 2025-03-12
- overall geometric mean: 1.047x faster
- HPT reliability: 99.79%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250312-arminc-aarch64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 297 ms: 1.04x faster                                                              |
| docutils       | 2.98 sec                                                              | 2.96 sec: 1.01x faster                                                            |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                                      |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250312-arminc-aarch64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 474 ms: 1.64x faster                                                              |
| async_tree_none            | 624 ms                                                                | 386 ms: 1.62x faster                                                              |
| async_tree_io              | 1.41 sec                                                              | 881 ms: 1.60x faster                                                              |
| async_tree_io_tg           | 1.40 sec                                                              | 891 ms: 1.58x faster                                                              |
| async_tree_memoization_tg  | 740 ms                                                                | 480 ms: 1.54x faster                                                              |
| async_tree_none_tg         | 577 ms                                                                | 384 ms: 1.50x faster                                                              |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 657 ms: 1.39x faster                                                              |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 650 ms: 1.36x faster                                                              |
| Geometric mean             | (ref)                                                                 | 1.52x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250312-arminc-aarch64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 87.5 ms: 1.05x faster                                                             |
| pidigits       | 233 ms                                                                | 236 ms: 1.02x slower                                                              |
| nbody          | 105 ms                                                                | 126 ms: 1.20x slower                                                              |
| Geometric mean | (ref)                                                                 | 1.05x slower                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250312-arminc-aarch64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.98 ms: 1.17x faster                                                             |
| regex_compile  | 137 ms                                                                | 125 ms: 1.10x faster                                                              |
| regex_dna      | 254 ms                                                                | 241 ms: 1.05x faster                                                              |
| Geometric mean | (ref)                                                                 | 1.08x faster                                                                      |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250312-arminc-aarch64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|---------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| xml_etree_parse     | 195 ms                                                                | 176 ms: 1.11x faster                                                              |
| tomli_loads         | 2.59 sec                                                              | 2.42 sec: 1.07x faster                                                            |
| xml_etree_iterparse | 150 ms                                                                | 141 ms: 1.07x faster                                                              |
| xml_etree_generate  | 112 ms                                                                | 111 ms: 1.01x faster                                                              |
| pickle_pure_python  | 365 us                                                                | 395 us: 1.08x slower                                                              |
| json_loads          | 30.7 us                                                               | 33.9 us: 1.10x slower                                                             |
| json_dumps          | 12.3 ms                                                               | 13.8 ms: 1.13x slower                                                             |
| Geometric mean      | (ref)                                                                 | 1.01x slower                                                                      |

Benchmark hidden because not significant (2): xml_etree_process, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250312-arminc-aarch64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 10.3 ms: 1.23x slower                                                             |
| python_startup         | 11.4 ms                                                               | 16.2 ms: 1.43x slower                                                             |
| Geometric mean         | (ref)                                                                 | 1.32x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250312-arminc-aarch64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_text    | 27.4 ms                                                               | 26.8 ms: 1.02x faster                                                             |
| mako           | 12.9 ms                                                               | 14.0 ms: 1.09x slower                                                             |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                                      |

Benchmark hidden because not significant (2): genshi_xml, django_template

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250312-arminc-aarch64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 474 ms: 1.64x faster                                                              |
| async_tree_none            | 624 ms                                                                | 386 ms: 1.62x faster                                                              |
| async_tree_io              | 1.41 sec                                                              | 881 ms: 1.60x faster                                                              |
| async_tree_io_tg           | 1.40 sec                                                              | 891 ms: 1.58x faster                                                              |
| async_tree_memoization_tg  | 740 ms                                                                | 480 ms: 1.54x faster                                                              |
| async_tree_none_tg         | 577 ms                                                                | 384 ms: 1.50x faster                                                              |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 657 ms: 1.39x faster                                                              |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 650 ms: 1.36x faster                                                              |
| deepcopy                   | 446 us                                                                | 329 us: 1.35x faster                                                              |
| deepcopy_memo              | 49.6 us                                                               | 38.2 us: 1.30x faster                                                             |
| generators                 | 43.5 ms                                                               | 35.6 ms: 1.22x faster                                                             |
| deepcopy_reduce            | 4.10 us                                                               | 3.39 us: 1.21x faster                                                             |
| dulwich_log                | 62.0 ms                                                               | 51.5 ms: 1.20x faster                                                             |
| comprehensions             | 25.4 us                                                               | 21.2 us: 1.20x faster                                                             |
| regex_effbot               | 4.64 ms                                                               | 3.98 ms: 1.17x faster                                                             |
| go                         | 157 ms                                                                | 136 ms: 1.16x faster                                                              |
| pylint                     | 355 ms                                                                | 310 ms: 1.15x faster                                                              |
| xml_etree_parse            | 195 ms                                                                | 176 ms: 1.11x faster                                                              |
| async_generators           | 491 ms                                                                | 444 ms: 1.11x faster                                                              |
| regex_compile              | 137 ms                                                                | 125 ms: 1.10x faster                                                              |
| raytrace                   | 353 ms                                                                | 322 ms: 1.10x faster                                                              |
| logging_simple             | 7.63 us                                                               | 6.96 us: 1.10x faster                                                             |
| sqlalchemy_imperative      | 16.7 ms                                                               | 15.2 ms: 1.10x faster                                                             |
| pathlib                    | 24.5 ms                                                               | 22.5 ms: 1.09x faster                                                             |
| sympy_sum                  | 154 ms                                                                | 142 ms: 1.09x faster                                                              |
| logging_format             | 8.34 us                                                               | 7.72 us: 1.08x faster                                                             |
| sqlalchemy_declarative     | 157 ms                                                                | 146 ms: 1.07x faster                                                              |
| tomli_loads                | 2.59 sec                                                              | 2.42 sec: 1.07x faster                                                            |
| xml_etree_iterparse        | 150 ms                                                                | 141 ms: 1.07x faster                                                              |
| regex_dna                  | 254 ms                                                                | 241 ms: 1.05x faster                                                              |
| float                      | 92.1 ms                                                               | 87.5 ms: 1.05x faster                                                             |
| spectral_norm              | 131 ms                                                                | 124 ms: 1.05x faster                                                              |
| sympy_str                  | 280 ms                                                                | 267 ms: 1.05x faster                                                              |
| 2to3                       | 308 ms                                                                | 297 ms: 1.04x faster                                                              |
| chaos                      | 71.4 ms                                                               | 69.0 ms: 1.03x faster                                                             |
| mdp                        | 3.41 sec                                                              | 3.32 sec: 1.03x faster                                                            |
| genshi_text                | 27.4 ms                                                               | 26.8 ms: 1.02x faster                                                             |
| docutils                   | 2.98 sec                                                              | 2.96 sec: 1.01x faster                                                            |
| xml_etree_generate         | 112 ms                                                                | 111 ms: 1.01x faster                                                              |
| thrift                     | 937 us                                                                | 943 us: 1.01x slower                                                              |
| meteor_contest             | 112 ms                                                                | 113 ms: 1.01x slower                                                              |
| nqueens                    | 99.2 ms                                                               | 101 ms: 1.01x slower                                                              |
| pycparser                  | 1.26 sec                                                              | 1.27 sec: 1.01x slower                                                            |
| pidigits                   | 233 ms                                                                | 236 ms: 1.02x slower                                                              |
| richards                   | 50.9 ms                                                               | 51.8 ms: 1.02x slower                                                             |
| pprint_pformat             | 1.88 sec                                                              | 1.92 sec: 1.02x slower                                                            |
| pprint_safe_repr           | 916 ms                                                                | 940 ms: 1.03x slower                                                              |
| pyflate                    | 559 ms                                                                | 574 ms: 1.03x slower                                                              |
| scimark_lu                 | 146 ms                                                                | 150 ms: 1.03x slower                                                              |
| sympy_expand               | 454 ms                                                                | 467 ms: 1.03x slower                                                              |
| bench_thread_pool          | 1.31 ms                                                               | 1.35 ms: 1.03x slower                                                             |
| scimark_fft                | 418 ms                                                                | 432 ms: 1.03x slower                                                              |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.51 ms: 1.05x slower                                                             |
| hexiom                     | 6.98 ms                                                               | 7.35 ms: 1.05x slower                                                             |
| json                       | 5.54 ms                                                               | 5.91 ms: 1.07x slower                                                             |
| pickle_pure_python         | 365 us                                                                | 395 us: 1.08x slower                                                              |
| mako                       | 12.9 ms                                                               | 14.0 ms: 1.09x slower                                                             |
| typing_runtime_protocols   | 181 us                                                                | 196 us: 1.09x slower                                                              |
| json_loads                 | 30.7 us                                                               | 33.9 us: 1.10x slower                                                             |
| fannkuch                   | 443 ms                                                                | 493 ms: 1.11x slower                                                              |
| coverage                   | 87.3 ms                                                               | 97.8 ms: 1.12x slower                                                             |
| json_dumps                 | 12.3 ms                                                               | 13.8 ms: 1.13x slower                                                             |
| telco                      | 8.51 ms                                                               | 10.0 ms: 1.18x slower                                                             |
| nbody                      | 105 ms                                                                | 126 ms: 1.20x slower                                                              |
| python_startup_no_site     | 8.37 ms                                                               | 10.3 ms: 1.23x slower                                                             |
| python_startup             | 11.4 ms                                                               | 16.2 ms: 1.43x slower                                                             |
| gc_traversal               | 4.40 ms                                                               | 6.79 ms: 1.54x slower                                                             |
| create_gc_cycles           | 1.92 ms                                                               | 3.69 ms: 1.92x slower                                                             |
| bench_mp_pool              | 7.05 ms                                                               | 4.02 sec: 570.35x slower                                                          |
| Geometric mean             | (ref)                                                                 | 1.04x slower                                                                      |

Benchmark hidden because not significant (16): deltablue, html5lib, scimark_monte_carlo, genshi_xml, sqlite_synth, asyncio_websockets, sympy_integrate, crypto_pyaes, xml_etree_process, regex_v8, coroutines, unpickle_pure_python, scimark_sor, django_template, logging_silent, richards_super
Ignored benchmarks (17) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250312-3.14.0a5+-2a08194/bm-20250312-arminc-aarch64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.047x faster

# HPT report

- Reliability score: 99.79% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x