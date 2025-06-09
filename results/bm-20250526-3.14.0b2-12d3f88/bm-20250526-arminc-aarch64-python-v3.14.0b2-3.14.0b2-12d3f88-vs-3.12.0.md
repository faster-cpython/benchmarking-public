# Results vs. 3.12.0

- fork: python
- ref: v3.14.0b2
- machine: linux-aarch64
- commit hash: 12d3f88
- commit date: 2025-05-26
- overall geometric mean: 1.058x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250526-arminc-aarch64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| html5lib       | 65.1 ms                                                               | 61.0 ms: 1.07x faster                                        |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                 |

Benchmark hidden because not significant (2): 2to3, docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250526-arminc-aarch64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 467 ms: 1.66x faster                                         |
| async_tree_none            | 624 ms                                                                | 390 ms: 1.60x faster                                         |
| async_tree_io              | 1.41 sec                                                              | 883 ms: 1.60x faster                                         |
| async_tree_memoization_tg  | 740 ms                                                                | 464 ms: 1.60x faster                                         |
| async_tree_none_tg         | 577 ms                                                                | 372 ms: 1.55x faster                                         |
| async_tree_io_tg           | 1.40 sec                                                              | 916 ms: 1.53x faster                                         |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 658 ms: 1.39x faster                                         |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 659 ms: 1.34x faster                                         |
| Geometric mean             | (ref)                                                                 | 1.53x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250526-arminc-aarch64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 87.0 ms: 1.06x faster                                        |
| pidigits       | 233 ms                                                                | 241 ms: 1.03x slower                                         |
| nbody          | 105 ms                                                                | 125 ms: 1.19x slower                                         |
| Geometric mean | (ref)                                                                 | 1.05x slower                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250526-arminc-aarch64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.88 ms: 1.20x faster                                        |
| regex_compile  | 137 ms                                                                | 120 ms: 1.15x faster                                         |
| regex_dna      | 254 ms                                                                | 233 ms: 1.09x faster                                         |
| regex_v8       | 28.3 ms                                                               | 28.0 ms: 1.01x faster                                        |
| Geometric mean | (ref)                                                                 | 1.11x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250526-arminc-aarch64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|---------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| xml_etree_parse     | 195 ms                                                                | 182 ms: 1.07x faster                                         |
| tomli_loads         | 2.59 sec                                                              | 2.45 sec: 1.06x faster                                       |
| xml_etree_iterparse | 150 ms                                                                | 142 ms: 1.06x faster                                         |
| xml_etree_process   | 79.0 ms                                                               | 80.4 ms: 1.02x slower                                        |
| json_dumps          | 12.3 ms                                                               | 13.3 ms: 1.08x slower                                        |
| pickle_pure_python  | 365 us                                                                | 399 us: 1.09x slower                                         |
| json_loads          | 30.7 us                                                               | 35.9 us: 1.17x slower                                        |
| Geometric mean      | (ref)                                                                 | 1.02x slower                                                 |

Benchmark hidden because not significant (2): xml_etree_generate, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250526-arminc-aarch64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.55 ms: 1.02x slower                                        |
| python_startup         | 11.4 ms                                                               | 15.9 ms: 1.40x slower                                        |
| Geometric mean         | (ref)                                                                 | 1.20x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250526-arminc-aarch64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| genshi_xml     | 60.6 ms                                                               | 61.4 ms: 1.01x slower                                        |
| mako           | 12.9 ms                                                               | 14.0 ms: 1.08x slower                                        |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                 |

Benchmark hidden because not significant (2): django_template, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250526-arminc-aarch64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.69 sec: 2.02x faster                                       |
| async_tree_memoization     | 777 ms                                                                | 467 ms: 1.66x faster                                         |
| async_tree_none            | 624 ms                                                                | 390 ms: 1.60x faster                                         |
| async_tree_io              | 1.41 sec                                                              | 883 ms: 1.60x faster                                         |
| async_tree_memoization_tg  | 740 ms                                                                | 464 ms: 1.60x faster                                         |
| async_tree_none_tg         | 577 ms                                                                | 372 ms: 1.55x faster                                         |
| async_tree_io_tg           | 1.40 sec                                                              | 916 ms: 1.53x faster                                         |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 658 ms: 1.39x faster                                         |
| deepcopy                   | 446 us                                                                | 328 us: 1.36x faster                                         |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 659 ms: 1.34x faster                                         |
| deepcopy_memo              | 49.6 us                                                               | 38.9 us: 1.28x faster                                        |
| go                         | 157 ms                                                                | 131 ms: 1.20x faster                                         |
| regex_effbot               | 4.64 ms                                                               | 3.88 ms: 1.20x faster                                        |
| comprehensions             | 25.4 us                                                               | 21.3 us: 1.19x faster                                        |
| generators                 | 43.5 ms                                                               | 36.8 ms: 1.18x faster                                        |
| dulwich_log                | 62.0 ms                                                               | 53.5 ms: 1.16x faster                                        |
| regex_compile              | 137 ms                                                                | 120 ms: 1.15x faster                                         |
| pylint                     | 355 ms                                                                | 311 ms: 1.14x faster                                         |
| deepcopy_reduce            | 4.10 us                                                               | 3.63 us: 1.13x faster                                        |
| regex_dna                  | 254 ms                                                                | 233 ms: 1.09x faster                                         |
| deltablue                  | 4.12 ms                                                               | 3.84 ms: 1.07x faster                                        |
| xml_etree_parse            | 195 ms                                                                | 182 ms: 1.07x faster                                         |
| scimark_monte_carlo        | 85.1 ms                                                               | 79.4 ms: 1.07x faster                                        |
| pathlib                    | 24.5 ms                                                               | 22.9 ms: 1.07x faster                                        |
| html5lib                   | 65.1 ms                                                               | 61.0 ms: 1.07x faster                                        |
| async_generators           | 491 ms                                                                | 461 ms: 1.06x faster                                         |
| sympy_integrate            | 21.6 ms                                                               | 20.3 ms: 1.06x faster                                        |
| tomli_loads                | 2.59 sec                                                              | 2.45 sec: 1.06x faster                                       |
| float                      | 92.1 ms                                                               | 87.0 ms: 1.06x faster                                        |
| xml_etree_iterparse        | 150 ms                                                                | 142 ms: 1.06x faster                                         |
| raytrace                   | 353 ms                                                                | 336 ms: 1.05x faster                                         |
| sqlalchemy_declarative     | 157 ms                                                                | 150 ms: 1.05x faster                                         |
| pyflate                    | 559 ms                                                                | 535 ms: 1.04x faster                                         |
| crypto_pyaes               | 86.6 ms                                                               | 83.7 ms: 1.04x faster                                        |
| sqlalchemy_imperative      | 16.7 ms                                                               | 16.1 ms: 1.03x faster                                        |
| regex_v8                   | 28.3 ms                                                               | 28.0 ms: 1.01x faster                                        |
| pprint_pformat             | 1.88 sec                                                              | 1.86 sec: 1.01x faster                                       |
| meteor_contest             | 112 ms                                                                | 113 ms: 1.01x slower                                         |
| asyncio_websockets         | 658 ms                                                                | 667 ms: 1.01x slower                                         |
| genshi_xml                 | 60.6 ms                                                               | 61.4 ms: 1.01x slower                                        |
| logging_format             | 8.34 us                                                               | 8.47 us: 1.02x slower                                        |
| xml_etree_process          | 79.0 ms                                                               | 80.4 ms: 1.02x slower                                        |
| sqlite_synth               | 3.77 us                                                               | 3.85 us: 1.02x slower                                        |
| python_startup_no_site     | 8.37 ms                                                               | 8.55 ms: 1.02x slower                                        |
| sympy_expand               | 454 ms                                                                | 467 ms: 1.03x slower                                         |
| scimark_fft                | 418 ms                                                                | 433 ms: 1.03x slower                                         |
| scimark_lu                 | 146 ms                                                                | 150 ms: 1.03x slower                                         |
| pidigits                   | 233 ms                                                                | 241 ms: 1.03x slower                                         |
| fannkuch                   | 443 ms                                                                | 465 ms: 1.05x slower                                         |
| coroutines                 | 29.0 ms                                                               | 30.9 ms: 1.07x slower                                        |
| mako                       | 12.9 ms                                                               | 14.0 ms: 1.08x slower                                        |
| json_dumps                 | 12.3 ms                                                               | 13.3 ms: 1.08x slower                                        |
| json                       | 5.54 ms                                                               | 6.02 ms: 1.09x slower                                        |
| pickle_pure_python         | 365 us                                                                | 399 us: 1.09x slower                                         |
| telco                      | 8.51 ms                                                               | 9.34 ms: 1.10x slower                                        |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.93 ms: 1.12x slower                                        |
| typing_runtime_protocols   | 181 us                                                                | 203 us: 1.13x slower                                         |
| json_loads                 | 30.7 us                                                               | 35.9 us: 1.17x slower                                        |
| coverage                   | 87.3 ms                                                               | 103 ms: 1.18x slower                                         |
| nbody                      | 105 ms                                                                | 125 ms: 1.19x slower                                         |
| python_startup             | 11.4 ms                                                               | 15.9 ms: 1.40x slower                                        |
| gc_traversal               | 4.40 ms                                                               | 6.53 ms: 1.49x slower                                        |
| create_gc_cycles           | 1.92 ms                                                               | 3.66 ms: 1.91x slower                                        |
| logging_silent             | 127 ns                                                                | 633 ns: 4.99x slower                                         |
| Geometric mean             | (ref)                                                                 | 1.03x faster                                                 |

Benchmark hidden because not significant (18): sympy_sum, sympy_str, chaos, django_template, scimark_sor, docutils, nqueens, pprint_safe_repr, pycparser, spectral_norm, 2to3, hexiom, richards_super, genshi_text, xml_etree_generate, logging_simple, richards, unpickle_pure_python
Ignored benchmarks (20) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250526-3.14.0b2-12d3f88/bm-20250526-arminc-aarch64-python-v3.14.0b2-3.14.0b2-12d3f88.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.058x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.09x